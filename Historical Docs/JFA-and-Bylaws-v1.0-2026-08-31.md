# Janus Facing Architecture and the Bylaws That Steward It

**Reading copy prepared 2026-08-31 · For Grace Graves, Treasurer, and Calvin Secrest, Vice President**

This document carries two instruments in full. The first is the Janus Facing Architecture — the official technical document describing a five-layer economic architecture for prosumership. The second is the bylaws of Network Theory Applied Research Institute, Inc., version 1.0, which govern the organization that stewards it.

They are printed in that order deliberately. The architecture came first and the bylaws answer to it, not the reverse. The bylaws' own §15.2 forbids any amendment that crosses the architecture's twelve lines, which means the organization has bound itself to a technical standard it can amend only in the open, and cannot quietly outgrow.

## Why the process is the argument

The premise of this work is that a platform's architecture materializes a theory of who may know and who may decide. If that is true of economic platforms, it is equally true of the governance instrument written to steward one — a bylaw that cannot be checked is the same failure as a ledger that cannot be audited. So the method used to produce these two documents was designed to be inspectable, and what follows is a plain description of it rather than a summary of the contents.

**One authoritative document.** There is exactly one official text of the architecture. A companion structure article describes it and never governs it. Prior instruments are not deleted when superseded; they are preserved, and the concepts carried forward from them are recorded in a concept triage record. A concept retired by that record stays retired unless the act reintroducing it amends the record and says so out loud.

**Twelve lines that cannot be crossed.** The architecture names twelve constraints and states the consequence of breaking one: a build that crosses any of them is not a smaller version of the architecture, it is different software wearing the name. This replaces the usual practice of describing a system by its features with describing it by what would falsify it.

**An executable conformance suite, and an honesty rule.** The document is checked against itself by a runnable test suite carrying a registry of twenty-five invariants, each with a stable identifier, the section of the document whose text must bear it, and a statement of where its enforcement lives. Only three are enforceable by the suite itself. The other twenty-two require tests beside running code, or a governance instrument — and the suite reports those as *delegated and unbound* rather than as passing. Reporting an unbound invariant as satisfied would be self-attestation wearing a test runner, and the suite refuses to do it. Consequently the honest current state is legible at a glance: three invariants proven, twenty-two awaiting the code and instruments that will bind them.

**A living record of what is not settled.** An open-questions document names every question raised and not resolved, with a status on each. It is treated as a duty rather than a courtesy: the bylaws make a stale open-questions document grounds for business in the governance channel, on the reasoning that a project which stops naming its unknowns has stopped describing itself honestly. Two questions stand open today, and both are named in it.

**Provenance, provision by provision.** The bylaws close with an appendix mapping every structural demand they answer to its source in the corpus — sixty-one entries, each naming a provision, the demand it satisfies, and where that demand came from. It is marked informative rather than operative. Its purpose is that a reader can ask of any clause "why is this here?" and get an answer that is not the drafter's memory.

**When the instrument and the standard disagree, find out which one is wrong.** This is the part most easily lost. In preparing this version the bylaws were compared clause by clause against the architecture and its twelve lines, and several divergences were found. Most were errors in the bylaws and were corrected. One was not: line 10 required that a deployment begin in escrow with "no trust extended," and the objection raised was that escrow inherently requires trusting whoever holds the funds — a custodian the operator need never disclose. That objection was correct, and it was the line that was wrong, not the bylaws. The line now reads "no counterparty credit extended," which is what it always meant, and the bylaws gained a duty requiring an operator to disclose who holds prosumer funds, on what terms, and how they are recovered if the platform disappears. The amendment is recorded in the line, in the registry note, and in the provenance appendix.

That episode is the method working as intended. A standard that cannot be found wrong is not a standard; it is a claim.

## What is deliberately unfinished

Version 1.0 was prepared and adopted by the founder board as a bootstrap act under Article XVI, and like every bootstrap act it stands open to the membership. Four things are incomplete, and are stated rather than smoothed over:

- Twenty-two of twenty-five invariants remain delegated and unbound, pending the code and instruments that will cite their identifiers.
- The organization's coordination venue is still a proprietary hosted service, held as a named interim with a committed exit to member-owned substrate.
- The governance federation is expected to remain very small, and the bylaws answer this by opening its franchise to prosumers rather than by pretending the roll will grow.
- Whether a manufactured prosumer roll could capture that franchise is an open question, recorded as such. The delegate structure bounds the damage to one vote of five; it does not eliminate it.

Version numbering restarts at 1.0 because this is the first bylaws instrument written to the architecture. The prior line, versions 6.0 through 8.0, is archived rather than amended.

## What bears on each of your offices

**Calvin — Vice President.** Article XII is where the office's powers now live, and they are deliberately narrow: audits under §12.2, expulsion referrals docketed under §12.3, and the appeal and readmission procedure of §12.5, in which the office is the venue rather than the decider. Two provisions are worth reading closely. Under §8.3 and §6.8 the office is elected *and recalled* by the Governance federation — which now includes prosumer members — with recall immediate and requiring no cause. And under §5.7 the office, sitting as that federation's delegate, casts the federation's decision rather than its own, with the registry recording the mandate beside the vote cast so the two can be compared. The powers are small; the accountability is direct.

**Grace — Treasurer.** §8.5 carries the accounts and the filings, and §9.7 draws the line the office exists to hold: the Institute's own funds are ordinary funds in the exogenous currency of its accounts, and the Institute is never a counterparty, custodian, or clearer in any exchange on the architecture. The custody duty added to §10.2 is the operator-side counterpart of that separation — operators must disclose who holds prosumer funds and how they are recovered — and it is the provision most likely to raise questions from platforms during escrow. §14.2's books-and-records requirement and §14.4's compensation discipline also sit with the office. Under §7.2 the office is bound to the Federation of Economy & Information, which elects and recalls it.

## The two parts that follow

**Part One — Janus Facing Architecture.** The official document: introduction, principles, the five layers in their three tiers, and the twelve lines.

**Part Two — Bylaws of Network Theory Applied Research Institute, Inc., v1.0.** Sixteen articles and the provenance appendix.

Both are reproduced verbatim from the working corpus, including cross-references to companion files that resolve in the repository rather than in this reading copy.

---

# Part One — Janus Facing Architecture

*Official document, as stewarded by Network Theory Applied Research Institute, Inc. Reproduced verbatim, 2026-08-31.*

---

# JFA: Janus Facing Architecture

## Introduction

Janus Facing Architecture — named for the Roman god who looks in two directions at once, just as every economic participant faces demands for both production and consumption — allows communities to address the economic reality of prosumership. Every member of an economy is not just a consumer, but a prosumer (Toffler, 1980), simultaneously producing something of value even if all they have to offer is time. It also provides an option to transform the issuance model from exogenous, chartal money (issued by an authority outside the community) to endogenous mutual credit (issued by members to one another as they transact).

