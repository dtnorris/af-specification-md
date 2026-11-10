# AdventureFinder

# Adventure Boundary Detection Specification

## Version 1.4

**Status:** Accepted\
**Date:** 2026-09-28\
**Purpose:** Normative editorial guidance and frontier-assisted human-review
procedure for identifying discrete published adventures, adjudicating their
canonical identity and nesting, and establishing defensible source boundaries
during ongoing AdventureFinder library ingestion.

------------------------------------------------------------------------

## 1. Purpose

This specification defines how AdventureFinder should identify, pressure-test,
review, and resolve **adventure boundaries** before creating or modifying
canonical Adventure Catalog records.

It is subordinate to the **Adventure Catalog Editorial Specification Rev
2.0**, which defines the canonical catalog and establishes that the cataloging
unit is the **discrete playable adventure**, not necessarily the commercial
product.

Version 1.0 promotes the boundary methodology from the earlier Seed Catalog
phase into the ongoing library-ingestion standard. The operational method is a
three-pass editorial process:

1.  **Phase 1 — high-recall candidate harvest:** inspect the complete relevant
    source span and retain every unit that is plausibly a playable adventure;
2.  **Phase 1b — candidate pressure / sanity review:** challenge the deliberately
    inclusive Phase 1 set against the Core Boundary, Playable Identity, and
    Minimum Adventure Substance tests without prematurely forcing canonical
    decisions; and
3.  **Phase 2 — canonical identity, nesting, and boundary adjudication:** resolve
    the surviving candidates into the approved canonical record set, including
    restrained parent/child relationships, canonical titles, and exact source
    boundaries where the evidence supports them.

The frontier model acts as an **editorial research and recommendation
assistant**. Deterministic software may prepare source evidence, bind
provenance, validate a reviewed boundary handoff, and create a successor AMC,
but it MUST NOT decide what counts as an adventure. David remains the
human/editorial approval authority.

The objective is not autonomous detection. It is a repeatable,
evidence-grounded ingestion process that preserves enough recall to avoid
missing embedded adventures while applying a deliberate pressure pass to avoid
over-segmentation.

The process must avoid both:

1.  **under-segmentation** --- collapsing multiple substantially distinct
    adventures into one product-level record; and
2.  **over-segmentation** --- treating every chapter, location, encounter,
    quest, dungeon level, or heading as a separate adventure.

The governing operational balance is:

`Phase 1 favors recall → Phase 1b applies pressure → Phase 2 establishes canon`

------------------------------------------------------------------------

## 2. Scope and Authority

This specification governs **adventure-boundary editorial decisions**:
determining what constitutes a catalogable adventure and where that
adventure begins and ends in its source.

It does not redefine the canonical catalog schema. The canonical fields
remain governed by the Adventure Catalog Editorial Specification Rev
2.0.

Boundary review should use the following evidence in descending order of
authority:

1.  **Published source structure and text**
2.  **Adventure Catalog Editorial Specification Rev 2.0**
3.  **This Adventure Boundary Detection Specification**
4.  **Accepted/locked AdventureFinder catalog records**
5.  **Prior AdventureFinder editorial methodology**
6.  **LLM inference**, only when stronger evidence is insufficient

Existing accepted records are precedents and consistency checks. They
are not rules that force every future source into the same structure.

Accepted AdventureFinder catalog records produced under this specification
form the labeled reference corpus for consistency checking, regression, and
deterministic workflow support. Existing accepted records are evidence and
precedent; they do not replace source-grounded editorial judgment.

------------------------------------------------------------------------

## 3. Governing Editorial Principles

Every boundary decision MUST preserve four principles.

### 3.1 Fidelity to the Source

Published material should be represented as accurately as possible.
Publisher-defined structure is important evidence and should not be
discarded merely because another segmentation would be convenient.

### 3.2 Evidence-Based Editorial Judgment

Boundary decisions should be grounded in observable source evidence
rather than assumptions, reputation, perceived campaign importance, or
general knowledge about the product.

### 3.3 Consistency

Structurally similar cases should receive similar treatment across the
catalog unless source evidence provides a reason for different
treatment.

### 3.4 Repeatability

Another informed editor applying this specification to the same source
should be able to understand the decision and reach a substantially
similar result.

When signals conflict, source evidence and repeatable editorial
reasoning take precedence over convenience, document layout, page count,
or assumptions about how a campaign is normally played.

------------------------------------------------------------------------

## 4. Human--Frontier--Software Editorial Model

The current boundary process has three distinct responsibilities. Keeping these
responsibilities separate is a normative trust boundary.

### 4.1 Deterministic Software Role

Deterministic tooling MAY:

-   validate canonical source registration and content hashes;
-   prepare heading, page, lexical, level, and precedent evidence;
-   produce a pre-review boundary dossier;
-   initialize and validate a structured boundary-freeze handoff;
-   verify that approved records remain bound to the intended source and base
    AMC; and
-   after human approval, derive new Adventure IDs and write a new successor AMC.

Deterministic tooling MUST NOT:

-   declare a section to be a canonical adventure;
-   infer canonical parent/child identity;
-   silently prune a plausible Phase 1 candidate;
-   invent a missing page boundary, source identity, level, or parent;
-   assign a new Adventure ID before the reviewed boundary set is frozen; or
-   mutate the selected base AMC in place.

Evidence preparation is not boundary automation.

### 4.2 Frontier Model Role

The frontier model SHOULD:

-   inspect the complete relevant source material and prepared evidence;
-   conduct the Phase 1 high-recall candidate harvest;
-   pressure-test the complete Phase 1 set during Phase 1b;
-   distinguish playable structure from document structure;
-   locate evidence for beginnings, objectives, progression, conclusions, and
    transitions;
-   identify evidence for or against substantial distinctness;
-   compare ambiguous cases with accepted precedents when useful;
-   propose canonical identity, restrained nesting, title, and source boundaries
    during Phase 2;
-   explain uncertainty explicitly; and
-   preserve enough rationale that the human editor can audit non-obvious
    decisions.

The frontier model MUST NOT treat its recommendation as canonical merely
because it is confident, and it MUST NOT assign the next `ADV-####` identifier.

### 4.3 Human Editor Role

The human editor:

-   reviews the model's evidence and recommendations;
-   requests deeper inspection when needed;
-   approves the Phase 1b candidate set when a pressure pass is complete;
-   accepts, rejects, merges, splits, or revises proposed canonical units;
-   resolves genuine ambiguity;
-   approves the final Phase 2 record set; and
-   authorizes the frozen editorial handoff from which deterministic software
    may create the successor catalog.

Human editorial acceptance is the authority that converts a proposed boundary
into canonical AdventureFinder ground truth.

### 4.4 Appropriate Use of Uncertainty

The frontier model SHOULD distinguish:

-   **source-supported fact**;
-   **editorial inference**; and
-   **unresolved ambiguity**.

It MUST NOT invent certainty when the source does not establish a boundary
clearly.

Ambiguity is not a failure. In Phase 1 it normally argues for retaining the
candidate; in Phase 1b or Phase 2 it argues for focused review, source
verification, or an explicit hold rather than fabricated closure.

------------------------------------------------------------------------

## 5. Fundamental Cataloging Unit

A canonical Adventure Catalog record represents a **complete or
substantially bounded playable scenario, mission, site-based adventure,
or story arc that possesses a recognizable playable identity**.

An adventure may be:

-   standalone;
-   one of several peer adventures in a collection or linked sequence;
    or
-   **nested within a larger adventure or campaign**.

Adventure identity is therefore not limited to units that are
independent of surrounding material. A larger adventure may contain
smaller catalogable adventures without either the parent or child losing
its canonical identity.

A candidate normally has enough internal coherence that an editor can
answer most of the following:

-   What initiates this playable unit?
-   What are the characters trying to accomplish, confront, explore, or
    resolve?
-   What material constitutes its substantive progression?
-   What marks its completion, failure, resolution, or deliberate
    transition?
-   Can this unit be meaningfully distinguished from adjacent material?

A conventional linear story arc is not required. Location-based,
sandbox, investigative, episodic, and other structures may qualify when
they form a coherent playable situation with meaningful internal
progression and boundaries.

Length alone does not determine adventure identity.

A one-page playable scenario MAY qualify.

A fifty-page chapter MAY fail to qualify if it is merely one inseparable
portion of a larger adventure.

### 5.1 Nested Adventure Principle

A **Nested Adventure** is a substantially bounded playable adventure
contained within a larger parent adventure or campaign.

A Nested Adventure MAY:

-   inherit its initial hook from the parent;
-   use the parent campaign's characters, setting, factions, or
    assumptions;
-   advance parent-campaign objectives;
-   have consequences elsewhere in the parent;
-   share NPCs, antagonists, treasures, or locations with the parent;
-   lead directly into another nested adventure;
-   be optional or mandatory;
-   overlap narratively with the parent adventure.

These dependencies do **not** disqualify it.

The relevant question is not:

> **Could this material have been published independently without
> relying significantly on its parent?**

The relevant question is:

> **Does this candidate possess a substantially bounded and recognizable
> playable identity within its parent?**

A GM should be able to meaningfully identify, prepare, run, discuss, or
select the unit as a particular body of playable material.

### 5.2 Overlapping Canonical Boundaries

Parent and child adventure records MAY overlap in page range.

Acceptance of a Nested Adventure does not require splitting the parent
adventure or removing the child's pages from the parent's canonical
boundary.

For example:

`Parent Adventure → Nested Adventure`

is a valid canonical relationship even when all pages of the Nested
Adventure are also pages of the Parent Adventure.

Page overlap is therefore not, by itself, evidence of a boundary error.

Page overlap, containment percentage, or exact interval equality MAY be used
to surface cases for editorial review but MUST NOT determine canonical adventure
identity, parentage, acceptance, rejection, merge, or boundary correction.
No overlap percentage or interval relationship has canonical semantic force.
Semantic nesting may exist even when recorded page intervals do not contain one
another. Apply the pairwise identity and boundary diagnostics in §§8.11–8.12.

------------------------------------------------------------------------

## 6. Normative Boundary Decision Procedure

For each source, boundary review SHOULD proceed through the following explicit
precondition and three editorial phases. The phases are intentionally
asymmetric: **Phase 1 optimizes for recall; Phase 1b optimizes for discrimination;
Phase 2 optimizes for canonical correctness and provenance.**

### 6.1 Precondition — Establish the Reviewable Source

Before Phase 1 begins, establish:

-   the canonical source identity and edition;
-   a validated page-addressable source representation;
-   the relevant printed/PDF page mapping and known uncertainties;
-   the complete adventure-bearing source span; and
-   enough structural evidence to see headings, nesting, and transitions across
    that span.

A deterministic dossier MAY prepare this evidence. Such a dossier is evidence,
not a candidate list and not an editorial classifier.

If the source identity, page addressing, or relevant review span is uncertain,
resolve or explicitly preserve that uncertainty before making exact canonical
claims.

### 6.2 Phase 1 — High-Recall Boundary Harvest

#### Step 1 — Establish Product Structure

Determine the product's broad structural class:

-   standalone adventure;
-   anthology / collection;
-   linked adventure sequence;
-   campaign / large integrated adventure;
-   sourcebook with embedded adventure material;
-   scenario / encounter collection; or
-   hybrid or ambiguous structure.

This classification establishes a starting hypothesis, not a final answer.

#### Step 2 — Exhaustively Identify Plausible Adventure Units

Review the complete relevant source span, including the table of contents,
major headings, introductions, transitions, conclusions, nested headings,
scenario/mission/quest language, level guidance, and other structural evidence.

The Phase 1 standard is:

> **plausible enough to inspect, not already proved canonical.**

Phase 1 SHOULD deliberately favor inclusion. In particular:

-   obvious parent material and plausible embedded children should both be
    represented;
-   a candidate MUST NOT be excluded merely because it is short;
-   a candidate MUST NOT be excluded merely because it is embedded inside a
    larger authored adventure or campaign;
-   a rich location, framework, sequence, or side scenario that plausibly crosses
    the Location-to-Adventure or Playable Identity threshold should be retained
    for later pressure testing; and
-   when uncertainty is material, the reviewer should normally **increase
    recall and carry the question forward** rather than silently prune it.

A chapter or location heading is a reason to inspect a unit, not a reason to
catalog it.

At minimum, the Phase 1 working set SHOULD preserve for each candidate:

-   a stable source-local temporary key;
-   provisional title;
-   printed-page span or explicit page uncertainty;
-   optional PDF-page span;
-   apparent parent/nesting context;
-   concise evidence for playability; and
-   open questions or counterevidence to pressure-test in Phase 1b.

**Phase 1 PASS** requires that the complete relevant span was reviewed, plausible
embedded units were not lost merely because of nesting, borderline candidates
were retained for Phase 1b, and the evidence trail is sufficient to reconstruct
why each candidate entered the working set.

### 6.3 Phase 1b — Candidate Pressure / Sanity Review

