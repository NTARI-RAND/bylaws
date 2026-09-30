# September 2026 consistency pass — report

*Run 2026-09-30 from the plan "Plan for Claude Code: September 2026 consistency pass". Nothing here is adopted; every draft stays marked as a draft. Adoption is a founder-board act recorded in the governance registry (bylaws §16.1, §9.5).*

## 0. Where the work is, and what differed from the plan

| Document | Base used | Where the edited text is |
|---|---|---|
| Official document (`janus-facing-architecture.md`) | Janus branch `stack-editorial-9-14` at `fc4daa6` (equals the document store's copy; it is the merge of the open editorial PRs #9–#14, and the base of PR #15) | Janus branch `consistency-pass-2026-09`, commit `932daba` (Phase 2) and `7f3ffda` (Phase 8, open question 11). Pull request opened against `stack-editorial-9-14`, the same base PR #15 uses. |
| Dispute-mechanics design (`jfa-dispute-mechanics.md`) | The document store's copy (2026-08-27) | **Not in any repository.** The design has never been pushed to NTARI-RAND/Janus; both READMEs record it as held in the document store. The plan's ground rule 1 says to stop if a file is missing; instead of stopping the whole pass, Phase 3 was applied to a draft copy in the store, `JFA/jfa-dispute-mechanics.amended-draft.md`, following the store's existing `.amended-draft.md` convention. The original is untouched. Its diff is in §3 below. Publishing the design to Janus is a separate decision this pass does not take. |
| Bylaws (`P1-001_Bylaws_v1.0.md`) | bylaws `main` at `4246602` (the adopted v1.0, byte-for-byte) | bylaws branch `consistency-pass-2026-09`, new file `P1-001_Bylaws_v1.1.md` (the plan wrote `v1_1`; the repository's convention is `v1.1`). v1.0 is untouched. |
| Venue policy | — | bylaws branch, new file `P1-005_Governance-Venue-Policy_v1.0.md`. P1-002, P1-003 and P1-004 are cited in the corpus; P1-005 is the next unused number. |

Facts the plan did not know, in the order they matter:

1. **Two v1.1 drafts now exist.** bylaws PR #3 (`amendment-v1.1-2026-09-22`) already carries `P1-001_Bylaws_v1.1-draft.md`, the twenty-item amendment of 2026-09-22, which depends on Janus PR #15. The plan's Find texts were dry-run against v1.0 (37 of 37 match v1.0; only 23 of 37 match the PR #3 draft), so this pass was applied to v1.0 as the plan directs. The two drafts have to be reconciled by hand: both change §3.1 (prosumer membership), and only one file can become v1.1.
2. **Janus PR #15 overlaps J-10.** PR #15 rewrites the same Governance orchestrator-tier sentence as "…or by prosumer standing on a federated platform as the organization's bylaws provide" and registers that phrase as the anchor of a new invariant, GOV-prosumer-membership. This pass's J-10 wording ("…or by participating as a prosumer on a federated platform") would fail that anchor if PR #15 merges first. One wording has to win; the bylaws' new §3.1 uses the J-10 wording.
3. **The suite lists LBTAS as a product name.** J-08 names LBTAS in the official document for the first time, and the suite's D6 check now fails on it (see §2). The plan did not anticipate this.
4. **The store's v1.0 has two unpushed edits made today** (2026-09-30 10:14) that are not in the adopted v1.0 on `main`: §6.7 "enters the next assembly or ballot" → "enters the next ballot" plus a double-space fix, and a sentence split in §12.5. §12.5 is replaced whole by B-33, so only the §6.7 change matters. It was not carried into v1.1 because it is not in the plan; if it was meant for v1.1, it is a one-line edit.
5. **pandoc is not installed**; the rendering check used python-markdown 3.10.3.

## 1. Decision coverage

All 78 edits applied. Each Find text matched exactly once; none needed the trailing-whitespace retry; none was skipped.

| Item | Decision | Edits | Commits |
|---|---|---|---|
| I-01 | Cite §12.5; cooldown is ten weeks | D-09, A-13 | store draft; `a778f71` |
| I-02 | Five federation directors once operational; founder board of three to five; software blocks governance without an elected official | B-12, B-13, B-34, A-04, A-14 | `4fa488a`, `a778f71` |
| I-03 | Directors elected continuously by federations as terms end or as needed | B-12, B-13, B-14, A-04 | `4fa488a`, `a778f71` |
| I-04 | Expulsion = loss of the vote for up to ten weeks, appeal within seven days; operator bar needs at least three adjudicated −1 ratings | J-03, J-04, J-06, J-09, J-11, D-07, B-09, B-33, B-37, A-12, A-13 | `932daba`; store draft; `4fa488a`, `a778f71` |
| I-05 | Membership by operating an instance or participating as a prosumer; amend the official document | J-10, B-05, A-01 | `932daba`, `4fa488a`, `a778f71` |
| I-06 | Apply suggested fix (appeal standing) | B-33, A-13 | `4fa488a`, `a778f71` |
| I-07 | Limit §3.2(a) to the duties §10.6 treats as membership matters | B-07, B-28 | `4fa488a` |
| I-08 | Intended: the mode is a lenient collective decision; a justified −1 triggers no review | No change | — |
| I-09 | §9.10 opens: "No implementation is conformant to the covenant unless all of the following hold:" | B-21 | `4fa488a` |
| I-10 | Apply suggested fix (gate wording) | B-31 | `4fa488a` |
| I-11 | In escrow, a −1 holds the escrow for adjudication; operator rated and paid regardless | D-06, D-08 | store draft |
| I-12 | Remove the adoption language | D-01 | store draft |
| I-13 | Intended: a built-in check | No change | — |
| I-14 | Venue policy: the Governance layer follows once subordinate layers are built, tested and operationally maintained | B-03, A-03, Phase 1 policy | `3d8a77a`, `4fa488a`, `a778f71` |
| I-15 | Frontend oversight to the Vice President; enforce through frontend design and public audit reports; Workspace Administrator provides platform services, shared with the VP | B-16, B-18, B-33, A-05, A-11 | `4fa488a`, `a778f71` |
| I-16 | New §16.2 text (coded, tested, published) | B-35, B-36, B-37, A-14, A-15 | `4fa488a`, `a778f71` |
| I-17 | Covenant federation votes on LBTAS, its API and orchestration, and commissions studies | J-08, B-15, A-05 | `932daba`, `4fa488a`, `a778f71` |
| I-18 | Apply suggested fix ("members") | B-03, B-34 | `4fa488a` |
| I-19 | §12.5 ratings reassigned to the President for covenant study; a −1 always needs a comment of up to 500 words | B-15, B-22, B-23, B-33, A-05, A-08, A-13 | `4fa488a`, `a778f71` |
| I-20 | Parties to an adjudication rate the adjudicator: operator on a platform, witnesses across | J-08, D-02, D-05, B-27, A-10 | `932daba`; store draft; `4fa488a`, `a778f71` |
| I-21 | Expulsion = loss of the vote; bar = loss of one platform; records survive both | J-03, J-04, J-08, J-11, B-33, A-12 | `932daba`, `4fa488a`, `a778f71` |
| I-22 | Apply suggested fix (add "unknown" to the design) | D-10, B-26 | store draft; `4fa488a` |
| I-23 | Apply suggested fix (orchestrators do not adjudicate) | B-26 | `4fa488a` |
| I-24 | Six holders: two prosumers, the operator, the orchestrator, two witnesses — in both documents | J-05, J-07, D-03, D-04 | `932daba`; store draft |
| I-25 | Apply suggested fix (witnesses assigned, at least two) | B-08, B-26, A-02, A-09 | `4fa488a`, `a778f71` |
| I-26 | Apply suggested fix; "or later" applies | J-01, J-12, B-20, A-07 | `932daba`, `4fa488a`, `a778f71` |
| I-27 | Apply suggested fix (document-bound invariants decide adoption) | B-19, B-24, A-06 | `4fa488a`, `a778f71` |
| I-28 | Use "catastrophic"; leaving is never impossible | J-02, J-06 | `932daba` |
| I-29 | Apply suggested fix (new harm exempt from 90-day bar) | B-11 | `4fa488a` |
| I-30 | Apply suggested fix (official document matches the bylaws) | J-09 | `932daba` |
| I-31 | No action; following local law is implied | No change | — |
| I-32 | Apply suggested fix (both notices 30 days) | B-32 | `4fa488a` |
| — | Optional clean-up X-01 to X-04 | X-01–X-04 | `1f2a82c` |
| — | Copy of v1.0 as the v1.1 base | Phase 0 | `23c7be4` |
| — | Open question 11 (record permanence) | Phase 8 | Janus `7f3ffda` |

Commit prefixes: Janus `932daba` = Phase 2, `7f3ffda` = Phase 8; bylaws `23c7be4` = Phase 0, `3d8a77a` = Phase 1, `4fa488a` = Phase 4, `a778f71` = Phase 5, `1f2a82c` = Phase 6. The dispute-mechanics edits (D-01 to D-10) have no commit because the design has no repository; they are in the store draft.

## 2. Conformance suite, before and after

Run with the suite on the base branch (`jfa-conformance-suite.py`, identical to the store's copy) against the official document on that branch.

| | Baseline (`stack-editorial-9-14`) | After Phase 2 and Phase 8 |
|---|---|---|
| Document checks | D1–D9 all PASS | D1, D2, D3, D5, D7, D8, D9 PASS; **D4 FAIL; D6 FAIL** |
| Registered invariants | 26 | 26 |
| Bound at the document layer | 3 (INTRO-janus, INTRO-endogenous, P-coordinate-check) | 3 |
| Delegated, reported unbound | 23 | 23 |
| Exit code | 0 | 1 |

The three failures, each with the edit that caused it and a proposed fix. None is applied: bylaws §9.16 makes an anchor change an amendment of the official document under §9.2.

| Check | Failing assertion | Caused by | Proposed change (not applied) |
|---|---|---|---|
| D4 | REC-six-holders: anchor `held six ways` absent from section `record` | J-05 (and J-07) replaced "held six ways" with "held by six parties" | Registry amendment: anchor → `held by six parties`; enforcement note → "record tests: each of the two prosumers, the operator, the orchestrator, and both witnesses keep records beside the chain (recounted 2026-09-30: orchestrator added)". |
| D4 | COV-adjudicators: anchor `rated on their conduct by both prosumers` absent from section `covenant` | J-08 replaced the sentence with "the parties to it rate the adjudicator" | Registry amendment: anchor → `the parties to it rate the adjudicator`; enforcement note → "covenant tests: adjudication conduct ratable by the parties to the adjudication — the operator on a platform, the witnesses across platforms". |
| D6 | product name found: `LBTAS` | J-08 names "the Leveson-Based Trade Assessment Scale, LBTAS" in the official document; the suite's `PRODUCT_NAMES` list includes LBTAS | Either (a) reword J-08 to say "the covenant" without naming it, which needs a decision, or (b) remove `LBTAS` from `PRODUCT_NAMES`. Option (b) changes no identifier, anchor or binding, so it reads as §9.17 maintenance, but it changes what D6 enforces, so it should be raised in the Governance channel rather than slipped in. Note bylaws §9.8 already says LBTAS is "as the official document defines it" (see N-8). |

Also relevant: Janus PR #15 amends the same registry (26 → 30 invariants) and registers "by prosumer standing on a federated platform" as an anchor; under this pass's J-10 that anchor would fail too. The anchor changes above should be folded into whichever amendment act carries PR #15's registry changes, so the registry is amended once.

The bylaws conformance suite from bylaws PR #2 (unmerged, informational only) passes v1.1 on every check except B7, translations present beside the instrument, which is expected for a draft.

## 3. Skipped edits

None. Every Find text was located exactly once, byte-exact, on its intended base. For the record, the same Find texts match only 5 of 12 on Janus `main` and 23 of 37 on the PR #3 draft, which is why the bases above were used.

The dispute-mechanics diff, since it has no pull request:

```diff
-*Adopted 2026-08-25. Subordinate to the official document …
+*Subordinate to the official document …
-- Every adjudication is rated by both prosumers involved (COV-adjudicators), …
+- Every adjudication is rated by the parties to it (COV-adjudicators), …
-**Who may file.** Any record holder of the exchange: either transactor, the operator, or a witness. …
+**Who may file.** Any record holder of the exchange: either transactor, the operator, the orchestrator, or a witness. …
-… stays in the four holders' own records.
+… stays in the six holders' own records: the two prosumers, the operator, the orchestrator, and the two witnesses.
-**Rating the adjudicator.** Whoever adjudicates — operator or witness — is rated on their conduct by both prosumers involved, and the rating enters their public distribution like any other covenant assessment.
+**Rating the adjudicator.** Wherever adjudication occurs, the parties to it rate the adjudicator: on a platform, the operator; across platforms, the witnesses. The rating enters the adjudicator's public distribution like any other covenant assessment.
-2. **Restitution** — … within the community-wide limit. Final.
+2. **Restitution** — … within the community-wide limit; in escrow, restitution is made from the held escrow (below). Final.
-4. **Expulsion referral** — … Operators and witnesses never expel; only governance does. Appealable.
+4. **Expulsion referral** — … Expulsion suspends a member's vote for a bounded term; operators and witnesses never expel, only governance does. Appealable.
+
+An operator's **bar** — ending a prosumer's activity on its own platform — is not a remedy of adjudication. It rests on at least three adjudicated −1 ratings, attached as evidence (in NTARI's instance, bylaws §12.3(b)).
+
+**In escrow.** Where a deployment operates in escrow, a −1 rating on an exchange holds that exchange's escrow for adjudication. The adjudication may return all or part of the amount to the consumer, deliver all or part of the payment to the producer, or divide it between them. The operator is rated on its adjudication and receives its payment regardless of outcome.
-… (In NTARI's instance, bylaws §2.9: submission to the office of the Vice President, a one-week rating period in the appropriate Federation Channel, and resubmission permitted after a one-week cooldown.)
+… (In NTARI's instance, bylaws §12.5 governs, including its ten-week cooldown before resubmission.)
-- **Annotated by kind.** *Deceased*, *departed*, or *adjudicated* — a death …
+- **Annotated by kind.** *Deceased*, *departed*, *adjudicated*, or *unknown* — a death …
```

## 4. Drafted edits, applied as drafted (from the plan's Confirm list)

| Edit | What was drafted, and is now in the text |
|---|---|
| B-33 | **Open question.** When an expulsion's term ends, readmission is docketed automatically under §12.5(b) and a denial continues the suspension for up to ten more weeks. The alternative, not taken, is that the vote returns automatically unless the federation votes to extend. |
| B-33 | Bar evidence is "submitted to the Governance Federation Channel" by reference and hash. "On an existing account" is read as the member's recognized membership, which §3.8 reckons per person. |
| B-18 | The Workspace Administrator keeps its substrate R&D and orchestration duties and adds governance-platform services. |
| B-12 | "Once a stack is launched and operational" is tied to the end of bootstrap under §16.2. |
| B-09 | "Expelled" removed as a kind of lapse in §3.6, since expulsion no longer ends membership. |
| B-28 | §10.6 now points to §3.2(b)–(e), breaking the loop with the new §3.2(a). |
| B-36 | §16.3 reworded because the new §16.2 removed the "service prerequisite". |
| B-05 | §3.1 says "participating as a prosumer" to match the official document. |
| J-08 | Official-document prose on what a bar costs: the record survives, its standing does not follow by default. |
| J-06 | "Catastrophic, never impossible" carried into the Record layer. |
| D-03 | The orchestrator, now a record holder, may file disputes. |
| D-10 | "Unknown" added to the design rather than dropped from the bylaws. |
| Phase 1 | The venue policy names the subordinate layers as Substrate, Record, Covenant, and Economy & Information. |
| Phase 8 (new) | Open question 11's `**Status:**` line ("open (2026-09-30)") and `**Inherits:**` line were drafted to the file's format; the body is the plan's text verbatim. The opening count moved from four to five, as CONTRIBUTING.md requires. |

## 5. Verification results (Phase 7)

- **Leftover wording:** none of the listed strings remains in any of the three files.
- **Terminology:** 38 uses in the bylaws, 9 in the official document, 6 in the dispute design, listed in full in the working notes. All read as either the Institute's suspension of the vote (expulsion) or exclusion from one platform (bar), with the two idiomatic uses the plan expects, §6.5 "a higher bar" and §7.5 "bars the Board". **One stray:** the official document's Record layer now says "Nobody can be barred from the record" (J-06, the plan's own wording); that is neither sense. Consider "put out of the record", which the same paragraph already uses.
- **Rendering** (python-markdown 3.10.3): §9.18 renders as a paragraph, not a heading; each §10.1 and §10.2 duty is its own paragraph; the §16.2 criteria render as a three-item list; the only level-two headings are the Preamble, the Articles and the Appendix.
- **Characters and layout:** U+2212 and U+2014 preserved (bylaws 13 → 16 minus signs, 57 → 62 em dashes, all from the plan's own text); LF endings, one paragraph per line, no reflow. The Lines That Cannot Be Crossed section is byte-identical to the base.

## 6. New issues found while drafting (from the plan; not fixed)

- **N-1.** §6.5 says §12.5 petitions are decided by the federation's internal majority, with no delegate vote. §12.5(d) has the delegate decide whenever the mode is not −1.
- **N-2.** A cross-platform exchange has two operators, so "six parties" describes a single-platform exchange.
- **N-3.** Trust suspension does nothing in escrow, where every trade is already collateralized; I-11 settled restitution only.
- **N-4.** D-08 pays the operator regardless of outcome in escrow disputes, but cross-platform disputes are adjudicated by witnesses (§10.9). Say whether the same rule covers them.
- **N-5.** §9.8 sends every LBTAS amendment to all five delegates under §9.2, while J-08 has the Covenant federation vote on LBTAS changes. Decide whether the Covenant vote is final for programmatic changes or feeds §9.2.
- **N-6.** The new §16.2 does not say its criteria must be met before a federation elects, so read literally they are a standing requirement. "Before the threshold" now means before every federation has elected.
- **N-7.** The governance registry (§9.5) records expulsions but not bars, though bar evidence goes to the Governance Federation Channel.
- **N-8.** §9.8 says LBTAS is "as the official document defines it". After J-08 the official document names LBTAS, but the definition still lives in bylaws §9.9–§9.11.

Found while running the plan (new, not fixed):

- **R-1.** Two v1.1 drafts (this branch and PR #3) and two rewrites of the same official-document sentence (J-10 and PR #15) now compete; see §0.
- **R-2.** The suite treats LBTAS as a product name; see §2.
- **R-3.** "Barred from the record" is a third sense of "bar"; see §5.
- **R-4.** §4.1(c) still gives non-members standing to "contest an expulsion referral", while §12.5 now speaks of "an appeal of an expulsion". Since expulsion is now the loss of a member's vote, a non-member can be referred but never expelled; the standing clause may want the same words as §12.5.
- **R-5.** The store's v1.0 carries today's unpushed §6.7 edit; see §0 item 4.
- **R-6.** The bylaws README still describes v1.0 only and lists neither the v1.1 draft nor P1-005; the plan did not ask for README changes, so none were made.

## 7. Counsel reassessment (after all changes)

Each item quotes the final text of the provisions it names.

**C-1. Board.** Kentucky's nonprofit statute sets a minimum board size and rules for vacancies. Counsel should confirm vacancies cannot take the Board below that minimum or leave it unable to act.

> **7.2 Composition and term.** From the end of bootstrap under §16.2, the Board consists of five directors, each elected by the federation bound to their office: the President by the Covenant federation, the Vice President by the Governance federation, the Secretary by the Record federation, the Workspace Administrator by the Substrate federation, and the Treasurer by the Economy & Information federation. Federations elect continuously, as terms end or as needed, for one-year terms; a director serves until a successor is elected. Until bootstrap ends, the founder board of §16.1 serves as the Board. There are no term limits; the recall of §6.8 is the discipline.
>
> **7.3 Vacancies.** A vacant office is filled by election of the federation bound to it, under §6.8. A federation whose office is vacant conducts no other governance business until it elects, and the governance software enforces this.
>
> **8.1 The offices.** The directors of the Institute are a President, a Vice President, a Workspace Administrator, a Secretary, and a Treasurer. Each is elected continuously by the federation bound to the office under §7.2, as terms end or as needed, for a one-year term, and is recallable under §6.8.
>
> **16.1 Bootstrap.** The Network Theory Applied Research Institute is currently administered by a founder board of no fewer than three and no more than five directors, developing the initial JFA stack. Until independent members recognized under §3.3 are elected to hold federation representation, the founder board serves as the Board and exercises the powers of the membership. Each act taken under this authority is recorded in the governance registry as a bootstrap act. Bootstrap acts remain valid but stand open to the membership under §2.3 like any other decision.

**C-2. Prosumer members.** The official document now authorizes prosumer membership. Counsel should confirm how Kentucky law treats voting members at platform scale, including notice, voting and records inspection.

> *Official document, Governance Layer, Orchestrator Tier:* Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software or by participating as a prosumer on a federated platform.
>
> **3.1 Membership Types.** Membership in the Institute is obtained by operating a federated instance of JFA software, or by participating as a prosumer on a federated platform under §3.8. Orchestrators run software that links operators across regions and cultures while operators run frontend software that prosumers (users) interact with. Despite the functional hierarchy, the two operating types have equal standing in governance. Where these bylaws distinguish the paths, an operating member is a member by federated instance and a prosumer member is a member under §3.8.
>
> **3.8 Prosumer membership.** A prosumer of a federated platform is a member of the Institute in the Governance layer, and in that layer alone, upon recognition under §3.3. Recognition requires at least one sealed exchange committed to the public chain, verified from the chain and never from an operator's assertion, and is reckoned per person rather than per account. Prosumer membership carries the vote of §3.4 and the candidacy of §8.3, and no duty under Article X. A prosumer member decides every matter the Governance federation decides, the amendment of these bylaws under §15.1 included — the governed hold the vote on the structure that governs them. Its weight is bounded not by subject matter but by the delegate channel of §5.3: the Governance federation carries one vote of five however large its roll grows. It lapses when the member so elects, or when no sealed exchange of that member stands on a federated platform and none is restored within ninety days; lapse is recorded by annotation under §3.6.
>
> **14.2 Books and records.** The Institute keeps the books and records that KRS Chapter 273 and its federal 501(c)(3) recognition require, alongside the governance registry of §9.5. Members may inspect the Institute's records on reasonable notice.

**C-3. Member discipline.** Expulsion suspends the vote for up to ten weeks, with a seven-day appeal and an automatic readmission docket; an operator bar needs three adjudicated −1 ratings. Counsel should confirm the procedure meets Kentucky requirements for suspending members' rights.

> **12.3 Expulsion and bar.**
>
> (a) **Expulsion.** Expulsion is the loss of a member's right to vote in the Institute, for a term of up to ten weeks. An adjudicator's referral of expulsion is filed with the Governance Federation Channel, whose members decide it and its term by majority of votes cast under §6.5. Expulsion is recorded by annotation in the governance registry, and the expelled member may appeal it under §12.5. When the term ends, the member's readmission is docketed under §12.5(b) without need of a petition; a denial continues the suspension for a further term of up to ten weeks.
>
> (b) **Bar.** A bar is the loss of a party's ability to operate on one specific platform. An operator may bar a prosumer from prosumer activity on its platform only on at least three adjudicated −1 ratings of that prosumer, attached as evidence and submitted to the Governance Federation Channel by reference and hash under §2.4; the platform software refuses a bar without them.
>
> **12.5 The appeal and readmission procedure.** Any member, and any party with standing under §4.1 or §11.4, may bring an appeal of a trust suspension, an appeal of an expulsion, a challenge under §11.4, a petition for readmission after suspension or expulsion, or a petition for re-entry by an expelled or barred operator. Each proceeds as follows:
>
> (a) **Submission.** The petition is submitted to the office of the Vice President. It contains no personally identifying information; parties and exchanges are cited by reference and hash.
>
> (b) **Rating period.** The office of the President dockets the petition in the concerned federation channel for a one-week rating period, and keeps the ratings for its study of the covenant's effects on users under §8.2. An appeal of expulsion is decided no later than seven days after its submission.
>
> (c) **Ratings.** Each member of the federation may cast one covenant rating of the offense, on the scale of §9.9, in the governance relation of §9.10(d). A −1 carries the justifying comment that §9.10(b) requires, of up to five hundred words.
>
> (d) **Decision.** If the mode of the ratings cast is −1, the petition is denied and readmission is refused. Otherwise the federation's delegate decides the petition on the record of the ratings cast, and decides it likewise where no ratings are cast. No petition is granted automatically.
>
> (e) **Resubmission.** A denied petitioner may resubmit after a ten-week cooldown.
>
> (f) **Same path for operators.** A barred or expelled operator re-enters by this same path; upon a granted petition, recognition under §3.3 proceeds on its ordinary ministerial terms.

**C-4. Money.** §11.1 now reads as a closed gate. The new escrow remedy has operators hold funds pending adjudication and get paid regardless of outcome. That is a custody question for money-transmission and escrow review, alongside §10.2 Custody.

> *§11.1, second paragraph:* A deployment switches to a hybrid or full mutual credit system only when all three of the following are true: the operator has built the capacity to manage the stage it is entering, in accordance with local laws; the prosumer network has been notified under §11.3; and the publication required by §11.2 has been made. Until all three are true, the switch may not take effect, whatever else has been done, and each of the three is a condition of this section for the purposes of §11.4.
>
> *Dispute-mechanics design §4:* **In escrow.** Where a deployment operates in escrow, a −1 rating on an exchange holds that exchange's escrow for adjudication. The adjudication may return all or part of the amount to the consumer, deliver all or part of the payment to the producer, or divide it between them. The operator is rated on its adjudication and receives its payment regardless of outcome.
>
> *§10.2:* **Custody.** Where prosumer funds or collateral are held, disclose in the platform's published rules who holds them, on what terms, and how a prosumer recovers them if the platform ceases to operate; name every third-party processor or custodian in the chain, whether or not the platform touches the funds itself. Escrow is the one stage at which a prosumer's position does not survive the operator, so the trust it requires is answered by disclosure and exit: undisclosed custody is a failure of duty under §10.6 and grounds for referral under §12.3.

**C-5. Licensing.** AGPL-3.0-or-later lets future versions of the license apply, and the specification is CC BY-SA 4.0. Counsel should confirm the contribution terms keep that floor.

> **9.4 Licensing floor.** JFA software is licensed under the GNU Affero General Public License, version 3 or any later version (AGPL-3.0-or-later), and the specification under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0). The Institute never relicenses either into proprietary terms, accepts contributions only under terms consistent with this floor, and signs no agreement that would let any party — including the Institute — close what is open.

**C-6. Records and privacy.** The orchestrator is now a record holder. Counsel should confirm the privacy floor and data retention hold with one more holder.

> *Official document, Record Layer:* The record of what happened is held by six parties: the two prosumers to the exchange, the operator, the orchestrator, and two witnesses each keep a record of their own. The hashes are also committed to one public chain, distributed across the substrate — the record for everyone who holds none of their own. The chain is append-only: harm is forgiven by annotation, never by erasing. A platform must have at least two independent witnesses; with fewer, a deployment must label itself unfederated.
>
> **2.4 The privacy floor in governance.** The shared record of the architecture carries no narratives and no identities — hashes, types, timestamps, and references only. The Institute's own public proceedings honor the same floor: filings, ballots, and published records of proceedings identify parties by reference, never by personal information beyond what the proceeding itself requires.
>
> *Official document, line 7:* No narratives, no identities in the shared record — hashes, types, timestamps and references only.

**C-7. Appeals.** Non-member prosumers can now use §12.5. Counsel should confirm nothing else makes their appeal depend on membership.

> *§12.5, opening sentence:* Any member, and any party with standing under §4.1 or §11.4, may bring an appeal of a trust suspension, an appeal of an expulsion, a challenge under §11.4, a petition for readmission after suspension or expulsion, or a petition for re-entry by an expelled or barred operator. Each proceeds as follows:
>
> *§4.1(c):* appeal a trust suspension or contest an expulsion referral through the procedure of Article XII; and

---

*Prepared with Claude Code on 2026-09-30. Working notes (edit applier, dry-run results, verification output) are in the session's scratchpad, not in either repository.*