The name's second face is political. Acemoglu and Robinson (2019) show that liberty survives only inside a narrow corridor where a capable state — the Leviathan — is matched by a society equally capable of checking it. Outside the corridor the Leviathan takes its other forms: absent, and coordination fails; despotic, and the coordinator dominates the coordinated; paper, and the checks exist in writing but not in effect. Staying inside the corridor demands what they call the Red Queen effect: state and society running together, each growing capacity because the other does. Every economic platform is a Leviathan in miniature — it coordinates, enforces and records — and today's dominant platforms are despotic by construction, evolving at network speed while the institutions meant to check them move at the speed of meetings.

NTARI's research locates this failure in infrastructure itself. Deliberative systems are material culture: a platform's architecture materializes a theory of who may know and who may decide, and the prevailing broadcast architectures treat participants as passive recipients (NTARI, 2025b). The resulting velocity gap is structural — information moves at network speeds while democratic synthesis stays locked to electoral cycles synched by a postal clock (NTARI, 2025a). JFA is built to close that gap from inside: the community that coordinates is the community that checks, the two capacities exchanged continuously in the same software at the same speed, disciplined layer by layer by the cost of leaving. It is a shackled Leviathan in code.

The Janus Facing Architecture (JFA) is organized into five functional layers — Substrate, Record, Covenant, Governance, and Economy & Information (E&I) — each implemented in three tiers: the frontend — for prosumer collaboration; the orchestrator — a backend providing overlapping coordination across geographic communities; and the underlying protocol — the pattern for securely handling data across tiers.

JFA software is designed for release and management in a copyleft environment, generally the GNU Affero General Public License, allowing new frontends, federations, protocols and architectures to evolve in the global market, forming a free software commons. 

This is the official document, stewarded by Network Theory Applied Research Institute, Inc. Prior instruments are preserved in [Historical Docs](Historical%20Docs/); concepts carried from them are recorded in the [concept triage](jfa-concept-triage-2026-08-24.md); what remains unresolved is named in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Principles

**Shared Responsibility.** The community that coordinates the economy is the same community that checks the coordination. The two functions are exchanged continuously — never split into rulers and ruled.

**Institutional Discipline.** Each layer is disciplined by the cost of leaving it: where leaving is cheap, competition disciplines; where leaving is dear, members get a vote; where leaving is impossible, decisions stay open to challenge.

**Lean, auditable code.** Protocol software stays small, depends on nothing but its language's standard library, and is auditable whole.

## Substrate Layer

This is the hardware where everything happens, owned by prosumers of CPUs, GPUs, printers, storage and sensors.

### Protocol Tier

Exchanges instructions and orders across a distributed compute/storage market operated on consumer grade computers hosted in homes, offices and storage, as well as repurposed industrial equipment.

### Orchestrator Tier

Federated prosumer compute power creating more options across geography.

### Frontend Tier

E&I interface for prosuming compute/storage.

## Record Layer

A compensated function of the substrate, recording and serving dialog between E&I and Covenant layers for the public.

The record of what happened is held six ways. Each party to a transaction keeps a record of their own; the operator keeps its own; two witnesses keep their own; and the hashes are committed to one public chain, distributed across the substrate — the record for everyone who was neither transactor, witness, nor operator. The chain is append-only: harm is forgiven by annotation, never by erasing. A platform must have at least two independent witnesses; with fewer, a deployment must label itself unfederated. 

### Protocol Tier

Captures, categorizes and hashes each transmission within the stack in order to establish reputation through the covenant layer and establishing the basis of an exchange medium through E&I.

### Orchestrator Tier

Federates records across geography enabling shared reputation and exchange. What federation shares is recorded truth — reputation and exchange history — never a currency unit.

### Frontend Tier

Compensated compute/record service provided by prosumers on the substrate layer E&I.

## Covenant Layer

A social contract enforced in code, informing flexible expectations for prosumer interactions.

### Protocol Tier

A simple assessment, written in executable code for prosumers to rate interactions with one another across the stack.

### Orchestrator Tier

An API serving compliant assessments across the E&I markets of the stack from substrate prosumers. When apparent breaches of the covenant occur, platform operators adjudicate between their prosumers; disputes that cross platforms are adjudicated at the witness layer. Adjudicators are rated on their conduct by both prosumers/operators involved.

### Frontend Tier

The E&I interface where the API is served.

## Governance Layer

This is where and how humans assemble to collaboratively act on the stack.

### Protocol Tier

Nonprofit, copyleft software stewardship organization.

### Orchestrator Tier

Membership in the Network Theory Applied Research Institute, obtained by operating a federated instance of JFA software.   

### Frontend Tier

The synchronous/asynchronous coordination of members governed by the organization's bylaws.

## Economy & Information Layer

The E&I layer is hosted on substrate, syndicated with the record layer, and facilitates covenant compliance.

### Protocol Tier

Each economic or information platform has a protocol designed for the exchange taking place (i.e. agriculture, a game or research citations). 

### Orchestrator Tier

E&I must run on revokable hardware obtained and recorded by the substrate layer

### Frontend Tier

Frontend designs for E&I platforms must be customizeable by the user. 

## The Lines That Cannot Be Crossed

A build that crosses any of these is not a smaller JFA; it is different software wearing the name.

1. Money is created at the moment of exchange — one balance down, one up, always summing to zero.
2. Credit is earned, never bought, and never redeemable for fiat.
3. Each community's currency is sovereign — no shared unit, no conversion between communities.
4. Value stays home; only truth crosses.
5. Cross-community exchange is two sovereign spends bound atomically by the public chain — no clearer, no exchange rate.
6. The record is append-only — forgive harm by annotating, never by erasing.
7. No narratives, no identities in the shared record — hashes, types, timestamps and references only.
8. Reputation is never one number — what others see is the count of exchanges at each rating level.
9. Reputation decides whether a member trades on trust; a community-wide limit, set by the operator and never derived from reputation, decides how much.
10. A deployment begins in escrow — collateralized, no negative balances, no counterparty credit extended — and switches to a hybrid or full mutual credit system only after the operator builds capacity, the prosumer network is notified, and the local authorizations to provide mutual credit services are published to the governance layer — or, where the jurisdiction requires none, a finding to that effect is published there instead.
11. No single host, account, or vendor whose removal could stop the network.
12. A member's positions and history survive any frontend; a community's records survive any operator.

## References

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Network Theory Applied Research Institute. (2025a, October). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, June). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Software: AGPL-3.0 · Specification: CC BY-SA 4.0*

---

# Part Two — Bylaws of Network Theory Applied Research Institute, Inc.

*P1-001 version 1.0. Reproduced verbatim, 2026-08-31.*

---

# Bylaws of Network Theory Applied Research Institute, Inc.

**P1-001 · Version 1.0 · 2026-08-31**

Prepared and adopted by the founder board as a bootstrap act under §16.1, and recorded in the governance registry under §9.5. Version numbering restarts at 1.0: this is the first instrument written to the Janus Facing Architecture, and it supersedes the P1-001 v6.0 through v8.0 line, which is archived rather than amended. Like every bootstrap act, it stands open to the membership under §2.3.

---

## Preamble

Janus Facing Architecture assigns this organization a precise seat: the protocol tier of the Governance layer — a nonprofit, 501(c)(3), copyleft software stewardship organization, governed by these bylaws. The relationships between its operator-members is the architecture's Governance orchestration. The Governance frontend is currently hosted in Slack, granted by the Salesforce Corporation. A custom platform is being developed to replace this proprietary software dependency. 