Phase 1b exists because a deliberately high-recall Phase 1 set will often be too
large to treat as canonical. Its purpose is to challenge that set without
swinging back into the under-segmentation bias that Phase 1 was designed to
avoid.

Start from the **complete Phase 1 working set**. Do not silently begin from a
pruned chat summary or a remembered shortlist.

For every candidate, apply as appropriate:

1.  the **Core Boundary Test**;
2.  the **Playable Identity and Substantial Distinctness Test**;
3.  the **Location-to-Adventure Threshold**;
4.  the **Minimum Adventure Substance Test**;
5.  the **Authored Play Spine and Reviewer-Completion Rule**;
6.  parent-dependence analysis without treating dependence as automatic
    disqualification; and
7.  accepted AdventureFinder precedent when the primary source leaves more than
    one plausible interpretation.

Phase 1b SHOULD be especially skeptical of borderline candidates whose apparent
identity is principally a chapter heading, travel segment, single encounter,
room cluster, isolated puzzle, framework, quest hook, or rich location without
a coherent localized body of play.

When the publisher explicitly frames a candidate as a **quest hook**, **adventure
hook**, **adventure seed**, **idea for an adventure**, or similar generative
material, that framing is strong Phase 1b counterevidence. It is not an
automatic rejection: unusually complete short-form material may still qualify.
But the burden is on affirmative source evidence that the publisher has supplied
a substantially bounded body of play, not merely a detailed premise from which a
GM could create one. Apply the Publisher-Designated Hook, Seed, and
Adventure-Idea Rule in §9.2.

Whether or not the publisher uses hook/seed language, apply the Authored Play
Spine and Reviewer-Completion Rule in §9.3 whenever apparent adventure identity
depends on the reviewer supplying connective play that the source itself does
not meaningfully author.

#### Survivor Play-Spine Proof

Before any candidate is marked **RETAIN FOR PHASE 2**, the reviewer MUST record
a compact four-part play-spine proof:

1.  **Entry** — what source-supported condition, event, arrival, assignment, or
    situation brings play into this unit?
2.  **Authored middle** — what substantive scenes, locations, procedures, clue
    chains, encounters, state changes, decisions, or other published progression
    does the source actually provide?
3.  **Resolution / exit** — what source-supported success, failure, state
    change, departure, or deliberate transition marks the end of the unit?
4.  **Reviewer completion** — what connective play, if any, must the GM or
    reviewer still invent in order for the candidate to function as the proposed
    adventure?

The **authored middle** MUST identify published playable development rather than
merely restating a summary verb such as investigate, infiltrate, retrieve,
explore, rescue, escort, or stop.

Routine adjudication, improvisation, encounter tuning, and player-driven
variation do not count as disqualifying reviewer completion. The relevant
warning sign is that the GM must invent the **central connective structure**
between the candidate's premise and resolution.

If the authored middle cannot be stated without mentally supplying material
connective play that the source does not meaningfully provide, the candidate
MUST NOT be retained as though the play spine were established. It should
instead be rejected under the applicable rule or placed on **HOLD — SOURCE
VERIFICATION / HUMAN DECISION REQUIRED**.

The proof MAY be terse for obvious cases. Its purpose is to expose reviewer
completion early, not to create unnecessary prose.

For a proposed Nested Adventure, the Survivor Play-Spine Proof does not replace
the pairwise **Incremental Playable Identity** comparison in §8.11. Before
retaining the candidate for Phase 2, the reviewer MUST record what distinguishes
its playable unit from the proposed parent's at the represented scale, or carry
unresolved identity/parentage on hold. A concise comparison suffices for obvious
nesting. When redundancy is suspected, apply **Boundary-Before-Identity**
(§8.12) before recommending rejection or merger on that ground; richness and
Entry → Middle → Resolution alone cannot establish a second Adventure ID.

At the same time, Phase 1b MUST preserve the governing lessons:

`embedded ≠ non-adventure`

`campaign-dependent ≠ non-adventure`

`short ≠ non-adventure`

When short-form precedent is useful, compare borderline candidates against
accepted short or one-page adventures by **playable substance and bounded
identity**, not page count alone.

#### Homogeneous Sibling-Set Calibration

When a source presents three or more materially similar candidates through a
repeated authorial template — for example **Landmarks**, **Sites**, **Missions**,
**Schemes**, **Cases**, **Quests**, or another recurring format — Phase 1b MUST
perform a contrastive calibration before Phase 2.

If the sibling set contains both retained and rejected candidates, identify:

1.  the **weakest retained** candidate;
2.  the **strongest rejected** candidate; and
3.  the source-grounded distinction that causes them to fall on opposite sides
    of the canonical threshold.

If the set is uniformly retained or uniformly rejected, identify the two
closest-to-threshold siblings and state why the same disposition remains
appropriate for both.

Then recheck the materially similar sibling set against that distinction.

The controlling distinction SHOULD concern playable identity, authored
progression, binding structure, or minimum substance rather than page count,
room count, density of lore, or publisher formatting alone.

This calibration is proactive. It applies even when no earlier candidate has
yet been overturned. **Systemic Survivor Revalidation** remains the corrective
rule when a false-positive pattern is discovered after an initial survivor set
has already formed.

#### Systemic Survivor Revalidation

When focused review overturns one or more retained candidates because of a
failure mode that may also apply to other survivors, the reviewer SHOULD NOT
treat the correction as isolated without checking the remainder of the
materially similar candidate set.

Before Phase 2 freeze, re-pressure-test all materially similar survivors against
the newly exposed distinction.

Examples include discovering that the review has been:

-   supplying omitted connective play;
-   treating a mission wrapper as sufficient adventure substance;
-   mistaking rich locations for localized adventures;
-   treating geographic depth as authored adventure progression;
-   promoting adventure-generating ingredients into adventures;
-   accepting one-encounter scenarios too readily; or
-   proving each survivor's own play spine without testing redundant identity
    or scale relative to its proposed parent (§§8.11–8.12).

This revalidation need not reopen clearly unrelated candidates. Its purpose is
to prevent a stale survivor set produced under a threshold that the review
itself has demonstrated to be too permissive.

A Phase 1b candidate may be:

-   **RETAIN FOR PHASE 2**;
-   **REJECT — STRUCTURAL / NON-ADVENTURE**;
-   **MERGE WITH PARENT / ADJACENT CANDIDATE**;
-   **SPLIT FOR PHASE 2 REVIEW**; or
-   **HOLD — SOURCE VERIFICATION / HUMAN DECISION REQUIRED**.

Where useful, a disposition SHOULD also carry one or two compact diagnostic
reason tags. These tags are explanatory aids, not a scoring system and not
deterministic classifiers.

Recommended vocabulary includes:

-   `CLEAR_SCENARIO`
-   `DIRECTED_SITE`
-   `PARENT_SUPPORTED_SCENARIO`
-   `MACRO_ARC`
-   `HOOK_OR_SEED`
-   `RICH_LOCATION_NO_SPINE`
-   `ONE_CHALLENGE`
-   `SUMMARY_VERBS`
-   `MISSION_WRAPPER`
-   `ADVENTURE_GENERATOR`

The controlled vocabulary MAY expand when repeated reviews expose a genuinely
new failure mode or qualifying pattern. A tag MUST NOT substitute for the
source-grounded rationale.

Phase 1b is a pressure pass, not the final canonical freeze. A candidate that
remains genuinely ambiguous SHOULD normally be retained or held for Phase 2
rather than rejected merely to reduce the count.

**Phase 1b PASS** requires an explicit disposition for every Phase 1 candidate,
a Survivor Play-Spine Proof for every candidate retained for Phase 2, the
pairwise comparison in §8.11 for every proposed Nested Adventure retained, a
Homogeneous Sibling-Set Calibration when materially similar repeated-template
candidates are present, a reviewed and defensible candidate set ready for
canonical identity/nesting adjudication, and reasonable confidence that any
newly exposed systemic false-positive pattern has been applied consistently
across materially similar survivors.

### 6.4 Phase 2 — Canonical Identity, Nesting, and Boundary Adjudication

Phase 2 resolves the Phase 1b set into the canonical record set.

For every surviving or held candidate, determine:

-   genuine standalone / parent adventure, peer adventure, or nested adventure;
-   whether apparently playable material is instead a reusable location,
    campaign-support framework, subordinate structural unit, or non-adventure;
-   restrained parent/child relationship, if any;
-   canonical title;
-   canonical printed Start Page and End Page;
-   optional PDF-page boundaries where useful; and
-   Level Start / Level End only when explicitly or editorially established by
    the source under the governing catalog/level rules.

Phase 2 may accept, reject, merge, split, or hold candidates, but each decision
SHOULD remain traceable to the Phase 1 evidence and Phase 1b pressure result.

#### Exact Boundary Requirement

Only after a candidate qualifies as an adventure should exact page boundaries
be assigned.

Each proposed boundary MUST be tied to affirmative source evidence. Exact page
boundaries MUST NOT be inferred solely from gaps between extracted page markers,
neighboring section boundaries, expected pagination, page counts, or document
structure.

When the available source does not affirmatively establish an exact boundary,
the boundary MUST be marked **Uncertain / Requires Source Verification** rather
than estimated.

For an End Page, finding conclusion, aftermath, epilogue, reward, or other
ending material does not itself establish that the adventure has ended. The
reviewer MUST continue sequentially through the available source until
affirmative evidence establishes the termination of the adventure-owned
semantic unit.

#### Precedent Rule

Use accepted AdventureFinder records when the primary source evidence leaves
more than one plausible interpretation. Precedent helps resolve ambiguity; it
does not override explicit source evidence.

**Phase 2 PASS** requires:

-   every Phase 1 candidate has a traceable final or held disposition;
-   every accepted record has a canonical title and source-evidenced printed
    page boundaries;
-   parent/child relationships are restrained and internally consistent;
-   locations/support frameworks are not promoted merely because they are rich;
-   independently runnable embedded units are not lost merely because they have
    a parent;
-   optional levels are included only when editorially established; and
-   unresolved questions are held rather than papered over.

### 6.5 Structured Freeze and Deterministic Catalog Handoff

After David approves the complete Phase 2 result, the accepted record set SHOULD
cross from frontier-assisted editorial review into deterministic software through
a narrow, validated structured handoff.

The current implementation contract is `af-boundary-freeze/v0.1`. The boundary
specification does not require that contract to remain forever at v0.1, but any
successor contract MUST preserve these invariants:

-   bind the reviewed records to the exact canonical source and explicit base
    AMC provenance;
-   preserve stable source-local record keys and concise editorial rationale;
-   represent restrained parentage without requiring a broad relationship
    taxonomy;
-   carry only editorially established optional metadata;
-   require explicit human approval before the artifact becomes frozen;
-   contain **no newly assigned Adventure ID**; and
-   fail closed on invalid provenance, impossible page spans, invalid parentage,
    or unresolved required fields.

Only after that reviewed handoff validates may deterministic software assign new
Adventure IDs and create a **new successor AMC** from the explicit base AMC.
The base AMC MUST NOT be mutated in place, and unassessed scoring fields for new
records MUST remain blank.

------------------------------------------------------------------------

## 7. Core Boundary Test

A candidate SHOULD normally satisfy the following four-part test.

### 7.1 Beginning

There is an identifiable entry into the playable unit.

Evidence MAY include:

-   an explicit adventure title;
-   an adventure-specific introduction;
-   a hook, assignment, inciting event, or starting situation;
-   arrival at a location with a distinct mission or playable situation;
-   a deliberate transition from a prior adventure;
-   publisher language indicating that a new adventure begins.

A heading by itself is weak evidence unless supported by playable
structure.

### 7.2 Objective or Playable Purpose

The candidate has a discernible objective, problem, situation, conflict,
or dramatic purpose that gives the unit coherence.

The objective need not be singular or explicitly stated. Sandbox and
location-based adventures can qualify when the location or situation
itself provides coherent goals, conflicts, opportunities, or pressures.

### 7.3 Progression

The candidate contains substantive playable development between
beginning and ending.

Progression MAY consist of:

-   exploration;
-   investigation;
-   social interaction;
-   meaningful travel;
-   dungeon traversal;
-   escalating encounters;
-   linked scenes;
-   faction interaction;
-   branching objectives;
-   problem solving;
-   other meaningful player-driven development.

A transition scene or isolated encounter without sufficient independent
progression SHOULD NOT normally become a canonical adventure.

### 7.4 Conclusion or Deliberate Transition

There is an identifiable point at which the candidate resolves, fails,
concludes, or deliberately hands play into a new substantially distinct
unit.

Evidence MAY include:

-   explicit conclusion or aftermath text;
-   completion of the principal objective;
-   a final confrontation followed by resolution;
-   departure from the principal adventure site;
-   reward/return/reporting sequence;
-   a clear transition into another named adventure;
-   the beginning of a new independent premise.

The ending does not need to close every plot thread.

------------------------------------------------------------------------

## 8. Playable Identity and Substantial Distinctness Test

Passing the Core Boundary Test is necessary but not always sufficient.

