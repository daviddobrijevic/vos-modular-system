#!/usr/bin/env python3
"""
Keeps the shared header (logo, menu, offcanvas) and footer identical across
every page on the site.

Edit partials/header.html or partials/footer.html once, then run:

    python3 sync-partials.py

...and every page listed in PAGES gets the same block dropped in, between
the same marker comments that are already in each file. Add new pages to
PAGES as they're created.
"""

PAGES = ["index.html", "lgs.html"]

HEADER_START = "<!-- Begin magic cursor -->"
HEADER_END = "</header>\n    <!-- header area end -->"

FOOTER_START = "<footer>"
FOOTER_END = "</footer>"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def replace_block(content, start_marker, end_marker, new_block):
    s = content.index(start_marker)
    e = content.index(end_marker, s) + len(end_marker)
    return content[:s] + new_block.rstrip("\n") + content[e:]


def main():
    header = read("partials/header.html")
    footer = read("partials/footer.html")

    for page in PAGES:
        content = read(page)
        updated = replace_block(content, HEADER_START, HEADER_END, header)
        updated = replace_block(updated, FOOTER_START, FOOTER_END, footer)
        if updated != content:
            write(page, updated)
            print(f"synced: {page}")
        else:
            print(f"already up to date: {page}")


if __name__ == "__main__":
    main()