---

## Article I — The Corporation

**1.1 Name and identity.** The corporation is Network Theory Applied Research Institute, Inc. ("NTARI" or "the Institute"), a nonprofit corporation with its principal office in Louisville, Kentucky, holding federal employer identification number 92-3047136.

**1.2 Authorities referenced.** The Institute is incorporated under the Kentucky nonprofit corporation law, KRS Chapter 273, and is recognized as exempt under section 501(c)(3) of the Internal Revenue Code. The articles of incorporation carry the provisions those authorities require. These bylaws restate none of that language.

**1.3 Registered office and agent.** The Institute maintains the registered office and registered agent that KRS Chapter 273 requires. Their current identities are those on file with the Kentucky Secretary of State and are not restated here.

**1.4 Purpose.** The Institute exists to steward the Janus Facing Architecture and the commons built on it:

(a) to hold, maintain, and amend the official document of the Janus Facing Architecture and its executable conformance suite;

(b) to steward JFA software as a free software commons under copyleft terms;

(c) to conduct and publish research on network systems, deliberative infrastructure, and endogenous economics; and

(d) to educate the public in the same.

**1.5 Defined instruments.** In these bylaws, "the official document" means [janus-facing-architecture.md](../JFA/janus-facing-architecture.md) as stewarded by the Institute; "the twelve lines" means the section of the official document titled "The Lines That Cannot Be Crossed"; "the conformance suite" means the executable suite and invariant registry that verify the official document; "the dispute-mechanics design" means the design recorded in [jfa-dispute-mechanics.md](../JFA/jfa-dispute-mechanics.md).

---

## Article II — Principles

These principles are operative rules of interpretation. Every other provision of these bylaws is read to serve them.

**2.1 Shared Responsibility.** The community that coordinates is the same community that checks the coordination. The two functions are exchanged continuously among the members and are never split into rulers and ruled. No organ created by these bylaws may become a body that only decides and is never answerable.

**2.2 Gravity.** Each layer of the architecture — and each organ of this Institute — is disciplined by the cost of prosumer's ability to leave it. Where leaving is cheap, competition disciplines and these bylaws impose no gate. Where leaving is dear, the members vote. Where leaving is catastrophic, decisions stay open to challenge. Any provision of these bylaws that creates a power must name its check; a power whose check cannot be identified is void until the membership supplies one.

**2.3 No decision permanently closed.** No decision of the membership is permanently closed. Any member may bring a decided matter back before the body under §6.7.

**2.4 The privacy floor in governance.** The shared record of the architecture carries no narratives and no identities — hashes, types, timestamps, and references only. The Institute's own public proceedings honor the same floor: filings, ballots, and published records of proceedings identify parties by reference, never by personal information beyond what the proceeding itself requires.

**2.5 Append-only governance record.** The Institute forgives by annotating, never by erasing. Minutes, ballots, recognitions, publications, and decisions of record are corrected by annotation; no record of a governance act is deleted or rewritten.

---

## Article III — Membership

**3.1 Membership Types.** Membership in the Institute is obtained by operating a federated instance of JFA software, or by prosumer standing in the Governance layer under §3.8. Orchestrators run software that links operators across regions and cultures while operators run frontend software that prosumers (users) interact with. Despite the functional heirarcy, the two operating types have equal standing in governance. Where these bylaws distinguish the paths, an operating member is a member by federated instance and a prosumer member is a member under §3.8.   

**3.2 Federated instance.** An instance is federated when all of the following are true:

(a) complys with membership duties in section §10.

(b) maintains at least two independent witnesses hired from the substrate layer; an instance with fewer must label itself unfederated and does not qualify;

(c) commits its hashes to the public chain distributed across the substrate;

(d) its source, including modifications, is published as copyleft license requires; and

(e) its operation does not cross any of the twelve lines.

**3.3 Recognition.** Membership begins upon recognition by the office of the Secretary. Recognition is ministerial, not discretionary: the Secretary verifies §3.2 for an operating member, or the sealed exchange that §3.8 requires for a prosumer member, from the public chain and the published record, and records the recognition in the governance registry (§9.5). A refusal to recognize must state which condition failed and is challengeable through Article XII.

**3.4 One member, one vote.** Each member holds one vote in each federation to which it belongs, and never more than one there however many instances it operates in that layer. An operating member belongs to the federation of every layer it operates; a prosumer member belongs to the Governance federation alone. A federation's decision is carried to the Institute by its delegate under §5.3, so headcount decides within a federation and never beyond it. Governance weight, like credit, is never bought.

**3.5 Operating members are operators.** An operating member is the person or entity responsible for the operation of its instance, and its membership carries the duties of Article X for every platform economy it hosts. A prosumer member operates no instance and carries no duty under Article X.

**3.6 Lapse.** Membership lapses when the member's last federated instance ceases to satisfy §3.2 and is not restored within ninety days. Lapse is recorded by annotation, with its kind — ceased, lapsed, or expelled — and is not an erasure of the member's history. A lapsed member is readmitted by the same recognition path as a new member, except where Article XII governs.

**3.7 Continuous exchange of roles.** Every member is simultaneously a coordinator of the network and a checker of its coordination. No class of membership may be created whose function is only one of the two. Prosumer membership is not such a class: a prosumer member coordinates the network by transacting on it and checks that coordination by voting in the Governance channel.

**3.8 Prosumer membership.** A prosumer of a federated platform is a member of the Institute in the Governance layer, and in that layer alone, upon recognition under §3.3. Recognition requires at least one sealed exchange committed to the public chain, verified from the chain and never from an operator's assertion, and is reckoned per person rather than per account. Prosumer membership carries the vote of §3.4 and the candidacy of §8.3, and no duty under Article X. A prosumer member decides every matter the Governance federation decides, the amendment of these bylaws under §15.1 included — the governed hold the vote on the structure that governs them. Its weight is bounded not by subject matter but by the delegate channel of §5.3: the Governance federation carries one vote of five however large its roll grows. It lapses when the member so elects, or when no sealed exchange of that member stands on a federated platform and none is restored within ninety days; lapse is recorded by annotation under §3.6.

---

## Article IV — Prosumer Standing

**4.1 Rights that never require membership.** The architecture grants standing to prosumers directly, and nothing in these bylaws conditions those rights on membership in the Institute. Without being a member, a prosumer may:

(a) verify any commitment on the public chain against content and salt held in their own records;

(b) file a dispute as a record holder of an exchange, and rate an adjudicator's conduct, as the dispute-mechanics design provides;

(c) appeal a trust suspension or contest an expulsion referral through the procedure of Article XII; and

(d) address the appropriate Federation Channel in any proceeding that concerns them.

**4.2 Standing, and the franchise.** Prosumer standing under §4.1 is voice and process, and requires no membership. The vote is not part of that standing: a prosumer who takes up Governance-layer membership under §3.8 holds the vote as a member, on the terms of §3.4, and votes on every matter the Governance Federation Channel decides — including the election and recall of the Vice President under §8.3 and expulsion referrals under §12.3.

**4.3 The Institute serves the standing.** The offices and organs of the Institute are obligated to receive, docket, and process prosumer filings on equal terms with member filings.