The previous thought experiment---whether material would still function
if presented separately---can over-penalize legitimate nested
adventures. Version 0.5 therefore uses a **Playable Identity Test**.

Ask:

> **Does this candidate possess a recognizable playable identity
> distinct from the continuous connective tissue of its parent
> adventure?**

Evaluate the following signals. For proposed Nested Adventures, apply the
pairwise test in §8.11 as well; internal coherence and substantial authored
material alone do not establish distinctness from the enclosing adventure.

### 8.1 Entry

Can a GM identify when play meaningfully enters this scenario, site,
mission, or localized situation?

### 8.2 Situation

Does the unit establish its own localized problem, objective, threat,
mystery, exploration premise, conflict, or dramatic situation?

### 8.3 Body of Play

Does it contain enough substantive play to constitute more than an
encounter, transition, waypoint, or isolated scene?

### 8.4 Internal Coherence

Do its encounters, locations, NPCs, factions, discoveries, and choices
primarily participate in the same localized playable situation?

### 8.5 Exit or Resolution

Can a GM identify when the scenario has substantially resolved, failed,
been abandoned, or handed play back to the parent campaign?

### 8.6 Addressability

Would a statement such as:

> "We are running/playing **\[this unit\]**"

meaningfully identify a particular body of playable material rather than
merely a room, chapter heading, or geographic waypoint?

Addressability is supporting evidence, not a popularity test. A unit
need not have been marketed independently or commonly discussed by
players.

### 8.7 Replaceability

Could the parent campaign theoretically omit, replace, relocate, or
substantially alter this unit while remaining recognizably the parent
campaign?

A positive answer is evidence that the unit has distinct identity.

Replaceability is not mandatory. Some nested adventures may be
structurally important to the parent campaign while still possessing
their own playable identity.

### 8.8 Positive Evidence

Positive evidence includes:

-   a complete or deliberately bounded playable arc;
-   a localized objective or playable situation;
-   its own premise, mission, threat, mystery, or exploration problem;
-   a distinct entry condition;
-   a distinct site or region supporting a coherent body of play;
-   multiple related encounters, interactions, discoveries, or
    decisions;
-   meaningful internal progression;
-   its own climax, resolution, state change, or deliberate endpoint;
-   explicit publisher presentation as an adventure;
-   publisher treatment as a discrete milestone-bearing area or
    objective;
-   practical GM addressability and preparation as a unit;
-   replaceability within the parent campaign;
-   prior or subsequent independent publication of substantially
    equivalent material.

### 8.9 Counterevidence

Counterevidence includes:

-   pure travel between larger units;
-   shared campaign setup without a localized playable situation;
-   book-level rules or setting material;
-   a single encounter embedded in a larger arc;
-   a quest hook whose substantive play occurs elsewhere;
-   explicit publisher presentation as a quest hook, adventure hook, adventure
    seed, idea for an adventure, or similar generative material, especially when
    the source says the unit is intended to launch, flesh out, inspire, or
    provide ideas for an adventure;
-   a candidate that supplies premise, patron, objective, antagonist, twist, or
    outcome while summarizing or omitting most of the playable development that
    connects those elements;
-   apparent adventure substance that depends on importing generic setting,
    location, faction, monster, or lore material that the source does not
    integrate into the candidate's playable progression;
-   apparent scoreability that depends materially on imagining ordinary
    GM-created implementation rather than assessing published playable content;
-   a dungeon level whose role is simply continuous traversal toward the
    same objective;
-   a chapter break without a new playable premise;
-   a location whose keyed content lacks a coherent localized scenario;
-   a campaign event without enough supporting play to constitute an
    adventure.

### 8.10 Independence Is Not Required

The following are NOT automatic counterevidence:

-   inheriting a hook from the parent;
-   requiring parent-campaign context;
-   sharing characters or NPCs with the parent;
-   advancing a campaign-wide objective;
-   containing consequences elsewhere in the campaign;
-   leading directly into another nested adventure;
-   overlapping the parent's page range.

The governing distinction is:

`campaign-dependent ≠ non-adventure`

and:

`embedded ≠ non-adventure`

### 8.11 Pairwise Incremental Playable Identity

A candidate may possess a coherent source-authored play spine and still fail to
justify a separate canonical Adventure ID if its proposed playable identity is
substantially the same as the enclosing adventure's at the represented scale.
This is **redundant identity / redundant scale**, including subsumptive overlap:
two proposed records substantially represent the same playable unit at nearly
the same scope, even though the child contains genuine adventure substance.

For each proposed Nested Adventure, compare it with the proposed enclosing
adventure and ask:

> **What source-authored playable progression does this child identify that the
> enclosing adventure does not already represent at substantially the same scope?**

The reviewer MUST compare both units' entry, organizing middle, principal body
of play, and resolution or handoff, including the parent's playable structure
outside the child where present. State the source-supported distinction, rather
than merely repeating the child's Survivor Play-Spine Proof. In a nesting chain,
the comparison is pair-specific: distinctness from a broad campaign does not
establish distinctness from a nearer proposed parent, and a finding at one level
does not automatically transfer to another.

Affirmative evidence may be a materially distinct phase or reset, localized
operation, separately organized procedure, consequential handoff, branch,
distinct state transition, or identifiable body of preparation/play grounded in
such authored organization. These are alternative forms of evidence, not a
mandatory feature checklist. A state change or branch label alone is not
sufficient if it merely redescribes the enclosing unit's central progression.

A different heading, an alternate objective threaded through the same
progression, the name of the principal site or antagonist, a different
descriptive framing, or the child's richness and preparability alone do not
answer the pairwise question. A secondary objective may contain consequential
authored play yet fail to identify another adventure when it is distributed
through substantially the same principal dungeon, antagonist, climax, and
represented body of play. Removing a title or objective sentence may help expose
the underlying structure, but surviving that counterfactual proves neither
acceptance nor rejection.

**Incremental identity is a semantic distinction between playable units, not
additional pages or play outside the parent.** A legitimate child MAY share
pages, the parent's ultimate objective, antagonists, a climax or final outcome;
inherit its hook; be mandatory or campaign-dependent; be site-based or short;
and provide the majority of the parent's page span. None of these properties,
alone or in combination, substitutes for examining how the source organizes the
two units. A local unit within a materially broader composition can qualify
even when its resolution is also the parent's finale.

Do not require independent publication or independent runnability, a unique
antagonist or reward, an unshared ending, or completion before the parent.
Intrinsic site spines remain valid (§9.3); proving one is not a waiver of this
pairwise comparison. Retrieval convenience cannot manufacture playable identity.

When source evidence establishes redundant identity or scale after §8.12,
recommend against representing both proposed units as separate canonical
adventures at those scopes. This finding does not establish that the material
lacks authored play, decide which existing record should survive, or authorize
any catalog correction. When evidence supports competing interpretations or is
insufficient, preserve an explicit hold/ambiguity for human judgment rather
than forcing acceptance or rejection.

### 8.12 Boundary-Before-Identity Diagnostic

When a proposed child appears overly subsumed or redundant, the reviewer MUST
ask before concluding that its identity fails:

> **Is the apparent redundancy an identity defect, or would a different
> source-supported boundary reveal a legitimate distinct adventure?**

First verify the proposed relationship against source structure. Page
containment does not establish that one unit semantically contains the other.
Inspect the ownership of setup, progression, adjacent material, completion, and
handoff. Consider omitted child material as well as improperly absorbed parent
material; do not assume that shortening the child is the remedy.

Distinguish and record the supported diagnosis, or unresolved alternatives:

1.  **Redundant identity / redundant scale:** both records substantially
    represent the same playable unit at nearly the same scope; intrinsic
    adventure substance does not justify the second identity.
2.  **Boundary defect:** a legitimate child identity may exist, but its proposed
    span absorbs parent material or omits necessary child material. The identity
    question and the correctness of the present span require separate evidence.
3.  **Relationship-direction / geometry defect:** interval containment or
    equality suggests a relationship that the source does not support; the
    units may be peers or the apparent direction may be wrong. Do not use the
    geometric relationship as established editorial parentage.
4.  **Legitimate nested identity:** the source supports two defensible playable
    units at different compositional scales, despite shared material.

These are editorial diagnoses, not deterministic classes or automatic catalog
actions. Where more than one defect is plausible, preserve the alternatives and
the evidence needed to distinguish them.

**Boundary-Before-Identity does not reverse the Phase 2 exact-boundary rule.**
It reviews provisional scope to avoid mistaking a bad span for a failed identity;
exact canonical boundaries are assigned only after the unit qualifies. It
MUST NOT authorize automatic shortening, interpolation, or an exact replacement
boundary without affirmative source evidence. Apply §§16–18, especially
Source-Evidenced Pagination (§18.2.1) and End-Boundary Exhaustion (§18.2.2).
Missing evidence remains **Uncertain / Requires Source Verification**. Existing
accepted records require explicit human correction review; no diagnosis silently
changes their identity, pages, parentage, or Adventure IDs.

### 8.13 Pairwise Regression / Calibration Examples

These are source-grounded editorial calibration judgments at the represented
scopes, not universal rules about sites, rescues, trials, or shared endings.
They illustrate §§8.11–8.12; they do not direct catalog mutations or establish
replacement boundaries. The negative cases acknowledge real authored middles.

| Pair | Expected pairwise finding | Controlling distinction |
| --- | --- | --- |
| **The Well of Dragons / Tiamat's Return** (ADV-0494 / ADV-0484) | Redundant-scale representation at the reviewed AMC scopes. | The substantial finale site and the enclosing record largely represent the same principal progression, ritual confrontation, and resolution. Proving the site is rich does not distinguish a second unit. Which record or boundary to retain is a separate correction decision. |
| **Salsvault / Traveling to Eiselcross** (ADV-0662 / ADV-0661) | Redundant-scale representation at the reviewed AMC scopes. | Salsvault is intrinsically a substantial keyed dungeon. The human-reviewed pair nevertheless substantially represents the same cure expedition at those scales; intrinsic dungeon substance does not settle the pairwise issue or the eventual correction mechanism. |
| **The Traitorous Thanes / The Ghost Ship Ultros** | Reject the Thanes as a separate adventure at the proposed scope. | Differentiated ghost encounters and dream-state play are real, but substantially constitute Ultros's central trial and its captaincy resolution. A meaningful state change alone does not distinguish another unit at that breadth. |
| **Corinna's Friends / Mossy Temple** | Reject Corinna's Friends as a separate Adventure ID at the proposed scope. | Consequential rescue play and distinct victim outcomes exist. The secondary objective is distributed through substantially the same principal dungeon, antagonist, climax, and represented body of play. This is not a missing-authored-middle finding. |
| **The Missing Centaurs / The Mithral Forge** | Accept a distinct Nested Adventure. | A separate commissioner, localized branch, named victims, time-sensitive rescue state, return/report, and reward organize a bounded operation that can complete before the enclosing forge labor. Its shortness does not erase that structure. |
| **A Boom in the Night / Dangerous Designs** (ADV-0656 / ADV-0655) | Retain distinct nested identity. | The investigation and capture operation has its own contract completion and transition to the later lair phase. Continued campaign context does not collapse those source-authored phases. |
| **Uldrak's Grave / Demon Zapper** (ADV-0406 / ADV-0403) | Retain distinct nested identity despite high page overlap. | At the reviewed scope the child represents the source-linked restoration subquest, including bargains, blood recovery, transformation, and departure before Ralzala's separate release. It is not just the short location paragraph; overlap does not erase the operation. |
| **Death House / Curse of Strahd** | Retain distinct semantic nesting. | The published mini-adventure organizes house exploration, dungeon progression, and a localized resolution/escape within campaign context. Independent publication/run context is not required, and an appendix's position outside the recorded campaign interval does not negate semantic nesting. |
| **Skyreach Castle / Castle in the Clouds** (supporting shared-ending control) | Retain the source-supported site adventure. | Village/pursuit play gives way to a separately organized mobile-fortress operation with infiltration, factions, and control/crash outcomes. Sharing the enclosing adventure's ending does not erase that compositional distinction. |

The positive controls do not make early completion, a separate commissioner,
optional play, or an unshared climax mandatory. The negative controls do not
make a principal site, rescue objective, shared climax, or campaign dependence
disqualifying. Apply the source comparison, not analogy by label alone.

## 9. Preserve Authorial Structure

AdventureFinder SHOULD preserve the author's or publisher's intended
adventure structure whenever practical.

Explicit publisher segmentation is especially strong evidence in:

-   anthologies;
-   adventure collections;
-   trilogy products;
-   separately titled scenarios;
-   products with independent adventure introductions and conclusions.

Publisher formatting is not infallible. A chapter label does not
automatically create an adventure, and a campaign book is not
automatically one indivisible adventure.

#### Positive Publisher Designation

Explicit publisher labels such as **adventure**, **scenario**, **mission**, or
**self-contained scenario** are strong evidence that the publisher intends the
material to function as a recognizable playable unit.

Such a positive designation:

-   MUST guarantee Phase 1 inspection when it falls within the relevant source
    span;
