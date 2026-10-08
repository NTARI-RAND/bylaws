# Contributing

This repository carries P1-001, the bylaws of Network Theory Applied Research
Institute, Inc., and its translations. Two rules govern every change: **sign
your commits off**, and **keep the suite green**.

## Amendments go into the instrument

Propose a change by editing `P1-001_Bylaws_v1.0.md` and opening a pull request.
The diff is the proposal, and the board approves or rejects it in review. Do
not add proposal files or version-documentation alongside the instrument — git
history is the version record, and a parallel proposal document starts drifting
from the text it describes the moment it is merged.

Amendment itself is governed by Article XV. Nothing here overrides it; this
file describes how a change reaches the repository, not who may adopt one.

Prior instruments are archived in `Historical Docs/` rather than amended. The
version line restarts at 1.0 for the first instrument written to the Janus
Facing Architecture — see the header and §16.1.

## Sign-off (DCO)

Every commit needs a `Signed-off-by` trailer. The DCO check requires the name
and email in that trailer to match the commit author exactly, so let git add it
rather than typing it by hand:

```
git commit -s
```

If the check fails on an existing branch, add the trailer to every commit and
force-push:

```
git rebase HEAD~<n> --signoff
git push --force-with-lease
```

## The conformance suite

```
python bylaws-conformance-suite.py              # check the instrument
python bylaws-conformance-suite.py --doc PATH   # check another copy
```

Exit code 0 when every check passes, 1 otherwise. It runs on every pull request
as the **Conformance** check.

To catch failures before you push, install the hook once in your clone:

```
git config core.hooksPath .githooks
```

That is a convenience, not a gate — hooks are not distributed with a
repository, and `git push --no-verify` skips them. The pull request check is
what actually holds.

### What the suite constrains

The instrument carries 104 numbered provisions and 199 internal cross
references. Nothing about that is self-checking: renumber a provision and every
reference to it keeps pointing at a number that now means something else, or
nothing at all, and the breakage stays invisible until a reader follows one.

Edits fail the suite if they:

- drop, rename or reorder the preamble, the sixteen articles, or the appendix.
- leave a gap in the provisions inside an article. They run 1..n, and the
  groups must match the article count — renumbering `9.10` to `9.99` fails.
- leave a section cross reference pointing at a provision that does not exist.
- leave a lettered sub-item reference — `§3.2(e)` — pointing at a sub-item that
  does not exist.
- disagree with the filename about the version number.
- introduce an email address other than the organizational footer's.
- remove a translation, or the archived prior instruments.

### What it does not constrain

It checks that the instrument is internally whole. It does not check that a
provision is wise, lawful, or consistent with the architecture — those bind a
reader, not a parser.

In particular there is **no invariant registry yet**. The JFA suite binds prose
to registered invariants with stable IDs, so the document and the registry
cannot drift apart without a check failing. The equivalent here would bind
provisions to the architecture's lines — §9.10(a) to the privacy floor, §1.4(a)
to stewardship of the document, and so on. That requires deciding which
provisions are load bearing, which is a governance judgment rather than a
mechanical one, and is deliberately left for a later change.

## Translations

The English instrument is authoritative; translations are for reach, not
interpretation. The suite checks that all seven are present, not that they say
the same thing. If you amend the English, say in the pull request whether the
translations should be updated before the change is adopted or after.