**4.4 The path into membership.** Every operator provides, in the frontend of its platform, the function by which a prosumer takes up Governance-layer membership under §3.8 and thereafter raises business and votes in the Governance Federation Channel — as an operating member joins a federation through the console of §5.3. Withholding that function is a failure of duty under §10.6.

**4.5 A prosumer's vote is their own.** No operator or orchestrator casts, directs, withholds, or aggregates the vote of a prosumer member, and none conditions service, credit, or standing on how a prosumer member votes. A platform's prosumer-member votes are published as cast, so that a bloc moving together is visible on the record. Doing otherwise is a failure of duty under §10.6 and grounds for referral under §12.3.

---

## Article V — Federation Channels 

**5.1 Federation Channels.** The Institute maintains one Federation Channel for each layer of the architecture: Substrate, Record, Covenant, Governance, and Economy & Information. Each member belongs to the channel of every layer it operates. A channel is where the members of a layer troubleshoot, coordinate security, evolve the shared protocol, and conduct the layer's governance business. The Governance channel comprises, in addition, the prosumer members of §3.8.

**5.2 The appropriate channel.** Where these bylaws direct a matter to "the appropriate Federation Channel," that is the channel of the layer in which the matter arose; where a matter spans layers, the Governance channel is appropriate.

**5.3 Federation.** A federation is the community of the members of each layer (substrate, covenant, record, governance, and Economy & Information) — its operators and orchestrators, and in the Governance layer its prosumer members. Members join automatically through a console in the backend of JFA software produced by the Institute. Each federation elects one delegate, who is the director bound to that federation under §7.2. The delegate carries the federation's single vote in every matter these bylaws give to the delegates. A delegate is recallable at any time by vote of the federation that elected them, without cause and with immediate effect.

**5.4 Officer Responsibilities.** Each officer of the Institute is filled by federation-elected delegates. The federation is the body through which the members continuously check that office: it observes the office's work, and its delegate acts for the office where these bylaws so provide, including §12.5(d).

**5.5 Federation records.** Orchestrators and operators keep append-only records of their proceedings under §2.5, honoring the privacy floor of §2.4.

**5.6 Venues.** The Institute's coordination venues — the software in which channels, the federations, and assemblies meet — must be leaveable: the governance record must be exportable whole, and no venue may become a host whose removal could stop the Institute's coordination. A proprietary venue may be used only as a named interim with a committed exit. The venue in force is designated by board policy, which names it, states its interim status, and records the committed exit; changing venues is a policy act and never requires amendment of these bylaws.

**5.7 How a delegate votes.** A delegate casts their federation's vote as the federation decided it, and casts nothing else. A delegate who casts against their federation's decision, or who casts where the federation reached none, is subject to the recall of §5.3, and the governance registry records the federation's decision beside the vote cast so the two can be compared. Where a federation reaches no decision within the window of §6.4, its delegate abstains and the abstention is recorded.

---

## Article VI — Assemblies and Decisions

**6.1 Coordination, synchronous and asynchronous.** The membership acts in synchronous assembly or by asynchronous ballot. The two have equal force, and the body does not adjourn between them: the Institute stands in continuous session under §6.3.

**6.2 Annual assembly.** The membership assembles at least once each year to receive the reports of the officers and the Board and to take up the business of the Institute. Directors are elected by their own federations under §6.8, not by the assembly.

**6.3 Continuous session.** The federations and the delegates stand in continuous session in the Institute's governance venue. No matter requires a meeting to be called and no assembly is special: any member may put a matter before a federation to which it belongs at any time, and the matter opens for decision on notice under §6.4 and is decided under §6.5. Voting is conducted asynchronously, each matter establishing a voting window during which members cast their own votes. No member may delegate or assign their vote to another; a federation's delegate carries the federation's decision under §5.7 and never a member's vote.

**6.4 Notice and window.** Notice of any assembly or ballot states the matter to be decided and is published to the appropriate Federation Channel at least one week before the vote closes. The default voting window for an asynchronous ballot is one week.

**6.5 Quorum and majority.** A matter before the Institute is decided by the delegates, each federation casting one vote through its delegate under §5.3. The delegates' ballot is valid when at least three federations cast, and except where these bylaws require more the matter is decided by a majority of the votes cast.

Within a federation, the matter is decided by a majority of votes cast by its members. A federation's ballot is valid when notice under §6.4 was given and at least one member casts; in the Governance federation, at least one operating member must be among them. A federation's small roll is not a defect to be cured by a higher bar: the record of each ballot states the roll the federation then held, so a thin decision is visible rather than hidden.

Where these bylaws give a matter to a channel or a federation rather than to the Institute — including expulsion referrals under §12.3 and the petitions of §12.5 — that body decides it by the same internal majority and no delegate vote is taken.

**6.6 Open proceedings.** Assemblies and ballots are open to observation by prosumers and the public, subject to the privacy floor of §2.4.

**6.7 Reopening a decided matter.** Any member may, by filing in the appropriate Federation Channel, bring any decided matter back before the body; the filing states what decision is challenged and what outcome is sought, and the matter enters the next assembly or ballot. If the body reaffirms its decision without change, the same member may not reopen the same matter for ninety days; any other member may. A matter may not be argued using  verbiage that has been defeated more than once.  

**6.8 Elections and recall.** Each director is elected and recalled by the federation to which §7.2 binds the office, by majority of votes cast in that federation under §6.5 — the Vice President by the Governance federation, in which prosumer members vote under §3.4. Recall requires no cause and takes effect immediately.

**6.9 Deliberation procedure.** The Institute maintains a procedure for deliberating substantive matters, set by policy and resident with the governance venue rather than in these bylaws, so that it may be tuned as the venue changes. Whatever procedure is in force must satisfy the rule the covenant applies to trade: a single documented harm suffices to reopen a synthesis, and harm is never averaged into it. A procedure that averages harm, or that closes a synthesis over a documented harm, is void to that extent.

---

## Article VII — Board Governance

**7.1 Delegates, not principals.** The directors are recallable delegates of the bodies that elect them. The Board conducts the affairs of the Institute between assemblies; it does not hold what Article XV reserves to the members.

**7.2 Composition and term.** The Board consists of no fewer than three and no more than five directors. Directors are elected at the annual assembly for one-year terms and serve until their successors are elected. Each delegate is elected to their bound federation and layer: (President-Covenant, Vice president- Governance, Secretary-Record, Workspace Administrator-Substrate, Treasurer-E&I). There are no term limits; the recall of §6.8 is the discipline. 

**7.3 Vacancies.** The Board may fill a vacancy until the next assembly or ballot, at which the membership fills it.

**7.4 Action.** The Board acts in meetings, synchronous or asynchronous, on one week's notice to its members, a majority constituting a quorum and a majority of those present deciding. Board proceedings are open to observation by members, and their records are kept under §2.5. The Board holds no recurring meeting requirement: its action may be taken continuously by written consent under KRS 273.375, recorded under §2.5 like any other proceeding.