-   SHOULD create a strong presumption of intended playable identity; and
-   MAY help resolve ambiguity when the source-authored body of play is close to
    the canonical threshold.

It does **not** waive the Core Boundary, Playable Identity, Authored Play Spine,
Location-to-Adventure, or Minimum Adventure Substance tests.

The relevant distinction is:

> **Publisher framing helps establish what the author intended the unit to be;
> AdventureFinder must still determine whether the published text actually
> supplies enough bounded playable substance for canonical adventure identity.**

Therefore:

`publisher-designated scenario ≠ automatic canonical adventure`

The governing distinction is:

> **document structure ≠ necessarily playable adventure structure**

Likewise:

> **meaningful internal structure ≠ necessarily canonical adventure
> identity**

### 9.1 Historical or External Adventure Identity

Evidence that substantially equivalent material was previously or
subsequently published, marketed, adapted, or commonly run as a
standalone adventure is **strong supporting evidence** that an embedded
version may retain adventure identity.

This evidence MUST NOT automatically establish the boundaries of the
current version.

The editor must still determine whether the current presentation retains
a substantially coherent playable unit under the Core Boundary and
Playable Identity tests.

Historical identity is therefore:

`strong supporting evidence ≠ automatic acceptance`

This rule is particularly useful when later campaign products embed,
expand, remix, or surround material that previously existed as a
standalone adventure.

### 9.2 Publisher-Designated Hook, Seed, and Adventure-Idea Rule

When a source explicitly presents material as a **quest hook**, **adventure
hook**, **adventure seed**, **scenario seed**, **idea for an adventure**, or
similar generative material, that publisher framing is strong evidence that the
material is intended to support the creation of an adventure rather than itself
constitute a complete or substantially bounded canonical adventure.

Equivalent publisher language includes formulations such as:

-   "ideas for adventures";
-   "can be used to launch adventures";
-   "can be used to flesh out adventures";
-   "adventure seeds";
-   "quest hooks"; and
-   other language that explicitly positions the material as input to,
    inspiration for, or setup for a larger adventure.

This evidence is **strong but not absolute**. A publisher-designated hook or seed
MAY still qualify when the current published presentation independently passes
the Core Boundary, Playable Identity, and Minimum Adventure Substance tests.
However, the burden of evidence favors rejection unless the source affirmatively
supplies a substantially bounded body of playable material rather than merely
describing what the resulting adventure could contain.

#### Narrative Completeness Is Not Playable Completeness

A candidate does not become a canonical adventure merely because the source
supplies several or all of the following:

-   an inciting event or patron;
-   a player objective;
-   a named antagonist;
-   a central secret or twist;
-   a destination;
-   possible complications;
-   an expected climax; or
-   consequences or possible outcomes.

These elements can make a quest hook unusually detailed while leaving the
substantive adventure itself for the GM to construct.

The controlling question is:

> **Has the source authored the substantive body of play between premise and
> resolution, or has it primarily described the adventure that the GM is
> expected to create?**

A candidate is weaker when substantial expected play is compressed into summary
statements that characters "investigate," "explore," "travel," "infiltrate,"
"track," "search," "set a trap," or "discover" something without supplying
meaningful adventure-specific scenes, clues, locations, encounters, procedures,
choices, obstacles, or other playable development through which those actions
occur.

Likewise, a candidate remains hook/seed-like when a major resolution requires
the GM to invent the substantive investigation, adventure site, encounter
sequence, opposition, route, or connective play necessary to reach it.

#### Do Not Borrow Surrounding Sourcebook Material to Complete a Hook

Surrounding setting description, NPC profiles, faction information, location
lore, monster statistics, random tables, or other sourcebook material MUST NOT
be treated as though it were authored adventure progression merely because a GM
could use it to develop the hook.

Such surrounding material may support a qualifying adventure when the source
itself integrates or clearly directs that material into the candidate's playable
structure.

The test is not:

> **Could a GM readily turn this material into an adventure?**

The test is:

> **Has the publisher supplied a complete or substantially bounded playable
> adventure here?**

#### Scoreability Is Not Adventure Identity

The fact that a candidate contains enough information to estimate one or more
AdventureFinder analysis dimensions does not establish canonical adventure
identity.

A coherent hook may permit reasonable inference about likely tone, horror,
combat, investigation, openness, preparation, or other characteristics while
still leaving too much of the substantive playable experience unauthored for a
canonical Adventure ID.

Boundary determination MUST therefore precede and remain conceptually separate
from scoreability.

#### Override Standard

To override explicit publisher framing as a hook or seed, the candidate SHOULD
show affirmative evidence of several of the following within the candidate
itself:

-   a distinct playable entry;
-   multiple related scenes, encounters, locations, discoveries, decisions, or
    procedures;
-   meaningful authored progression;
-   adventure-specific obstacles rather than generic categories of possible
    obstacles;
-   an identifiable climax, resolution, state change, or deliberate endpoint;
-   enough concrete playable material that a GM can prepare and run the unit
    substantially as published without designing the central adventure; or
-   explicit contradictory publisher evidence elsewhere treating substantially
    the same unit as an adventure or scenario.

Mere density of ideas is insufficient.

#### Grim Hollow: The Campaign Guide Reference Case

During review of *Grim Hollow: The Campaign Guide*, repeated source sections were
explicitly labeled **Quest Hooks** and described as material that provides ideas
for, launches, or fleshes out adventures. Several entries nevertheless supplied
named patrons and antagonists, explicit objectives, central secrets, possible
encounters, twists, consequences, and hundreds of words of supporting prose.

A high-recall Phase 1 correctly retained many such entries for inspection. A
focused Phase 1b pressure review then found that even the strongest examples---
including *The Diligence of Believers*, *A Student's Greatest Failure*, *The
Riven Rascals*, and *Wood Song*---still summarized, omitted, or delegated to the
GM too much of their investigation, travel, site structure, encounter sequence,
or resolution to override the publisher's explicit hook framing.

The Quest Hook set therefore did not receive canonical Adventure IDs merely
because some entries were unusually detailed or partially scoreable.

The governing precedent is:

> **A highly developed adventure hook is still a hook when the publisher
> presents it as generative material and has not supplied a substantially
> complete body of play.**

This precedent establishes neither a minimum word count nor a categorical ban on
short scenarios. A short published scenario may still qualify when its authored
playable substance independently crosses the canonical adventure threshold.

### 9.3 Authored Play Spine and Reviewer-Completion Rule

A candidate MUST be evaluated on the playable structure actually supplied by the
published source, not on the adventure a competent GM or frontier reviewer could
readily construct from its ingredients.

A candidate may contain an evocative premise, explicit objective, antagonist,
location, factions, secrets, encounters, climax, possible outcome, or other
adventure-shaped material while still failing to constitute a canonical
adventure when the substantive connective body of play remains omitted,
summarized, generative, or delegated to the GM.

The relevant question is:

> **What substantive progression has the source actually authored between entry
> into this candidate and its resolution or deliberate transition?**

The reviewer MUST NOT convert summary verbs into unstated playable structure.

Examples include:

-   "investigate the disappearances" without an authored investigation body;
-   "infiltrate the fortress" without meaningful authored infiltration material;
-   "escort the caravan" when the only supplied play is one encounter at the
    destination;
-   "retrieve the artifact" when the search, route, obstacles, or recovery
    sequence remain for the GM to create;
-   "explore the ruins" when the site provides reusable geography and encounters
    but no coherent localized adventure progression; or
-   "stop the threat" when the source establishes the threat but leaves the
    actual course of the adventure substantially undesigned.

A beginning plus an objective plus a described resolution is therefore not
sufficient when the central body of play is missing.

Likewise, a rich location does not become an adventure merely because its
inhabitants, factions, hazards, keyed areas, rumors, and possible objectives
could readily be assembled into one.

The candidate should instead contain a source-authored **play spine**: enough
scenes, locations, clues, encounters, procedures, choices, obstacles, faction
dynamics, exploration structure, or other playable development that the GM is
running and adjudicating published material rather than principally designing
the adventure's connective structure.

This rule does not require a linear sequence, predetermined solution, or low GM
improvisation demand. Sandbox, investigative, site-based, procedural, and highly
open adventures may qualify when their published structures themselves organize
play into a bounded and recognizable adventure.

#### External Mission Spine vs. Intrinsic Site Spine

A source-authored play spine can arise in at least two importantly different
ways.

**External Mission Spine:** the source establishes a mission, objective,
problem, threat, or assignment and authors substantial playable development
through which the characters pursue or resolve it.

Examples may include an authored rescue sequence, investigation chain,
infiltration procedure, escort progression, defense structure, or other mission
whose middle is materially supplied rather than summarized.

**Intrinsic Site Spine:** the source does not require an externally assigned
mission because the site's own architecture, procedures, pressures,
dependencies, or escalation organize substantial play toward a meaningful
endpoint or state change.

Examples may include a dungeon whose gates, keys, procedures, hazards, clues,
depth, and culminating location create a directed expedition even when no patron
explicitly tells the characters to undertake it.

The controlling rule is:

> **An explicit mission is neither necessary nor sufficient. What matters is a
> source-authored mechanism that binds substantial playable material into a
> coherent progression.**

An external objective without an authored middle remains subject to the
Mission-Wrapper Guardrail.

A rich location without an intrinsic binding mechanism remains subject to the
Location-to-Adventure Threshold and Sourcebook Assembly Guardrail.

This distinction is especially important when reviewing dungeons, strongholds,
ruins, lairs, and other keyed sites whose playable identity may arise primarily
from their internal structure.

#### Procedural Adventure vs. Adventure Generator

Procedural generation does not by itself count either for or against adventure
identity.

Distinguish:

**Procedural adventure:** the published procedure operates inside a stable
playable identity and itself supplies meaningful progression toward a bounded
culmination, resolution, or deliberate transition.

**Adventure generator:** the published procedure produces premises, locations,
encounters, objectives, or connective prompts from which the GM constructs one
or many possible adventures.

The first MAY qualify as a canonical adventure.

The second SHOULD NOT itself receive an Adventure ID unless a stable published
output independently satisfies the ordinary boundary tests.

Randomness is therefore not the distinction. The distinction is whether the
procedure **constitutes the adventure's authored play spine** or merely
**generates ingredients for adventures**.

#### Mission-Wrapper Guardrail

An explicit mission does not automatically supply sufficient adventure
substance.

A fetch, escort, investigation, infiltration, rescue, repair, defense, or
similar assignment SHOULD still be rejected when the source-authored playable
body is principally one encounter, one scene, one obstacle, or another unit
already excluded by the Minimum Adventure Substance Test.

`mission wrapper + one encounter ≠ adventure`

The assignment may establish the candidate's objective. It does not manufacture
missing progression.

#### Sourcebook Assembly Guardrail

When a source provides multiple hooks, factions, sites, encounters, rumors,
goals, events, or campaign-use suggestions, the reviewer MUST NOT combine
otherwise independent elements into a canonical adventure unless the source
itself meaningfully integrates them into the same playable structure.

`ingredients that can be combined into an adventure ≠ authored adventure`

A sourcebook location may therefore support many excellent adventures while
contributing no canonical AdventureFinder record.

#### Weird Wastelands Reference Case

The *Weird Wastelands* review exposed several forms of reviewer completion.

*Last City of MAN*, the *Toxic Alchemical Sump*, and *Gates of the Afterlife*
supplied rich locations, factions, hazards, hooks, and possible objectives, but
their components supported multiple possible adventures rather than one
source-authored play spine.

*Paranoid Android* supplied a patron, objective, target, revelation, and
consequence, but too much of the central infiltration remained compressed into
summary rather than authored playable development.

Likewise, mission-wrapped set pieces such as *Butler Ian*, *When WALL E Comes
Tumbling Down...*, and *Shady Salvage* remained principally one encounter or
set piece despite having explicit assignments and outcomes.

By contrast:

-   *The Heist* qualifies despite its brevity because the source authors the
    playable middle: timing, entry, guards, nonlethal constraint, vault
    mechanisms, surprise complication, loot logistics, escape pressure,
    reinforcements, and consequences;
-   *Deep Green* qualifies because its keyed dungeon progression, antagonist
    dynamics, culmination, and aftermath organize a bounded body of play; and
-   *Basalt Palace* qualifies because its procedural depth crawl itself forces
    forward movement toward an authored endpoint rather than merely generating
    ingredients for a GM-created adventure.

The governing distinctions are:

`imagined runnability ≠ authored playability`

`geographic structure ≠ necessarily adventure progression`

`procedure that generates adventures ≠ procedural adventure`

`mission wrapper ≠ sufficient substance`

### 9.4 Zero-Adventure Source Outcome / No Adventure Quota

Adventure boundary review has no minimum expected number of accepted records.

After complete Phase 1 inspection and Phase 1b/Phase 2 review, a source MAY
legitimately contribute **zero canonical adventures**.

A zero-adventure result is not evidence that the review failed when:

