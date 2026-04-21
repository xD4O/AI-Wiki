#!/usr/bin/env python3
"""
Walk every HTML file in AI-Wiki, extract URLs, validate concurrently, emit a
broken-URL report. Uses a browser User-Agent because many sites 403 curl.
"""
import re
import sys
import pathlib
import concurrent.futures as cf
import urllib.request
import urllib.error
import ssl
import socket

# Repository root — resolved relative to this file so it works in any checkout.
ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

URL_RE = re.compile(r'href="(https?://[^"]+)"')

def collect_urls():
    """Return {url: [file1, file2, ...]} so we dedupe across files."""
    out = {}
    for p in ROOT.rglob("*.html"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in URL_RE.finditer(txt):
            url = m.group(1)
            out.setdefault(url, []).append(str(p.relative_to(ROOT)))
    return out

def check(url, timeout=12):
    """Return (url, status_code_or_error_str). Follows redirects implicitly."""
    # Strip trailing punctuation that sometimes glued in (parens, commas)
    clean = url.rstrip('.,)')
    req = urllib.request.Request(clean, headers={"User-Agent": UA}, method="GET")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return url, r.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except (urllib.error.URLError, socket.timeout, TimeoutError) as e:
        return url, f"ERR:{type(e).__name__}"
    except Exception as e:
        return url, f"ERR:{type(e).__name__}"

def main():
    urls = collect_urls()
    print(f"Found {len(urls)} unique URLs across {sum(1 for _ in ROOT.rglob('*.html'))} HTML files.", file=sys.stderr)

    results = {}
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        for url, status in ex.map(check, urls.keys()):
            results[url] = status

    # Classify
    ok, redirect, client_err, server_err, network = [], [], [], [], []
    for url, st in results.items():
        if isinstance(st, int):
            if 200 <= st < 300: ok.append((url, st))
            elif 300 <= st < 400: redirect.append((url, st))
            elif 400 <= st < 500: client_err.append((url, st))
            else: server_err.append((url, st))
        else:
            network.append((url, st))

    # We treat 403, 429, 503 as "probably fine behind bot protection" — these are
    # common for Twitter, X, Substack, Reddit, etc.
    likely_fine_codes = {403, 429, 503, 999}

    truly_broken = []
    for url, st in client_err + server_err + network:
        if isinstance(st, int) and st in likely_fine_codes:
            continue
        # arxiv.org and github.com 404s are actually broken (not bot-protection)
        truly_broken.append((url, st, urls[url]))

    print(f"\n=== Summary ===", file=sys.stderr)
    print(f"  OK (2xx):       {len(ok)}", file=sys.stderr)
    print(f"  Redirect (3xx): {len(redirect)}", file=sys.stderr)
    print(f"  Client err 4xx: {len(client_err)}", file=sys.stderr)
    print(f"  Server err 5xx: {len(server_err)}", file=sys.stderr)
    print(f"  Network err:    {len(network)}", file=sys.stderr)
    print(f"  Truly broken:   {len(truly_broken)}", file=sys.stderr)

    print("\n=== TRULY BROKEN URLS ===")
    for url, st, files in sorted(truly_broken, key=lambda r: str(r[1])):
        print(f"{st}  {url}")
        for f in files[:5]: print(f"       in: {f}")

    print("\n=== BOT-PROTECTED (403/429/503 — likely OK but unverifiable) ===")
    for url, st in sorted([(u, s) for u, s in client_err + server_err if s in likely_fine_codes]):
        print(f"{st}  {url}")

    print("\n=== NETWORK ERRORS ===")
    for url, st in network:
        print(f"{st}  {url}")

if __name__ == "__main__":
    main()