**7.5 Reserved powers.** The Board may not amend these bylaws, amend the official document, expel any party, dispose of the Institute's stewardship of the official document or the conformance suite, or dissolve the Institute. Those powers belong to the membership alone. Where these bylaws give a matter to the delegates, a director casting their federation's decision under §5.7 acts as that federation's delegate and not as the Board; this section bars the Board from deciding such a matter on its own motion.

**7.6 No gate not named.** The Board may not insert itself as an approval step in any process these bylaws or the official document define without it — including recognition under §3.3 and stage changes under Article XI.

---

## Article VIII — Directors

**8.1 The offices.** The directors of the Institute are a President, a Vice President, workspace administrator, a Secretary, and a Treasurer. Officers are elected by the membership federations at the annual assembly for one-year terms and are recallable under §6.8. 

**8.2 President.** Elected by the Covenant Federation, the office of the President directs research and development (RAND) on the Covenant Layer protocol, oversees the LBTAS API serving compliant covenant assessments to the network, and its socioeconomic effects on the federated communities. 

**8.3 Vice President.** Elected by the Governance Federation, the office of the Vice President enforces these bylaws with powers specified in Article XII. Any member of that federation may stand for the office, prosumer members of §3.8 included. 

**8.4 Secretary.** Elected by the Record Federation the Secretariat keeps governance records, performs the ministerial recognition of members under §3.3, maintains the governance registry of §9.5, receives and records the publications of Article XI, and issues the notices these bylaws require.

**8.5 Treasurer.** Elected by the Federation of Economy & Information, the office of the Treasurer keeps the accounts of the Institute, report to annual assemblies, and complies with authorities referenced in §1.2.

**8.6 Workspace Administrator.** Elected by the Substrate Federation, the office of Workspace Administration oversees RAND of the substrate protocol, substrate orchestration and the Governance Layer frontend. 

---

## Article IX — Stewardship of the Architecture

**9.1 What the Institute stewards.** The Institute stewards the official document and software stack of janus Facing Architecture, the conformance suite and its invariant registry, the concept triage record, and the living open-questions document. 

**9.2 Amending the official document.** The official document is amended only by a majority vote of the delegates, each federation having decided under §6.5. An amendment is not adopted until the conformance suite passes against the amended text. A concept retired by the triage record stays retired unless the same act that reintroduces it amends the triage record and says so.

**9.3 The open-questions obligation.** The Institute keeps its open-questions document current. A question raised in governance and not resolved is entered; a stale open-questions document means the project has stopped describing itself honestly, and any member may raise staleness as business in the Governance channel.

**9.4 Licensing floor.** JFA software is licensed under the GNU Affero General Public License (AGPL-3). The Institute never relicenses either into proprietary terms, accepts contributions only under terms consistent with this floor, and signs no agreement that would let any party — including the Institute — close what is open.

**9.5 The governance registry.** The Secretary maintains a public, append-only governance registry recording: recognitions and lapses of membership; the publications of Article XI; expulsions, readmissions, and re-entries under Article XII; and each amendment of the official document and of these bylaws. The registry honors §2.4.

**9.6 Conformance and the name.** The Institute recognizes a claim of conformance only where executable tests cite the invariant registry's IDs; every other claim it names self-attested. A build that crosses any of the twelve lines is not a smaller JFA; the Institute does not recognize it, federate with it, or count its operation toward membership.

**9.7 The Institute's money is not the federation's money.** The Institute's own funds are ordinary funds held and disbursed in the exogenous currency of its accounts. The Institute issues no currency, holds no community's credit, and is never a counterparty, custodian, or clearer in any exchange on the architecture.

**9.8 The covenant.** The covenant layer of the architecture is the Leveson-Based Trade Assessment Scale ("LBTAS"). Where these bylaws refer to the covenant, to a covenant assessment, or to a covenant rating, they refer to LBTAS as the official document defines it. The Institute stewards LBTAS under §9.1, licenses it under §9.4, and amends it only under §9.2.

**9.9 The scale.** LBTAS is a standing promise not to harm, not a marketing score. It adapts a safety methodology in which harm is a discrete event to be surfaced, never an average to be smoothed. Its scale is six meaning-loaded ordinal levels from −1 through +4, each carrying a fixed definition rather than an interchangeable point on a continuous axis. Its lowest rating, −1, means a party was harmed, exploited, or served with no discipline or with malicious intent.

**9.10 The covenant's binding rules.** No implementation is conformant to the covenant, and no member's operation satisfies §3.2(e), unless all of the following hold:

(a) **Reputation is never explicit.** No platform publishes a reputation. What it publishes is the record: the count of ratings at each of the six levels together with the total, displayed as the chart of §9.11. Reputation is what a prosumer derives for themselves by reading that chart — their own judgment of a peer's recorded rating history, never a figure the platform computes, asserts, or ranks. No system average, per-category mean, or overall score exists in any return value, report, or display. 

(b) **A −1 is the breach and it is accountable.** The −1 category in an LBTAS Chart is color coded red to visually indicate, along with the negative sign, the harm category. Harm is surfaced and never diluted, and every exchange that received one must be named. A −1 carries a justifying comment of five hundred words or less, required where the rating is written; a −1 without a comment is refused, and an overlong comment is refused rather than silently shortened. Levels 0 through +4 require no comment. Under §2.4, only the comment's hash reaches the shared record; the text stays in the rating party's own erasable records and is verified against that hash on read.

(c) **Assessment is bidirectional and symmetric.** Both parties to a sealed exchange rate each other, every claim is answerable, and a dismissal is a visible annotation, never an erasure. Where one party adjudicates or otherwise acts upon another, the rated party retains an answer path.

(d) **Ratings are typed by relation.** A rating carries the relation in which it was made so no reader collapses one relation into another. Trade, adjudication conduct, and verdict satisfaction are the relations of an economic deployment; knowledge claim and citation are the relations of an education deployment. A profile serving another domain declares its own relations and is bound by the same rule. Pooling across relations is the average forbidden by (a), committed across types instead of across ratings.

(e) **Reputation gates whether, never how much.** Reputation decides whether a prosumer transacts on trust. Sizing a commitment belongs to the economy and to the community-wide credit limit of §10.2, which is never derived from reputation. Merging the two rebuilds a credit score and is a breach of this section.

(f) **Reputation is per-platform and non-portable by default.** Identifiers are platform-scoped key hashes; human-chosen identifiers are refused. Carrying standing across platforms is a decision of the membership, never a default of an implementation.

**9.11 The LBTAS chart.** The LBTAS chart is the display method for covenant reputation. Within each category, the six levels — −1 through +4 — stand as the column titles, and beneath each column stands the tally of every rating that party has ever received at that level. The −1 column is marked in red, so the harm category is legible by color as well as by sign. The chart displays counts and the total; it displays no score. No column is pooled with another, no category is pooled with another, and no figure summarizing the chart into a single number appears on it or beside it. Where these bylaws make a decision turn on ratings, the mode of the ratings cast serves as the decision rule and is never displayed as a reputation.

**9.12 Reading is a privileged act.** Submitting a rating and reviewing accumulated records are separate capabilities, authorized separately, and authorization fails closed.

**9.13 The conformance suite.** The conformance suite is the executable instrument by which the official document is checked against itself. It consists of the runnable suite and the invariant registry it carries. The registry is what gives the official document force: an invariant not in the registry binds nothing, and a claim of conformance that cites no registry identifier is self-attested under §9.6.