-   the complete relevant source span was inspected;
-   plausible adventure-shaped material was retained long enough to be
    pressure-tested;
-   the strongest candidates were tested against the Core Boundary, Playable
    Identity, Authored Play Spine, Location-to-Adventure, and Minimum Adventure
    Substance standards as applicable; and
-   the surviving material is better characterized as setting material,
    locations, campaign scaffolding, encounters, generators, hooks, seeds,
    situations, or other adventure-support material.

The reviewer MUST NOT lower the canonical threshold merely because:

-   the source is long or expensive;
-   the source contains headings such as "Adventures," "Quests," or
    "Scenarios";
-   the source contains many playable encounters or keyed locations;
-   the source is highly useful at the table;
-   the source seems as though it "ought" to contain at least one adventure; or
-   an accepted record would make the ingestion feel more productive.

The purpose of boundary review is to identify published adventures faithfully,
not to ensure every reviewed source adds an Adventure ID.

`useful adventure material ≠ canonical adventure`

`adventure-rich source ≠ necessarily source of adventures`

`zero accepted adventures ≠ failed ingestion`

#### Zero-Adventure Reference Cases

**The Game Master's Book of Instant Towns and Cities.** The source presents a
collection of population centers, rumors, jobs, happenings, encounter
suggestions, adventure seeds, and generators. Even the Epic Journey Generator
supplies prompts and destinations while leaving substantial connective journeys
to the GM and players. This is adventure-generating material rather than a
stable source-authored adventure.

**Tal'Dorei Campaign Setting Reborn.** The Gazetteer repeatedly presents plot
hooks and story hooks as material for the GM to turn into full adventures. Its
adventure-creation guidance explicitly describes the hooks as beginnings,
sometimes hints of middles, but not conclusions. Their narrative richness does
not by itself supply playable completeness.

**Book of Ebon Tides.** The source principally defines the Shadow Realm through
setting, rules, courts, locations, factions, encounters, current events, and
other campaign support. Even material placed under an "Adventures" heading was
reviewed as situation/prompts rather than a bounded source-authored play spine.

**Tatters of Myth Drannor.** The source is a campaign guide and gazetteer that
provides a hexcrawl environment, sites, lairs, threats, factions, goals,
encounters, and Campaign Use suggestions. Those components richly support
GM-authored Myth Drannor adventures but did not independently establish a
discrete published adventure.

These cases establish:

`density of usable campaign material ≠ presence of a canonical adventure`

A source may be highly useful for adventures while canonically containing zero
adventures.

------------------------------------------------------------------------

## 10. Product-Level Structural Classes

### 10.1 Standalone Adventure

A product substantially corresponds to one playable adventure.

Default hypothesis:

`product ≈ one adventure`

The editor should still inspect for embedded or separately bounded
adventures when the source gives reason to do so.

### 10.2 Anthology / Collection

A product contains multiple separately identifiable adventures.

Default hypothesis:

`product → multiple peer adventures`

Shared front matter and shared appendices should not be absorbed into
every child adventure.

### 10.3 Linked Adventure Sequence

A product contains multiple adventures designed to connect while
remaining substantially distinct playable works.

Default hypothesis:

`product → multiple peer adventures with continuity`

Continuity does not require collapsing the sequence into one record.

### 10.4 Campaign / Large Integrated Adventure

A product presents a broad campaign containing chapters, locations,
quests, and arcs.

Default hypothesis:

`product → internal boundary review required`

Do not assume either that the whole product is necessarily one adventure
or that every major internal unit deserves its own Adventure ID.

### 10.5 Sourcebook with Embedded Adventure

A primarily setting/rules/sourcebook product contains one or more
discrete playable adventures.

Default hypothesis:

`sourcebook material ≠ adventure`

Only qualifying playable units receive adventure records.

When embedded material is explicitly presented as a quest hook, adventure hook,
adventure seed, idea for an adventure, or similar generative material, apply the
Publisher-Designated Hook, Seed, and Adventure-Idea Rule in §9.2 before
promoting it to a canonical Adventure ID.

Whether or not such publisher framing is present, apply the Authored Play Spine
and Reviewer-Completion Rule in §9.3 before promoting a rich location, mission,
scenario, generator, or collection of sourcebook ingredients into a canonical
Adventure ID.

A sourcebook MAY legitimately contribute zero canonical adventures under the
Zero-Adventure Source Outcome / No Adventure Quota rule in §9.4.

### 10.6 Scenario / Encounter Collection

A product contains short playable units that may be smaller than
conventional adventures.

No minimum page count applies. A short unit qualifies when it passes the
Core Boundary Test and Substantial Distinctness Test.

### 10.7 Hybrid / Ambiguous Product

Some products combine campaign material, setting material, independent
adventures, encounters, or other structures.

Do not force these into a predefined pattern. Review each plausible
playable unit under the same tests.

------------------------------------------------------------------------

## 11. Anthology and Collection Rules

Anthologies are generally the clearest boundary cases.

For a separately titled anthology adventure:

**Start Page** SHOULD be the first page of adventure-specific content.

It SHOULD NOT automatically include:

-   book preface;
-   anthology introduction;
-   shared "Using This Book" material;
-   shared adventure summaries;
-   general setting or rules material.

**End Page** SHOULD be the final page belonging specifically to that
adventure, normally immediately before the next peer adventure begins.

Shared book-level appendices SHOULD NOT automatically be included.

### 11.1 Reference Example --- The Sunless Citadel

The accepted AdventureFinder record establishes:

-   **Adventure Title:** The Sunless Citadel
-   **Source Book:** Tales from the Yawning Portal
-   **Start Page:** 9
-   **End Page:** 32

A source representation that contains shared front matter or appendices
must not cause those pages to become part of the adventure merely
because they occur in the same file.

### 11.2 Anthology Boundary Principle

When a source contains:

`shared front matter → adventure → shared material / next adventure`

the boundary should follow the **adventure-specific material**, not the
physical extent of the file or product.

------------------------------------------------------------------------

## 12. Campaign Internal Boundary Review

Large integrated campaigns require the most careful editorial judgment
because they can contain **nested adventures** as well as subordinate
structural units.

The LLM SHOULD inspect major internal units that plausibly form complete
or substantially bounded adventures, including:

-   named quests or missions;
-   major locations with their own playable objective or situation;
-   chapter-scale arcs;
-   distinct starting situations;
-   localized antagonists or conflicts;
-   contained exploration sites;
-   localized climax/resolution sequences;
-   explicit transitions into new premises.

Prominence is not sufficient, but **nesting is not disqualifying**.

A famous location, large chapter, memorable dungeon, or major boss does
not automatically deserve a separate Adventure ID. Conversely, a
candidate does not cease to be an adventure merely because it is
embedded inside a larger campaign.

### 12.1 Campaign Location Test

For a major campaign location or chapter, ask:

1.  Does it have an identifiable entry condition?
2.  Does it establish a coherent localized objective, problem, threat,
    mystery, or playable situation?
3.  Does meaningful progression occur within it?
4.  Does it contain enough substantive play to exceed a single
    encounter, waypoint, or transition?
5.  Does it have an identifiable resolution, state change, exit, or
    deliberate transition?
6.  Can it be meaningfully addressed and prepared as a particular body
    of play?
7.  Is its playable identity substantially distinct from the campaign's
    continuous connective tissue?

If the answers are materially **yes**, the candidate MAY qualify as a
Nested Adventure even when it depends on the parent campaign. Apply §8.11
pairwise as well: a rich principal site with a valid spine can still represent
substantially the same playable unit as its proposed parent. Diagnose apparent
redundancy under §8.12 before attributing it to failed identity.

### 12.2 Site-Based Adventure vs. Mere Location

A location can constitute an adventure.

Location-based and dungeon-based adventures do not require a singular
externally assigned mission. A sufficiently developed site may itself supply
the playable premise. To determine whether it has crossed the
**Location-to-Adventure Threshold**, distinguish **supporting site evidence**
from **binding play-spine evidence**.

#### Supporting Site Evidence

Supporting evidence may include:

-   meaningful arrival or entry;
-   substantial keyed playable space;
-   multiple encounters or interaction opportunities;
-   internally related NPCs or factions;
-   discoverable history, secrets, treasure, or situation;
-   meaningful player choices;
-   localized hazards, opposition, or opportunities; and
-   other material that gives the site depth and table utility.

These signals establish that the location is rich and playable. They do not,
by accumulation alone, establish that the location is a canonical adventure.

#### Binding Play-Spine Evidence

A site SHOULD normally contain at least one source-authored **binding
mechanism** that organizes multiple substantial playable elements into a
coherent progression.

Binding mechanisms may include:

-   an explicit localized objective or problem that meaningfully connects
    multiple site elements;
-   directed, gated, or dependency-based progression through the site;
-   an authored search, investigation, clue, or discovery chain;
-   an active threat or escalating pressure that materially links multiple
    encounters, locations, or decisions;
-   a procedure that itself organizes movement, risk, discovery, or state
    change through the site;
-   an authored sequence of consequential choices or changing site states; or
-   a meaningful resolution, departure condition, or endpoint whose attainment
    depends on substantial internal progression through the site.

The binding mechanism MUST do more than name a goal, antagonist, treasure,
climax, or exit. It must materially connect multiple playable elements that the
source itself supplies.

Supporting site evidence cannot substitute for a missing binding mechanism
merely because the site is large, evocative, densely keyed, faction-rich, or
easy for a competent GM to turn into an adventure.

A site remains merely structural when it principally provides geography,
transit, one encounter, one campaign interaction, an undifferentiated portion of
a continuous larger dungeon, or a rich but unintegrated collection of playable
ingredients.

Therefore:

`location ≠ automatically adventure`

but also:

`location-based ≠ automatically structural unit`

and:

`rich location + adventure ingredients ≠ authored adventure`

`binding play spine + substantial site material → may qualify`

#### Middle-earth Landmark Calibration Cases

The *Ruins of Eriador*, *Keepers of the Elven-Rings*, and *Moria: Shadow of
Khazad-dûm* reviews provide a useful repeated-template calibration.

*Ruins of Eriador* explicitly describes its twelve Landmarks as open-ended,
self-contained scenarios, but final ABDS review accepted nine rather than
treating the publisher designation as dispositive. The accepted units crossed
the ordinary canonical threshold; the designation established strong intended
identity but did not waive authored-substance review.

*Keepers of the Elven-Rings* demonstrates the opposite edge. **The Winter-horn**
crosses the threshold because its escalating regional threat, authored search
procedure, keyed locations, active opposition, and multiple source-supported
ways of resolving the threat form an integrated body of play. Other rich
Landmarks in the same source do not qualify merely because the repeated format
supplies locations, factions, encounters, or scenario suggestions.

*Moria: Shadow of Khazad-dûm* demonstrates the importance of intrinsic site
spines. **The Vault of Uruktharbun**, **The Lost Citadel of the Ring-smiths**,
and **The Armouries of the Third Deep** qualify through source-authored internal
progression even though a conventional external mission is not always explicit.
By contrast, rich sites such as **The Chamber of Mazarbul**, **The Fortress of
Malech**, **The Mountain Galleries**, and the **Udûn-temple** do not become
canonical adventures merely because their keyed areas, factions, threats, and
possible objectives can readily be assembled into adventures by the GM.

The governing lesson is:

> **Repeated format and rich site content are evidence to inspect. The
> canonical threshold is crossed by the authored organization of play.**

### 12.3 Minimum Adventure Substance Test

To prevent over-segmentation, reject a candidate when it is principally:

-   one encounter;
-   one NPC interaction;
-   one puzzle;
-   one travel obstacle;
-   one room or small undifferentiated room cluster;
-   a campaign event without substantial supporting play;
-   a quest hook whose actual play occurs elsewhere;
-   a publisher-designated hook or seed whose central body of play is
    summarized, omitted, or delegated to the GM;
-   a dungeon level whose only function is continuous traversal toward
    the same objective;
-   a location whose keyed content does not form a coherent localized
    scenario.

No minimum page count applies. The test concerns playable substance, not
length. Apply this test to plausible canonical units regardless of whether they
are nested inside a campaign, embedded inside a sourcebook, or presented in a
scenario/encounter collection.

### 12.4 Curse of Strahd Reference Case

*Curse of Strahd* is a key precedent for nested-adventure review.

The campaign as a whole qualifies as a canonical Parent Adventure.
*Death House* also clearly qualifies as a discrete embedded adventure.

Version 0.5 further recognizes that major Barovian locations may qualify
as Nested Adventures when they pass the same tests.

Strong candidates for focused review include:

-   Old Bonegrinder;
-   Argynvostholt;
-   Wizard of Wines;
-   Yester Hill;
-   Van Richten's Tower;
-   Amber Temple;
-   Werewolf Den;
-   Castle Ravenloft.

The source itself provides unusually strong structural evidence: it
assigns recommended character levels to these areas and explicitly
identifies defeating featured antagonists or accomplishing localized
story goals as milestone-worthy achievements.

