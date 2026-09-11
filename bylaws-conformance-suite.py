#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bylaws conformance suite (P1-001).

The instrument is 104 numbered provisions carrying 199 internal cross
references. Nothing about that is self-checking: renumber a provision and
every reference to it keeps pointing at a number that now means something
else, or nothing at all, and the breakage stays invisible until a reader
follows one. This suite makes that failure loud.

What it checks is structure, not meaning. It does not know whether a provision
is wise, lawful, or consistent with the architecture, only that the document is
internally whole:

  * the preamble, sixteen articles in order, and the appendix are present
  * provisions run 1..n inside each article with no gaps, and the groups
    match the article count
  * every section cross reference resolves to a provision that exists
  * every lettered sub-item reference resolves to a sub-item that exists
  * the version in the header agrees with the version in the filename
  * no personal data beyond the organizational footer
  * the translations named beside the instrument are all present
  * the prior instruments are preserved

A registry binding provisions to the architecture's invariants, in the manner
of the JFA suite, is deliberately not here yet. That requires deciding which
provisions are load bearing, which is a governance judgment rather than a
mechanical one.

Usage:

  python bylaws-conformance-suite.py              # check the instrument
  python bylaws-conformance-suite.py --doc PATH   # check another copy

Exit code 0 when every check passes, 1 otherwise. Standard library only.
"""

from __future__ import print_function

import argparse
import collections
import glob
import io
import os
import re
import sys

Result = collections.namedtuple("Result", "name ok detail")

DOC_DEFAULT = "P1-001_Bylaws_v1.0.md"

ARTICLES = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
            "XI", "XII", "XIII", "XIV", "XV", "XVI"]

TRANSLATIONS = ["ar", "es", "fr", "hi", "pt", "tok", "zh"]

FOOTER_EMAIL = "info@ntari.org"

SECTION_SIGN = u"§"

# A provision heading, e.g.  **9.10 The covenant's binding rules.**
PROVISION_RE = re.compile(r"^\*\*(\d+)\.(\d+)", re.M)
# A cross reference, e.g.  section 9.10, with or without a space after the sign
SECTION_REF_RE = re.compile(SECTION_SIGN + r"\s?(\d+\.\d+)")
# A lettered sub-item reference, e.g.  section 3.2(e)
SUBITEM_REF_RE = re.compile(SECTION_SIGN + r"\s?(\d+\.\d+)\(([a-z])\)")


def read(path):
    return io.open(path, encoding="utf-8", errors="replace").read()


def provision_bodies(doc):
    """Map '9.10' to the text of that provision, up to the next heading."""
    bodies = {}
    pattern = re.compile(r"^\*\*(\d+\.\d+)(.*?)(?=^\*\*\d+\.\d+|^## |\Z)",
                         re.M | re.S)
    for m in pattern.finditer(doc):
        bodies[m.group(1)] = m.group(2)
    return bodies


def defined_provisions(doc):
    return set("%s.%s" % (a, b) for a, b in PROVISION_RE.findall(doc))


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_structure(doc):
    problems = []
    if not re.search(r"^## Preamble", doc, re.M):
        problems.append("preamble absent")
    found = re.findall(r"^## Article ([IVX]+)", doc, re.M)
    if found != ARTICLES:
        problems.append("articles %s, expected %s" % (found, ARTICLES))
    if not re.search(r"^## Appendix", doc, re.M):
        problems.append("appendix absent")
    return Result("B1 preamble, sixteen articles in order, appendix",
                  not problems, "; ".join(problems))


def check_numbering(doc):
    problems = []
    groups = collections.defaultdict(list)
    for a, b in PROVISION_RE.findall(doc):
        groups[int(a)].append(int(b))
    for key in sorted(groups):
        got = sorted(groups[key])
        want = list(range(1, len(got) + 1))
        if got != want:
            missing = [n for n in want if n not in got]
            problems.append("article %d: provisions %s%s"
                            % (key, got,
                               " (gaps at %s)" % missing if missing else ""))
    if groups and sorted(groups) != list(range(1, len(ARTICLES) + 1)):
        problems.append("provision groups %s do not match %d articles"
                        % (sorted(groups), len(ARTICLES)))
    total = sum(len(v) for v in groups.values())
    return Result("B2 provisions numbered 1..n inside each article",
                  not problems,
                  "; ".join(problems) if problems
                  else "%d provisions across %d articles" % (total, len(groups)))


def check_cross_references(doc):
    defined = defined_provisions(doc)
    refs = SECTION_REF_RE.findall(doc)
    dangling = sorted(set(r for r in refs if r not in defined),
                      key=lambda x: [int(p) for p in x.split(".")])
    return Result("B3 every section cross reference resolves", not dangling,
                  ("dangling: " + ", ".join(SECTION_SIGN + d for d in dangling))
                  if dangling
                  else "%d references, %d distinct, all resolve"
                       % (len(refs), len(set(refs))))


def check_sub_items(doc):
    bodies = provision_bodies(doc)
    refs = SUBITEM_REF_RE.findall(doc)
    missing = []
    for num, letter in sorted(set(refs)):
        body = bodies.get(num, "")
        if not re.search(r"^\(%s\)" % letter, body, re.M):
            missing.append("%s%s(%s)" % (SECTION_SIGN, num, letter))
    return Result("B4 every lettered sub-item reference resolves", not missing,
                  ("unresolved: " + ", ".join(missing)) if missing
                  else "%d sub-item references, all resolve" % len(set(refs)))


def check_version(doc, doc_path):
    name = os.path.basename(doc_path)
    m_file = re.search(r"_v(\d+\.\d+)\.", name)
    m_head = re.search(r"Version\s+(\d+\.\d+)", doc)
    if not m_file:
        return Result("B5 header version agrees with the filename", True,
                      "filename carries no version; header only")
    if not m_head:
        return Result("B5 header version agrees with the filename", False,
                      "no 'Version N.N' in the header")
    ok = m_file.group(1) == m_head.group(1)
    return Result("B5 header version agrees with the filename", ok,
                  "version %s" % m_head.group(1) if ok
                  else "filename says %s, header says %s"
                       % (m_file.group(1), m_head.group(1)))


def check_no_pii(doc):
    emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", doc))
    emails.discard(FOOTER_EMAIL)
    return Result("B6 no personal data beyond the organizational footer",
                  not emails,
                  ("unexpected addresses: " + ", ".join(sorted(emails)))
                  if emails else "")


def check_translations(doc_path):
    base, ext = os.path.splitext(os.path.abspath(doc_path))
    missing = [code for code in TRANSLATIONS
               if not os.path.isfile("%s.%s%s" % (base, code, ext))]
    return Result("B7 translations present beside the instrument", not missing,
                  ("absent: " + ", ".join(missing)) if missing
                  else "%d translations present" % len(TRANSLATIONS))


def check_history(doc_path):
    hist = os.path.join(os.path.dirname(os.path.abspath(doc_path)),
                        "Historical Docs")
    if not os.path.isdir(hist):
        return Result("B8 prior instruments preserved", False,
                      "Historical Docs absent beside the instrument")
    prior = glob.glob(os.path.join(hist, "P1-001_Bylaws_v*"))
    return Result("B8 prior instruments preserved", bool(prior),
                  "%d prior instruments archived" % len(prior) if prior
                  else "Historical Docs holds no prior P1-001")


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Bylaws conformance suite")
    ap.add_argument("--doc", default=DOC_DEFAULT)
    args = ap.parse_args()

    if not os.path.isfile(args.doc):
        print("no such document: %s" % args.doc)
        return 1

    doc = read(args.doc)
    results = [
        check_structure(doc),
        check_numbering(doc),
        check_cross_references(doc),
        check_sub_items(doc),
        check_version(doc, args.doc),
        check_no_pii(doc),
        check_translations(args.doc),
        check_history(args.doc),
    ]

    title = "Bylaws conformance: %s" % os.path.basename(args.doc)
    print(title)
    print("-" * len(title))
    for r in results:
        line = "%s %s" % ("[PASS]" if r.ok else "[FAIL]", r.name)
        if r.detail:
            line += " -- " + r.detail
        print(line)
    print()
    print("This suite checks that the instrument is internally whole. It does")
    print("not check that a provision is wise, lawful, or consistent with the")
    print("architecture; those bind a reader, not a parser.")
    print()

    failed = [r for r in results if not r.ok]
    if failed:
        print("RESULT: %d check(s) FAILED" % len(failed))
        return 1
    print("RESULT: all checks PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