**9.14 The registry and its bindings.** Each registered invariant carries a stable identifier, the section of the official document whose text must bear it, and the binding that states where its executable enforcement lives:

(a) **Document.** Enforced in full by the suite itself, against the text of the official document.

(b) **Implementation.** Enforceable only by tests living beside running code. The binding is complete when a repository ships tests citing the identifier.

(c) **Instrument.** Enforceable only by a governance instrument and its venue tooling. The binding is complete when that instrument and its tooling cite the identifier.

**9.15 Delegated invariants are reported unbound.** The suite never reports as checked an invariant it does not execute. An invariant bound to implementation or instrument is reported as delegated and unbound until something cites its identifier, and the Institute counts it as unsatisfied for every purpose these bylaws give conformance. The count of bound and unbound invariants is published with each run. Reporting a delegated invariant as passing is self-attestation wearing a test runner, and the Institute does not recognize it.

**9.16 Amending the registry.** A change to the registry — adding an invariant, retiring one, or altering its identifier, anchor, or binding — is an amendment of the official document and is made under §9.2. An identifier once issued is never reused; a retired identifier stays retired, and where an invariant descends from a retired one, the registry records the lineage.

**9.17 Maintaining the suite.** Repairs to the suite that leave every identifier, anchor, and binding unchanged are ordinary maintenance, made in the open in the Governance Federation Channel and requiring no ballot. Any member may propose a repair, and any member may run the suite: it is published and executable by anyone under §9.4, and a result no one outside the Institute can reproduce is not a result.

**9.18 A failing suite is business.** If the suite fails against the current official document, the failure is entered in the open-questions document under §9.3 and stands as business in the Governance Federation Channel until it is resolved by repair of the suite or by amendment of the document. While a failure stands, the Institute recognizes no conformance claim, membership condition, or publication as satisfied by the invariant the failure touches.
---

## Article X — Member Duties

**10.1 Orchestrator Specific.**
**Economic Orchestration** Provide operators with covenant adjudicated cross-platform information markets based on protocol; 
**Protocol Involvement** Maintain continuous integration, continuous development (CI/CD) that improves governance and maintains protocol; 
**Covenant Compliance** Serve bi-directional Covenant layer assessments at all points where orchestrators and operators exchange information or materials, according to §9.10.

**10.2 Operator Specific.** 
**Protocol Orchestration** Provide prosumers (users) with covenant adjudicated socioeconomic markets based on protocol;
**Orchestration Link** When able, link prosumer communities by broadcasting to an orchestrator; 
**Protocol Involvement** maintain CI/CD that improves governance and maintain the protocol; 
**Covenant Compliance** Serve bi-directional Covenant layer assessments at all points where orchestrators and operators exchange information or materials according to §9.10, adjudicate covenant breeches between prosumers and execute the remedies an adjudication yields.
**Defaults** annotate defaults on the record by kind — deceased, departed, or adjudicated, unknown — never erasing them; publish the platform's trailing default rate — dead credit created over a recent rolling window as a share of trade volume.
**Credit Setting** When using mutual credit, set the community-wide credit limit: one number for everyone, never set per member, and never derived from reputation
**Custody** Where prosumer funds or collateral are held, disclose in the platform's published rules who holds them, on what terms, and how a prosumer recovers them if the platform ceases to operate; name every third-party processor or custodian in the chain, whether or not the platform touches the funds itself. Escrow is the one stage at which a prosumer's position does not survive the operator, so the trust it requires is answered by disclosure and exit: undisclosed custody is a failure of duty under §10.6 and grounds for referral under §12.3.
**Witnesses** Maintain a ledger of protocol transmissions and pay two randowm witnesses from the substrate layer to monitor the same. 
**Ledger.** Maintain third party observation of covenant mediated interactions. 
**Governance Access** Provide prosumers a function in the platform frontend to join, raise business in, and vote in the Governance Federation Channel under §4.4, and never cast or direct those votes.

**10.3 Substrate Commitment.** Purchase storage and processing from a federated Substrate Market or provide your own storage and processing capacity

**10.4 Adjudication is rated.** Whoever adjudicates is rated on their conduct by both prosumers involved, and the ratings are displayed as the count of outcomes at each rating level, never as one number as a reflection of the entire platform or the witness when witnesses adjudicate.

**10.5 Dispute windows.** Where an Economy & Information category protocol is silent on its dispute window, the operator's published platform rules set the default window.

**10.6 Failure of duties.** Persistent failure of the duties of §§10.1–10.3 is a covenant matter first — adjudicated, rated, and disciplined by the market's cheap exit — and a membership matter only where it amounts to loss of a §3.2 condition or grounds for referral under §12.3.

**10.7 No institutional routing.** The Institute does not supervise, ratify, or pre-clear operators' economic management. The checks are the architecture's own: filings that land on the public chain the moment they are made, publicly adjudicatied reputation, published limits and default rates, and prosumers' freedom to leave.

**10.8 Copyleft Reporting.** Compliance with the GNU Affero General Public License, copyleft sharing principles

**10.9 Who adjudicates.** An apparent covenant breach between prosumers of the same platform is adjudicated by that platform's operator, as §10.2 provides. A dispute that crosses platforms is adjudicated at the witness layer, by the witnesses of the exchange in question, and never by either operator: neither is neutral between its own prosumer and another's. Adjudicating witnesses are rated on their conduct under §10.4 exactly as an operator is, and the dispute-mechanics design provides the procedure.

---

## Article XI — Mutual Credit Markets

**11.1 The gate.** Deployments begin with escrow as the default transaction formatting — collateralized, no negative balances, and no counterparty credit extended. The only trust escrow requires is in the operator's custody of the funds, which §10.2 requires the operator to disclose.

A deployment switches to a hybrid or full mutual credit system only when all three of the following are true: the operator has built the capacity to manage the stage it is entering, in accordance with local laws; the prosumer network has been notified under §11.3; and the publication required by §11.2 has been made. Until all three are true the switch is not gated, whatever else has been done, and each of the three is a condition of this section for the purposes of §11.4.

**11.2 Publication is the act.** Publication to the governance registry of the local authorizations to provide mutual credit services — or, where the jurisdiction requires none, of a finding to that effect — is itself the operative act, and authorizes mutual credit transactions across orchestrators. A finding that no authorization is required is an assertion on the record, contestable under §11.4 like any other condition of the gate. 

**11.3 Notification.** The applicable federation must be notified when an operator gives notice to prosumers, no less than thirty days before the switch takes effect.

**11.4 Challenges to Local Compliance.** Any member, or any prosumer of the deployment, may challenge whether the conditions of §11.1 were in fact met, through the procedure of Article XII.

**11.5 Hybrid Systems.** In a hybrid deployment, escrow and mutual credit operate across the same system and each prosumer decides which they accept. Compliance with the standards of Article XI and notices of §11.3 is the qualification for hybrid system operation. 

---

## Article XII — Discipline, Expulsion, Readmission, and Appeals

**12.1 What only the Governance Layer may do.** The Office of the Vice President enforces these bylaws across the stack by exercising the following powers.