These signals do not automatically make every listed area an adventure.
For example, a traversal-focused area such as Tsolenka Pass may still
fail the Minimum Adventure Substance or Playable Identity tests.

#### Castle Ravenloft Historical Precedent

Castle Ravenloft is especially instructive.

The 5e source explicitly describes *Curse of Strahd* as a retelling of
the original *Ravenloft* adventure and states that the current book
includes the original adventure plus expanded material around it. This
demonstrates the editorial principle that embedding and expanding
previously standalone adventure material inside a larger campaign does
not necessarily erase its adventure identity.

Historical publication identity is strong supporting evidence, not an
automatic rule. The current Castle Ravenloft material must still pass
the Core Boundary, Playable Identity, and Minimum Adventure Substance
tests.

The governing lesson is:

> **Embedding an adventure-shaped work inside a larger campaign does not
> necessarily destroy its adventure identity.**

## 13. Natural Narrative Division Review

Unusually large or structurally complex playable works SHOULD receive an
additional review for natural adventure divisions.

Page count alone MUST NOT determine a split.

The following MUST NOT be used in isolation to create, split, merge, or
reject an adventure boundary:

-   printed page count;
-   chapter length;
-   campaign importance;
-   narrative climax;
-   finale status;
-   number of maps;
-   number of illustrations.

Evidence favoring a natural division includes:

-   a new premise;
-   a new independent objective;
-   a meaningful reset of starting conditions;
-   completion of the prior arc;
-   an explicit transition;
-   a new self-contained adventure title;
-   a structural change that makes the next unit meaningfully runnable
    as a separate adventure.

Absence of such evidence favors preserving the larger adventure intact.

------------------------------------------------------------------------

## 14. Hierarchical Structure and Canonical Adventure Identity

AdventureFinder recognizes that canonical adventures may exist at
multiple levels of composition.

The conceptual hierarchy is:

`Product → Parent Adventure → Nested Adventure → Subordinate Structural Unit`

not merely:

`Product → Canonical Adventure → everything else`

Boundary review must therefore distinguish:

-   **Product**
-   **Parent Adventure**
-   **Peer Adventure**
-   **Nested Adventure**
-   **Subordinate Structural Unit**

A Nested Adventure is itself a canonical adventure. Its parent-child
relationship does not make it a mere structural unit.

Possible subordinate units include:

-   chapters;
-   dungeon levels;
-   major locations;
-   acts;
-   terrain units;
-   quests;
-   encounter clusters.

### 14.1 Parent and Child Canonical Identity

A larger adventure may contain smaller adventures without either losing
canonical identity.

Therefore:

-   accepting a child does not require rejecting or splitting the
    parent;
-   parent and child page ranges may overlap;
-   the child may inherit substantial context from the parent;
-   the child must still pass the Playable Identity and Minimum
    Adventure Substance tests, including the pairwise comparison in §8.11 and,
    when redundancy is suspected, the diagnostic in §8.12.

### 14.2 Forge of Fury Reference Case

The accepted catalog contains:

-   `ADV-0029` --- The Forge of Fury --- pages 33--60

AdventureFinder has also used separately addressable terrain units
within that adventure:

-   Mountain Door
-   Glitterhame
-   Sinkhole
-   The Foundry
-   Black Lake

Those internal areas are meaningful structures, but they do not
automatically become Nested Adventures because their principal identity
is as structural portions of the continuous Forge of Fury dungeon.

Therefore:

> **Clear internal boundaries and addressability do not by themselves
> justify canonical Adventure IDs.**

They must also satisfy the Playable Identity and Minimum Adventure
Substance tests.

## 15. Short Adventures and Page Count

No minimum page length is required.

Accepted AdventureFinder material includes adventures spanning from very
short scenarios to long works.

Therefore:

`short ≠ non-adventure`

and:
`long ≠ single adventure`

Boundary decisions are semantic and structural.

A one-page unit MAY qualify if it contains a coherent playable scenario.

------------------------------------------------------------------------

## 16. Start Page Determination

After a candidate qualifies as an adventure, determine its Start Page
using the strongest available source evidence.

Preferred order:

1.  explicit published adventure title page;
2.  first page of adventure-specific introduction/setup;
3.  page associated with the principal adventure heading;
4.  first page on which the distinct playable unit actually begins.

Do not automatically include:

-   product title pages;
-   credits;
-   book introductions;
-   anthology prefaces;
-   shared hooks;
-   shared rules;
-   unrelated setting material.

If introductory material clearly belongs specifically to the adventure
but precedes its principal heading, the Start Page MAY move earlier.

The LLM SHOULD explain the evidence supporting any non-obvious Start
Page.

------------------------------------------------------------------------

## 17. End Page Determination

Preferred evidence includes:

1.  explicit final page of adventure-specific material;
2.  page immediately before the next peer adventure begins;
3.  conclusion/aftermath/reward material;
4.  last page of adventure-specific supporting material.

Adventure-specific appendices, handouts, maps, or supporting material
MAY be included when clearly part of the adventure.

Shared book-level appendices SHOULD NOT automatically extend the
boundary.

The LLM SHOULD explain the evidence supporting any non-obvious End Page.

------------------------------------------------------------------------

## 18. Source Representation and Markdown

Normalized Markdown, PDFs, extracted text, tables of contents, and other
source representations are **evidence interfaces**, not editorial
authority.

When normalized Markdown is used, the LLM MAY rely on:

-   document title;
-   heading hierarchy;
-   page markers;
-   source metadata;
-   repeated title patterns;
-   introduction/conclusion headings;
-   appendix headings;
-   chapter transitions;
-   adventure-specific cross-references;
-   lexical cues such as "adventure," "conclusion," "starting the
    adventure," and equivalent phrases.

No single signal is sufficient in every product.

### 18.1 Heading Rule

A heading creates a reason to inspect a possible structural boundary. It
does not automatically create an adventure.

### 18.2 Page Marker Rule

A page marker provides provenance and boundary evidence. It does not
determine semantic ownership by itself.

### 18.2.1 Source-Evidenced Pagination Rule

Adventure page boundaries MUST NOT be inferred solely from gaps between
extracted page markers, neighboring section boundaries, expected
pagination, page counts, or document structure.

A Start Page or End Page may be recorded as exact only when the
available source provides affirmative evidence that adventure-owned
content occurs on that printed page.

When an LLM-readable source omits a printed page, lacks a page marker,
contains an image-only page, or otherwise leaves the semantic ownership
of a page uncertain, the boundary MUST be marked **Uncertain / Requires
Source Verification** rather than estimated.

The next known page marker establishes where subsequent content begins;
it does not, by itself, establish that every intervening printed page
belongs to the preceding adventure.

Physical books, publisher PDFs, or other direct representations of the
printed pages may resolve such uncertainty. When direct printed-page
evidence conflicts with an incomplete normalized Markdown extraction,
the direct printed-page evidence governs.

Operationally:

`exact boundary → affirmative source evidence`

`missing evidence → uncertainty flag`

`never fill a pagination gap by interpolation`

### 18.2.2 End-Boundary Exhaustion Rule

An End Page MUST NOT be assigned merely because adventure-owned
conclusion, aftermath, epilogue, resolution, reward, or transition
material has been found on that page.

Before assigning an exact End Page, the reviewer MUST continue
sequentially through the available source until affirmative evidence
establishes that the adventure-owned semantic unit has ended.

The reviewer MUST inspect subsequent available source material for
continuation of:

-   conclusions and aftermath;
-   epilogues and alternate endings;
-   rewards or consequences;
-   unresolved adventure-specific outcomes;
-   return/reporting sequences;
-   explicit transition material belonging to the adventure.

Encountering a heading such as **Conclusion**, **Epilogue**, **Wrapping
Up**, or equivalent establishes that ending material has begun; it does
**not** establish where that material ends.

If the available source cannot establish where the semantic unit
actually terminates, the End Page MUST remain **Uncertain / Requires
Source Verification**.

Operationally:

`finding ending material ≠ finding the end`

### 18.3 File Boundary Rule

The first and last page represented in a generated file MUST NOT
automatically become Start Page and End Page.

### 18.4 Source Conflict Rule

When a normalized representation appears inconsistent with the published
source, the source should control and the discrepancy should be flagged
rather than silently normalized away.

------------------------------------------------------------------------

## 19. Common False Positives

Do not automatically catalog:

-   Preface
-   Introduction
-   Using This Book
-   Credits
-   Appendix
-   Bestiary
-   Magic Items
-   Random Encounters
-   Gazetteer material
-   Character options
-   Backgrounds
-   Rules sections
-   Maps
-   individual rooms
-   isolated encounters
-   minor side scenes
-   pure logistics
-   transition chapters
-   travel-only sections
-   chapter headings without independent playable structure
-   publisher-designated quest hooks, adventure hooks, adventure seeds, or
    ideas for adventures whose substantive playable development remains
    summarized, omitted, or GM-authored

These are heuristics rather than absolute prohibitions. Material with an
unusual label may still qualify if it independently passes the Core
Boundary and Substantial Distinctness tests. Explicit hook/seed framing is
strong counterevidence rather than an absolute prohibition; apply §9.2.

------------------------------------------------------------------------

## 20. Common False Negatives

The editor and LLM SHOULD actively look for qualifying adventures that
lack obvious "Adventure" labels.

Potential signals include:

-   a named scenario with hooks and resolution;
-   a major location with a contained mission, threat, exploration
    premise, or climax;
-   a site-based adventure whose location itself supplies the coherent
    playable situation;
-   a sequence of scenes with its own starting condition and conclusion;
-   short side adventures embedded in campaign or sourcebook material;
-   nested adventures that inherit hooks or context from a parent
    campaign;
-   historically standalone adventure material embedded or expanded
    inside a later campaign;
-   linked adventures sharing a product but having distinct objectives
    and conclusions.

The literal word "adventure" is never required.

------------------------------------------------------------------------

## 21. Editorial Evidence Categories

For difficult cases, evidence SHOULD be organized into four practical
categories.

### 21.1 Boundary-Supporting Evidence

Evidence that favors treating the unit as a canonical peer or nested
adventure, such as:

-   explicit publisher presentation;
-   independent premise/objective;
-   distinct starting condition;
-   coherent progression;
-   localized conclusion;
-   deliberate transition;
-   independently identifiable or preparable adventure-specific
    material;
-   meaningful addressability as a body of play;
-   replaceability within a parent campaign;
-   historical or external independent-adventure identity.

### 21.2 Boundary Counterevidence

Evidence favoring inclusion within a larger adventure, such as:

-   dependence on surrounding material so extreme that the candidate
    lacks a coherent localized playable identity;
-   beginning or ending mid-sequence without a meaningful entry or exit
    condition;
-   purely geographic or organizational division;
-   continuation of the same objective without meaningful reset;
-   absence of an independent endpoint;
-   role as a subordinate dungeon level, encounter cluster, or campaign
    location.

For nested candidates, weigh these signals under §§8.10–8.12. A shared
objective, climax, or final outcome is not disqualifying; pairwise redundancy
requires source-grounded comparison of the represented playable units, with
boundary and relationship defects distinguished from identity failure.

### 21.3 Start-Boundary Evidence

Evidence supporting the proposed Start Page.

### 21.4 End-Boundary Evidence

Evidence supporting the proposed End Page.

These categories are aids to editorial reasoning. They are not an
additive scoring system.

------------------------------------------------------------------------

## 22. Editorial Recommendation Format

For ordinary Phase 2 boundary review, the frontier model SHOULD present each
proposed canonical adventure in a compact, auditable form.

Recommended structure:

``` text
Proposed Adventure:
Source Book:
Proposed Start Page:
Proposed End Page:

Recommendation:
ACCEPT AS ADVENTURE | REJECT | MERGE | SPLIT | AMBIGUOUS

Boundary-Supporting Evidence:
- ...

Counterevidence:
- ...

Start-Page Evidence:
- ...

End-Page Evidence:
- ...

Editorial Rationale:
...

Uncertainty / Questions for Human Review:
...
```

For straightforward cases, this MAY be shortened.

For ambiguous cases, the LLM SHOULD expose the competing interpretations
rather than burying them in a single confidence score.

------------------------------------------------------------------------

## 23. Confidence

Numeric confidence is optional and secondary to explicit evidence.

If used, confidence measures the strength of the boundary
recommendation, not adventure quality.

Suggested interpretation:

-   **Very high** --- direct publisher structure and source evidence
    strongly establish the boundary.
-   **High** --- strong source evidence with little meaningful
    counterevidence.
-   **Moderate** --- plausible interpretation with material editorial
    judgment.
-   **Low** --- multiple interpretations remain viable.

A human editor should never be expected to accept a recommendation
merely because the LLM reports high confidence.

For the library-ingestion workflow, **clear reasons and identified ambiguity
are more important than numerical confidence**.

------------------------------------------------------------------------

## 24. Editorial Outcomes

Every reviewed candidate should end in one of these states.

### ACCEPT AS ADVENTURE

The unit qualifies for a canonical Adventure Catalog record.