**12.2 Audits.** Confirmation of the official record against orchestrators, witnessess, and prosumer records as well as the executed code. The Governance and adjacent Federation(s) involved in an issue may agree to commission hardware inspections.    

**12.3 Expulsion referrals.** An adjudicator's referral of expulsion is filed with the governance federation's frontend channel. The channel decides the expulsion by majority of votes cast. Expulsion is recorded by annotation in the governance registry. While expulsion from a frontend platform does not bar a prosumer or operator from joining another platform or orchestrator, it does not stop an operator or orchestrator from baring them.   

**12.4 What expulsion reaches.** Expulsion does not erase history; the expelled party's record stands, annotated. It does not reach what the architecture guarantees: a member's positions and history survive any frontend, and a community's records survive any operator or orchestrator.

**12.5 The appeal and readmission procedure.** An individual member blocked from rejoining a specific platform or orchestrator may appeal a trust suspension, a challenge under §11.4, a petition for readmission after suspension, or a petition for re-entry by an expelled or banned operator proceeds as follows:

(a) **Submission.** The petition is submitted to the office of the Vice President. It contains no personally identifying information; parties and exchanges are cited by reference and hash.

(b) **Rating period.** The office dockets the petition in the concerned federation channel for a one-week rating period.

(c) **Ratings.** Each member of the federation may cast one covenant rating of the offense, on the scale of §9.9, whose lowest rating is −1.

(d) **Decision.** If the mode of the ratings cast is −1, the petition is denied and readmission is barred. Otherwise the federation's delegate decides the petition on the record of the ratings cast, and decides it likewise where no ratings are cast. No petition is granted automatically. 

(e) **Resubmission.** A denied petitioner may resubmit after a ten-week cooldown.

(f) **Same path for operators.** A banned or expelled operator re-enters by this same path; upon a granted petition, recognition under §3.3 proceeds on its ordinary ministerial terms.

---

## Article XIII — Self-Binding of the Institute

**13.1 No chokepoint.** The Institute may not hold, own, or operate any single host, account, key, or vendor relationship whose removal could stop the network. Anything the Institute holds must be replaceable without the network noticing.

**13.2 The record survives the steward.** The official document and the software are licensed such that they survive the Institute; the public chain, the per-party records, and the exportable governance record survive it likewise. No act of the Board or the membership may impair a license already granted or a record already committed.

**13.3 Succession.** If the Institute dissolves, the membership designates a successor steward for the official document, the conformance suite, and the governance registry before dissolution completes; assets are distributed as the articles of incorporation and the authorities referenced in §1.2 require. Dissolution of the Institute is an event in the governance layer, not in the network: no deployment, currency, record, or exchange depends on the Institute's existence, only the substrate. 

---

## Article XIV — Corporate Administration

**14.1 Fiscal year.** The fiscal year is the calendar year.

**14.2 Books and records.** The Institute keeps the books and records that KRS Chapter 273 and its federal 501(c)(3) recognition require, alongside the governance registry of §9.5. Members may inspect the Institute's records on reasonable notice.

**14.3 Conflicts of interest.** Every director, officer, and delegate discloses any interest they hold in a matter before acting on it, and abstains where the interest conflicts. The Board maintains a conflict-of-interest policy consistent with the Institute's federal recognition; disclosures are recorded under §2.5.

**14.4 Compensation discipline.** Directors serve without compensation for board service. The Institute may compensate staff and contractors reasonably for services rendered, subject to the authorities referenced in §1.2. 

**14.5 Indemnification.** The Institute indemnifies its directors, officers, and delegates to the extent KRS Chapter 273 permits and its federal recognition allows, and may purchase insurance for the purpose.

**14.6 Nondiscrimination.** Membership recognition, prosumer standing, and every procedure of these bylaws are administered without discrimination; the single standard of §3.1 and the conditions of §3.2 are the only tests of membership.

**14.7 Lean instrument.** These bylaws are kept lean and auditable, as the official document requires of the code. A provision is added only where it names a power, a duty, or a check that nothing else in the corpus carries; where the official document, the conformance suite, or the dispute-mechanics design already governs a matter, these bylaws cite it rather than restate it. A provision that has become redundant is removed by amendment under Article XV.

---

## Article XV — Amendment

**15.1 By the membership alone.** These bylaws are amended only by a majority vote of the delegates, each federation having decided under §6.5 with every member of that federation holding the vote, prosumer members included, in a ballot noticed under §6.4 carrying the full text of the amendment.

**15.2 Subordination.** No amendment may cross the twelve lines, override the official document, or delete the checks that §2.2 requires each power to carry.

**15.3 Open to challenge.** An adopted amendment, like any decision, remains open under §2.3.

---

## Article XVI — Transition

**16.1 Bootstrap.** The Network Theory Applied Research Institute is currently administered by a founder board developing the initial JFA stack. Until independent orchestrators/operators recognized under §3.3 are elected to hold federation representation, the founder board exercises the powers of the membership. Each act taken under this authority is recorded in the governance registry as a bootstrap act. Bootstrap acts remain valid but stand open to the membership under §2.3 like any other decision.

**16.2 End of bootstrap.** The founder board shall be dissolved upon the election of representatives from no less than three federations. Representatives elected before the threshold shall share power with the founder board. Federations must provide E&I and orchestration services before being eligible to elect a representative. A single operator/orchestrator, whether individual or corporation may not elect themselves as a representative.

**16.3 The Governance channel during bootstrap.** The service prerequisite of §16.2 is written for federations that sell a service, and the Governance federation sells none: it hosts the instrument by which the others are governed. It is therefore eligible to elect its representative when two things are true — a recognized operating member hosts the governance platform, and the function of §4.4 is live on at least one federated platform, so that prosumers can be recognized under §3.8 and vote. Where the Governance federation holds a single operating member, the bar of §16.2 on electing oneself is satisfied by the prosumer members' votes, which that host neither casts nor directs (§4.5); a Governance federation of one operating member and no prosumer members elects no one. The founder board records in the governance registry, as a bootstrap act, the date the channel opened and the roll it then held.

---

## Appendix — Provenance of Demands

*Informative, not operative. Each structural demand these bylaws answer, and its source in the JFA corpus.*