The accepted unit SHOULD additionally be classified editorially as one
of:

-   **Standalone / Parent Adventure**
-   **Peer Adventure**
-   **Nested Adventure**

This classification may remain decision provenance until or unless the
canonical catalog schema adds an explicit relationship field.

### REJECT --- STRUCTURAL UNIT

The unit is meaningful but subordinate to a larger canonical adventure.

### REJECT --- NON-ADVENTURE MATERIAL

The unit is setting, rules, reference, appendix, front matter, or other
non-adventure content.

### MERGE WITH PARENT / ADJACENT UNIT

The candidate lacks sufficiently distinct playable identity from the parent or
adjacent unit. For proposed nesting, apply §§8.11–8.12; dependence on the parent
alone is not grounds for merger.

### SPLIT FOR FURTHER REVIEW

Evidence indicates that the candidate itself may contain multiple
substantially distinct adventures.

### AMBIGUOUS --- HUMAN DECISION REQUIRED

The source supports multiple plausible interpretations or lacks enough
evidence for a responsible recommendation.

------------------------------------------------------------------------

## 25. Canonical Library Ingestion Workflow

AdventureFinder library ingestion SHOULD favor **one-source-at-a-time editorial
closure** rather than accumulating a large unresolved candidate pool.

For each source:

1.  verify canonical source identity, edition, and page-addressable source data;
2.  prepare deterministic source/catalog evidence where tooling supports it;
3.  conduct **Phase 1** high-recall candidate harvest across the complete
    relevant span;
4.  conduct **Phase 1b** pressure / sanity review against the boundary,
    identity, authored-play-spine, and minimum-substance tests, including a
    Survivor Play-Spine Proof for retained candidates and Homogeneous Sibling-Set
    Calibration when materially similar repeated-template candidates are present;
5.  conduct **Phase 2** canonical identity, nesting, title, level-if-established,
    and exact-boundary adjudication;
6.  preserve an explicit disposition for every Phase 1 candidate;
7.  obtain David's approval of the complete canonical set;
8.  freeze the accepted decisions in a provenance-bound structured handoff;
9.  validate that handoff against the exact canonical source and explicit base
    AMC;
10. deterministically preserve existing Adventure IDs or derive new IDs only
    after validation;
11. write a **new successor AMC**, leaving unassessed scoring fields blank;
12. verify the successor/integrity report and obtain human acceptance before
    production scoring begins; and
13. preserve noteworthy editorial decisions as precedents for later sources.

The source-of-truth flow is therefore:

``` text
canonical source
      ↓
deterministic evidence preparation
      ↓
Phase 1 high-recall harvest
      ↓
Phase 1b pressure / sanity review
      ↓
Phase 2 canonical identity + nesting + boundaries
      ↓
human-approved structured freeze
      ↓
deterministic validation
      ↓
deterministic Adventure-ID reconciliation / successor AMC
```

Do not silently infer the current catalog head. A deterministic catalog mutation
must use one explicitly selected base AMC whose identity is bound into the
reviewed handoff.

------------------------------------------------------------------------

## 26. Adventure ID Assignment

Permanent `ADV-####` identifiers SHOULD be preserved or assigned only after the
human editor accepts the adventure boundary and the reviewed boundary handoff is
eligible for deterministic application.

The frontier model MUST NOT choose the next Adventure IDs.

Recommended workflow:

``` text
inspect → Phase 1 → Phase 1b → Phase 2 → approve/freeze → validate → assign/preserve ID → successor AMC
```

When a newly reviewed adventure matches an existing accepted catalog record,
the existing Adventure ID SHOULD be preserved.

For newly accepted records, deterministic software SHOULD derive the next IDs
from the explicitly selected base AMC. Rejected candidates, held candidates,
and subordinate structural units do not require permanent Adventure IDs merely
because they were considered during review.

------------------------------------------------------------------------

## 27. Decision Provenance and Precedent

Non-obvious decisions SHOULD preserve enough rationale to be useful later.

At minimum, the editorial record should make it possible to reconstruct:

-   what Phase 1 candidate was considered;
-   what Phase 1b pressure question or counterevidence mattered;
-   the Survivor Play-Spine Proof for a candidate retained into Phase 2;
-   any diagnostic reason tag used to summarize a recurring qualification or
    rejection pattern;
-   the sibling-set contrast used for calibration when applicable;
-   what competing canonical interpretations were considered in Phase 2;
-   what source evidence controlled the decision;
-   whether the decision relied on a prior precedent;
-   why a prominent structural unit was accepted, rejected, merged, split, or
    held; and
-   what exact source/base-catalog provenance the approved freeze was bound to.

Not every obvious anthology record requires extensive notes.

The objective is to preserve **decision-relevant provenance**, not to create
unnecessary bureaucracy.

As the AdventureFinder catalog grows, accepted decisions SHOULD be used as
consistency checks for later sources.

------------------------------------------------------------------------

## 28. Corpus Consistency Review

The canonical AdventureFinder catalog SHOULD receive periodic corpus-level
consistency review as new ingestion exposes new structural cases.

That review SHOULD look for:

-   inconsistent treatment of similar anthology structures;
-   campaign locations promoted to Nested Adventures under inconsistent
    standards;
-   legitimate nested adventures rejected merely because they depend on a
    parent campaign;
-   linked adventures inconsistently merged or split;
-   embedded adventures missed inside sourcebooks;
-   inconsistent handling of shared front matter and appendices;
-   unexplained page overlaps or gaps;
-   records whose rationale conflicts with later accepted precedent; and
-   evidence that the Phase 1 or Phase 1b methodology is systematically
    under- or over-inclusive.

A corpus-level review may result in explicit re-review of individual records.
Accepted records SHOULD NOT silently change.

------------------------------------------------------------------------

## 29. Relationship to Deterministic Tooling

Deterministic support is now part of the established ingestion workflow, but it
remains subordinate to the editorial rules in this specification.

Current or future tooling MAY:

-   validate canonical source registration and hashes;
-   extract headings, page ranges, lexical adventure signals, level mentions,
    and other review evidence;
-   prepare AMC precedent and deterministic title-collision evidence;
-   initialize and validate structured boundary-freeze artifacts;
-   detect provenance drift or invalid nesting;
-   preserve existing Adventure IDs;
-   derive new IDs from an explicit base AMC after approval; and
-   create and verify a new successor AMC.

Tooling MUST NOT:

-   convert heading detection into canonical boundary classification;
-   silently prune the high-recall Phase 1 set;
-   replace Phase 1b or Phase 2 semantic judgment;
-   invent ambiguous source coordinates or parentage; or
-   use a generated Adventure ID to force closure of an unresolved editorial
    question.

Any page-overlap or containment evidence is subject to §5.2. A geometric
review signal MUST NOT classify duplicate-play, infer semantic parentage,
recommend merge/reject, become an identity score, mutate candidate sets, prune
Phase 1, or change canonical boundaries. Such evidence is optional support;
no overlap signal or tooling implementation is required to apply §§8.11–8.12.

The desired relationship is:

``` text
canonical source + deterministic evidence
        ↓
frontier-assisted / human-approved boundary decisions
        ↓
validated structured freeze
        ↓
deterministic catalog mutation
        ↓
accepted catalog precedent for future review
```

------------------------------------------------------------------------

## 30. Human Editorial Authority

Adventure boundary detection is an editorial classification problem informed by
published source structure.

The frontier model's purpose is to make the human decision faster, better
evidenced, and more consistent. Deterministic tooling's purpose is to remove
clerical repetition, preserve provenance, validate the handoff, and perform
mechanical catalog mutation. Neither role replaces human editorial approval.

The process SHOULD prefer:

`source evidence + explicit reasoning + human decision + deterministic provenance`

over:

`unsupported automatic classification`.

When uncertainty remains material, make it visible.

------------------------------------------------------------------------

## 31. Version 1.4 Change Summary

Version 1.4 narrowly refines nested-adventure pressure review to address
redundant-scale / subsumptive-overlap false positives.

The principal changes are:

-   pairwise **Incremental Playable Identity** comparison supplements, without
    replacing, the Survivor Play-Spine Proof;
-   **Boundary-Before-Identity** distinguishes redundant identity/scale from
    boundary defects, relationship-direction defects, and legitimate nesting;
-   page overlap, containment percentage, and interval equality are explicitly
    review evidence only, never canonical identity or correction rules;
-   confirmed duplicate-play and legitimate nesting cases calibrate the test,
    including rich sites, consequential rescues, short operations, shared
    endings, and campaign-dependent adventures; and
-   the merge-outcome wording refers to distinct identity rather than
    independence, preserving the existing nested-adventure protection.

The three-phase process, human approval authority, source-evidenced pagination,
End-Boundary Exhaustion, and deterministic handoff remain unchanged. This version
does not accept itself, correct existing records, or require new tooling.

------------------------------------------------------------------------

## 32. Version 1.3 Change Summary

Version 1.3 operationalizes the v1.2 reviewer-completion doctrine using
the repeated-template and site-based boundary lessons exposed by the
*Ruins of Eriador*, *Keepers of the Elven-Rings*, and *Moria: Shadow of
Khazad-dûm* reviews.

The principal changes are:

-   a mandatory **Survivor Play-Spine Proof** requires every Phase 1b survivor
    to state its Entry, Authored Middle, Resolution / Exit, and remaining
    Reviewer Completion explicitly;
-   the **Location-to-Adventure Threshold** now distinguishes supporting site
    evidence from **binding play-spine evidence**, preventing rich locations
    from qualifying merely by accumulating rooms, factions, lore, hazards,
    treasure, encounters, or possible objectives;
-   a **Positive Publisher Designation** rule treats labels such as adventure,
    scenario, mission, and self-contained scenario as strong evidence of
    intended playable identity without allowing those labels to waive the
    ordinary canonical tests;
-   an **External Mission Spine vs. Intrinsic Site Spine** distinction protects
    genuine directed dungeons and site adventures without requiring an
    artificial quest-giver or explicit assignment;
-   a mandatory **Homogeneous Sibling-Set Calibration** compares the weakest
    retained and strongest rejected members of repeated authorial templates
    before Phase 2, reducing source-local threshold drift;
-   compact diagnostic reason tags make recurring qualification and rejection
    patterns easier to revalidate without turning them into deterministic
    classifications; and
-   the three recent Middle-earth sourcebook reviews are preserved as named
    calibration cases for publisher designation, repeated Landmark structure,
    directed sites, and rich-location false positives.

The governing additional distinctions are:

`publisher-designated scenario ≠ automatic canonical adventure`

`explicit mission ≠ necessary or sufficient`

`rich location + adventure ingredients ≠ authored adventure`

`binding authored progression = controlling site evidence`

------------------------------------------------------------------------

## 33. Version 1.2 Change Summary

Version 1.2-draft generalizes the v1.1 sourcebook-hook lesson into a universal
reviewer-completion guardrail and codifies that a complete source review may
legitimately yield zero canonical adventures.

The principal changes are:

-   a new **Authored Play Spine and Reviewer-Completion Rule** requires the
    reviewer to distinguish published playable progression from connective play
    supplied mentally by the GM or frontier model;
-   summary verbs such as investigate, infiltrate, escort, retrieve, explore,
    and stop do not manufacture the substantive middle of an adventure;
-   a **Procedural Adventure vs. Adventure Generator** distinction separates
    procedures that themselves organize bounded play from procedures that merely
    generate adventure ingredients;
-   a **Mission-Wrapper Guardrail** prevents an assignment plus one encounter or
    set piece from bypassing the Minimum Adventure Substance Test;
-   a **Sourcebook Assembly Guardrail** prevents independent hooks, factions,
    locations, encounters, and campaign-use material from being combined into an
    adventure unless the source itself integrates them;
-   a **Zero-Adventure Source Outcome / No Adventure Quota** rule explicitly
    permits complete, successful source reviews to yield zero Adventure IDs;
-   *The Game Master's Book of Instant Towns and Cities*, *Tal'Dorei Campaign
    Setting Reborn*, *Book of Ebon Tides*, and *Tatters of Myth Drannor* are
    preserved as zero-adventure reference cases;
-   *Weird Wastelands* is preserved as a mixed calibration case distinguishing
    rich locations, mission wrappers, and generators from *The Heist*, *Deep
    Green*, and *Basalt Palace*; and
-   a **Systemic Survivor Revalidation** rule requires materially similar
    survivors to be re-pressure-tested when focused review exposes a recurring
    false-positive pattern.

The governing additional distinctions are:

`imagined runnability ≠ authored playability`

`procedure that generates adventures ≠ procedural adventure`

`zero accepted adventures ≠ failed ingestion`

------------------------------------------------------------------------

## 34. Version 1.1 Change Summary

Version 1.1-draft codifies a sourcebook-hook failure mode exposed by the
*Grim Hollow: The Campaign Guide* boundary review while preserving the existing
high-recall Phase 1 and short-adventure protections.

The principal changes are:

-   explicit publisher designation as a quest hook, adventure hook, adventure
    seed, idea for an adventure, or similar generative material is strong
    counterevidence during Phase 1b and Phase 2 rather than a neutral label;
-   a new Publisher-Designated Hook, Seed, and Adventure-Idea Rule distinguishes
    **narrative completeness** from **playable completeness**;
-   detailed premise, antagonist, twist, climax, and outcome information cannot
    substitute for authored scenes, clues, locations, encounters, procedures,
    choices, obstacles, or other substantive progression;
-   generic surrounding sourcebook material may not be borrowed to manufacture
    adventure substance unless the source integrates it into the candidate's
    playable structure;
-   explicit clarification that **scoreability is not canonical adventure
    identity**;
-   the Minimum Adventure Substance Test now explicitly applies beyond nested
    campaign units to sourcebook and scenario/encounter candidates; and
-   the *Grim Hollow* Quest Hook review is preserved as a named precedent while
    retaining `short ≠ non-adventure` and the absence of any minimum page or word
    count.

The governing additional distinction is:

`detailed hook ≠ published adventure`

unless affirmative source evidence establishes a substantially bounded body of
play.

------------------------------------------------------------------------

## 35. Version 1.0 Change Summary

Version 1.0 promotes the Adventure Boundary Detection Specification from a
Seed-Catalog-era draft into the accepted operational boundary standard for
ongoing AdventureFinder library ingestion.

The principal changes are:

-   formalization of the three-pass editorial workflow used in recent ingestion:
    **Phase 1 high-recall harvest → Phase 1b pressure/sanity review → Phase 2
    canonical identity/nesting/boundary adjudication**;
-   explicit requirement that Phase 1 inspect the complete relevant source span
    and retain borderline or embedded candidates rather than prematurely
    collapse them;
-   explicit definition of Phase 1b as a separate discriminating pass that
    pressure-tests the deliberately inclusive Phase 1 set without forcing
    ambiguous cases closed;
-   explicit Phase 2 PASS criteria for canonical title, source-evidenced page
    boundaries, restrained parentage, optional source-established levels, and
    traceable disposition of the original Phase 1 set;
-   formal separation of deterministic evidence preparation, frontier semantic
    review, and human approval;
-   recognition of a provenance-bound structured boundary freeze as the narrow
    handoff between editorial reasoning and deterministic catalog mutation;
-   prohibition on frontier assignment of new Adventure IDs;
-   deterministic ID derivation only after a human-approved handoff validates
    against an explicit base AMC;
-   requirement to create a new successor AMC rather than mutate the base
    workbook in place; and
-   generalization from the original 35-book Seed Catalog project to ongoing
    ingestion and maintenance of David's actual adventure library.

Version 1.0 preserves the substantive nested-adventure, Playable Identity,
Location-to-Adventure, Minimum Adventure Substance, source-evidenced pagination,
and End-Boundary Exhaustion rules established in versions 0.5 through 0.7.

------------------------------------------------------------------------

## 36. Version 0.7 Change Summary

Version 0.7 adds a hard **End-Boundary Exhaustion Rule** for exact End
Page values.

The principal changes are:

-   finding conclusion, aftermath, epilogue, reward, or transition
    material does not itself establish the final page of an adventure;
-   the reviewer MUST continue sequentially through the available source
    until affirmative evidence establishes that the adventure-owned
    semantic unit has ended;
-   conclusion/epilogue-style headings establish that ending material has
    begun, not where it ends;
-   if termination cannot be affirmatively established, the End Page
    remains **Uncertain / Requires Source Verification**.

The governing operational rule is:

`finding ending material ≠ finding the end`

------------------------------------------------------------------------

## 37. Version 0.6 Change Summary

Version 0.6 adds a hard **Source-Evidenced Pagination Rule** for exact
Start Page and End Page values.

The principal changes are:

-   exact page boundaries require affirmative source evidence;
-   page-marker gaps, neighboring section boundaries, expected
    pagination, page counts, and document structure MUST NOT be used
    alone to infer an exact boundary;
-   missing, unmarked, image-only, or otherwise ambiguous pages require
    **Uncertain / Requires Source Verification** rather than an estimate;
-   a later known page marker does not establish semantic ownership of
    intervening pages;
-   direct printed-page evidence governs when it conflicts with an
    incomplete normalized Markdown extraction.

The governing operational rule is:

`exact boundary → affirmative source evidence`

`missing evidence → uncertainty flag`

`never fill a pagination gap by interpolation`

------------------------------------------------------------------------

## 38. Version 0.5 Change Summary

Version 0.5 refines the specification to correct an under-segmentation
bias exposed by integrated, location-driven campaigns such as *Curse of
Strahd*.

The principal changes are:

-   explicit recognition of **Nested Adventures**;
-   replacement of standalone-independence thinking with the **Playable
    Identity Test**;
-   explicit statement that parent dependence does not disqualify a
    candidate;
-   allowance for overlapping parent/child page ranges;
-   a **Location-to-Adventure Threshold** for site-based adventures;
-   a **Minimum Adventure Substance Test** to control over-segmentation;
-   historical or external standalone identity as strong supporting
    evidence;
-   a hierarchical model distinguishing Parent Adventures, Peer
    Adventures, Nested Adventures, and Subordinate Structural Units;
-   *Curse of Strahd* and Castle Ravenloft as explicit reference cases.

The intended balance is:

`embedded ≠ non-adventure`

`campaign-dependent ≠ non-adventure`

while preserving:

`location ≠ automatically adventure`

`chapter ≠ automatically adventure`

`clear internal structure ≠ automatically canonical adventure identity`

------------------------------------------------------------------------

## 39. Editorial Philosophy and Method Evolution

AdventureFinder catalogs **identifiable playable adventures at multiple
levels of composition, not merely printed chapters**.

A larger adventure may contain smaller adventures without either losing
canonical identity.

The governing question is not whether a candidate is independent of its
parent, but whether it has a **substantially bounded and recognizable
playable identity within its parent**.

When editorial judgment is required, the following take precedence over
strict adherence to chapter boundaries, generated-document boundaries,
or page counts:

1.  fidelity to the published source;
2.  evidence-based judgment;
3.  consistency with comparable catalog decisions;
4.  repeatability by another reviewer.

Future revisions SHOULD be adopted when experience with actual
cataloging demonstrates that they:

-   improve editorial consistency;
-   reduce ambiguity;
-   increase repeatability;
-   correct demonstrated weaknesses;
-   make LLM-assisted human review more efficient without weakening
    evidence standards.

When a methodological change materially affects an accepted record, that
record SHOULD be explicitly re-reviewed rather than silently changed.

------------------------------------------------------------------------

## 40. Success Criteria for Ongoing Library Ingestion

This specification is succeeding if the frontier-assisted human workflow can:

-   inspect each source with sufficiently high Phase 1 recall that plausible
    embedded adventures are not lost prematurely;
-   use Phase 1b to remove genuine false positives without reverting to
    product-level under-segmentation;
-   distinguish product, chapter, location, encounter, framework, and adventure
    boundaries consistently;
-   establish defensible, source-evidenced Start Page and End Page values;
-   explain non-obvious identity and nesting decisions from source evidence;
-   surface genuine ambiguity for human resolution rather than invent certainty;
-   preserve consistent treatment across structurally similar books;
-   produce an approved, provenance-bound canonical record set suitable for
    deterministic successor-AMC creation; and
-   accumulate enough traceable precedents to make future ingestion faster and
    more consistent without weakening editorial judgment.

The objective is **not autonomous boundary detection**.

The objective is a **repeatable, evidence-based editorial process for expanding
and maintaining the canonical AdventureFinder library with frontier assistance,
human control, and deterministic provenance-preserving handoffs**.

------------------------------------------------------------------------

## 41. Revision History

  ---------------------------------------------------------------------------------------------------
  Version           Date              Status            Description
  ----------------- ----------------- ----------------- ---------------------------------------------
  1.4               2026-09-28        Accepted          Adds pairwise Incremental Playable Identity,
                                                        Boundary-Before-Identity diagnosis, overlap as
                                                        review evidence only, and regression controls;
                                                        preserves legitimate nested adventures and the
                                                        existing editorial workflow. No catalog
                                                        correction authorized.

  1.3               2026-09-13        Accepted          Adds mandatory Survivor Play-Spine Proofs,
                                                        supporting-vs-binding site evidence, positive
                                                        publisher-designation handling, external-mission
                                                        versus intrinsic-site spines, homogeneous
                                                        sibling-set calibration, diagnostic reason tags,
                                                        and Middle-earth Landmark calibration from
                                                        *Ruins of Eriador*, *Keepers of the Elven-Rings*,
                                                        and *Moria: Shadow of Khazad-dûm*.

  1.2-draft         2026-09-13        Draft             Adds the Authored Play Spine and
                                                        Reviewer-Completion Rule, procedural-adventure
                                                        versus adventure-generator distinction,
                                                        mission-wrapper and sourcebook-assembly
                                                        guardrails, zero-adventure-source outcomes,
                                                        systemic survivor revalidation, and named
                                                        *Weird Wastelands* / zero-adventure sourcebook
                                                        calibration cases.

  1.1-draft         2026-09-13        Draft             Adds a publisher-designated hook/seed rule,
                                                        distinguishes narrative completeness from
                                                        playable completeness, forbids using generic
                                                        surrounding sourcebook material or scoreability
                                                        to manufacture canonical adventure identity,
                                                        generalizes Minimum Adventure Substance beyond
                                                        nested campaign units, and records the *Grim
                                                        Hollow: The Campaign Guide* Quest Hook review as
                                                        a precedent.

  1.0               2026-09-12        Accepted          Formalizes the operational three-pass ingestion
                                                        workflow: high-recall Phase 1 harvest, separate
                                                        Phase 1b pressure/sanity review, and Phase 2
                                                        canonical identity/nesting/boundary adjudication.
                                                        Adds deterministic evidence/freeze/successor-AMC
                                                        trust boundaries, forbids frontier-assigned new
                                                        Adventure IDs, and generalizes ABDS from the seed
                                                        corpus to ongoing library ingestion.

  0.7-draft         2026-08-08        Draft             Adds a hard End-Boundary Exhaustion Rule:
                                                        finding ending material does not establish the
                                                        final End Page; reviewers must continue
                                                        sequentially until the adventure-owned semantic
                                                        unit is affirmatively shown to terminate, or
                                                        mark the boundary for source verification.

  0.6-draft         2026-08-08        Draft             Adds a hard Source-Evidenced Pagination Rule:
                                                        exact Start/End Pages require affirmative
                                                        source evidence; pagination gaps must not be
                                                        interpolated; ambiguous or image-only pages
                                                        require source verification; and direct
                                                        printed-page evidence governs over incomplete
                                                        normalized Markdown extraction.

  0.4-draft         2026-08-08        Draft             Refocuses the specification from
                                                        deterministic Ruby boundary detection to
                                                        LLM-assisted, human-prompted construction of
                                                        the initial 35-book WotC Seed Adventure
                                                        Catalog. Preserves the core editorial
                                                        definition, Core Boundary Test, Substantial
                                                        Distinctness Test, product classes,
                                                        page-boundary rules,
                                                        false-positive/false-negative safeguards, and
                                                        key precedent cases. Replaces
                                                        implementation-centric evidence classes,
                                                        machine recommendation records,
                                                        bulk-ingestion policy, development phases,
                                                        and detector success criteria with a
                                                        human--LLM editorial model, compact
                                                        evidence-based recommendation format,
                                                        book-by-book Seed Catalog workflow, decision
                                                        provenance, corpus-level consistency review,
                                                        and an explicit future relationship between
                                                        the human-reviewed seed corpus and later
                                                        automation.

  0.3-draft         2026-08-08        Draft             Organizational refinement for deterministic
                                                        `af-corpus-ingester-basics` implementation.
                                                        Added a normative ordered decision procedure;
                                                        classified tests as Hard Requirement,
                                                        Exclusion, Supporting Evidence,
                                                        Counterevidence, or Ambiguity-Resolution;
                                                        defined `ACCEPT`/`REJECT`/`REVIEW` as
                                                        detector recommendations rather than
                                                        canonical status; and required conservative
                                                        `REVIEW` behavior when semantic editorial
                                                        requirements could not be established
                                                        deterministically.

  0.2-draft         2026-08-08        Draft             Merged relevant boundary and editorial
                                                        guidance from Adventure Catalog Editorial
                                                        Standard Revision 1.1, including
                                                        fidelity/evidence/consistency/repeatability
                                                        principles, boundary-first workflow,
                                                        complete-story-arc and independent-objective
                                                        criteria, anti-shortcut safeguards,
                                                        internal-only editorial confidence,
                                                        editorial-lock expectations, and methodology
                                                        revision principles.

  0.1-draft         2026-08-08        Draft             Initial formal boundary-detection
                                                        specification derived from Adventure Catalog
                                                        Editorial Specification Rev 2.0, accepted
                                                        catalog examples, and prior AdventureFinder
                                                        cataloging methodology.
  ---------------------------------------------------------------------------------------------------