| Bylaws provision | Demand | Source |
|---|---|---|
| Preamble, §1.4 | Nonprofit copyleft stewardship org is the Governance protocol tier | Official document, Governance Layer |
| §1.5 | The instruments named and bound: official document, twelve lines, conformance suite, dispute-mechanics design | Concept triage, 2026-08-24 (meta) |
| §2.1 | Shared Responsibility — coordinator and checker are the same body | Official document, Principles |
| §2.2 | Gravity — each layer and organ disciplined by the cost of leaving it | Official document, Principles |
| §2.3, §6.7 | No decision permanently closed | Concept triage, 2026-08-24 resolutions; bylaws-level per 2026-08-27 revision |
| §2.4, §12.5(a) | Privacy floor; no PII in filings | Official document, line 7 (L7); open questions §2, §7 |
| §2.5, §10.2 (Defaults), §12.4 | Append-only; forgive by annotation, never erasure | Official document, line 6 (L6) |
| §3.1 | Membership obtained by operating a federated instance | Official document, Governance Layer, orchestrator tier |
| §3.2(b) | Two-witness minimum; "unfederated" label below it | Official document, Record Layer (REC-witness-minimum); open questions §4 |
| §3.2(c) | Hashes committed to one public chain across the substrate | Official document, Record Layer (REC-public-chain) |
| §3.4, §6.5 | One vote per member in each federation; headcount decides within a federation and never beyond it; weight never bought | Official document, line 2 (L2), applied to governance; §2.1 |
| §3.8, §4.2 | Prosumer standing ripens into Governance-layer membership; the vote comes with it | Structure article, "Between Federations"; §2.1 |
| §4.5, §10.2 (Governance Access) | The vote is the prosumer member's own; blocs visible on the record | Official document, line 2 (L2), applied to governance |
| §5.1 | Members organized by the layer(s) they operate | Structure article, "Between Federations" |
| §5.3, §5.7, §7.1 | Federations electing recallable delegates; one federation, one delegate, one vote; mandate recorded beside the vote cast | Concept triage, carried (bylaws-level per 2026-08-27 revision) |
| §5.6 | Leaveable venues, record exportable whole; venue designated by board policy, interim status and committed exit in the bylaws | Official document, line 11 (L11); P1-001 v8.0 §3.2 |
| §6.1, §6.3 | Continuous session; asynchronous voting windows; no vote assignment | P1-001 v8.0 §§2.3, 3.9 (imported 2026-08-31) |
| §6.9 | Deliberation procedure held to the covenant harm rule; workflow lives with the venue | P1-001 v8.0 §6.3; bylaws §9.10(b); §14.7 |
| §7.1, §8.3 | Candidacy open to the electing body; directors are its delegates | Concept triage, carried (recallable delegates) |
| §7.4 | Continuous board action by written consent | KRS 273.375; P1-001 v8.0 Appendix B (P1-003) |
| §8.2 | Covenant RAND; LBTAS API serving compliant assessments to the network | Official document, Covenant Layer |
| §9.2 | Official document amended by a majority of delegates, and not adopted until the conformance suite passes | Structure article, "Legibility, mechanized"; §2.2 |
| §9.3 | Living open-questions document | Concept triage, carried (meta) |
| §9.4 | AGPL-3 software, CC BY-SA specification, copyleft commons | Official document, Introduction and footer |
| §9.6 | Conformance recognized only with registry-citing tests; else self-attested | Structure article, "Legibility, mechanized"; dispute-mechanics design §7 |
| §9.7 | Institute never a counterparty, custodian, or clearer | Official document, line 5 (L5) |
| §9.8, §9.9 | The covenant layer is LBTAS; six ordinal levels, −1 through +4 | Official document, Covenant Layer |
| §9.10(a) | Reputation is never explicit: the platform publishes the record, the reader derives the reputation | Official document, line 8 (L8) |
| §9.10(b) | −1 is the breach, surfaced and comment-justified; hash only in the shared record | Official document, lines 7 and 8 (L7, L8); dispute-mechanics design §4 |
| §9.10(c) | Bidirectional, symmetric assessment; dismissal by annotation | Official document, line 6 (L6); dispute-mechanics design §3 |
| §9.10(d) | Relations typed and never collapsed; profiles declare their own | Record model, profile row 4 (relation types) |
| §9.10(e) | Reputation decides whether, the community-wide limit decides how much | Official document, line 9 (L9) |
| §9.10(f) | Reputation is per-platform; portability is a governance decision | Open questions §5 (reputation portability) |
| §9.11 | The chart is the display — tallies by level and category, never a score | Official document, line 8 (L8); LBTAS integration guide (display rules) |
| §9.13, §9.14 | The registry gives the document force; stable IDs and three bindings | Conformance suite registry; structure article, "Legibility, mechanized" |
| §9.15 | Delegated invariants reported unbound, never as passing | Conformance suite, delegated registry |
| §9.16 | Registry changes are amendments; identifiers never reused | Conformance suite registry (lineage notes) |
| §9.17 | Suite published and runnable by anyone; repairs need no ballot | Official document, Principles (lean, auditable) |
| §9.18 | A failing suite is open business, not a silent pass | Concept triage, carried (meta); §9.3 |
| §10.1, §10.2 | Orchestrator and operator duties; operator responsibility as the frame | Dispute-mechanics design §1 (bylaws-level per 2026-08-27 revision) |
| §10.2 (Covenant Compliance) | Bidirectional covenant assessment at every exchange point; operator adjudicates and executes remedies | Official document, Covenant Layer; dispute-mechanics design §§3, 4 |
| §10.2 (Credit Setting) | Community-wide limit, one number, never derived from reputation | Official document, line 9 (L9) |
| §10.2 (Custody) | Custody disclosed, since escrow is where L12's guarantee does not reach | Official document, line 10 (L10); §2.2 (a power names its check) |
| §10.2 (Witnesses, Ledger) | Two compensated witnesses; third-party observation of covenant-mediated exchange | Official document, Record Layer (REC-witness-work); open questions §6 |
| §10.3 | Substrate purchased from a federated market or self-provided | Official document, Substrate Layer |
| §10.4 | Adjudicators rated; distribution display, never one number | Dispute-mechanics design §§1, 3; official document, line 8 (L8) |
| §10.5 | Operator's published rules set the default dispute window | Dispute-mechanics design §2 |
| §10.7 | No institutional routing; the architecture's own checks discipline | Dispute-mechanics design §1 |
| §10.9 | Operator adjudicates within a platform; witnesses adjudicate across it | Official document, Covenant Layer (COV-operators-adjudicate, COV-witness-adjudication); dispute-mechanics design §3 |
| Art. XI | Escrow start; capacity, notice, and publication all gating, all challengeable | Official document, line 10 (L10) |
| §11.5 | Hybrid stage definition by reference only | Open questions §5 (EI-hybrid retired to companion article) |
| §12.1 | Only the governance layer expels | Dispute-mechanics design §4 |
| §12.2 | Audit of the record against orchestrators, witnesses, prosumers, and executed code | Dispute-mechanics design §§6, 7 |
| §12.3 | Expulsion is platform-local; the record stands annotated | Dispute-mechanics design §4 |
| §12.4, §13.2 | Positions and records survive frontends, operators — and the steward | Official document, line 12 (L12) |
| §12.5 | VP venue, one-week federation rating, one rating each, mode −1 bars, delegate decides on silence, ten-week cooldown, same path for banned operators | Open questions §7 |
| §13.1 | No single point whose removal stops the network | Official document, line 11 (L11) |
| §14.7 | Lean instrument — lean, auditable code, applied to governance | Official document, Principles |
| §15.1 | These bylaws amended by a majority of delegates, every member of each federation voting | §2.1; §2.2 (gravity); §7.5 |
| §16.1, §16.2 | Bootstrap by founder board; each act recorded and open to challenge | Concept triage, 2026-08-24 (meta) |
| §16.3 | Governance federation sells no service; the channel opens on a live §4.4 function | §16.2; §2.2 (gravity) |

---

*Network Theory Applied Research Institute, Inc. — EIN 92-3047136 — Louisville, Kentucky — info@ntari.org*
