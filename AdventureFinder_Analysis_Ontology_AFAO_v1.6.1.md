# AdventureFinder Analysis Ontology

## Version 1.6.1

**Status:** Candidate — Pending targeted GM Preparation Burden 4/5 revalidation
**Date:** 2026-08-28

## Purpose

This document defines the 19-dimension AdventureFinder
ontology used to describe and match published adventures.

The working set includes two editorially assessed catalog
dimensions---**\# of Sessions** and **Levels**---alongside seventeen
interpretive AdventureFinder analysis dimensions. Their inclusion in the
same working ontology reflects their shared role in adventure matching;
it does not erase the architectural distinction between catalog data and
interpretive analysis.

## Canonical Dimension Acronyms

The following acronyms are the canonical AdventureFinder shorthand identifiers
for the nineteen dimensions in this ontology. They MAY be used in documentation,
filenames, experiment manifests, tables, logs, and user interfaces.

The full canonical dimension names remain authoritative. These acronyms are
aliases only: they do not rename dimensions, alter assessment fields, change
scoring semantics, or modify any definition, anchor, calibration guidance, or
matching behavior. In particular, **LSLE** refers to the single editorially
assessed **Levels** dimension represented by its two canonical assessment values,
**Level Start** and **Level End**.

Canonical acronyms are case-sensitive as shown and MUST NOT be reassigned to a
different AdventureFinder dimension in a later ontology version.

| # | Acronym | Canonical dimension |
| ---: | :--- | --- |
| 1 | **NoS** | **# of Sessions** |
| 2 | **LSLE** | **Levels** (*Level Start / Level End*) |
| 3 | **CE** | **Combat Emphasis** |
| 4 | **EE** | **Exploration Emphasis** |
| 5 | **SIE** | **Social Interaction Emphasis** |
| 6 | **IE** | **Investigation Emphasis** |
| 7 | **PPSE** | **Puzzle / Problem-Solving Emphasis** |
| 8 | **TC** | **Tactical Complexity** |
| 9 | **LFS** | **Lethality / Failure Severity** |
| 10 | **RSMD** | **Rules / System-Mastery Demand** |
| 11 | **SO** | **Structural Openness** |
| 12 | **CPA** | **Consequential Player Agency** |
| 13 | **SR** | **Seriousness** |
| 14 | **DHI** | **Darkness / Horror Intensity** |
| 15 | **FW** | **Fantastic Weirdness** |
| 16 | **GMPB** | **GM Preparation Burden** |
| 17 | **GMID** | **GM Improvisation Demand** |
| 18 | **PBS** | **Player Beginner Suitability** |
| 19 | **GMBS** | **GM Beginner Suitability** |

## Editorially Assessed Catalog Dimensions

  -----------------------------------------------------------------------
  \#                      Dimension               What it measures
  ----------------------- ----------------------- -----------------------
  1                       **\# of Sessions        The normalized
                          (2.5--3.0 hour          practical number of
                          sessions)**             2.5--3.0 hour play
                                                  sessions required to
                                                  complete the adventure.

  2                       **Levels**              The primary intended
                                                  starting character level
                                                  and the character level
                                                  reached by completion of
                                                  the canonical adventure.
  -----------------------------------------------------------------------

## Analysis Dimensions

  ----------------------------------------------------------------------------
  **\#**                  **Dimension**           **What it measures**
  ----------------------- ----------------------- ----------------------------
  **Play Mix**                                    

  3                       **Combat Emphasis**     How much of the adventure's
                                                  play is centered on combat.

  4                       **Exploration           How much play centers on
                          Emphasis**              discovering, traversing, and
                                                  interacting with
                                                  environments.

  5                       **Social Interaction    How much meaningful play
                          Emphasis**              centers on interaction with
                                                  NPCs.

  6                       **Investigation         How much play centers on
                          Emphasis**              gathering, connecting, and
                                                  interpreting information to
                                                  determine what is happening
                                                  or has happened.

  7                       **Puzzle /              How much play centers on
                          Problem-Solving         overcoming explicit
                          Emphasis**              noncombat problems through
                                                  reasoning or creative
                                                  solutions.

  **Challenge Character**                         

  8                       **Tactical Complexity** How much live tactical
                                                  decision load meaningful
                                                  encounters create through
                                                  interacting factors,
                                                  changing state, and required
                                                  tactical adaptation.

  9                       **Lethality / Failure   How readily mistakes or
                          Severity**              failure can produce severe,
                                                  lasting, or irreversible
                                                  consequences.

  10                      **Rules /               How strongly successful play
                          System-Mastery Demand** depends on understanding and
                                                  effectively using the game's
                                                  mechanical systems.

  **Adventure Structure**                         

  11                      **Structural Openness** How much freedom players
                                                  have over the path,
                                                  sequence, and order through
                                                  the adventure.

  12                      **Consequential Player  How substantially player
                          Agency**                decisions can alter events,
                                                  relationships, states, or
                                                  outcomes.

  **Experience / Tone**                           

  13                      **Seriousness**         How far the dominant
                                                  experience runs from
                                                  comic/playful/lighthearted
                                                  toward
                                                  earnest/dramatic/serious.

  14                      **Darkness / Horror     How disturbing, frightening,
                          Intensity**             grim, horrific, or
                                                  emotionally dark the
                                                  adventure is.

  15                      **Fantastic Weirdness** How far the adventure
                                                  departs from
                                                  familiar/conventional
                                                  fantasy toward bizarre,
                                                  surreal, dreamlike, or
                                                  highly unusual material.

  **GM Demands**                                  

  16                      **GM Preparation        How much work the GM
                          Burden**                ordinarily must perform
                                                  before play to run the
                                                  adventure effectively.

  17                      **GM Improvisation      How much the GM must invent,
                          Demand**                synthesize, react, or
                                                  adjudicate beyond explicitly
                                                  prepared material during
                                                  play.

  **Beginner                                      
  Suitability**                                   

  18                      **Player Beginner       How well the adventure
                          Suitability**           supports inexperienced
                                                  players in understanding
                                                  objectives, making
                                                  meaningful choices, learning
                                                  expected modes of play, and
                                                  participating successfully.

  19                      **GM Beginner           How well the published
                          Suitability**           adventure supports an
                                                  inexperienced GM in
                                                  understanding, preparing,
                                                  explaining, adjudicating,
                                                  and successfully running it.
  ----------------------------------------------------------------------------


## Editorially Assessed Matching-Dimension Rubrics

### 1. # of Sessions

**Definition:** The normalized practical number of **2.5--3.0 hour table
sessions** ordinarily required to complete the canonical adventure
substantially as published.

# of Sessions is an **editorially assessed matching dimension**, not a 1--5
interpretive analysis score. Its purpose is to provide a consistent practical
duration estimate that supports user requests such as one-shot,
short-adventure, mini-campaign, and campaign-length filtering even when
publishers and individual tables use different meanings of a "session."

The assessment describes the amount of **expected substantive table play**,
not the adventure's page count, advertised format, level range, GM preparation
time, or maximum theoretically available content.

**Status:** Frozen, calibrated, and blind-validated duration-estimation rubric.
The definition, 2.5--3.0 hour normalization baseline, whole-number estimator,
substantially-as-published standard, optional-content weighting, Practical
Range, Confidence, Path Sensitive handling, calibration regimes, and
assessment-state rules below are locked for the current ontology version.
Future changes to their wording or meaning require an explicit ontology
revision and revalidation.

#### Primary Assessment Value

The primary # of Sessions value is a **positive whole-number best estimate**.

Examples:

- `1`
- `2`
- `4`
- `9`
- `18`
- `35`

The integer represents the editor's best estimate of how many normalized
AdventureFinder sessions an ordinary group would practically require to
complete the canonical adventure.

It is not an ordinal category. An adventure assessed at 12 sessions is
expected to require approximately twice as much normalized table time as one
assessed at 6 sessions, subject to the ordinary uncertainty inherent in
tabletop play.

Fractions and half-sessions are not used. Uncertainty between adjacent
whole-number estimates is represented through Practical Range and Confidence.

#### Supporting Assessment Fields

A completed # of Sessions assessment SHOULD retain the following supporting
information:

| Field | Meaning |
| --- | --- |
| **Normalized Sessions** | Best whole-number estimate of required 2.5--3.0 hour sessions. |
| **Practical Range** | Reasonable low-to-high normalized session range for substantially-as-published play. |
| **Confidence** | 0%--100% confidence in the best estimate. |
| **Path Sensitive** | Whether substantially supported published paths can materially change completion time. |

The **Normalized Sessions** value is the principal value used for matching and
filtering. Practical Range represents meaningful uncertainty and ordinary
variation rather than replacing the best estimate.

For example, an assessment might be represented conceptually as:

`Normalized Sessions: 4`  
`Practical Range: 3--5`  
`Confidence: 80%`  
`Path Sensitive: No`

A broad Practical Range does not by itself require low confidence. An
adventure can be confidently known to have substantial inherent duration
variation. Likewise, a narrow Practical Range does not guarantee high
confidence if the available published evidence is insufficiently informative
about actual table duration.

#### Normalized Session Baseline

AdventureFinder normalizes all assessments to a **2.5--3.0 hour play
session**.

The midpoint of approximately **2.75 hours** MAY be used as a reasoning aid
when converting explicit hour estimates or other duration evidence, but
reviewers SHOULD NOT mechanically derive the final assessment by inventing a
total-hour estimate and dividing it by 2.75.

The governing question is:

> **How many ordinary 2.5--3.0 hour AdventureFinder sessions would the
> expected substantive play of this canonical adventure practically occupy?**

The normalization exists so adventures and user requests can be compared even
when publishers or individual tables use different definitions of a
"session."

#### Published Duration and Format Claims

Publisher statements such as:

- "one-shot";
- "one evening";
- "4--6 hours";
- "two-session adventure";
- "mini-campaign";
- "campaign"

are relevant evidence but do **not** automatically determine the normalized
AdventureFinder value.

A publisher's description records intended or advertised form.
AdventureFinder records a normalized practical estimate.

An adventure advertised as a one-shot may therefore receive `2` normalized
sessions when ordinary completion does not comfortably fit the 2.5--3.0 hour
baseline. Conversely, compact material not advertised as a one-shot may still
receive `1`.

When a publisher provides an explicit hour estimate, that estimate SHOULD
receive substantial evidentiary weight, but source inspection should still
determine whether it describes:

- full completion;
- convention or accelerated play;
- a particular route;
- selected rather than complete material; or
- another play assumption materially different from AdventureFinder's
  substantially-as-published baseline.

Published duration evidence SHOULD be recorded separately from the normalized
assessment when the production data model supports it.

#### Canonical Adventure Unit

The assessment MUST score the **canonical Adventure ID**, not automatically the
containing source book, campaign, chapter, or parent adventure.

If a canonical nested adventure occupies only part of a larger campaign, its
duration is assessed independently.

Likewise, the existence of separately cataloged nested adventures does not
require subtracting their play time from a parent adventure when the parent
canonically includes that material. Parent and child Adventure IDs may
therefore legitimately have overlapping duration just as their canonical page
boundaries may overlap.

#### Substantially-as-Published Completion

Estimate an ordinary group attempting to **complete the adventure
substantially as published**.

Do not estimate either:

1. the shortest theoretically possible route; or
2. exhaustive completion of every piece of material in the publication.

The assessment SHOULD include substantive play that ordinary completion is
likely to involve and probability-weight optional or branching material
according to its expected presence in substantially-as-published play.

#### What Counts Toward Session Duration

Substantive table activities ordinarily count when they are expected to
consume meaningful play time, including:

- combat;
- meaningful social interaction;
- investigation;
- puzzles and problem solving;
- environmental exploration;
- dungeon or site traversal;
- meaningful travel;
- player planning and strategy;
- consequential decision-making;
- adventure-specific structured activities;
- required transitions, aftermaths, and resolutions;
- other interactive material expected to occur at the table.

The existence of an activity does not imply a fixed time cost. Reviewers
should judge the amount of table play it is likely to generate in context.

#### What Does Not Automatically Count

The following MUST NOT be converted directly into session time merely because
they occupy published space:

- GM-facing background;
- setting exposition;
- histories and lore;
- stat blocks;
- rules reference;
- appendices;
- character options;
- maps;
- handouts;
- random tables;
- duplicated reference material;
- optional material unlikely to arise;
- material belonging to the source book but outside the canonical Adventure
  ID.

Such material can indirectly affect duration when it supports substantive
table play, but publication length is not itself play duration.

#### Page Count Is Evidence, Not a Formula

Page count MAY provide supporting evidence, especially when comparing
adventures with similar presentation and structural density, but MUST NOT be
used as a direct conversion formula.

Two adventures of equal page length may generate very different amounts of
substantive table play because of differences in encounter density, branching,
social interaction, exploration, puzzles, reference material, presentation
style, or optional content.

Likewise, a short publication can support substantial play, while a longer
publication may devote considerable space to material that consumes little or
no table time.

#### Level Range Is Evidence, Not a Formula

Character level and level range MAY provide contextual evidence about
adventure scope but MUST NOT determine # of Sessions mechanically.

An adventure spanning many levels often contains substantial playable
material, but advancement rate varies considerably across published
adventures. Milestone advancement, starting level, ending level, or number of
expected level gains therefore cannot substitute for direct examination of the
adventure's playable structure.

#### Optional and Branching Content

Optional and branching material SHOULD be **probability-weighted** according
to substantially-as-published expected play.

If an adventure contains five optional quests but an ordinary supported
trajectory is likely to use approximately two, estimate the expected two
rather than automatically adding the play time of all five.

If the adventure presents several mutually exclusive large alternatives, an
ordinary trajectory that uses one alternative should count approximately one,
not the sum of every authored alternative.

If players are expected to spend substantive time choosing among routes,
locations, factions, or objectives, that decision-making and the selected
material count normally.

Material that is technically available but rarely encountered should carry
substantially less weight.

#### Bypasses and Alternate Resolutions

Published methods for bypassing encounters or resolving situations through
different modes of play are part of the expected duration model.

Reviewers MUST NOT assume that every combat occurs, every keyed area is
explored, every clue is pursued, or every optional objective is completed when
the adventure explicitly supports ordinary routes that omit them.

At the same time, the mere theoretical possibility of unusually rapid play
does not establish the expected duration. The relevant question remains what
an ordinary group following substantially supported published play is likely
to experience.

#### In-Fiction Time Is Not Table Time

Adventure clocks, travel durations, rests, day-by-day structures, countdowns,
and other **in-fiction time measures** MUST NOT be mechanically converted into
real table duration.

A one-hour fictional deadline may occupy several hours of table play; an
in-fiction journey of weeks may be resolved rapidly. Such structures matter
only insofar as the procedures and decisions they generate consume substantive
table play.

This guardrail proved important during calibration for adventures containing
one-hour mission clocks, multi-day investigation structures, fixed-duration
festival clocks, and campaign events unfolding over months in fiction.

#### Player Pace and Ordinary Table Variation

# of Sessions necessarily contains more table-to-table variability than most
AdventureFinder dimensions.

Groups differ in:

- deliberation speed;
- roleplaying duration;
- combat speed;
- rules familiarity;
- exploration thoroughness;
- puzzle-solving speed;
- use of optional content;
- amount of planning and discussion.

The assessment SHOULD assume an **ordinary engaged D&D table**, neither
unusually accelerated nor unusually leisurely.

Reviewers MUST NOT inflate duration for extensive unrelated table talk,
elaborate GM-added scenes, or player-created side activity unsupported by the
adventure. Reviewers likewise MUST NOT assume convention-style acceleration,
aggressive scene cutting, foreknowledge, unusually optimized combat
resolution, or other speed-running behavior.

Practical Range exists in part to represent normal variation around the best
estimate.

#### Practical Range

The **Practical Range** expresses a reasonable low-to-high number of normalized
sessions for substantially-as-published play.

It should capture ordinary variation arising from factors such as:

- supported route differences;
- combat duration;
- exploration thoroughness;
- decision speed;
- optional content;
- social-play depth.

It should not attempt to capture extreme theoretical possibilities.

The best Normalized Sessions estimate SHOULD fall inside the range.

A broad range does not automatically imply low confidence.

#### Path Sensitivity

**Path Sensitive: Yes** should be recorded when **published structural
choices** can materially alter total duration.

Examples include adventures where:

- major branches contain substantially different amounts of playable material;
- large regions or objectives can legitimately be omitted;
- one supported resolution bypasses a substantial body of play;
- sandbox selection can produce significantly shorter or longer completion
  paths;
- randomized adventure structure materially changes how much content is
  encountered.

Minor variation in encounter order, ordinary exploration thoroughness,
ordinary puzzle-solving speed, or ordinary table pace is not sufficient.

Path sensitivity concerns **structural duration variance arising from the
published adventure**, not merely the universal fact that different groups
play at different speeds.

When path sensitivity is present, the best estimate should represent the
expected substantially-as-published trajectory, while Practical Range should
capture plausible materially shorter and longer supported paths.

#### Confidence

Confidence records how strongly the source and available evidence support the
assigned best estimate.

High confidence is appropriate when:

- the playable body is clearly bounded;
- expected encounters and activities are readily identifiable;
- optionality is limited or well understood;
- publisher duration evidence is compatible with source structure;
- comparison with calibrated benchmarks produces a stable estimate.

Lower confidence may be appropriate when:

- the adventure is highly open-ended;
- optional content dominates;
- published duration claims conflict with playable structure;
- expected player behavior strongly affects how much material appears;
- the available source is incomplete;
- adventure boundaries relevant to duration are uncertain.

Uncertainty between adjacent whole-number estimates ordinarily should be
represented through Confidence and Practical Range rather than by using
fractions.

#### Assessment State

AdventureFinder distinguishes between an assessment not yet performed and an
attempted assessment that cannot responsibly produce a normalized session
estimate.

- **Blank --- Not Yet Assessed.** No completed # of Sessions assessment exists.
- **`-1` --- Insufficient Evidence.** Assessment was attempted, but available
  evidence cannot support a responsible normalized estimate.
- **Positive integer --- Assessed.** Evidence supports a best whole-number
  normalized session estimate.

`-1` is a sentinel value and MUST NOT participate in duration calculations,
filtering, ranking, averages, or other operations treating it as an actual
session count.

Insufficient Evidence should be used sparingly. Normal uncertainty about
tabletop pace, disagreement between adjacent estimates, or a broad Practical
Range does not by itself justify `-1`.

#### Calibration Regimes

Because # of Sessions is a numeric duration estimate rather than an ordinal
1--5 interpretive score, its calibration procedure uses practical duration
regimes for **coverage and validation only**:

| Calibration regime | Normalized session range | Calibration purpose |
| --- | ---: | --- |
| **Very Short** | **1--2 sessions** | Tests one-shot and near-one-shot estimation, where a difference of one session is proportionally large and especially important for matching. |
| **Short** | **3--5 sessions** | Tests compact multi-session adventures and the transition from one-shot-scale material to short arcs. |
| **Medium** | **6--11 sessions** | Tests substantial standalone adventures and compact mini-campaign-scale material. |
| **Short Campaign-scale** | **12--23 sessions** | Tests adventures that clearly function across an extended series of sessions but remain materially shorter than long-form campaigns. |
| **Long Campaign-scale** | **24+ sessions** | Tests full-length campaigns whose expected play extends across many normalized sessions. |

These regimes are **calibration bands only**. They MUST NOT replace the
adventure's numeric Normalized Sessions value and MUST NOT be treated as a
second categorical scoring system.

The regime boundaries exist to:

- ensure calibration coverage across the duration spectrum;
- detect systematic compression or inflation by reviewers;
- provide useful benchmark neighborhoods; and
- ensure that calibration does not concentrate only on conventional short
  adventures.

An adventure assessed at 11 sessions and one assessed at 12 sessions remain
numerically adjacent even though they fall into different regimes. The
5/6, 11/12, and 23/24 regime boundaries are therefore **not qualitative score
anchors requiring adjacent-boundary calibration** in the manner of the 1--5
interpretive dimensions.

Particular attention SHOULD nevertheless be given to the **1-session versus
2-session distinction** because one-shot suitability is a common and
practically important user constraint.

#### Calibration Benchmarks

The following normalized session estimates are reference exemplars produced by
full-source calibration under the frozen rubric. They illustrate the estimator
across the duration spectrum but do not replace direct assessment of future
adventures.

| Normalized Sessions | Calibrated benchmark adventures | Calibration regime |
| ---: | --- | --- |
| **1** | **ADV-0200 — Lake Monster** | Very Short |
| **2** | **ADV-0230 — Salvage Operation**; **ADV-0062 — No Honour Among Thieves**; **ADV-0053 — Call of the Wild** | Very Short |
| **3** | **ADV-0287 — House of Lament** | Short |
| **4** | **ADV-0034 — Tomb of Horrors** | Short |
| **7** | **ADV-0040 — Expedition to the Barrier Peaks** | Medium |
| **10** | **ADV-0262 — Lost Mine of Phandelver** | Medium |
| **18** | **ADV-0277 — The Wild Beyond the Witchlight** | Short Campaign-scale |
| **26** | **ADV-0303 — Storm King's Thunder** | Long Campaign-scale |

These benchmarks are empirical duration reference points rather than
qualitative anchors. Future adventures MUST NOT be assigned a session count
solely because they resemble a benchmark in page count, level range, genre, or
product format.

Useful benchmark comparison asks whether the future adventure contains
materially more or less **expected substantive table play** than a calibrated
reference while applying the same normalization and optional-content rules.

#### Calibration and Blind Validation Record

Initial full-source calibration deliberately covered the full duration
spectrum rather than searching for artificial examples immediately adjacent to
every calibration-regime boundary. The ten-case pass produced best estimates
of **1, 2, 2, 2, 3, 4, 7, 10, 18, and 26 sessions** across all five regimes.

A subsequent independent blind reviewer applied the frozen specification
without access to prior # of Sessions estimates, Practical Ranges, confidence
values, path-sensitivity judgments, regime placements, duration rationales, or
benchmark assignments.

The blind pass exactly reproduced the best integer estimate for eight of ten
cases:

- **ADV-0200 — Lake Monster:** 1;
- **ADV-0230 — Salvage Operation:** 2;
- **ADV-0062 — No Honour Among Thieves:** 2;
- **ADV-0053 — Call of the Wild:** 2;
- **ADV-0287 — House of Lament:** 3;
- **ADV-0034 — Tomb of Horrors:** 4;
- **ADV-0040 — Expedition to the Barrier Peaks:** 7;
- **ADV-0262 — Lost Mine of Phandelver:** 10.

For the two campaign-scale cases, the blind reviewer returned **16** rather
than 18 for **ADV-0277 — The Wild Beyond the Witchlight** and **24** rather than
26 for **ADV-0303 — Storm King's Thunder**. These were treated as successful
**practical reproduction**, not material estimator disagreement: both blind
ranges heavily overlapped the initial ranges, both cases remained in the same
calibration regime, and the independent reviewer identified substantially the
same expected-play structure and optional-content weighting.

The blind pass also independently reproduced the most important methodological
guardrails:

- publisher "one-shot" labels for **No Honour Among Thieves** and **Call of the
  Wild** were treated as evidence rather than automatically scored as one
  normalized session;
- mutually exclusive or optional content was probability-weighted rather than
  exhaustively summed;
- in-fiction clocks and calendars were not converted mechanically into table
  time;
- page count and level span did not substitute for direct playable-structure
  assessment; and
- the same estimator remained usable from a one-session quest through a
  long-form campaign.

The blind pass therefore successfully pressure-tested the practically important
**1 versus 2** distinction: **Lake Monster 1 → Salvage Operation / No Honour
Among Thieves / Call of the Wild 2 → House of Lament 3** was reproduced
independently.

Two blind disagreements concerned the supporting **Path Sensitive** flag rather
than the Normalized Sessions estimate: **Salvage Operation** and **Tomb of
Horrors** were initially flagged path-sensitive but the blind reviewer treated
their duration variation primarily as ordinary exploration, reasoning, and
pace variance. These supporting-flag disagreements do not alter the calibrated
integer duration benchmarks above and reinforce the frozen rule that Path
Sensitive requires materially different **published structural paths**, not
merely ordinary table-speed variation.

No calibration case required `-1 — Insufficient Evidence`, and no defect or
material ambiguity requiring revision of the frozen duration-estimation rubric
was identified.

#### Blind-Validation Agreement Interpretation

Because # of Sessions estimates an inherently variable numeric quantity,
validation MUST NOT treat every non-identical integer as analogous to a
1--5-anchor disagreement.

Validation SHOULD distinguish:

1. **Exact agreement** — reviewers assign the same best estimate.
2. **Practical agreement** — estimates differ modestly while Practical Ranges
   materially overlap and reviewers identify substantially the same expected
   playable body and normalization logic.
3. **Material numeric disagreement** — estimates differ enough to imply a
   meaningfully different practical duration.
4. **Structural disagreement** — reviewers disagree about what published
   material belongs in the ordinary completion trajectory.
5. **Normalization disagreement** — reviewers identify similar playable
   material but translate it into 2.5--3.0-hour sessions differently.

Structural and normalization disagreements are particularly important because
they can reveal defects in the estimator even when two numeric results happen
to be close. Conversely, a small campaign-scale integer difference with
strongly overlapping ranges need not imply a calibration failure.

#### Relationship to User Query Normalization

The stored # of Sessions assessment and interpretation of a user's requested
session length are separate operations.

AdventureFinder stores adventure duration in normalized **2.5--3.0 hour
sessions**.

A user may instead request:

- "one night";
- "three four-hour sessions";
- "two eight-hour sessions";
- "under ten sessions";
- "a campaign for six months."

Where sufficient information exists, the query layer SHOULD translate the
user's available table time into the AdventureFinder normalized baseline before
matching.

For example, three unusually long sessions should not automatically be
interpreted as equivalent to an adventure with `Normalized Sessions = 3`.

This separation allows the underlying adventure-duration data to remain stable
while the query layer accommodates different table schedules.



### 2. Levels

**Definition:** The primary intended character starting level and the character
level reached by completion of the canonical adventure.

Levels is an **editorially assessed matching dimension**, not a 1--5
interpretive analysis score. It is represented canonically by two discrete
integer assessment values:

- **Level Start** --- the primary intended character level at which ordinary
  substantially-as-published play of the canonical adventure begins.
- **Level End** --- the character level the published adventure expects
  characters to have reached by completion of the canonical adventure,
  including advancement explicitly awarded as part of completing that
  adventure.

For an adventure whose primary published play begins and ends at the same
character level, Level Start and Level End contain the same integer value.

**Status:** Frozen as **Levels v2.1**, calibrated, pressure-tested, and
blind-validated. The discrete-integer representation, canonical-Adventure-ID
rule, primary-design rule, completion-advancement rule, alternate/scalable
support handling, evidence hierarchy, and uncertainty handling below are locked
for the current ontology version. Future changes to their wording or meaning
require an explicit ontology revision and revalidation.

#### Primary Assessment Values

A completed Levels assessment ordinarily contains two integer values:

| Field | Meaning |
| --- | --- |
| **Level Start** | Primary intended character level at which ordinary substantially-as-published play of the canonical adventure begins. |
| **Level End** | Character level the published adventure expects characters to have reached by completion of the canonical adventure. |

Both values are discrete integers. `Level End` MUST be greater than or equal to
`Level Start`.

Examples:

| Published support | Level Start | Level End |
| --- | ---: | ---: |
| Adventure for 3rd-level characters with no adventure-supported advancement | `3` | `3` |
| Adventure begins at 1st level and takes characters to 5th by completion | `1` | `5` |
| Adventure designed for characters of levels 5--20 | `5` | `20` |

A formatted level value MAY be derived for presentation:

- `Level Start = 5`, `Level End = 5` → **5**
- `Level Start = 5`, `Level End = 8` → **5--8**

The formatted value is presentation only. **Level Start** and **Level End** are
the canonical assessment values.

#### Governing Assessment Principle

> **Record the primary character level at which the published adventure expects
> ordinary substantially-as-published play to begin and the character level the
> adventure expects the characters to have reached when that same canonical
> adventure is complete.**

The assessment SHOULD answer two separate questions:

1. **At what level does the published adventure primarily expect ordinary play
   to begin?**
2. **What level does the published adventure expect characters to have reached
   when this canonical adventure is complete?**

It SHOULD NOT answer:

> At what levels could a sufficiently motivated GM conceivably adapt, rebalance,
> or scale this adventure?

#### Canonical Adventure ID

Level Start and Level End MUST be assessed for the discrete playable unit
represented by the canonical **Adventure ID**.

Do not silently inherit the level span of:

- the containing source book;
- a parent campaign;
- an anthology;
- an adjacent adventure;
- a sequel or continuation; or
- a broader sequence containing the canonical adventure.

Nested adventures are assessed independently even when their page ranges and
fiction overlap their parent adventure.

This rule is especially important for Level End. Advancement that belongs to a
subsequent canonical unit MUST NOT be assigned backward to the adventure that
preceded it merely because the transition is narratively continuous.

#### Prefer Explicit Adventure-Specific Guidance

Where the source explicitly states the intended level or progression for the
canonical adventure, that guidance is the strongest evidence.

Examples include:

- "designed for 5th-level characters";
- "for characters of levels 5--10";
- "characters begin at 1st level";
- "by the end of the adventure, characters will be 5th level";
- "upon completing the adventure, the characters gain a level"; and
- section-by-section recommended character levels that collectively establish
  the adventure's intended progression.

Explicit adventure-specific guidance takes precedence over generic inference
from monster difficulty, challenge ratings, treasure, spell access, apparent
lethality, publication order, or community reputation.

#### Determining Level Start

**Level Start** records the adventure's **primary published entry level**.

When the source directly states a starting level, use that level unless the
statement clearly refers to a different canonical unit.

When several starts are supported, distinguish the **primary intended start**
from alternate starts. Do not convert discrete alternate starts into a false
continuous range.

For example, if an adventure assumes a 1st-level start but explicitly allows a
3rd-level alternate start:

- `Level Start = 1`
- the 3rd-level option is **alternate level support**, not a reason to store
  `Level Start = 3` or to reinterpret the primary start as `1--3`.

#### Determining Level End

**Level End** records the character level the published adventure expects the
characters to have reached **by completion of the same canonical adventure**.

Relevant evidence includes:

- direct statements of ending level;
- milestone advancement;
- chapter- or section-level advancement instructions;
- explicit XP progression;
- "reach," "advance to," "finish at," or equivalent language; and
- advancement explicitly awarded for completing the adventure.

The central ownership question is:

> **Does this level gain belong to completion of the assessed canonical
> adventure, or does it belong to entering or beginning later material?**

#### Completion Advancement Counts

A level explicitly awarded **as part of completing the canonical adventure**
IS included in Level End even when little or no substantive play occurs after
the level is awarded.

This rule intentionally defines Level End as the **completion level**, not the
highest level at which a minimum amount of post-advancement table play occurs.

For example:

- adventure begins at level 11;
- characters gain one level during the adventure;
- completing the adventure explicitly grants another level;

→ `Level Start = 11`, `Level End = 13`.

This avoids converting a comparatively factual editorial field into an
interpretive judgment about how much post-level-up play is "substantive."

#### Advancement Belonging to Later Material Does Not Count

Advancement that occurs only upon **entering, beginning, or undertaking a
subsequent canonical adventure or other material outside the assessed
Adventure ID** does NOT increase Level End.

For example, if a nested adventure is played entirely at level 1 and the source
says the characters gain a level only when they leave that adventure and arrive
in the next named region or chapter that belongs to a different canonical unit:

- `Level Start = 1`
- `Level End = 1`

The later level gain belongs to the subsequent unit.

#### Primary Design Takes Priority over Scaling Support

If an adventure identifies a specific intended level or primary level span but
also provides procedures for scaling it to other levels, the scalable range
MUST NOT replace or expand the primary Level Start and Level End values.

For example, an adventure designed for **10th-level characters** but providing
explicit encounter scaling for **levels 1--20** remains primarily a level-10
adventure. If completing that adventure awards one level, its primary values
are:

- `Level Start = 10`
- `Level End = 11`

The 1--20 scaling is separate compatibility evidence.

This distinction is essential for matching: a purpose-built 10th-level
adventure should be treated as a stronger match for a party beginning at level
10 than for a party beginning at level 2 merely because the publisher supplies
scaling instructions.

#### Alternate / Scalable Level Support

Explicit publisher-supported alternate starts or scaling regimes MAY be
retained as **supporting evidence or metadata**, but they are not part of the
canonical Level Start / Level End pair.

Examples:

| Situation | Primary assessment | Supporting level evidence |
| --- | --- | --- |
| Designed for level 10; encounters scalable 1--20 | Start `10`; End according to canonical progression | `1--20 scalable` |
| Assumes level 1; explicitly permits level 3 start | Start `1`; End from primary progression | `Alternate start: 3` |
| Designed for 5--10; generic statement that GM can adapt it | Start `5`; End `10` | No separate scalable range unless affirmative support is provided |

Do not infer alternate support merely because adaptation is mechanically
possible.

#### Multiple Advancement Methods

Some adventures provide more than one published advancement method, such as
conventional XP and milestone advancement.

When one method explicitly states the adventure's intended completion level or
awards a level for completing the adventure, that statement MAY establish the
best-supported Level End even if another supported XP route could produce
variation at individual tables.

The Levels dimension does **not** attempt to model every possible terminal
level produced by every advancement procedure. It records the best-supported
primary Level End under the published adventure's own guidance.

Where competing methods prevent a responsible primary value from being
established, use the uncertainty procedure below rather than inventing an
average or range.

#### Open and Nonlinear Campaigns

An open structure does not by itself prevent a Level End assessment.

When the publisher explicitly states that a campaign is designed for a span
such as **5th through 20th level**, that statement can establish Level Start and
Level End even if:

- characters can enter some areas early;
- characters can retreat and return later;
- not every route generates identical XP;
- the final region supports more than one character level; or
- the campaign has no single mandatory traversal of every location.

Do not replace explicit campaign-level guidance with a lower terminal level
merely because some supported trajectories can end earlier.

#### Do Not Expand the Primary Values for Off-Level Possibility

Statements that higher- or lower-level characters *can* participate do not
automatically alter the primary Level Start or Level End.

Likewise, generic language such as:

- "higher-level characters may find this easier";
- "lower-level characters should exercise caution";
- "characters may enter this area early"; or
- "the adventure can be adapted for other tiers"

does not itself redefine the primary assessment.

AdventureFinder records primary published intent, not every level at which play
is theoretically possible.

#### Do Not Infer Levels from Encounter Challenge Alone

Monster challenge ratings, encounter difficulty, treasure value, spell
requirements, apparent danger, or adventure reputation MAY corroborate a
source interpretation but SHOULD NOT ordinarily establish Level Start or Level
End on their own.

An adventure that merely appears "appropriate for level 11" is not thereby an
11th-level adventure.

This guardrail is especially important when the source gives only qualitative
language such as **"high-level characters."** Do not manufacture a discrete
integer from anthology placement or expected difficulty.

#### Adventure-Supported Advancement Only

Level End SHOULD NOT be extended because characters might gain levels through:

- unrelated side adventures;
- arbitrary GM-awarded XP;
- downtime;
- unrelated random encounters;
- substantial GM-created additions; or
- material outside the canonical Adventure ID.

The assessment describes the adventure's own substantially-as-published
progression.

#### Optional and Branching Material

Optional branches may influence Level End when the published adventure itself
identifies them as part of the supported progression to its primary completion
level.

Do not lower Level End merely because a supported path can omit some milestones
when the source nevertheless explicitly identifies a higher level as the
adventure's intended or supported completion endpoint.

Conversely, rare, exhaustive, unsupported, or highly exceptional advancement
possibilities SHOULD NOT inflate Level End beyond the best-supported published
completion level.

#### Evidence Hierarchy

When evidence conflicts, use approximately this order:

1. **Explicit canonical-adventure starting or ending level statement**
2. **Explicit canonical-adventure completion advancement**
3. **Explicit chapter/adventure advancement instructions**
4. **Explicit milestone or XP progression**
5. **Explicit recommended character levels for constituent sections**
6. **Publisher-supported alternate/scaling instructions**
7. **Strong structural inference from the published adventure**
8. **Mechanical inference**, only as corroborating evidence

Do not substitute community knowledge, commonly played levels, edition
history, anthology order, or adventure reputation for published evidence.

#### Evidence Basis

When useful for audit or provenance, a Levels assessment MAY retain an evidence
basis:

- **Explicit** --- the relevant value is directly stated or directly
  established by explicit canonical-adventure level guidance.
- **Derived** --- the value is calculated directly from explicit advancement
  instructions or section-level guidance.
- **Editorially Inferred** --- no complete direct statement exists and
  editorial interpretation was necessary.

Evidence Basis is supporting audit metadata, not a separate AdventureFinder
matching dimension.

#### Insufficient Evidence and Assessment State

Levels distinguishes between an assessment that has not yet been performed and
one for which the available published evidence cannot responsibly establish a
discrete integer.

- **Blank --- Not Yet Assessed.** No completed Levels assessment exists yet for
  the Adventure ID.
- **Uncertain / Requires Source Verification.** Assessment was attempted, but
  Level Start, Level End, or both cannot responsibly be established from the
  available published evidence.
- **Integer value --- Assessed.** Published evidence supports the relevant
  Level Start or Level End.

The interpretive-analysis `-1` sentinel MUST NOT be reused as a Level Start or
Level End value. Character levels are themselves integers, and Levels does not
use the 1--5 interpretive scoring framework.

If only one endpoint can be established responsibly, the unresolved endpoint
SHOULD be marked uncertain rather than inferred solely to complete the pair.

#### Matching Guidance

Level Start and Level End answer related but distinct recommendation questions.

**Level Start is the primary field for party-entry compatibility.** A request
such as "I have 5th-level characters; what adventure can I start?" should
primarily compare the party level with **Level Start**, not assume that every
integer between Start and End is an equally supported entry point.

**Level End describes where the canonical adventure takes the characters by
completion.** It supports requests such as:

- "I want an adventure that starts at 1st and gets us to 5th";
- "what can bridge my party from 10th to 11th?"; or
- "how far does this campaign advance characters?"

A simple test such as `Level Start <= requested level <= Level End` MUST NOT be
used as a universal starting-level compatibility rule. An adventure with
`Level Start = 1` and `Level End = 5` is not thereby established as an equally
supported adventure to **begin** at levels 2, 3, 4, and 5.

Explicit alternate/scalable support can be used as additional compatibility
evidence, but SHOULD rank below a direct primary Level Start match unless the
product layer intentionally asks for adaptable rather than primary-fit results.

#### Calibration Reference Cases

Levels is not a 1--5 ordinal scale, so its calibration references are not score
anchors. They are **rule exemplars** chosen to exercise distinct editorial
problems.

| Adventure | Level Start | Level End | Calibration role |
| --- | ---: | ---: | --- |
| **ADV-0062 — No Honour Among Thieves** | **10** | **11** | Primary level 10 versus explicit 1--20 scaling; completion milestone belongs to the canonical adventure. |
| **ADV-0277 — The Wild Beyond the Witchlight** | **1** | **8** | Primary start 1 versus alternate start 3; explicit supported terminal level of 8 despite path variation. |
| **ADV-0322 — Waterdeep: Dungeon of the Mad Mage** | **5** | **20** | Explicit long-form campaign span and open megadungeon progression. |
| **ADV-0262 — Lost Mine of Phandelver** | **1** | **5** | Clean nested-unit progression; must not inherit the containing campaign's later 12th-level endpoint. |
| **ADV-0287 — House of Lament** | **1** | **3** | Explicit 1st-level start and advancement to 3rd within the canonical adventure. |
| **ADV-0034 — Tomb of Horrors** | **Uncertain** | **Uncertain** | Qualitative "high-level" guidance only; demonstrates refusal to invent integers. |
| **ADV-0040 — Expedition to the Barrier Peaks** | **11** | **13** | Completion advancement counts in Level End even when the final level is awarded for completing the adventure. |
| **ADV-0278 — Witchlight Carnival** | **1** | **1** | Clean canonical-transition control: level 2 is gained only after leaving the child unit and arriving in Hither. |

These references illustrate application of the frozen rules. Future adventures
MUST be assessed against the rubric itself rather than by superficial similarity
to a benchmark title.

#### Calibration and Adjudication History

Levels calibration began with a broader candidate rubric and was revised to the
current two-integer representation before formal blind validation.

The principal calibration findings were:

1. **Discrete Level Start / Level End storage is preferable to a formatted
   range.** The integer pair gives the matching layer clean data while allowing
   ranges such as `1--5` to be derived for display.
2. **Primary design must remain distinct from alternate/scalable support.**
   *No Honour Among Thieves* established that a level-10 adventure with explicit
   1--20 scaling is not primarily a 1--20 adventure.
3. **Level End is a completion level, not a "highest substantively played
   level" test.** Focused adjudication of *Expedition to the Barrier Peaks*,
   *The Wild Beyond the Witchlight*, and *House of Lament*, using *Witchlight
   Carnival* as a canonical-transition control, changed the provisional
   Barrier Peaks interpretation from 12 to **13** and established the current
   completion-ownership rule.
4. **Canonical boundaries control advancement ownership.** A level awarded for
   completing the assessed adventure counts; a level awarded only upon entering
   subsequent canonical material does not.
5. **Qualitative level guidance does not justify invented integers.** *Tomb of
   Horrors* remained `Uncertain / Requires Source Verification` rather than
   being assigned a number from difficulty, reputation, or anthology order.
6. **Advancement Variable was tested as supporting metadata and then dropped.**
   It is not part of the frozen Levels rubric or production schema. Variation is
   represented through source evidence and alternate/scalable support where
   useful, without a generalized boolean.

#### Blind Validation

A subsequent independent blind reviewer received the frozen Levels v2.1 rules,
the eight calibration cases, and the relevant published sources without access
to AdventureFinder's prior Level Start / Level End outcomes or adjudications.

The blind pass independently reproduced **all eight primary outcomes**:

| Adventure | Frozen result | Blind result |
| --- | --- | --- |
| No Honour Among Thieves | `10 → 11` | `10 → 11` |
| The Wild Beyond the Witchlight | `1 → 8` | `1 → 8` |
| Waterdeep: Dungeon of the Mad Mage | `5 → 20` | `5 → 20` |
| Lost Mine of Phandelver | `1 → 5` | `1 → 5` |
| House of Lament | `1 → 3` | `1 → 3` |
| Tomb of Horrors | `Uncertain → Uncertain` | `Uncertain → Uncertain` |
| Expedition to the Barrier Peaks | `11 → 13` | `11 → 13` |
| Witchlight Carnival | `1 → 1` | `1 → 1` |

The blind reviewer also independently reproduced the two key structural
principles:

- scalable or alternate level support does not overwrite the primary values;
- advancement belonging to later canonical material does not increase the
  preceding adventure's Level End.

The blind reviewer raised disagreements only around the experimental
**Advancement Variable** supporting field. Because that field did not serve a
necessary Levels matching purpose and introduced overlapping semantics with
alternate/scalable support, it was removed rather than further calibrated.
This removal does not alter any Level Start or Level End validation result.

#### Production Application Procedure

For a new adventure, apply Levels in this order:

1. **Confirm the canonical Adventure ID and boundaries.**
2. **Locate explicit starting-level language.** Assign Level Start from the
   primary published entry point.
3. **Locate explicit ending-level or advancement language.** Follow milestone,
   XP, chapter, and completion instructions through the end of the same
   canonical adventure.
4. **Determine ownership of terminal advancement.** Include advancement awarded
   for completing the canonical adventure; exclude advancement triggered only
   by entering subsequent material.
5. **Separate alternate/scalable support.** Do not use alternate starts or
   scaling ranges to overwrite the primary integer pair.
6. **Apply the evidence hierarchy.** Prefer direct source guidance over
   mechanical or reputational inference.
7. **Refuse unsupported precision.** If a discrete endpoint cannot be
   established responsibly, mark it `Uncertain / Requires Source Verification`.
8. **Record concise source evidence.** Preserve enough evidence for later audit
   or adjudication.

#### Frozen Levels v2.1 Core Rule

> **Level Start records the primary intended character level at which ordinary
> substantially-as-published play of the canonical adventure begins. Level End
> records the character level the published adventure expects characters to
> have reached by completion of that canonical adventure, including advancement
> explicitly awarded as part of completing it. Both values are stored as
> discrete integers and may be identical. Advancement that occurs only upon
> entering, beginning, or undertaking subsequent material outside the assessed
> Adventure ID does not increase Level End. Explicit alternate starting levels,
> scaling ranges, or other supported adaptations do not replace or expand the
> primary values merely because the adventure can be adapted to them.**

## Provisional Analysis Scoring Framework

The seventeen interpretive AdventureFinder analysis dimensions are intended
to use a common scoring framework. This framework is provisional and will be
tested and refined against the AdventureFinder Analysis Validation Corpus
before it is locked.

The two editorially assessed matching dimensions---**# of Sessions** and
**Levels**---do not use this 1--5 interpretive scoring scale. **# of Sessions** uses the frozen normalized-duration framework defined above;
**Levels** uses the frozen Level Start / Level End framework defined above.

### Common Scoring Principles

1. **Scale: 1--5 integers.** Each interpretive analysis dimension is scored
   from 1 through 5. Dimension-specific anchors define the meaning of those
   values. Half-points are not used at this stage.

2. **Absolute, not percentile-based.** Scores describe the adventure against
   stable dimension definitions rather than against the current corpus
   distribution. A score should retain the same meaning as the AdventureFinder
   corpus grows.

3. **Empirically inhabited endpoints.** Ordinal anchors remain semantically
   defined rather than percentile-defined, but the low and high endpoints of
   each interpretive dimension should be empirically inhabited by clear,
   reproducible examples from the broad target adventure corpus. Persistent
   inability to identify and independently reproduce defensible endpoint cases
   is evidence that the anchor may not provide useful differentiation across
   the corpus and SHOULD trigger semantic review of that dimension's scale or
   endpoint wording. Endpoint calibration MUST NOT redefine a score by
   percentile or require any predetermined score distribution.

4. **Score the canonical Adventure ID.** Analysis applies to the discrete
   playable unit represented by the canonical Adventure ID, including when
   that unit is nested inside a larger adventure or campaign. Analysis must
   not silently substitute the characteristics of a containing product or
   parent adventure.

5. **Weight expected table play, not pages or encounter counts.** Scores should
   reflect the expected substantive play experience. Page count, number of
   keyed locations, number of encounters, or similar document-level counts
   may provide evidence but are not themselves the thing being scored.

6. **Score substantially-as-published play.** Analysis describes the adventure
   as it is ordinarily supported and expected to be played from the published
   material. It should not score hypothetical rewrites, extensive GM
   modifications, or transformations merely because they are possible.

7. **Mandatory and common material takes priority over rare optional
   material.** Material likely to occur in ordinary play should carry more
   weight than unusual, highly conditional, or rarely selected branches. This
   is a weighting consideration rather than a separate scoring rule.

8. **Keep dimensions analytically separate.** A score on one dimension must
   not serve as an implicit proxy for another. For example, Combat Emphasis
   is distinct from Tactical Complexity and Lethality / Failure Severity;
   Seriousness is distinct from Darkness / Horror Intensity; and GM
   Preparation Burden is distinct from GM Beginner Suitability.

9. **Record confidence from 0% to 100%.** Every interpretive dimension score
   should be accompanied by a confidence value expressing how strongly the
   available published evidence supports that assessment. Confidence measures
   confidence in the score, not the intensity of the dimension.

10. **Flag materially path-sensitive dimensions.** If substantially supported
   published paths through an adventure could produce meaningfully different
   experiences on a dimension, the assessment should carry a path-sensitivity
   flag rather than silently averaging away that variation.

### Insufficient Evidence and Assessment State

AdventureFinder distinguishes between an assessment that has not yet been
performed and one that was attempted but cannot be responsibly scored from the
available published evidence.

- **Blank score --- Not Yet Assessed.** No completed analytical assessment
  exists yet for that Adventure ID and dimension.
- **`-1` --- Insufficient Evidence.** An assessment was attempted, but the
  available published evidence does not support a responsible placement on the
  1--5 scale. `-1` is a reserved sentinel value, not a score on the scale.
- **`1`--`5` --- Scored.** The published evidence supports a best assessment on
  the dimension's 1--5 scale.

Confidence is recorded only for scored values (`1`--`5`). A blank score or
`-1` therefore has a blank confidence value.

`-1` MUST be excluded from numerical calculations, similarity measures,
averages, ranking scores, and other operations that interpret the 1--5 scale.

Insufficient Evidence should be used only when an assessment has actually been
attempted and the published material cannot responsibly support a 1--5 score.
Difficulty, brevity, uncertainty between adjacent scores, or low confidence
alone do not justify `-1`. When meaningful evidence exists, reviewers should
make the best supported score and represent uncertainty through the 0%--100%
confidence value and, where appropriate, the path-sensitivity flag.

## Provisional Dimension Rubrics

Only dimensions with explicit rubrics in this section have begun calibration.
All other dimension definitions remain conceptual until corresponding scoring
anchors are developed and tested.

### 3. Combat Emphasis

**Definition:** How much of the adventure's expected substantive table play is
centered on combat as the primary mode of play or resolution.

Combat Emphasis does **not** measure encounter count, tactical sophistication,
or lethality. Those may correlate with combat-heavy play but belong to other
dimensions or supporting evidence.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Combat is absent, exceptional, or readily bypassed; the adventure fundamentally functions through other modes of play. |
| **2 — Low** | Combat occurs and matters, but is clearly secondary to other modes. |
| **3 — Mixed** | Combat is a substantial recurring component alongside comparably important noncombat play. |
| **4 — High** | Combat is one of the adventure's dominant modes and regularly drives progress. |
| **5 — Dominant** | The adventure is fundamentally organized around fighting/overcoming combat encounters; removing most combat would substantially change its playable identity. |

**Status:** Frozen calibration rubric. The anchors above are locked for the
current ontology version. Future changes to their wording or meaning require an
explicit ontology revision and revalidation against the Analysis Validation
Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during Combat
Emphasis calibration. They illustrate application of the rubric but do not
redefine the score anchors; future adventures are scored against the anchor
meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0278 — Witchlight Carnival**; **ADV-0200 — Lake Monster**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **2 — Low** | **ADV-0034 — Tomb of Horrors**; **ADV-0287 — House of Lament** |
| **3 — Mixed** | **ADV-0053 — Call of the Wild**; **ADV-0062 — No Honour Among Thieves** |
| **4 — High** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0303 — Storm King's Thunder**; **ADV-0230 — Salvage Operation** |
| **5 — Dominant** | **ADV-0032 — Dead in Thay**; **ADV-0033 — Against the Giants** |

Initial calibration tested the adjacent **1/2**, **2/3**, **3/4**, and **4/5**
boundaries using the then-current benchmark set, which at that time placed
**ADV-0230 — Salvage Operation** at **5 — Dominant**. A subsequent blind
independent pass applied the frozen rubric without access to prior Combat
scores, rationales, benchmark assignments, or calibration outcomes. Source-grounded adjudication of the
resulting disagreements changed **ADV-0062 — No Honour Among Thieves** from 2 to
3, **ADV-0277 — The Wild Beyond the Witchlight** from 2 to 1, and **ADV-0287 —
House of Lament** from 3 to 2. An initial blind assessment of **ADV-0262 — Lost
Mine of Phandelver** mistakenly scored its containing campaign; a corrected
canonical-unit assessment independently reproduced score 4. No Combat anchor
wording changed as a result of the blind validation. These are corrections to
benchmark application under the frozen rubric, not changes to the rubric
itself. In particular, the **4/5** boundary continues to distinguish adventures
where combat is one dominant mode that regularly drives progress from adventures
fundamentally organized around fighting or overcoming combat opposition.

#### Post-1.0 Score-5 Benchmark Expansion and Blind Replication

After acceptance of Version 1.0, targeted upper-end calibration work sought
additional Combat-5 morphologies to test whether the **5 — Dominant** anchor
could be independently reproduced beyond **ADV-0230 — Salvage Operation**.
Two additional candidates were each subjected to two separate blind full-source
assessments under the frozen AFAO 1.0 Combat Emphasis rubric.

The blind protocol isolated the reviewers from AdventureFinder's existing Combat
scores, benchmark assignments, candidate-search ranking, regression-oracle
values, experimental Combat guardrails, prior reviewer conclusions, and
calibration outcomes. Reviewers received the complete canonical source, a
benchmark-free extract of the frozen Combat rubric, and a blind assessment
prompt. The second reviewer for each case was not given the first reviewer's
result.

**ADV-0033 — Against the Giants** independently reproduced **5 — Dominant** in
both blind assessments, at **96%** and **93%** confidence. Both reviewers marked
the case path-sensitive and independently identified **4 — High** as the
strongest adjacent-score alternative. Their structural reasoning converged on
the same discriminator: the adventure's three escalating hostile-stronghold
penetrations and assaults form the whole-adventure progression spine, while
infiltration, reconnaissance, stealth, negotiation, routing, retreat, and
bypass options chiefly determine **how those assaults are prosecuted** rather
than establishing a comparably important independent macro-progression mode.
Against the Giants therefore supplies a separately blind-replicated top-end
morphology and a strong empirical **4/5 discriminator**.

**ADV-0032 — Dead in Thay** likewise independently reproduced **5 — Dominant**
in both blind assessments, at **88%** and **96%** confidence. Both reviewers
independently identified **4 — High** as the strongest adjacent-score
alternative. Their whole-adventure reasoning also converged: glyph-key routing,
gate attunement and disruption, exploration, information gathering,
negotiation, surrender, deception, alliances, and magical-disruption procedures
are substantial, but principally organize, route, mitigate, or advance an
ongoing assault through an actively defended Doomvault. The later Temples of
Extraction reduce many earlier opportunities for negotiated passage, and the
mandatory Phylactery Vault culmination explicitly requires overcoming its
guardians and destroying Kazit Gul before the final disruption objective can be
completed. The two reviewers differed only on the supporting **Path Sensitive**
flag (**Yes** versus **No**); that disagreement does not alter their exact
integer-score replication or their shared 4/5 structural reasoning.

At Version 1.1, these two additions expanded the empirical score-5 benchmark
set from one case to three structurally distinct exemplars. Their admission did
**not** revise the Combat Emphasis definition, any 1--5 anchor wording, or the
established 4/5 boundary. Instead, the new blind-replicated cases strengthened
the evidence that score 5 is determined by **whole-adventure organizing
structure**: combat or combat-framed opposition must be fundamental to how
ordinary substantially-as-published progression functions, rather than merely
frequent, difficult, climactic, or locally dominant.

The subsequent Salvage Operation correction documented below leaves the current
score-5 benchmark set with the two independently blind-replicated cases,
**ADV-0032 — Dead in Thay** and **ADV-0033 — Against the Giants**, while
preserving the evidence that the 5 — Dominant endpoint is inhabited,
reproducible, and structurally distinct from score 4.

The score-5 clause that removing most combat would substantially change an
adventure's playable identity is a confirming consequence of the preceding
requirement, not an independently sufficient test for score 5.

#### Post-1.1 Salvage Operation Benchmark Re-Adjudication

A frozen Salvage-only decision record,
`combat-emphasis-ADV-0230-salvage-operation-readjudication-freeze-v0.2.md`,
prospectively supersedes the prior Combat-5 benchmark application for
**ADV-0230 — Salvage Operation** and places it at **4 — High** with **93%**
human-adjudication confidence and **Path Sensitive: No**.

This is a **benchmark-application correction under the unchanged Combat
Emphasis rubric**, not a rubric revision. The Combat definition, all five score
anchors, the established 4/5 structural distinction, and the rule that the
score-5 removal counterfactual is confirming rather than independently
sufficient remain unchanged.

The re-adjudication found that Combat is plainly one of Salvage Operation's
dominant modes and repeatedly drives progress through its central derelict-ship
crawl. However, the canonical adventure also contains a major independently
progress-bearing retrieval-and-extraction structure: locating and recovering
Aubreck's box, transporting the mission-critical objective, navigating the
rapidly deteriorating *Emperor of the Waves*, managing listing, flooding,
movement and carrying constraints, coordinating rescue timing, and escaping
before the fixed sinking endpoint.

The elder octopus principally drives the changing environmental state and
sinking timetable; defeating it is not the canonical success condition.
Likewise, surviving hostile creatures can complicate the escape without making
defeat of those creatures the defining prerequisite of the extraction
sequence. Treating creature-caused environmental pressure as automatically
combat-as-progression would improperly inflate Combat Emphasis.

The strongest score-5 case remains that hostile opposition is repeated and
central, the source explicitly describes characters fighting their way forward,
the cargo objective is surrounded by hostile creatures, and removing most
combat would substantially change the adventure's feel and identity. Those
facts establish a strong score 4 but do not overcome the independently
progress-bearing retrieval, transport, environmental-survival, rescue, and
escape structure.

The evidentiary balance changed after Version 1.1 for two reasons. First,
**Dead in Thay** and **Against the Giants** established independently
blind-replicated score-5 morphologies, so the validity of the endpoint no longer
depends on preserving Salvage as its sole exemplar. Second, focused
single-dimension Combat scoring removed simultaneous Play Mix elicitation as a
confound and returned Salvage at **4 / 4 / 4 / 4** across four controlled
Combat Guardrail v0.7 runs, with convergent reasoning that independently
identified the retrieval/extraction structure as the decisive 4↔5 discriminator.

The correction therefore reaffirms the Salvage-only portion of the earlier
source-grounded 5→4 re-adjudication and establishes Salvage as a useful
**4↔5 boundary control on the score-4 side**. It does not re-adjudicate
**ADV-0034 — Tomb of Horrors**, alter Combat Guardrail v0.7 wording, introduce
half-scores, or change any non-Combat ADV-0230 assessment.

In particular, **ADV-0230 — Salvage Operation remains 5 — Very High for
Tactical Complexity** under that dimension's separate frozen rubric. The
Combat correction must not be propagated into Tactical Complexity or any other
dimension merely because the same adventure serves as a benchmark there.


### 4. Exploration Emphasis

**Definition:** How much of the adventure's expected substantive table play is
centered on discovering, navigating, traversing, and materially interacting
with environments as a mode of play.

Exploration Emphasis does **not** measure geographic scale, distance traveled,
number of locations, number of keyed rooms, or Structural Openness. Travel
counts as exploration when navigating routes, hazards, landmarks, unknown
territory, or environmental conditions constitutes substantive play; merely
moving from one scene or destination to another does not. Likewise, a keyed
dungeon is not automatically exploration-heavy merely because characters move
through many rooms.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Environmental discovery, navigation, traversal, or interaction is absent, incidental, or rapidly resolved; environments function primarily as backdrops or connective space. |
| **2 — Low** | Meaningful exploration occurs and matters, but is limited in extent or clearly secondary to other modes of play. |
| **3 — Mixed** | Exploration is a substantial recurring component alongside comparably important non-exploration play. |
| **4 — High** | Exploration is one of the adventure's dominant modes and regularly drives progress through discovering, navigating, traversing, or interacting with environments. |
| **5 — Dominant** | The adventure is fundamentally organized around exploring a site, region, or environment; sustained environmental discovery, traversal, navigation, or interaction provides the primary structure of expected play, with other modes largely occurring within or being enabled by that exploration. |

**Status:** Frozen calibration rubric. The definition, clarification, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Exploration Emphasis calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0170 — The Shadow Parliament**; **ADV-0169 — Clockwork Memories**; **ADV-0198 — Cold-Hearted Killer** |
| **2 — Low** | **ADV-0257 — Magister's Masquerade**; **ADV-0062 — No Honour Among Thieves**; **ADV-0092 — An Actor's Life** |
| **3 — Mixed** | **ADV-0053 — Call of the Wild** |
| **4 — High** | **ADV-0262 — Lost Mine of Phandelver**; **ADV-0303 — Storm King's Thunder** |
| **5 — Dominant** | **ADV-0034 — Tomb of Horrors**; **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0287 — House of Lament** |

Initial calibration tested the adjacent **1/2**, **2/3**, **3/4**, and **4/5**
boundaries. A subsequent blind independent pass reproduced all eight original
Exploration Emphasis calibration scores. An additional blind assessment of
**ADV-0092 — An Actor's Life** scored it 2 rather than its then-calibrated score
of 1. Source-grounded adjudication confirmed score 2 and a path-sensitivity flag:
its conditional steeplechase makes sustained route-hazard traversal substantive
play when that path occurs. This is a correction to benchmark application under
the frozen rubric, not a change to the rubric itself.

A targeted Adventure Master Catalog endpoint search then identified and
source-reviewed three score-1 exemplars: **ADV-0170 — The Shadow Parliament**,
where environments function primarily as venues for debate and confrontation;
**ADV-0169 — Clockwork Memories**, where a mapped workshop primarily supplies
tactical setting rather than exploration play; and **ADV-0198 — Cold-Hearted
Killer**, where substantial movement between known settlements remains
connective travel rather than substantive environmental navigation. The frozen
Exploration definition, clarification, and anchors remain unchanged.

The **1/2** boundary distinguishes adventures where environmental discovery,
navigation, traversal, or interaction remains incidental, rapidly resolved,
backdrop, or connective material from adventures where environmental
interaction itself becomes a meaningful, though limited or secondary, mode of
play. The score-1 benchmarks demonstrate venue, mapped-site, and travel-heavy
forms that still remain Minimal. **ADV-0257 — Magister's Masquerade**,
**ADV-0062 — No Honour Among Thieves**, and **ADV-0092 — An Actor's Life**
anchor score 2 because bounded portions of play require characters to
meaningfully engage with environmental access, layout, movement, traversal, or
hazards.

The **4/5** boundary distinguishes adventures where exploration is one dominant
mode that regularly drives progress from adventures fundamentally organized
around exploring a site, region, or environment, with other modes largely
occurring within or being enabled by that exploration. The score-5 benchmarks
demonstrate that this organizing structure can occur at different scales and in
different forms, including a constructed deathtrap, an unfamiliar technological
site, a journey through successive fantastical realms, or a reactive haunted
house.

### 5. Social Interaction Emphasis

**Definition:** How much of the adventure's expected substantive table play is
centered on meaningful interaction with NPCs as a mode of play.

Social Interaction Emphasis does **not** measure number of NPCs, amount of
dialogue text, frequency of Charisma checks, or "roleplaying" in the broad
sense. Social interaction is substantive when engaging with NPCs---their goals,
attitudes, relationships, cooperation, opposition, information, or decisions---
constitutes meaningful player-facing play.

Social Interaction Emphasis is distinct from Investigation Emphasis. An NPC
conversation may contribute to both dimensions when interacting with the NPC as
a social actor is itself substantive play and the conversation also requires
characters to gather, connect, or interpret information. An NPC merely
delivering exposition or the next destination does not by itself make Social
Interaction substantial. Likewise, noncombat resolution is not automatically
social: stealth, environmental bypasses, puzzles, and other noncombat methods
belong to Social Interaction only when meaningful engagement with an NPC is part
of the play.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Meaningful NPC interaction is absent, incidental, primarily expository/transactional, or readily bypassed; the adventure fundamentally functions through other modes of play. |
| **2 — Low** | Meaningful NPC interaction occurs and matters, but is limited in extent or clearly secondary to other modes. |
| **3 — Mixed** | Social interaction is a substantial recurring component alongside comparably important non-social play. |
| **4 — High** | Social interaction is one of the adventure's dominant modes and regularly drives progress through negotiation, relationships, cooperation, persuasion, deception, faction interaction, or other meaningful engagement with NPCs. |
| **5 — Dominant** | The adventure is fundamentally organized around interacting with NPCs, relationships, or factions; sustained social interaction provides the primary structure of expected play, with other modes largely occurring within or being enabled by those interactions. |

**Status:** Frozen calibration rubric. The definition, clarification, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during Social
Interaction Emphasis calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0034 — Tomb of Horrors** |
| **2 — Low** | **ADV-0053 — Call of the Wild**; **ADV-0062 — No Honour Among Thieves** |
| **3 — Mixed** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0287 — House of Lament**; **ADV-0303 — Storm King's Thunder** |
| **4 — High** | **ADV-0257 — The Magister's Masquerade** |
| **5 — Dominant** | **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0229 — Danger at Dunwater** |

Initial calibration applied the frozen rubric to the eight Analysis Validation
Corpus calibration adventures. A targeted 4/5 pressure test then added
**ADV-0229 — Danger at Dunwater** as a likely score-5 endpoint before blind
validation. A subsequent blind independent pass applied the frozen rubric to
those nine adventures without access to prior Social scores, rationales,
benchmark assignments, or calibration outcomes. Source-grounded adjudication of
the resulting score disagreements changed **ADV-0040 — Expedition to the
Barrier Peaks** from 2 to 3, **ADV-0053 — Call of the Wild** from 3 to 2, and
**ADV-0277 — The Wild Beyond the Witchlight** from 4 to 5. No Social definition,
clarification, or anchor wording changed as a result; these are corrections to
benchmark application under the frozen rubric.

Because the adjudicated move of **ADV-0277 — The Wild Beyond the Witchlight**
from 4 to 5 left score 4 without a benchmark, a targeted endpoint search
identified **ADV-0257 — The Magister's Masquerade** as the strongest Social-4
candidate. A full-source sequential review of its complete canonical adventure
unit placed it at 4, and a subsequent one-case blind assessment independently
reproduced score 4. This supplies a source-reviewed and blind-reproduced score-4
benchmark without changing the frozen rubric.

The **3/4** boundary distinguishes adventures where Social Interaction is a
substantial recurring component alongside comparably important non-social play
from adventures where Social Interaction is one of the dominant modes and
regularly drives progress. The **4/5** boundary distinguishes adventures where
Social Interaction is one dominant mode from adventures fundamentally organized
around interacting with NPCs, relationships, or factions, with other modes
largely occurring within or being enabled by those interactions.

### 6. Investigation Emphasis

**Definition:** How much of the adventure's expected substantive table play is
centered on gathering, connecting, and interpreting information to determine
what is happening or has happened.

Investigation Emphasis does **not** measure whether an adventure has a mystery
theme, how much information is hidden from the players, number of clues,
frequency of Intelligence or Wisdom checks, or how often characters search
locations. Investigation is substantive when players must seek, compare,
connect, interpret, or test information as meaningful player-facing play in
order to understand events, identify causes or actors, determine relevant
facts, or decide what conclusion the evidence supports.

Simply receiving exposition, being told the solution, following explicit
instructions, or succeeding on an isolated check that directly supplies the
needed answer does not by itself make Investigation substantial.

Investigation Emphasis is distinct from **Social Interaction Emphasis**.
Questioning, persuading, deceiving, or otherwise engaging with an NPC may
contribute to both dimensions when interaction with the NPC as a social actor is
substantive and the information gained must also be gathered or interpreted as
evidence. An NPC merely providing a clue or answer does not by itself make the
scene substantively Social, and a meaningful social encounter does not
automatically constitute Investigation.

Investigation Emphasis is also distinct from **Exploration Emphasis**.
Searching or examining an environment may contribute to both dimensions when
interacting with the environment is itself substantive play and the information
discovered there must also be interpreted as evidence. Merely discovering a
room, landmark, object, or hidden feature does not automatically constitute
Investigation.

Investigation Emphasis is distinct from **Puzzle / Problem-Solving Emphasis**.
Investigation asks players to determine facts, causes, identities,
relationships, or explanations from incomplete information. Puzzle /
Problem-Solving asks players to overcome an explicit noncombat problem through
reasoning or creative solutions. A scene may contribute to both when
interpreting evidence and solving an explicit problem are separately
substantive parts of play.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Meaningful investigation is absent, incidental, primarily expository, or rapidly resolved; the adventure fundamentally functions without players needing to gather, connect, or interpret information. |
| **2 — Low** | Meaningful investigation occurs and matters, but is limited in extent or clearly secondary to other modes of play. |
| **3 — Mixed** | Investigation is a substantial recurring component alongside comparably important non-investigative play. |
| **4 — High** | Investigation is one of the adventure's dominant modes and regularly drives progress through gathering, connecting, interpreting, or testing information. |
| **5 — Dominant** | The adventure is fundamentally organized around investigation; sustained inquiry into facts, causes, identities, events, or relationships provides the primary structure of expected play, with other modes largely occurring within or being enabled by what the investigation reveals. |

**Status:** Frozen calibration rubric. The definition, clarification, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Investigation Emphasis calibration. They illustrate application of the rubric
but do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0034 — Tomb of Horrors**; **ADV-0062 — No Honour Among Thieves** |
| **2 — Low** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0053 — Call of the Wild**; **ADV-0303 — Storm King's Thunder** |
| **3 — Mixed** | **ADV-0262 — Lost Mine of Phandelver**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **4 — High** | **ADV-0287 — House of Lament** |
| **5 — Dominant** | **ADV-0234 — The Styes** |

Initial calibration applied the frozen rubric to the eight Analysis Validation
Corpus calibration adventures and then tested the adjacent **1/2**, **2/3**,
**3/4**, and **4/5** boundaries against full-source evidence. Because the
initial eight-adventure set did not supply a defensible score-5 endpoint, a
targeted Adventure Master Catalog search identified **ADV-0234 — The Styes** as
the strongest candidate. Full-source review placed it at 5 and established the
upper boundary against **ADV-0287 — House of Lament** at 4 without changing the
rubric wording.

The source-grounded pressure tests retained **ADV-0053 — Call of the Wild** at
2, **ADV-0303 — Storm King's Thunder** at 2, **ADV-0277 — The Wild Beyond the
Witchlight** at 3, and **ADV-0287 — House of Lament** at 4. An initial focused
review moved **ADV-0040 — Expedition to the Barrier Peaks** from 2 to 1 by
strictly separating environmental discovery and technological problem-solving
from Investigation.

A subsequent nine-adventure blind independent pass applied the frozen rubric
without access to prior Investigation scores, rationales, benchmark assignments,
pressure-test outcomes, or expected score distribution. It independently
reproduced seven of the nine then-adjudicated scores exactly. Both disagreements
occurred at the **1/2** boundary: the blind pass scored **ADV-0040 — Expedition
to the Barrier Peaks** 2 rather than 1 and **ADV-0062 — No Honour Among
Thieves** 1 rather than 2.

Focused full-source adjudication resolved both disagreements in favor of the
blind results. **ADV-0062 — No Honour Among Thieves** moved from 2 to 1 because
its apparent mysteries are principally prescribed trails, direct briefings, or
GM-side hidden information rather than substantive player-facing evidence
interpretation. **ADV-0040 — Expedition to the Barrier Peaks** returned from 1
to 2 because the published Aphelion/Oakley contradiction creates a bounded but
genuine sequence in which players can compare accounts, test a deceptive
explanation, and pursue the truth. These are corrections to benchmark
application under the frozen rubric, not changes to the rubric itself. After
those adjudications, the blind pass reproduces **all nine final Investigation
scores exactly**.

The **1/2** boundary distinguishes adventures that merely contain hidden
information, searching, prescribed clue-following, direct exposition, or
ordinary environmental examination from adventures containing at least one
bounded but substantive player-facing inquiry into facts, causes, identities,
relationships, or explanations. Investigation need not be mandatory for
completion to justify score 2; a materially investigative supported branch can
qualify while remaining path-sensitive. **ADV-0062 — No Honour Among Thieves**
anchors the former pattern, while **ADV-0040 — Expedition to the Barrier Peaks**
and **ADV-0053 — Call of the Wild** demonstrate two forms of the latter.

The **2/3** boundary distinguishes limited, localized, or concentrated inquiry
from Investigation that recurs broadly enough across the canonical unit to be a
substantial continuing mode of play. **ADV-0303 — Storm King's Thunder** remains
2 because its strongest investigation is a bounded late-campaign arc, whereas
**ADV-0262 — Lost Mine of Phandelver** and **ADV-0277 — The Wild Beyond the
Witchlight** sustain meaningful information-gathering and interpretation across
multiple phases alongside other modes.

The **3/4** boundary distinguishes recurring Investigation alongside comparably
important non-investigative play from adventures where Investigation is one of
the dominant modes and regularly drives major progress. **ADV-0287 — House of
Lament** reaches 4 because exploration, séances, and discoveries repeatedly
build and revise the players' understanding of the house and its spirits, even
though the climax becomes substantially survival- and confrontation-focused.

The **4/5** boundary distinguishes Investigation as one dominant mode from
Investigation as the adventure's primary organizing structure. At score 5,
what the players discover repeatedly changes what they understand the problem
to be and thereby creates the next actionable objective, actor, or location;
other major modes occur largely downstream of those discoveries. **ADV-0234 —
The Styes** exemplifies this cascading structure, while **ADV-0287 — House of
Lament** retains substantial independent non-investigative structure and
therefore remains 4.

Supporting full-source reviews of **ADV-0195 — Affair on the Concordant
Express** at 2 and **ADV-0228 — The Sinister Secret of Saltmarsh** at 3 provided
additional boundary evidence during calibration but are not required as primary
benchmark rows.

### 7. Puzzle / Problem-Solving Emphasis

**Definition:** How much of the adventure's expected substantive table play is
centered on overcoming explicit noncombat problems through reasoning,
experimentation, or creative solutions.

Puzzle / Problem-Solving Emphasis does **not** measure the number of puzzles,
puzzle difficulty, frequency of ability checks, general player cleverness, or
how tactically demanding combat is. Problem-solving is substantive when the
adventure presents a concrete noncombat obstacle, mechanism, constraint, or
challenge whose resolution requires players to work out **how** to overcome it
through reasoning, experimentation, combining information or resources, or
devising a supported creative approach.

A riddle, logic puzzle, coded message, mechanical device, spatial challenge,
trap whose operation must be understood, resource-allocation problem, or
open-ended environmental obstacle may contribute when solving it constitutes
meaningful player-facing play. Simply succeeding on a check that directly
resolves the obstacle, locating a hidden feature, using an explicitly prescribed
ability, or choosing from obvious stated options does not by itself make Puzzle
/ Problem-Solving substantial.

Puzzle / Problem-Solving Emphasis is distinct from **Investigation Emphasis**.
Investigation asks players to determine facts, causes, identities,
relationships, or explanations from incomplete information. Puzzle /
Problem-Solving asks players to determine **how to overcome a known problem or
constraint**. A scene may contribute to both when interpreting evidence and then
working out a solution are separately substantive parts of play.

Puzzle / Problem-Solving Emphasis is distinct from **Exploration Emphasis**.
Navigating or interacting with an environment may contribute to both when
environmental interaction presents an explicit problem that players must reason
through or solve. Merely traversing, searching, discovering, or choosing a route
does not automatically constitute Puzzle / Problem-Solving.

Puzzle / Problem-Solving Emphasis is also distinct from **Tactical Complexity**
and **Rules / System-Mastery Demand**. Combat tactics belong to Tactical
Complexity even when they require substantial reasoning. Knowing which rule,
spell, or character ability mechanically applies belongs to System-Mastery
Demand unless working out a broader noncombat solution is itself substantive
play.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Explicit noncombat problems requiring reasoning, experimentation, or creative solutions are absent, incidental, or rapidly resolved; the adventure fundamentally functions through other modes of play. |
| **2 — Low** | Meaningful puzzle or problem-solving play occurs and matters, but is limited in extent or clearly secondary to other modes. |
| **3 — Mixed** | Puzzle / Problem-Solving is a substantial recurring component alongside comparably important non-problem-solving play. |
| **4 — High** | Puzzle / Problem-Solving is one of the adventure's dominant modes and regularly drives progress through reasoning, experimentation, or creative solutions to explicit noncombat problems. |
| **5 — Dominant** | The adventure is fundamentally organized around solving puzzles or explicit noncombat problems; sustained reasoning, experimentation, or creative problem-solving provides the primary structure of expected play, with other modes largely occurring within or being enabled by those solutions. |

**Status:** Frozen calibration rubric. The definition, clarification, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during Puzzle /
Problem-Solving Emphasis calibration. They illustrate application of the rubric
but do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0262 — Lost Mine of Phandelver** |
| **2 — Low** | **ADV-0053 — Call of the Wild**; **ADV-0062 — No Honour Among Thieves**; **ADV-0287 — House of Lament**; **ADV-0303 — Storm King's Thunder** |
| **3 — Mixed** | **ADV-0277 — The Wild Beyond the Witchlight** |
| **4 — High** | **ADV-0031 — White Plume Mountain** |
| **5 — Dominant** | **ADV-0034 — Tomb of Horrors** |

Initial calibration applied the frozen rubric to the eight Analysis Validation
Corpus calibration adventures and then source-grounded the adjacent score
boundaries. Those pressure tests changed **ADV-0040 — Expedition to the Barrier
Peaks** from 3 to 2, **ADV-0062 — No Honour Among Thieves** from 3 to 2, and
**ADV-0277 — The Wild Beyond the Witchlight** from 4 to 3; **ADV-0287 — House of
Lament** remained 1 and **ADV-0034 — Tomb of Horrors** remained 5. No rubric
wording changed. Because those adjudications left score 4 without an exemplar, a
targeted search across the remaining 22 AVC validation adventures identified
**ADV-0031 — White Plume Mountain** as the strongest candidate. A full sequential
source review of its complete canonical unit placed it at 4, establishing the
3/4 and 4/5 boundaries without widening the search to the full Adventure Master
Catalog.

A subsequent nine-adventure blind independent pass applied the frozen rubric
without access to prior Puzzle / Problem-Solving scores, rationales, benchmark
assignments, pressure-test outcomes, or expected score distribution. It
independently reproduced six of the nine then-adjudicated scores exactly,
including **ADV-0062 — No Honour Among Thieves** at 2, **ADV-0277 — The Wild
Beyond the Witchlight** at 3, **ADV-0031 — White Plume Mountain** at 4, and
**ADV-0034 — Tomb of Horrors** at 5. All three disagreements occurred at the
1/2 boundary: the blind pass scored **ADV-0040 — Expedition to the Barrier
Peaks** 1 rather than 2, **ADV-0262 — Lost Mine of Phandelver** 1 rather than 2,
and **ADV-0287 — House of Lament** 2 rather than 1. Focused source-grounded
adjudication resolved all three disagreements in favor of the blind results.
These are corrections to benchmark application under the frozen rubric, not
changes to the rubric itself.

The **1/2** boundary distinguishes ordinary opportunities for player cleverness
from authored substantive problem-solving play. Score 1 may contain hazards,
unfamiliar mechanisms, or situations that creative players can improvise around
when the published material principally resolves them through checks, searching,
prescribed procedures, or ordinary environmental interaction. Score 2 requires
at least one meaningfully developed player-facing **how**-problem or bounded
problem-solving sequence whose resolution materially affects access, progress,
outcome, or resources. A substantively puzzle-heavy supported branch can justify
score 2 even when alternative paths contain less Puzzle / Problem-Solving play;
such cases should be marked path-sensitive when the difference is material.

The **2/3** boundary distinguishes limited or concentrated problem-solving from
a substantial recurring mode across the adventure. The **3/4** boundary
distinguishes substantial recurring problem-solving from adventures where it is
one of the dominant modes and regularly drives progress. The **4/5** boundary
distinguishes adventures where Puzzle / Problem-Solving is one dominant mode
from adventures fundamentally organized around sustained problem-solving as the
primary structure of expected play.

### 8. Tactical Complexity

**Definition:** Tactical Complexity measures the **live tactical decision load**
players must manage during meaningful encounters: how many consequential
tactical factors are simultaneously relevant, how strongly those factors
interact, and how much encounter state forces players to reassess priorities,
sequencing, positioning, objectives, resources, and coordination as play
develops.

Tactical Complexity measures the **decision structure of encounters**, not how
much combat the adventure contains and not how difficult its rules are to
understand. A combat-heavy adventure can still have low Tactical Complexity if
most encounters present straightforward choices. Conversely, mechanically
simple encounters can be highly tactically complex when several consequential
pressures remain live together, interact, and force repeated reassessment as
the encounter evolves.

The upper end of the scale is defined by **coupling and dynamic decision load**.
Tactical factors are coupled when a decision on one axis materially changes the
value, feasibility, urgency, or risk of decisions on another—for example when
movement changes objective timing, target choice changes environmental exposure,
resource use changes who can coordinate or reposition, or an evolving threat
forces the party to reorder priorities. Multiple factors merely being present
does not by itself establish high Tactical Complexity.

Tactical Complexity is distinct from **Rules / System-Mastery Demand**. Rules /
System-Mastery Demand asks how much mechanical understanding is required to
correctly understand and use the available option space. Tactical Complexity
asks, once the relevant mechanics and encounter state are understood, how
difficult the **live decision problem** is: which options to choose, in what
order, for which objectives, and how those choices must change as other tactical
factors change. A mechanically simple encounter can therefore be tactically
complex, while a mechanically intricate situation can impose substantial
System-Mastery Demand without high Tactical Complexity.

Tactical Complexity is also distinct from **Lethality / Failure Severity**.
Tactical mistakes may be punished severely in a lethal adventure, but severity
of consequence does not itself make the tactical decision structure more
complex. Likewise, an encounter can demand dense tactical adaptation without
being unusually lethal.

Tactical Complexity is distinct from **Puzzle / Problem-Solving Emphasis**.
Planning, decoding, mechanisms, route selection, and static reasoning challenges
do not become Tactical Complexity merely because they affect later combat. They
count here only when they become active encounter-time constraints, options,
priorities, or interactions that players must manage during meaningful
encounters.

Large battlefields, numerous enemies, unusual rules, boss monsters, persistent
adventure state, and spectacle are not proxies for Tactical Complexity. They
matter only to the extent that they create consequential **live tactical
decisions** during expected substantive encounters. Persistent or between-
encounter state matters when it becomes an active tactical constraint or option
during encounter play, not merely because it changes what encounter occurs
next.

Assess Tactical Complexity by the **substantive weight of encounter play** at
each level of live tactical decision load, not by raw encounter count. A long,
central, mandatory encounter sequence can carry enough substantive weight to
establish an upper score when it itself presents the required tactical load.
Conversely, a brief, rare, or optional extreme encounter does not automatically
dominate a broader body of materially simpler expected encounter play.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Meaningful encounters offer little tactical differentiation. Positioning, priorities, sequencing, environmental interaction, ability timing, or coordination are absent, obvious, or rarely change the effective approach. |
| **2 — Low** | Some tactical considerations matter, but most meaningful encounters can be handled through straightforward action selection. Tactical complexity is localized, limited, or usually involves only one significant factor at a time. |
| **3 — Moderate** | Multiple tactical considerations recur across meaningful encounters. Players regularly make consequential choices involving positioning, target or objective priority, timing, environment, resources, or coordination, but those considerations are usually **bounded, relatively stable, or separable**. Tactical adaptation matters without becoming a sustained multi-factor management problem. |
| **4 — High** | Substantial encounter play regularly creates **coupled tactical pressure**: several live factors matter together, choices on one axis affect others, or encounter state causes priorities to change. Players repeatedly benefit materially from re-sequencing actions, reallocating attention or resources, repositioning, changing targets or objectives, or coordinating responses. The pressure may occur across several encounters or within a substantial central sequence; it need not characterize most encounters. |
| **5 — Very High** | Across multiple major encounters—or within a **dominant sustained mandatory encounter sequence**—substantial encounter play presents **dense, sustained coupled tactical pressure**. Multiple consequential factors remain live simultaneously and materially interact; changes in threats, objectives, environment, positioning, timing, resources, or party state repeatedly alter the value or feasibility of other choices. Players must continually reprioritize, coordinate, or adapt across evolving encounter state rather than resolving tactical considerations independently or one at a time. |

**Status:** Accepted, frozen, corpus-calibrated, and blind-validated for
**AFAO 1.4.1** as **Tactical Complexity Revision 3**. Scores 1--2 retain the
AFAO 1.3 wording. The definition and scores 3--5 retain the AFAO 1.4 Revision-3
semantics around live tactical decision load, coupling among consequential
factors, and sustained dynamic reassessment. The completed AFAO 1.4.1 blind
revalidation and focused source-grounded adjudications establish the benchmark
placements below without changing the Revision-3 definition or score anchors.
Future changes to their wording or meaning require an explicit ontology revision
and revalidation against the calibration set.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Tactical Complexity calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0278 — Witchlight Carnival** |
| **2 — Low** | **ADV-0053 — Call of the Wild**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0034 — Tomb of Horrors** |
| **3 — Moderate** | **ADV-0262 — Lost Mine of Phandelver**; **ADV-0287 — House of Lament**; **ADV-0040 — Expedition to the Barrier Peaks** |
| **4 — High** | **ADV-0232 — The Final Enemy**; **ADV-0223 — Sunblight**; **ADV-0189 — Tockworth's Clockworks** |
| **5 — Very High** | **ADV-0303 — Storm King's Thunder**; **ADV-0062 — No Honour Among Thieves**; **ADV-0248 — Siege of Kalaman**; **ADV-0230 — Salvage Operation** |

#### Calibration Record and Boundary Guidance

The record below documents the historical calibration path through AFAO 1.3
Revision 2 and the subsequent AFAO 1.4 Revision-3 semantic change. Where that
historical record describes "final" 3/4 or 4/5 logic, the **Revision-3
boundaries below supersede it normatively**. Historical benchmark outcomes are
preserved to make the change auditable rather than silently rewritten; the
current AFAO 1.4.1 placements are established by the completed blind
revalidation and adjudication record below.

The Revision-3 adjacent-boundary interpretation is:

- **1/2 — ordinary tactical choice vs authored tactical differentiation.**
  This boundary is unchanged from AFAO 1.3.
- **2/3 — localized or mostly one-factor decisions vs recurring tactical
  management.** Score 3 begins when multiple tactical considerations recur often
  enough that players regularly make consequential encounter-time choices among
  them, even when those factors remain bounded, stable, or separable.
- **3/4 — recurring tactical factors vs coupled tactical pressure.** Score 4
  begins when several live factors materially affect one another or changing
  encounter state repeatedly changes priorities, sequencing, positioning,
  targets, objectives, resources, or coordination. The discriminator is not the
  number of encounters containing several factors, but whether substantive
  encounter play repeatedly creates a coupled decision problem.
- **4/5 — coupled pressure vs dense, sustained coupled pressure.** Score 5 begins
  when multiple consequential factors remain simultaneously live and interacting
  for long enough that players must continually reprioritize, coordinate, or
  adapt across evolving encounter state. This may occur across multiple major
  encounters or within one dominant sustained mandatory encounter sequence.
  Score 5 does **not** require proof that a straightforward plan is impossible,
  that sustained adaptation is a practical dependency for success, or that the
  score-5 structure appears in most encounters.

The original calibration pass applied the first frozen Tactical Complexity
rubric to the familiar eight Analysis Validation Corpus cases. A blind
independent pass reproduced six of those eight then-working scores exactly.
Focused full-source adjudication corrected **ADV-0277 — The Wild Beyond the
Witchlight** from 1 to 2 because its combat-light structure had improperly
suppressed qualifying authored tactical decisions, and corrected **ADV-0062 —
No Honour Among Thieves** from 5 to 4 because its densest vault-room structures
are route-selected rather than characteristic enough of expected substantive
encounter play. Those corrections left scores 1--4 well calibrated but score 5
without a defensible endpoint.

A targeted endpoint search then established **ADV-0278 — Witchlight Carnival**
at 1. Its expected encounters contain occasional positional, timing, or
objective choices, but those choices are too thin, obvious, or localized to
create substantive authored tactical differentiation. This confirms that score
1 can contain ordinary player tactical choices; score 2 requires an authored
encounter structure in which tactical adaptation meaningfully changes the
effective approach.

The **1/2** boundary therefore distinguishes incidental or ordinary tactical
choice from substantive authored tactical differentiation. **ADV-0278 —
Witchlight Carnival** anchors 1, while **ADV-0277 — The Wild Beyond the
Witchlight**, **ADV-0034 — Tomb of Horrors**, and **ADV-0053 — Call of the Wild**
demonstrate score 2 through limited or localized tactical considerations that
matter without becoming a recurring multi-factor encounter mode.

The **2/3** boundary distinguishes localized, limited, or mostly one-factor
tactical considerations from **recurring multiple tactical factors** across
meaningful encounters. **ADV-0262 — Lost Mine of Phandelver** and **ADV-0287 —
House of Lament** reach 3 because positioning, target priority, environment,
timing, or coordination recur often enough to become a substantial continuing
feature, while the complexity remains generally bounded rather than repeatedly
layered or evolving.

The **3/4** boundary distinguishes recurring but bounded multi-factor play from
major encounters that **repeatedly combine several factors or changing states**.
At score 4, adaptation is not merely available: it is often materially better
than straightforward default play. **ADV-0040 — Expedition to the Barrier
Peaks** and **ADV-0303 — Storm King's Thunder** provide broad score-4 anchors,
while later upper-end reviews supplied several distinct high-complexity
architectures without requiring a score-5 placement.

Those upper-end reviews were deliberately used to falsify the original score-5
anchor rather than to force an occupied endpoint. **ADV-0062 — No Honour Among
Thieves** demonstrated route-selected local density; **ADV-0230 — Salvage
Operation** demonstrated a mandatory, unusually dense climax; **ADV-0232 — The
Final Enemy** demonstrated strong reconnaissance reactions plus an optional
extreme assault; **ADV-0189 — Tockworth's Clockworks** demonstrated persistent
security state whose complexity often operates between encounters;
**ADV-0248 — Siege of Kalaman** demonstrated repeated changing-state set pieces
with a smaller number of truly dense peaks; and **ADV-0223 — Sunblight**
demonstrated multiple local high-density configurations complicated by
conditional faction, boss-location, and reinforcement state.

Across those cases, the original score-5 wording proved too structurally
restrictive. It required major encounters to routinely hinge on layered,
evolving tactical states or objectives and thereby made one particular encounter
architecture an implicit endpoint requirement. The revised score-5 wording
retains the demanding interaction and sustained-adaptation standard while
restoring a natural intensity progression from score 4. Changing states and
competing objectives remain strong evidence but are not mandatory architectural
features.

Under frozen Revision 2, all then-score-4 cases were re-adjudicated. **ADV-0230
— Salvage Operation** moved to 5 because its mandatory sinking-ship sequence
requires sustained coordination among the mission-critical box, movement,
action economy, deteriorating ship state, enemies, escape timing, and party
coordination; straightforward default combat can fail to resolve the actual
encounter objective. **ADV-0062 — No Honour Among Thieves**, **ADV-0232 — The
Final Enemy**, **ADV-0189 — Tockworth's Clockworks**, **ADV-0248 — Siege of
Kalaman**, and **ADV-0223 — Sunblight** ultimately remain 4 after the final blind
disagreement adjudications described below.

A dedicated six-case upper-boundary blind pass independently scored
**ADV-0062 — No Honour Among Thieves** at 4, **ADV-0230 — Salvage Operation** at
5, **ADV-0232 — The Final Enemy** at 5, **ADV-0189 — Tockworth's Clockworks** at
4, **ADV-0248 — Siege of Kalaman** at 4, and **ADV-0223 — Sunblight** at 4. The
reviewer disclosed prior Tactical Complexity exposure for Salvage Operation and
Siege of Kalaman, so those two cases are not perfectly blind; the remaining four
were assessed without recognized prior Tactical Complexity results. The blind
pass nevertheless reproduced the core distinction between score 4 as material
reward for adaptation and score 5 as dependence on sustained coordination of
interacting tactical factors.

Focused full-source adjudication of the three score disagreements accepted the
blind application for **ADV-0248 — Siege of Kalaman** and **ADV-0223 —
Sunblight**, moving both final Revision-2 placements from 5 to 4, and rejected
the blind 5 for **ADV-0232 — The Final Enemy**, retaining it at 4. The Final
Enemy's mandatory reconnaissance contains meaningful runner, alarm,
reinforcement, underwater-positioning, and extraction decisions, but its most
formal dense global tactical architecture belongs to an optional continuation;
mission-level strategic pressure and local reaction chains do not make dense
active encounter decision structures characteristic enough of the canonical
unit for 5. Siege of Kalaman contains genuine score-5-like encounters such as
the Mourning Sanctum, but dense interacting structures remain peaks within a
broader encounter experience where straightforward competent combat is often
still workable. Sunblight similarly contains highly dense local configurations,
especially around Xardorok, but much of its apparent complexity is conditional
or persistent adventure state that changes which encounter occurs rather than
creating simultaneous active tactical pressure inside expected encounters.

Historically, Revision 2 summarized the **4/5** boundary as material reward
for adaptation versus practical dependence on sustained coordination. Revision 3
**supersedes that normative test**. The Revision-3 boundary is now the difference
between **coupled tactical pressure** at 4 and **dense, sustained coupled
tactical pressure** at 5, as defined above. A workable default plan, possible
retreat, or the existence of simpler encounters elsewhere in the canonical unit
is not by itself evidence against 5.

A score-4 adventure may still contain individual score-5-like encounters,
routes, or sequences. Weight those structures by their substantive role in
expected encounter play. A long, central, mandatory sequence can itself support
5 when its live tactical decision load is dense and sustained; rare or optional
extreme material should receive less weight.

Several recurring false-positive patterns should be excluded during future
scoring:

- **Combat volume is not complexity.** More enemies or more fights do not by
  themselves increase Tactical Complexity.
- **Lethality is not complexity.** Severe punishment for a poor decision does
  not make the decision structure denser.
- **Rules difficulty is not complexity.** Knowing unusual creature, spell,
  vehicle, underwater, siege, or environmental rules belongs to Rules /
  System-Mastery Demand unless those rules create substantive active tactical
  choices.
- **Puzzle or strategic planning is not active tactics.** Route planning,
  deciphering mechanisms, choosing an infiltration plan, or manipulating a
  persistent system between encounters does not count merely because it affects
  later combat.
- **Persistent state is not automatically complexity.** Alarm networks,
  reinforcement pools, faction allegiance, boss location, cleared rooms, or
  other persistent conditions count only when they become live encounter-time
  constraints, options, priorities, or interactions. State that principally
  changes what happens next belongs outside Tactical Complexity unless and until
  it enters the active tactical decision problem.
- **Path sensitivity is not an automatic ceiling.** A path-sensitive adventure
  can score 5 when expected substantive play still satisfies the anchor; the
  path-sensitivity flag records meaningful variation rather than replacing the
  score.
- **Optional extreme material does not dominate the canonical score.** Rare or
  optional score-5-like sequences receive less weight than mandatory/common
  play under the common scoring principles.
- **A dominant mandatory sequence can establish an upper score.** A long,
  central, mandatory encounter sequence can legitimately define a large share
  of expected substantive encounter play. If that sequence presents dense,
  sustained coupled tactical pressure, raw counts of simpler encounters must not
  impose an independent ceiling.

The AFAO 1.3 Revision-2 calibrated set historically established empirical cases
on both sides of all four adjacent boundaries, with **ADV-0278 — Witchlight
Carnival** at 1 and **ADV-0230 — Salvage Operation** at 5. AFAO 1.4 deliberately
reopened the score-3 through score-5 applications under Revision 3 rather than
carrying those historical placements forward by assumption.

#### AFAO 1.4.1 Blind Revalidation and Final Benchmark Adjudication

Two separate blind full-source Revision-3 passes assessed the same ten-adventure
3--5 calibration cohort in the fixed order **ADV-0262, ADV-0287, ADV-0303,
ADV-0062, ADV-0040, ADV-0248, ADV-0232, ADV-0223, ADV-0189, ADV-0230**. Neither
reviewer reported target-specific Tactical Complexity contamination or material
rubric ambiguity. The passes agreed exactly on seven of ten integer scores and
placed every remaining case on an adjacent score.

Both blind passes independently reproduced **ADV-0262 — Lost Mine of
Phandelver** at 3, **ADV-0287 — House of Lament** at 3, **ADV-0062 — No Honour
Among Thieves** at 5, **ADV-0248 — Siege of Kalaman** at 5, **ADV-0223 —
Sunblight** at 4, **ADV-0189 — Tockworth's Clockworks** at 4, and **ADV-0230 —
Salvage Operation** at 5. This independently reproduced the intended semantic
distinctions between bounded recurring tactical considerations, coupled
tactical pressure, and dense sustained coupled tactical pressure, while also
producing multiple score-5 morphologies rather than preserving Salvage Operation
as a unique endpoint architecture.

Three cases required focused source-grounded adjudication:

- **ADV-0303 — Storm King's Thunder** is finalized at **5 — Very High**. The
  source supplies multiple major sequences with sustained interacting objectives,
  positioning, threats, environmental state, and action-allocation pressures.
  Retaining it at 4 would effectively reintroduce the whole-adventure prevalence
  gate that Revision 3 intentionally removed.
- **ADV-0040 — Expedition to the Barrier Peaks** is finalized at **3 —
  Moderate**. One blind pass followed an erroneous `171--224` scope from the
  blind-test target table, while the other reviewed the complete named canonical
  unit at `157--189`. Focused review of the correct complete unit found recurring
  tactical differentiation but predominantly bounded or separable live tactical
  problems; much of the adventure's apparent complexity instead belongs to
  exploration or Rules / System-Mastery Demand. The earlier blind 4 is therefore
  not treated as a clean same-scope disagreement.
- **ADV-0232 — The Final Enemy** is finalized at **4 — High**. Its mandatory
  reconnaissance supports genuine coupled tactical pressure through alarm,
  runner, reinforcement, underwater-positioning, pursuit, and extraction
  interactions, but the densest sustained score-5 structure belongs primarily to
  the optional Assault continuation. Under the substantive-weight rule, that
  optional extreme sequence does not dominate the canonical score.

Combined with the previously blind-validated lower anchors, the final fourteen-
adventure Revision-3 benchmark ladder is **1:** ADV-0278; **2:** ADV-0053,
ADV-0277, ADV-0034; **3:** ADV-0262, ADV-0287, ADV-0040; **4:** ADV-0232,
ADV-0223, ADV-0189; **5:** ADV-0303, ADV-0062, ADV-0248, ADV-0230. All five
score levels are therefore empirically inhabited, the 3/4 and 4/5 boundaries are
source-grounded on both sides, and Revision 3 is accepted as calibrated and
independently blind-validated without further anchor wording changes.

### 9. Lethality / Failure Severity

**Definition:** How readily mistakes or failure during expected substantive play
can produce severe, lasting, or irreversible consequences.

**Clarifications:**

- Measures the **consequence profile of failure**, not general difficulty.
- A mechanically difficult adventure may still be forgiving if failures are
  recoverable.
- A simple choice or hazard can score strongly if failure immediately has severe
  consequences.
- Qualifying severe consequences include:
  - character death;
  - permanent or difficult-to-reverse character loss or transformation;
  - irreversible loss of important objectives, NPCs, resources, or
    opportunities;
  - major persistent changes to adventure state; and
  - catastrophic mission failure or consequences substantially not undoable
    through ordinary continued play.
- Ordinary hit-point damage, expendable resource loss, temporary conditions,
  minor delays, and easily reversible setbacks do not by themselves establish a
  high score.
- The dimension considers both **severity** and **readiness of exposure**.
- Rare or highly optional catastrophic outcomes weigh less than severe
  consequences recurring in expected or common play.
- This dimension is distinct from **Combat Emphasis** and **Tactical
  Complexity**.
- This dimension is distinct from **Rules / System-Mastery Demand**.

| Score | Meaning |
| ---: | --- |
| **1 — Forgiving** | Severe, lasting, or irreversible consequences are absent, exceptional, or strongly buffered. Mistakes and failures ordinarily produce temporary or readily recoverable setbacks. |
| **2 — Low** | Severe consequences are possible and meaningful but uncommon, substantially avoidable, or concentrated in a small number of situations. Most ordinary mistakes and failures remain recoverable. |
| **3 — Moderate** | Severe consequences are a meaningful recurring possibility. Significant mistakes or failures can produce death, lasting loss, or major persistent setbacks, but warning, mitigation, retreat, recovery, or other margins for error remain substantial. |
| **4 — High** | Severe consequences are a recurring and readily credible feature of expected play. Individual mistakes, failed encounters, or poor decisions can regularly produce death, permanent loss, or major irreversible outcomes, with limited protection or recovery. |
| **5 — Extreme** | The adventure is fundamentally unforgiving: severe or catastrophic consequences are pervasive or structurally central, and relatively discrete mistakes, incorrect choices, or failures can readily produce death, irreversible loss, or adventure-ending outcomes with little reliable margin for recovery. |

**Status:** Frozen calibration rubric. The definition, clarifications, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Lethality / Failure Severity calibration. They illustrate application of the
rubric but do not redefine the score anchors; future adventures are scored
against the anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Forgiving** | **ADV-0278 — Witchlight Carnival** |
| **2 — Low** | **ADV-0053 — Call of the Wild**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **3 — Moderate** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0062 — No Honour Among Thieves**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0303 — Storm King's Thunder** |
| **4 — High** | **ADV-0287 — House of Lament** |
| **5 — Extreme** | **ADV-0034 — Tomb of Horrors** |

Initial calibration applied the frozen rubric to the familiar eight Analysis
Validation Corpus cases. Because none produced a defensible score 1, a targeted
AVC endpoint search identified **ADV-0278 — Witchlight Carnival** as the
strongest lower-end candidate. Full-source review placed the nested carnival
unit at 1 because ordinary failure is unusually and repeatedly buffered toward
unconsciousness, ejection, temporary conditions, contest loss, or other
recoverable outcomes rather than severe lasting consequences. The endpoint was
added without forcing the original eight-case score distribution.

Source-grounded pressure testing then examined every adjacent boundary without
changing the frozen wording. The **1/2** boundary distinguishes adventures where
severe outcomes are absent, exceptional, or actively buffered from adventures
where severe consequences become genuinely possible in ordinary supported play
but remain uncommon, substantially avoidable, or localized. **ADV-0278 —
Witchlight Carnival** anchors the former pattern; **ADV-0053 — Call of the Wild**
and **ADV-0277 — The Wild Beyond the Witchlight** demonstrate the latter.

The **2/3** boundary distinguishes limited or concentrated exposure from severe
failure becoming a **meaningful recurring possibility across substantive play**.
A score 3 can still provide substantial warning, mitigation, retreat, recovery,
or fail-forward support. **ADV-0262 — Lost Mine of Phandelver** is a useful
upper-side case because dangerous failure recurs across multiple phases while
the adventure also repeatedly buffers defeat and preserves alternate routes
forward.

The **3/4** boundary distinguishes recurring severe consequences with
substantial published safety valves from expected play in which severe
consequences are both recurring and **readily credible**, with materially more
limited protection or recovery. This was the strongest pre-blind pressure
point, especially for **ADV-0303 — Storm King's Thunder** and **ADV-0040 —
Expedition to the Barrier Peaks**. Both remained 3 because warning, retreat,
recovery, alternate progression, or fail-forward structures remain substantial.
**ADV-0287 — House of Lament** reaches 4 because the awakened house traps the
characters, turns the site into a recurring supernatural deathtrap, and makes
permanent spiritual imprisonment an explicit failure state while reducing the
reliability of escape and recovery.

The **4/5** boundary distinguishes an adventure that is highly dangerous but
still supplies meaningful ramp-up, warning, information, or mitigation from one
that is **fundamentally unforgiving**. **ADV-0034 — Tomb of Horrors** reaches 5
because catastrophic and often irreversible consequences are repeatedly tied to
relatively discrete interactions and incorrect choices with little dependable
recovery margin; **ADV-0287 — House of Lament** remains 4 because its danger
escalates and still provides substantially more warning, investigation, allies,
and supported means of victory or escape.

A subsequent nine-adventure blind independent pass applied the frozen rubric
without access to prior Lethality / Failure Severity scores, rationales,
benchmark assignments, pressure-test outcomes, or expected score distribution.
It reproduced **all nine scores exactly** and also reproduced **all nine
path-sensitivity judgments exactly**. No source-grounded score adjudication or
rubric wording change was therefore required.

The blind pass independently identified the interaction between **severity** and
**readiness of exposure** as the hardest application issue, especially because
ordinary combat can theoretically produce character death. Its successful
reproduction of the calibration set supports the existing wording without an
additional combat-specific rule: character death is a qualifying severe
consequence, but the mere theoretical possibility of death from ordinary combat
does not determine the score. Reviewers must evaluate the published consequence
profile, including whether defeat is actually converted into death, capture,
unconsciousness, retreat, resurrection, alternate progression, or another
buffered state.

Likewise, raw incident count does not determine the score in a long campaign,
and published recovery after death or catastrophic failure materially affects
severity. **ADV-0062 — No Honour Among Thieves** is a useful calibration case:
its explicit potential total-party-kill branch does not by itself raise the
adventure above 3 because that outcome follows optional overextension and the
published material explicitly supports capture, resurrection, and continued
play after failure.
### 10. Rules / System-Mastery Demand

**Definition:** How strongly successful play depends on understanding and
effectively using the game's mechanical systems.

Rules / System-Mastery Demand is distinct from **Tactical Complexity**. Tactical
Complexity concerns choosing effective positioning, targets, sequencing,
coordination, environmental interaction, and other tactical decisions.
System-Mastery concerns understanding the mechanical tools and rules through
which those choices operate. A mechanically simple encounter can be tactically
complex, and a mechanically intricate situation can impose substantial
System-Mastery Demand without being tactically complex.

It is also distinct from **Puzzle / Problem-Solving Emphasis**. Knowing which
rule, spell, character ability, resource, condition, or mechanical interaction
applies belongs primarily to Rules / System-Mastery Demand; determining a
broader noncombat solution belongs to Puzzle / Problem-Solving when working out
that solution is itself substantive play.

The following calibration rules apply:

- **Basic checks and attacks are not system mastery.** Ordinary participation
  in the core resolution loop does not by itself establish demand beyond score
  1.
- **Mechanical presence is not player-side mastery.** Beyond-basic mechanics can
  appear without raising an adventure above Minimal when players can participate
  effectively through ordinary prompted resolution, straightforward ability use,
  or intuitive responses without needing to understand, select, combine, or
  deliberately exploit the underlying mechanical interaction. Conditions,
  creature traits, environmental rules, traps, hazards, specialized equipment,
  and similar mechanics count toward this dimension only to the extent that
  successful play materially rewards or depends on players themselves
  understanding and effectively using them. Score 2 begins when player-side
  beyond-basic understanding materially improves or enables successful play in
  meaningful but still bounded or secondary situations.
- **Level is evidence, not destiny.** High-level characters may provide more
  mechanical tools, but character level alone cannot determine this score.
  The adventure must actually make successful play depend on understanding and
  using those tools.
- **Adventure-specific player-facing systems count.** A subsystem introduced
  by the adventure can contribute when players must understand, manage, or use
  it meaningfully. Purely GM-facing machinery does not increase player
  System-Mastery Demand unless it creates mechanical information or choices the
  players themselves must understand and act on.
- **Combat frequency, encounter difficulty, tactical sophistication, and
  lethality are not proxies for System-Mastery Demand.** They may coexist with
  high mechanical demand, but they belong to other dimensions unless
  successful play specifically depends on understanding and applying
  mechanical rules, abilities, resources, interactions, or player-facing
  systems.
- **Mechanical teaching does not inherently reduce demand.** Explicit teaching,
  discoverable procedures, or stable rules do not reduce the score when players
  must repeatedly retain and effectively use that mechanical understanding
  across substantive play. Conversely, a one-off prescribed procedure or
  localized exact mechanical gate does not by itself establish high demand.
- **Continuity can be persistent or distributed.** Repeated mechanically
  demanding situations can remain Moderate when their strongest demands are
  chiefly localized, concentrated, or separately resolved and do not aggregate
  into a sustained mechanical operating pattern. Upper-score continuity may
  arise either because consequential mechanical information, state, rules,
  interactions, or tools carry forward across later substantive play, **or**
  because substantive play repeatedly requires players to interpret and adapt
  to materially differentiated player-facing mechanical states, interactions,
  or response requirements. High begins when either form of sustained
  mechanical demand materially shapes substantive portions of play. Extreme
  begins when correctly operating, interpreting, exploiting, or adapting to
  such mechanics repeatedly becomes one of the substantive progression
  challenges itself.
- **The anchors are not sequential morphology gates.** Scores are absolute
  semantic placements, not a checklist in which every higher score must first
  exhibit the persistent-state or tool-carryover morphology of a lower-score
  exemplar. A case can reach Extreme through repeated differentiated mechanical
  response even when the particular solution or state from one challenge does
  not remain useful in the next, provided mechanical interpretation and
  adaptation itself repeatedly carries substantive progression across multiple
  major challenges.
- **Score 5 does not require universal coverage or one mechanical morphology.**
  Extreme does not require every encounter or supported route to demand mastery,
  nor does it require one persistent bespoke subsystem. A persistent
  player-operated subsystem, a recurring exact-rule environment, or repeated
  differentiated mechanical response can each qualify when mechanical mastery
  repeatedly carries substantive challenge progression.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Successful play requires little beyond ordinary basic rules use. Beyond-basic mechanics may occur, but players can generally participate effectively through straightforward or intuitive choices, ordinary prompted resolution, or straightforward ability use without needing to understand or deliberately exploit the underlying mechanical interaction. |
| **2 — Low** | Player-side understanding beyond the basics materially matters in some meaningful situations: understanding or deliberately using a non-basic rule, ability, resource, condition, interaction, or subsystem can materially improve or enable successful play. The demand remains bounded or secondary; competent ordinary play is generally sufficient without sustained system mastery. |
| **3 — Moderate** | Successful play repeatedly rewards and sometimes depends on competent understanding and use of abilities, resources, rules, or interactions. Mechanically demanding situations form a meaningful recurring part of play, but their strongest demands are generally localized, concentrated, or resolved as discrete problems and do not aggregate into a sustained player-facing mechanical layer or sustained differentiated-response pattern that materially shapes substantive progression. |
| **4 — High** | A sustained player-facing mechanical demand spans substantive portions of play. It may arise through a continuing mechanical environment or system whose information, state, rules, interactions, or tools remain consequential across multiple challenges or locations, **or** through recurring materially differentiated mechanical states or interactions that require continued interpretation and adaptation across substantive play. This mechanical layer or pattern materially shapes access, traversal, options, resources, or resolution, but correctly operating or adapting to it does not itself repeatedly form a principal progression challenge. |
| **5 — Extreme** | Player-facing mechanical mastery is a defining operating structure of substantive play. Across multiple major challenges, successful progression or effective resolution repeatedly consists of correctly operating persistent mechanical systems, recognizing and exploiting consequential rule interactions, or adapting among materially different mechanical states or responses. A particular solution, state, or tool need not carry forward when the recurring progression-bearing demand is instead the need to identify and apply the correct mechanical response anew. Explicit teaching, discoverable procedures, or stable rules do not reduce the score when players must repeatedly apply or adapt that mechanical understanding. |

**Status:** Accepted, calibrated, and blind-validated for AFAO 1.5. Scores
1--2 include the targeted lower-boundary clarification restoring the calibrated
distinction between mere mechanical presence and materially consequential
player-side mechanical understanding. Scores 3--5 include the targeted
continuity clarification distinguishing persistent carry-forward from sustained
distributed differentiated response. The AFAO 1.3 source-grounded calibration
record remains historical evidence; the AFAO 1.5 blind revalidation and focused
source-grounded benchmark adjudications below supersede it normatively. No
surviving RSMD wording defect or unresolved integer benchmark disagreement
remains.

#### Calibration Benchmarks

The following scored adventures are the final AFAO 1.5 Rules / System-Mastery
Demand reference exemplars. They illustrate application of the rubric but do
not redefine the score anchors; future adventures are scored against the anchor
meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0053 — Call of the Wild** |
| **2 — Low** | **ADV-0262 — Lost Mine of Phandelver**; **ADV-0287 — House of Lament**; **ADV-0303 — Storm King's Thunder** |
| **3 — Moderate** | **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0034 — Tomb of Horrors**; **ADV-0335 — Trobriand's Graveyard** |
| **4 — High** | **ADV-0062 — No Honour Among Thieves**; **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0031 — White Plume Mountain**; **ADV-0227 — Doom of Ythryn**; **ADV-0345 — Mad Wizard's Lair** |
| **5 — Extreme** | **ADV-0032 — Dead in Thay**; **ADV-0337 — Obstacle Course** |

#### Calibration Record and Boundary Guidance

AFAO 1.2 established the lower endpoint and lower-middle distinctions through
full-source calibration, adjacent-boundary pressure testing, and a twelve-case
blind independent pass. That work also exposed persistent difficulty at the
upper end: repeated Adventure Master Catalog searches struggled to identify a
clearly reproducible score-5 endpoint, and the resulting 4/5 distinction relied
heavily on broad terms such as advanced mastery, adventure-wide coverage, and
ordinary competence being insufficient.

For the AFAO 1.3 revision, nine compact upper-half calibration adventures were
reread from their complete canonical sources and treated as challengeable
hypotheses rather than target scores: **ADV-0034 — Tomb of Horrors**,
**ADV-0031 — White Plume Mountain**, **ADV-0062 — No Honour Among Thieves**,
**ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0227 — Doom of Ythryn**,
**ADV-0335 — Trobriand's Graveyard**, **ADV-0032 — Dead in Thay**,
**ADV-0337 — Obstacle Course**, and **ADV-0345 — Mad Wizard's Lair**.
**ADV-0303 — Storm King's Thunder** was deliberately set aside from that compact
source-comparison pass and retains its existing score 3 pending the revised
rubric's blind revalidation.

The source comparison produced a clearer upper ladder. At score 3, demanding
mechanical situations recur but are chiefly localized, concentrated, or resolved
as discrete problems. **Tomb of Horrors** and **White Plume Mountain** are clean
examples: exact mechanical interactions and environmental mechanisms matter,
but understanding or tooling acquired in one challenge has limited continuing
importance across later play. **No Honour Among Thieves** is an upper-side score
3 because its vault becomes mechanically dense, but much of that demand remains
concentrated in room-specific hazards and local response states.

Score 4 begins when the adventure establishes a continuing player-facing
mechanical environment or system whose information, state, rules, or tools carry
forward across substantive play. **Expedition to the Barrier Peaks** does this
through persistent ship technology, access states, devices, and operating rules;
**Doom of Ythryn** through the continuing arcane environment of Ythryn and its
linked rituals, protections, and machinery. AFAO 1.3 initially placed
**Trobriand's Graveyard** at 4 as the weakest 3/4 boundary case because its
construct-control ecology is coherent and recurring. Post-acceptance blind
revalidation did not reproduce that placement; the AFAO 1.5 adjudication below
moves it to 3.

Score 5 begins when mechanical mastery is not merely a continuing layer that
shapes play but repeatedly becomes one of the progression-bearing challenge
structures itself. The calibrated score-5 cases reach that endpoint through
three different morphologies. **Dead in Thay** uses a persistent player-operated
glyph-key and gate system that must be understood, retained, and repeatedly
operated to achieve progression objectives. **Obstacle Course** repeatedly makes
traversal and resolution depend on correctly reading and responding to
consequential exact-rule states. **Mad Wizard's Lair** repeatedly changes which
mechanical responses work, requiring differentiated judgments among spells,
interactions, tools, and creature or object states. Procedurality, explicit
teaching, discoverability, or stable rules therefore do not cap a case below 5
when successful play repeatedly requires players to retain and operate that
mechanical understanding.

The resulting adjacent-boundary interpretation is:

- **1/2 — mechanical presence vs player-side mechanical understanding.** Score
  1 can contain beyond-basic conditions, creature traits, environmental rules,
  traps, hazards, specialized equipment, or similar mechanics when the GM can
  apply them and players can respond effectively through ordinary or intuitive
  play without needing to understand or deliberately exploit the underlying
  interaction. Score 2 begins when players themselves materially benefit from or
  need beyond-basic mechanical understanding in meaningful but bounded or
  secondary situations. The existence or recurrence of a non-basic mechanic is
  not by itself evidence for score 2.
- **2/3:** distinguish limited or secondary mechanical understanding from
  mechanically demanding situations that recur as a meaningful part of
  substantive play.
- **3/4:** distinguish recurring but chiefly localized, concentrated, or
  separately resolved mechanical problems from a **sustained player-facing
  mechanical layer or adaptation pattern**. At score 4, either consequential
  information, state, rules, interactions, or tools carry forward across later
  substantive challenges or locations, **or** materially differentiated
  mechanical states and interactions recur strongly enough that continued
  mechanical interpretation and adaptation itself materially shapes
  substantive play. Mere variety or a large count of bespoke mechanisms is not
  sufficient when each remains independently resolvable and mechanical
  adaptation does not aggregate into a sustained operating pattern.
- **4/5:** distinguish a continuing mechanical layer that materially shapes and
  enables play from **mechanical mastery as a repeatedly progression-bearing
  operating structure**. At score 5, across multiple major challenges,
  successful progression or effective resolution repeatedly consists of
  correctly operating, interpreting, exploiting, or adapting to consequential
  player-facing mechanics. The same information, state, solution, or tool need
  not persist between those challenges when repeated differentiated response is
  the progression-bearing morphology.

#### AFAO 1.5 Post-Blind RSMD Correction and Benchmark Adjudication

Fresh independent application of the accepted AFAO 1.3 wording exposed one
reproducible ontology defect and one benchmark-application problem rather than a
general collapse of the RSMD ladder.

The wording defect was exposed by **ADV-0345 — Mad Wizard's Lair**. Two clean
blind assessments independently placed it at **3 — Moderate**, both for the same
reason: its demanding mechanics are heterogeneous and usually resolved within
individual rooms, so the AFAO 1.3 score-4 continuity language was read as a
mandatory prerequisite that the adventure failed before the score-5
"differentiated mechanical response" morphology could be considered. This is a
semantic contradiction in application, because AFAO 1.3 simultaneously stated
that Extreme does not require one persistent subsystem and explicitly intended
Mad Wizard's Lair to exemplify repeated differentiated mechanical response.

A fresh targeted blind confirmation also placed **ADV-0337 — Obstacle Course**
at **5 — Extreme**, showing that the score-5 endpoint itself remains viable when
a persistent progression-bearing mechanical system is clearly present. The
correction therefore does **not** weaken the 4/5 progression-bearing distinction
or make mechanical density sufficient for an upper score. Instead, it removes
the accidental requirement that every upper-score case first demonstrate the
same persistent-state morphology.

The benchmark-application problem was exposed by **ADV-0335 — Trobriand's
Graveyard**. Two clean blind assessments independently rejected the AFAO 1.3
score-4 placement, scoring it **2** and **3**. Both identified the same limiting
features: the Simulacrux, Shockerstomper, metal interactions, liquid-metal
procedure, control ring, and other beyond-basic mechanics are meaningful but
chiefly localized or optional; much of expected play can proceed without a
continuing player-operated construct system; and the strongest cross-location
control tool need not be acquired. Source-grounded adjudication places the
adventure at **3 — Moderate** rather than 2 because mechanically distinctive
interactions recur across enough substantive locations to make beyond-basic
mechanical adaptation a meaningful recurring part of play. It remains below 4
because those demands do not aggregate into either a sufficiently continuing
carry-forward layer or a sufficiently sustained differentiated-response pattern.

Accordingly, the AFAO 1.3 blind work established the need for the AFAO 1.5
semantic correction and moved **Trobriand's Graveyard** to the score-3 side of
the 3/4 boundary. The corrected wording then received a full fourteen-case blind
benchmark pass, a targeted lower-boundary confirmation after the 1/2
clarification, and focused source-grounded adjudication of every surviving
integer-score disagreement.

Those final adjudications produced six benchmark-application corrections under
the frozen AFAO 1.5 semantics:

- **ADV-0262 — Lost Mine of Phandelver:** **1 → 2**. Player-side understanding
  of several bounded interactions can materially improve or enable success,
  while those demands remain too localized for Moderate.
- **ADV-0277 — The Wild Beyond the Witchlight:** **2 → 3**. Mechanically
  exploitable antagonist weaknesses and exact finale interactions recur across
  major phases, but do not aggregate into a sustained score-4 operating layer.
- **ADV-0303 — Storm King's Thunder:** **3 → 2**. Genuine player-side
  beyond-basic demands occur, but remain bounded, route-local, taught, or
  substantially NPC-supported rather than a recurring mastery demand.
- **ADV-0062 — No Honour Among Thieves:** **3 → 4**. The central heist combines
  a persistent one-hour constraint and Vault-wide rules with recurring
  differentiated room-defense states strongly enough to form a sustained
  adaptation pattern.
- **ADV-0031 — White Plume Mountain:** **3 → 4**. The three weapon branches
  repeatedly impose materially different rules states across substantive
  traversal, creating sustained distributed mechanical adaptation without
  making that adaptation itself the defining progression structure.
- **ADV-0345 — Mad Wizard's Lair:** **5 → 4**. The AFAO 1.5 correction
  successfully removes the old false-negative trap at score 3, but source
  adjudication finds the resulting distributed differentiated-response pattern
  High rather than Extreme because mechanical adaptation shapes and enables
  progression without repeatedly becoming its defining operating structure.

The final adjudications retain **Call of the Wild = 1**, **House of Lament = 2**,
**Tomb of Horrors = 3**, **Trobriand's Graveyard = 3**, **Expedition to the
Barrier Peaks = 4**, **Doom of Ythryn = 4**, **Dead in Thay = 5**, and
**Obstacle Course = 5**. In particular, Tomb remains a score-3 negative control
because its many exact-rule mechanisms remain principally bespoke,
separately-resolved problems; Doom remains 4 because its accumulated Rite is a
continuing mechanical layer principally operated as a major gate rather than
repeatedly as the progression challenge; and Obstacle Course remains 5 because
mechanical interpretation and adaptation repeatedly constitute substantive
traversal and progression themselves.

After these adjudications, all five RSMD score levels retain empirical benchmark
coverage and no surviving blind disagreement requires further anchor or boundary
wording changes. The AFAO 1.5 RSMD rubric and benchmark ladder are therefore
frozen, corpus-calibrated, blind-validated, and source-adjudicated.

The calibration also establishes that a scene can contribute to both Puzzle /
Problem-Solving and Rules / System-Mastery Demand for different reasons. The
broader reasoning required to invent or discover a solution belongs to Puzzle /
Problem-Solving; the need to understand which rule, spell, ability, condition,
resource, interaction, state, or player-facing system actually works belongs
here. Exact mechanical gates do not by themselves make an adventure High when
they are too localized. Conversely, a persistent taught subsystem is not capped
below Extreme merely because its procedure becomes understandable or repeatable;
what matters is whether players must repeatedly retain and operate that
mechanical understanding as part of substantive challenge progression.

### 11. Structural Openness

**Definition:** How much freedom players have over the path, sequence, and order
through the adventure.

**Clarifications:**

- Structural Openness measures player freedom over **which substantial authored
  routes, objectives, locations, or scenes come next, and in what order**.
- It does **not** measure whether player choices substantially change events,
  relationships, states, or outcomes; that belongs to **Consequential Player
  Agency**. A branch can reconverge on the same later event or ending and still
  contribute to Structural Openness if players meaningfully chose among
  substantial routes, objectives, locations, or sequences.
- Structural Openness is distinct from **Exploration Emphasis**. A large
  environment can support extensive discovery, navigation, or traversal while
  still requiring a narrow mandatory progression. Conversely, an adventure can
  provide meaningful objective or branch ordering without exploration being a
  dominant mode of play.
- Alternative tactics or solutions **inside the same encounter or objective**
  do not by themselves increase Structural Openness. Fighting, sneaking,
  persuading, using a spell, or otherwise changing *how* a prescribed scene is
  resolved counts only when that choice meaningfully changes which substantial
  authored path, objective, location, or sequence follows.
- Openness may occur at different scales, including route selection through a
  site, player-selected ordering of locations or objectives, branch choice among
  substantial adventure segments, or campaign-scale wandering. Geographic size,
  room count, raw branch count, or GM-added side content are not themselves
  measures of Structural Openness.
- **Room-to-room routing counts when navigation itself constitutes substantial
  adventure progression**---when player choice determines which substantial
  authored areas, situations, or objectives are encountered and in what order.
  Merely choosing among adjacent rooms, side passages, or exits while pursuing
  the same prescribed objective and next major destination is fixed does not by
  itself increase Structural Openness.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Major progression is substantially prescribed; players have little meaningful freedom over which major objectives, locations, or scenes occur next or in what order. |
| **2 — Low** | Meaningful route, objective, or ordering choice occurs, but it is localized, shallow, highly constrained, or optional; most major progression remains prescribed. |
| **3 — Mixed** | Meaningful player-selected routes, objectives, or ordering recur across substantial portions of the adventure, but coexist with a significant fixed spine, mandatory sequence, or major gates. |
| **4 — High** | Player choice over routes, objectives, or sequence is a dominant structural feature across much of the adventure; fixed gates or a campaign spine remain, but they do not determine most of the journey. |
| **5 — Dominant** | The adventure is fundamentally organized around player-directed selection and ordering of substantial objectives, locations, or routes; no single prescribed sequence governs most expected play. |

**Status:** Frozen calibration rubric. The definition, clarifications, and anchors
above are locked for the current ontology version. Future changes to their
wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Structural Openness calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0288 — A Friend in Need**; **ADV-0200 — Lake Monster** |
| **2 — Low** | **ADV-0062 — No Honour Among Thieves**; **ADV-0053 — Call of the Wild** |
| **3 — Mixed** | **ADV-0034 — Tomb of Horrors**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0287 — House of Lament** |
| **4 — High** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0303 — Storm King's Thunder** |
| **5 — Dominant** | **ADV-0278 — Witchlight Carnival**; **ADV-0323 — Dungeon Level** |

Initial calibration applied the frozen anchors to the familiar eight Analysis
Validation Corpus cases. Because the original eight supplied neither a clean
score-1 nor a clean score-5 endpoint, a targeted search of the remaining AVC
cases identified **ADV-0288 — A Friend in Need** and **ADV-0200 — Lake Monster**
as the strongest plausible score-1 cases, and **ADV-0278 — Witchlight Carnival**
and **ADV-0323 — Dungeon Level** as the strongest plausible score-5 cases.
Full-source review placed all four at their proposed endpoints, so all four were
added to the working calibration set without changing the anchors or forcing a
particular score distribution.

Source-grounded pressure testing then examined all four adjacent boundaries
under the frozen wording. The **1/2** boundary distinguishes a substantially
prescribed progression from one containing at least one meaningful but bounded
choice among substantial authored routes, objectives, locations, or ordering.
Ordinary tactical, investigative, social, or room-level choices do not clear the
boundary when they leave the same prescribed objective and next major
destination intact. **ADV-0200 — Lake Monster** and **ADV-0288 — A Friend in
Need** anchor score 1; **ADV-0062 — No Honour Among Thieves** demonstrates score
2 through its localized but consequential Inner Vault room-selection problem.

The **2/3** boundary distinguishes one or a few localized or concentrated
structural choices from player-selected routes, objectives, or ordering that
**recur across substantial portions** of expected play. This pressure test moved
**ADV-0053 — Call of the Wild** from 3 to 2: its three-way quest choice controls
a substantial central segment, but it is essentially one major branch followed
by reconvergence rather than recurring openness. **ADV-0034 — Tomb of Horrors**
ultimately reaches 3 because developed route choices recur through substantial
portions of the tomb even though many routes are deceptive, punitive,
nonprogressing, or eventually constrained by mandatory gates.

The **3/4** boundary distinguishes recurring openness that coexists with a
significant fixed spine from openness that becomes a **dominant structural
feature across much of the adventure**. Fixed access gates or a late convergence
do not automatically cap an adventure at 3 if they do not determine most of the
journey. This distinction places **ADV-0262 — Lost Mine of Phandelver** and
**ADV-0287 — House of Lament** at 3, while **ADV-0040 — Expedition to the Barrier
Peaks**, **ADV-0277 — The Wild Beyond the Witchlight**, and **ADV-0303 — Storm
King's Thunder** reach 4.

The **4/5** boundary distinguishes dominant player-directed ordering within a
still-meaningful macrosequence from player-directed selection and ordering as
the adventure's **fundamental organizing structure**. A common entrance,
endpoint, clock, or light access gate does not by itself prevent score 5 when no
single prescribed sequence governs most expected play. **ADV-0278 — Witchlight
Carnival** and **ADV-0323 — Dungeon Level** provide different score-5
architectures: one explicitly supports freely ordered event/location selection,
while the other is an interconnected site whose substantial progression is
principally determined by player routing. **ADV-0277 — The Wild Beyond the
Witchlight** and **ADV-0303 — Storm King's Thunder** remain 4 because meaningful
campaign-scale gates and spines continue to shape substantial portions of their
journeys.

A subsequent twelve-adventure blind independent pass applied the frozen rubric
without access to prior Structural Openness scores, rationales, benchmark
assignments, pressure-test outcomes, or expected score distribution. It
independently reproduced **nine of the twelve then-working scores exactly**.
The three disagreements were all one-point upward shifts: **ADV-0288 — A Friend
in Need** at 2 rather than 1, **ADV-0034 — Tomb of Horrors** at 3 rather than 2,
and **ADV-0040 — Expedition to the Barrier Peaks** at 4 rather than 3.

Focused full-source adjudication treated all three disagreements as substantive.
**ADV-0034 — Tomb of Horrors** moved from 2 to 3 because its developed
alternative routes, loops, teleports, side sequences, and deceptive branches
recur broadly enough to satisfy the score-3 anchor even though successful
progress eventually narrows through strong mandatory gates. False, lethal, or
punitive routes are not excluded merely because they are poor choices; they count
when they create substantial authored sequences rather than merely raw,
immediate dead ends. This avoids using Lethality / Failure Severity as a proxy
for Structural Openness.

**ADV-0040 — Expedition to the Barrier Peaks** moved from 3 to 4 because
player-selected multi-level ship traversal and objective/location ordering
dominate much of expected play, while the strongest mandatory convergence occurs
late. The existing score-4 wording already allows meaningful gates so long as
they do not determine most of the journey, making this an application correction
rather than an anchor change.

**ADV-0288 — A Friend in Need** remains 1. Its published clue-and-location chain
governs the substantial rescue progression, while the blind score of 2 relied on
localized site routing inside that prescribed pursuit. The adjudication therefore
added the explicit room-to-room/site-routing clarification above: site navigation
counts when it is itself substantial adventure progression, but incidental local
routing toward the same fixed objective and next major destination does not.

After these adjudications, the blind pass agrees with **eleven of the twelve
final benchmark scores**. The sole remaining integer-score disagreement is
**ADV-0288 — A Friend in Need**, whose 1/2 ambiguity is now addressed by the
added clarification. The blind pass also surfaced several path-sensitivity
differences. Those flag disagreements are not used here to alter the integer
Structural Openness anchors or benchmark scores; path-sensitivity remains
governed by the common scoring principle and can be consolidated separately if
its cross-dimensional semantics require further refinement.

### 12. Consequential Player Agency

**Definition:** How substantially player decisions can alter events, relationships,
states, or outcomes.

**Clarification**

Consequential Player Agency measures how strongly the published adventure makes
**meaningful player decisions produce materially different consequences**.

A choice contributes when what the players decide changes something substantive
about subsequent play: what occurs, who survives or cooperates, how an NPC or
faction relates to the characters, what conditions or resources persist, what
later situations develop, or how the adventure ultimately resolves.

Consequential Player Agency is distinct from **Structural Openness**. Structural
Openness measures freedom over **which substantial route, objective, location,
or scene comes next and in what order**. Consequential Player Agency instead
measures **what becomes different because of what players decide**. A highly
open adventure can have low consequential agency if its branches repeatedly
reconverge without materially changing later states or outcomes. Conversely, a
largely prescribed sequence can have high consequential agency if decisions
made within that sequence persistently alter relationships, conditions, later
events, or the ending.

Consequential Player Agency is also distinct from **Lethality / Failure
Severity**. Severe consequences do not automatically imply high agency. Death,
resource loss, failed checks, or catastrophic outcomes matter here only insofar
as they are meaningfully responsive to player decisions and create
substantively different adventure states or outcomes. Merely making mistakes
dangerous does not establish consequential agency.

Likewise:

- **Immediate method is not necessarily consequence.** Choosing whether to
  fight, sneak, persuade, cast a spell, or use another tactic does not by itself
  increase this score if substantially the same adventure state follows.
- **Ordinary resource variation is not enough.** Losing hit points, spell slots,
  time, or treasure matters only when the published adventure makes that
  difference materially affect later play.
- **Random variation is not player agency.** Different outcomes created
  principally by dice, random tables, or scripted external events do not
  themselves increase the score merely because the resulting states differ.
- **GM-created responsiveness does not count as published agency.** Score
  substantially-as-published support for consequences, not the general ability
  of a skilled GM to make any player choice matter.
- **Ending count is not itself the measure.** Multiple endings are strong
  evidence only when they genuinely result from meaningful player decisions. A
  single major decision can still be highly consequential even if the adventure
  does not provide many formal endings.
- **Severity alone is insufficient.** A choice that can abruptly terminate play
  may be extremely consequential in the ordinary-language sense, but an
  isolated death, dead end, or TPK branch does not by itself establish sustained
  high Consequential Player Agency.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Player decisions primarily affect immediate method, detail, or flavor; major events, relationships, persistent states, and outcomes are substantially fixed or rapidly reconverge regardless of what players decide. |
| **2 — Low** | Meaningful decisions can produce localized or bounded differences in events, relationships, or states, but these consequences are limited, short-lived, optional, or largely reconverge; most major downstream developments and outcomes remain fixed. |
| **3 — Moderate** | Player decisions repeatedly produce substantive differences in events, relationships, or persistent states, **and/or a meaningful decision determines a major outcome**; consequences matter across significant portions of play, but substantial major developments still remain fixed or reconvergent. |
| **4 — High** | Consequential decisions are recurring and major across much of the adventure; player choices regularly alter persistent relationships, states, subsequent events, or outcomes and create materially different downstream play, though significant fixed developments or endpoints may remain. |
| **5 — Dominant** | Player decision and consequence are fundamental organizing features of the adventure; cumulative or repeatedly consequential choices substantially determine multiple major events, relationships, persistent states, or outcomes, such that materially different decision histories produce materially different adventure states or resolutions. |

**Status:** Frozen calibration rubric. The definition, clarification, and 1--5
anchors above are locked for the current ontology version. Full-source
calibration, adjacent-boundary pressure testing, blind independent validation,
and focused adjudication of substantive blind disagreements are complete. Future
changes to the wording or meaning require an explicit ontology revision and
revalidation against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during
Consequential Player Agency calibration. They illustrate application of the
rubric but do not redefine the score anchors; future adventures are scored
against the anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0031 — White Plume Mountain** |
| **2 — Low** | **ADV-0034 — Tomb of Horrors**; **ADV-0062 — No Honour Among Thieves**; **ADV-0053 — Call of the Wild**; **ADV-0287 — House of Lament** |
| **3 — Moderate** | **ADV-0262 — Lost Mine of Phandelver** |
| **4 — High** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0303 — Storm King's Thunder** |
| **5 — Dominant** | **ADV-0277 — The Wild Beyond the Witchlight** |

Initial calibration applied the frozen rubric to the familiar eight calibration
adventures. The first source-grounded placements were **ADV-0034 — Tomb of
Horrors** at 1, **ADV-0040 — Expedition to the Barrier Peaks** at 4,
**ADV-0053 — Call of the Wild** at 2, **ADV-0062 — No Honour Among Thieves** at
1, **ADV-0262 — Lost Mine of Phandelver** at 3, **ADV-0277 — The Wild Beyond
the Witchlight** at 5, **ADV-0287 — House of Lament** at 2, and **ADV-0303 —
Storm King's Thunder** at 3.

A blind independent pass then scored those same eight canonical units without
access to prior Consequential Player Agency scores, rationales, benchmark
assignments, boundary conclusions, or expected score distribution. It reproduced
**House of Lament** at 2, **Lost Mine of Phandelver** at 3, **Call of the Wild**
at 2, and **The Wild Beyond the Witchlight** at 5. It scored **Tomb of Horrors**
at 2 rather than 1, **No Honour Among Thieves** at 2 rather than 1, **Storm
King's Thunder** at 4 rather than 3, and **Expedition to the Barrier Peaks** at
3 rather than 4.

Focused full-source adjudication treated all four disagreements as substantive.
**Tomb of Horrors** moved 1→2 because kind treatment of the Siren and asking her
to accompany the party breaks her enchantment and creates a continuing authored
NPC/party state through the rest of the adventure. **No Honour Among Thieves**
moved 1→2 because accepting Nïniann's covert orbstone-substitution objective
changes the characters' objective state, equipment, and subsequent vault task.
**Storm King's Thunder** moved 3→4 because consequential decisions recur across
widely separated phases, including settlement-defense survivor states and later
Serissa/Hekaton outcomes. **Expedition to the Barrier Peaks** remained 4 rather
than the blind 3 because Aphelion provides a deeply integrated, recurring,
adventure-spanning reactive relationship/state system. No disagreement required
a change to the frozen rubric. After adjudication, seven of the eight final
scores agree with that initial blind pass.

The **2/3** boundary distinguishes localized or bounded consequential differences
from consequences that recur across significant portions of play, unless one
meaningful decision itself determines a genuinely major outcome. **House of
Lament** remains 2 because its largest spirit/climax divergence is selected by
the GM or randomly rather than caused by player choice, while **Lost Mine of
Phandelver** reaches 3 through repeated authored consequence threads. The
score-3 alternative is deliberately disjunctive: **one meaningful decision that
determines a major outcome can be sufficient for 3, but does not by itself
establish the recurrence and breadth required for 4 or 5**.

The **3/4** boundary distinguishes substantive consequences that matter across
significant portions of play from recurring major consequence structures across
much of the adventure. Score 4 does not require multiple independent channels:
**Storm King's Thunder** reaches 4 through multiple consequential threads across
a campaign, while **Expedition to the Barrier Peaks** reaches 4 through one
deeply integrated and repeatedly reactive Aphelion system. Fixed macro
progression does not cap an adventure at 3 when player decisions still create
materially different downstream play across much of the canonical unit.

The **4/5** boundary distinguishes recurring major consequential agency from
player decision-history itself becoming a fundamental organizing feature of the
adventure. **Expedition to the Barrier Peaks** and **Storm King's Thunder**
retain substantial fixed developments or endpoints despite major recurring
consequences. **The Wild Beyond the Witchlight** reaches 5 because accumulated
decision history is tracked and repeatedly carried forward across multiple
independent relationships, states, events, advantages, and resolution
conditions, so materially different histories produce materially different
later adventure states.

The initial eight supplied no defensible score-1 endpoint after blind
adjudication. A targeted validation-corpus search first identified
**ADV-0102 — Keyport in Danger** from *Sunken Isles* as a candidate, but a
subsequent catalog-boundary adjudication found that record did not represent the
complete discrete Week 2 playable adventure. The candidate was therefore removed
from calibration rather than allowing an invalid Adventure ID boundary to
anchor the scale; *Sunken Isles* records were excluded from further calibration
use pending separate boundary revalidation.

A new endpoint search outside *Sunken Isles* identified **ADV-0031 — White Plume
Mountain**. Full canonical-source falsification placed it at 1: its many
important player choices overwhelmingly alter route, puzzle resolution, method,
survival, access, or resources without the publication carrying those choices
forward into a substantively different authored relationship, persistent state,
later event, or outcome. A focused blind boundary pass independently reproduced
**White Plume Mountain** at 1 and **No Honour Among Thieves** at 2, while scoring
**Tomb of Horrors** at 1. The final Tomb-only adjudication retained 2 because the
blind assessment had omitted the decisive Siren interaction; the source
explicitly makes kind treatment plus asking her to accompany the party produce
a continuing companion/friend state through the remainder of the adventure.
This establishes the lower boundary without changing the rubric wording.

The final **1/2** interpretation is therefore that score 1 can contain abundant,
even high-stakes player choice when those choices principally govern route,
method, problem resolution, survival, or ordinary resources and then
substantially reconverge. Score 2 begins when at least one meaningful authored
player decision creates a substantive but localized or bounded difference in an
event, relationship, or persistent state. Such a consequence may be optional or
highly localized; rarity limits its weight toward higher scores but does not
make it disappear from the score-2 analysis.

### 13. Seriousness

**Definition:** How strongly the adventure's expected substantive table
experience is framed and sustained in an earnest or dramatic register rather
than a comic, playful, or lighthearted one.

Seriousness does **not** measure Darkness / Horror Intensity, lethality,
difficulty, or the objective scale of the stakes. An adventure can involve
horror, danger, death, or world-threatening events while remaining playful or
campy, and it can be highly serious without being horrific or especially dark.
Incidental jokes, eccentric characters, or moments of levity do not by
themselves make an otherwise earnest adventure less serious; likewise, isolated
dramatic stakes do not make a fundamentally playful adventure serious.

| Score | Meaning |
| ---: | --- |
| **1 — Playful** | The adventure is fundamentally comic, whimsical, playful, farcical, or lighthearted in its expected experience; earnest or dramatic material is absent, exceptional, or mainly serves as contrast. |
| **2 — Light** | A lighthearted or playful register predominates, but meaningful earnest or dramatic material recurs and matters. |
| **3 — Mixed** | Playful/lighthearted and earnest/dramatic registers are both substantial parts of the expected experience, or the adventure regularly moves between them without either clearly predominating. |
| **4 — Serious** | An earnest or dramatic register predominates and shapes most of the expected experience, while meaningful levity, playfulness, or comic material remains present. |
| **5 — Sustained Serious** | The adventure is fundamentally framed around a sustained earnest or dramatic experience; comic or playful material is rare, peripheral, or primarily serves as contrast rather than materially lightening the dominant register. |

**Status:** Frozen calibration rubric. The definition, clarification, and
1--5 anchors above were frozen unchanged for Pass 1 and retained unchanged
through endpoint search, full-source scoring, all four adjacent-boundary
pressure tests, a ten-case blind independent validation pass, and focused
full-source adjudication of the two resulting score disagreements. Seriousness
is now **frozen, corpus-calibrated, and blind-validated**. Future changes to the
definition, clarification, or anchor wording require an explicit ontology
revision and revalidation against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are the working reference exemplars produced
during Seriousness calibration. They illustrate application of the frozen
rubric but do not redefine the score anchors; future adventures are scored
against the anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Playful** | **ADV-0013 — A Conspiracy Most Cracked** |
| **2 — Light** | **ADV-0278 — Witchlight Carnival** |
| **3 — Mixed** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0062 — No Honour Among Thieves**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **4 — Serious** | **ADV-0053 — Call of the Wild**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0303 — Storm King's Thunder** |
| **5 — Sustained Serious** | **ADV-0034 — Tomb of Horrors**; **ADV-0287 — House of Lament** |

Pass 1 applied the frozen rubric to the familiar eight calibration adventures.
The initial placements were **ADV-0034 — Tomb of Horrors** at 4,
**ADV-0040 — Expedition to the Barrier Peaks** at 3, **ADV-0053 — Call of the
Wild** at 2, **ADV-0062 — No Honour Among Thieves** at 3,
**ADV-0262 — Lost Mine of Phandelver** at 4, **ADV-0277 — The Wild Beyond the
Witchlight** at 2, **ADV-0287 — House of Lament** at 5, and
**ADV-0303 — Storm King's Thunder** at 4. The original eight therefore supplied
no score-1 endpoint.

A targeted search of the full Analysis Validation Corpus identified
**ADV-0278 — Witchlight Carnival** as the strongest plausible score-1 candidate.
Full canonical-source falsification instead placed it at 2: the carnival's
whimsical register overwhelmingly predominates, but the recurring
Hourglass-Coven, disappearance, personal-loss, Zybilna, and Witch-and-Light
threads repeatedly become substantive player-facing dramatic business. Because
the AVC still supplied no defensible 1, a targeted full Adventure Master Catalog
search identified **ADV-0013 — A Conspiracy Most Cracked** as the strongest
candidate. A full section-by-section canonical-source review confirmed it at 1:
its burglary, travel hazards, Bounders, guard dog, possible embarrassment,
reputation consequences, and other potentially serious elements remain absorbed
into the same comic Hobbit-caper register rather than establishing a recurring
earnest counter-register.

Formal **1/2** pressure testing therefore established the distinction between
serious events that remain inside, exceptional to, or primarily contrastive
with a fundamentally playful register and a recurring earnest/dramatic
counter-register that becomes substantive play. **ADV-0013 — A Conspiracy Most
Cracked** anchors the former pattern. **ADV-0278 — Witchlight Carnival** reaches
2 because disappearance, loss, the coven, Zybilna, and the carnival owners'
predicament recur and matter despite overwhelmingly playful table activity. The
same pressure test initially retained **ADV-0053 — Call of the Wild** at 2, but
subsequent broader boundary testing corrected that application as described
below. The frozen 1/2 wording itself required no change.

The formal **2/3** pressure test corrected two lower-side applications while
retaining the frozen wording. **ADV-0277 — The Wild Beyond the Witchlight** moved
from 2 to 3 because fairy-tale whimsy remains pervasive while the hag-ruled
realms, trapped and exploited inhabitants, damaged Prismeer, and Zybilna's
imprisonment make the earnest register comparably substantial across the full
campaign. **ADV-0053 — Call of the Wild** moved from 2 to 4 rather than merely
3: its cozy village and festival material are meaningful, but the expected
adventure structure is predominantly earnest heroic play built around an
urgently threatened community, missing people, hostile gnolls, dangerous
wilderness problems, and a frost-wolf confrontation. **ADV-0040 — Expedition to
the Barrier Peaks** and **ADV-0062 — No Honour Among Thieves** remained 3. In
Barrier Peaks, lethal derelict-spacecraft danger coexists with recurring
authored absurd technological comedy; in No Honour, flamboyant festival/caper
play and serious timed-heist suspense are both substantial.

The **3/4** pressure test retained all then-current boundary cases. Score 3 is
anchored by adventures where playful/light and earnest/dramatic registers are
both substantial or alternate without either clearly predominating. Score 4
requires a clear tonal hierarchy: the earnest/dramatic register shapes most of
expected play while meaningful lighter material remains. **ADV-0053 — Call of
the Wild**, **ADV-0262 — Lost Mine of Phandelver**, and **ADV-0303 — Storm
King's Thunder** satisfy that pattern in different forms. Lost Mine sustains an
earnest rescue/community-threat spine while Phandalin's warm social material
and recurring comic characterization meaningfully lighten substantial portions
of play. Storm King's Thunder sustains epic heroic and political drama while
recurring eccentric, absurd, and grotesquely comic giant material remains a
meaningful secondary register.

The **4/5** pressure test produced one additional application correction:
**ADV-0034 — Tomb of Horrors** moved from 4 to 5. Its adversarial tricks,
mental-challenge framing, and the pleasure of surviving Acererak's mechanisms do
not themselves establish a comic/playful tonal register; treating game-like
challenge as playfulness would improperly use Puzzle / Problem-Solving
architecture as a proxy for Seriousness. The published canonical unit instead
sustains a malevolent, earnest deathtrap register without a meaningful secondary
light register. **ADV-0287 — House of Lament** remained 5: isolated authored
comic details can occur at score 5 when they are rare or peripheral and do not
materially lighten the sustained haunted-house register.

Across all four adjacent boundaries, the frozen rubric therefore remained
unchanged. The working boundary interpretation is that score 1 permits serious
stakes or consequences so long as they do not establish a recurring earnest
counter-register; score 2 requires such a counter-register to recur and matter
while light/playful framing still clearly predominates; score 3 requires both
registers to be substantial without a clear tonal hierarchy; score 4 requires
earnest/dramatic framing to predominate while meaningful lighter material
remains; and score 5 requires sustained earnest/dramatic framing with lighter
material only rare, peripheral, or primarily contrastive.

A subsequent **ten-case blind independent validation pass** applied the frozen
Seriousness rubric without access to prior Seriousness scores, benchmark
placements, calibration rationales, boundary-test outcomes, or adjudications.
The blind reviewer independently reproduced **8 of the 10 calibrated scores
exactly**: **ADV-0013 — A Conspiracy Most Cracked** at 1,
**ADV-0278 — Witchlight Carnival** at 2, **ADV-0040 — Expedition to the
Barrier Peaks**, **ADV-0062 — No Honour Among Thieves**, and
**ADV-0277 — The Wild Beyond the Witchlight** at 3,
**ADV-0303 — Storm King's Thunder** at 4, and **ADV-0034 — Tomb of Horrors**
and **ADV-0287 — House of Lament** at 5. The two disagreements were adjacent
boundary cases: the blind reviewer scored **ADV-0053 — Call of the Wild** at 3
rather than the calibrated 4 and **ADV-0262 — Lost Mine of Phandelver** at 5
rather than the calibrated 4.

Focused full-source adjudication retained **ADV-0053 — Call of the Wild** at
**4 — Serious**. Its cozy village and substantial festival material constitute
meaningful lighter play, but the expected adventure spine is predominantly
earnest heroic play: every principal branch centers on a substantive community
problem, all branches require dangerous wilderness intervention, and all
reconverge on the earnestly framed frost-wolf sequence before the celebratory
festival. The adjudication also established an application guardrail:
**friendly, cozy, hopeful, or welcoming material is not automatically
playful/lighthearted for Seriousness purposes**. The relevant question is
whether the authored lighter register itself becomes substantial enough to
remove the clear tonal hierarchy.

Focused full-source adjudication likewise retained
**ADV-0262 — Lost Mine of Phandelver** at **4 — Serious**. Its rescue,
community-threat, pursuit, and Wave Echo Cave spine is strongly earnest, but
the lighter register is more than rare or peripheral: a substantial central
Phandalin/Redbrand phase repeatedly uses authored comic or eccentric
player-facing material, including Carp Alderleaf, Harbin Wester, Droop,
intoxicated Redbrand knucklebones play, and Glasstaff's affected genteel
euphemisms. That material materially lightens a meaningful portion of expected
play while remaining clearly secondary to the dominant earnest register.

Neither blind disagreement exposed a defect in the frozen rubric, and neither
adjudication changed the calibrated benchmark placement. The blind pass
therefore produced **no post-blind benchmark-application corrections and no
rubric revisions**. The exercise instead reinforced the existing 3/4 and 4/5
boundaries: score 3 lacks a clear tonal hierarchy; score 4 has a clearly
predominant earnest/dramatic register while meaningful authored lighter
material remains; and score 5 requires that such lighter material be only rare,
peripheral, or primarily contrastive. The blind reviewer also correctly kept
horror, lethality, objective stakes, Fantastic Weirdness, and game-like
challenge analytically separate from Seriousness.


### 14. Darkness / Horror Intensity

**Definition:** How strongly the adventure's expected substantive table experience
exposes players to disturbing, frightening, horrific, grim, or emotionally dark
material.

Darkness / Horror Intensity measures the **presence, intensity, and sustained
experiential importance of dark or horrific material**, not whether the adventure
treats its events seriously. An adventure can be horrific but campy, playful, or
absurd, and can be completely serious without being particularly dark or
frightening.

Qualifying material can include, among other things:

- horror, dread, terror, or sustained menace;
- grotesque, macabre, or disturbing imagery;
- cruelty, suffering, corruption, or degradation;
- disturbing transformations or violations of bodily or mental integrity;
- death, undeath, possession, sacrifice, or similarly grim material when
  presented with meaningful dark weight;
- psychological horror, paranoia, helplessness, or emotional distress; and
- bleak or oppressive situations and themes.

Merely containing monsters, combat, danger, death, villains, or high stakes does
**not** by itself establish substantial Darkness / Horror Intensity. Likewise,
gothic imagery or nominal "horror" genre labeling matters only insofar as it
contributes to the adventure's expected substantive experience.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Dark, frightening, horrific, disturbing, or grim material is absent, exceptional, very mild, or largely decorative. The expected experience is fundamentally non-dark. |
| **2 — Low** | Meaningful dark or frightening material occurs and matters, but is limited, mild, intermittent, or clearly secondary to a predominantly non-dark experience. |
| **3 — Moderate** | Dark, disturbing, frightening, or grim material is a substantial recurring part of the expected experience, but does not consistently dominate it. |
| **4 — High** | Dark or horrific material strongly shapes much of the adventure's expected experience, with sustained menace, disturbing content, grimness, or horror recurring as a major experiential feature. |
| **5 — Extreme / Sustained Horror** | The adventure is fundamentally organized around a sustained disturbing, frightening, horrific, or intensely dark experience; such material pervades expected play rather than appearing merely as recurring episodes or themes. |

**Status:** Frozen calibration rubric. The definition, clarification, qualifying
material guidance, and 1--5 anchors above were frozen unchanged for Pass 1 and
retained unchanged through full-source scoring of the familiar eight calibration
adventures, pressure testing of all four adjacent boundaries, an eight-case blind
independent validation pass, and focused full-source adjudication of every blind
disagreement. Darkness / Horror Intensity is now **frozen, corpus-calibrated,
and blind-validated**. Future changes to the definition, clarification,
qualifying-material guidance, or anchor wording require an explicit ontology
revision and revalidation against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are the working reference exemplars produced
during Darkness / Horror Intensity calibration. They illustrate application of
the frozen rubric but do not redefine the score anchors; future adventures are
scored against the anchor meanings, not by relative similarity to these
examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0062 — No Honour Among Thieves** |
| **2 — Low** | **ADV-0053 — Call of the Wild**; **ADV-0040 — Expedition to the Barrier Peaks** |
| **3 — Moderate** | **ADV-0262 — Lost Mine of Phandelver**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0303 — Storm King's Thunder** |
| **4 — High** | **ADV-0034 — Tomb of Horrors** |
| **5 — Extreme / Sustained Horror** | **ADV-0287 — House of Lament** |

#### Calibration Record and Boundary Guidance

Pass 1 applied the frozen rubric to the familiar eight Analysis Validation
Corpus cases. The initial placements were **ADV-0062 — No Honour Among
Thieves** at 1, **ADV-0053 — Call of the Wild** at 2, **ADV-0040 — Expedition
to the Barrier Peaks** at 3, **ADV-0262 — Lost Mine of Phandelver** at 3,
**ADV-0277 — The Wild Beyond the Witchlight** at 3, **ADV-0303 — Storm King's
Thunder** at 3, **ADV-0034 — Tomb of Horrors** at 4, and **ADV-0287 — House of
Lament** at 5. The initial eight therefore populated all five score levels
without requiring an endpoint search outside the familiar calibration set.

Full-source pressure testing examined all four adjacent boundaries while keeping
the rubric frozen. The **1/2** boundary distinguishes danger, suspense,
threatening monsters, sinister objects, or catastrophic stakes that remain
exceptional or experiential background from material that creates a meaningful
recurring ominous, disturbing, frightening, or grim strand of play.
**ADV-0062 — No Honour Among Thieves** remains 1 because its soul-associated
weapon, isolated supernatural defenses, prophecy, traps, and possible lethal
outcomes occur inside a fundamentally non-dark festival/heist experience.
**ADV-0053 — Call of the Wild** reaches 2 because supported play can include a
bleak supernatural moor, disturbed burial cairns, a specter, predatory wilderness
menace, and related ominous material even though friendly Buckbridge play,
community-helping objectives, and the concluding festival keep darkness clearly
secondary overall.

The **2/3** boundary distinguishes darkness that is bounded, localized,
intermittent, or still clearly secondary from dark or horrific material that
becomes a **substantial recurring part of expected play across multiple
substantive phases**. **ADV-0262 — Lost Mine of Phandelver** reaches 3 because
murder, captivity, intended killing of prisoners, a flesh-eating nothic,
undead-haunted sites, corpse imagery, ghouls, zombies, a flameskull, and a wraith
recur across the Redbrand, regional-exploration, and Wave Echo Cave phases while
the adventure remains broad heroic fantasy rather than horror-dominant.

A later blind disagreement sharpened the lower side of that boundary.
**ADV-0040 — Expedition to the Barrier Peaks** initially received 3 because the
derelict vessel repeatedly contains the aftermath of mass death, killer mold,
corpses, biological grotesquerie, and machine menace. The blind reviewer instead
placed it at 2, and focused full-source adjudication accepted the blind
application. The original assessment had over-weighted the **recurrence of dark
facts and imagery** without sufficiently weighting their actual experiential
role. The adventure repeatedly converts the catastrophe into science-fantasy
discovery, alien ecology, technological experimentation, bizarre creatures,
and overt comedy. Recurring corpse, grotesque, or grim evidence is therefore
not sufficient for score 3 when qualifying darkness itself remains clearly
secondary to a predominantly non-dark experience.

The **3/4** boundary distinguishes substantial recurring darkness that continues
to share the adventure with extensive non-dark experiential registers from
darkness, menace, grimness, or horror that **strongly conditions most of the
substantive experience**. **ADV-0277 — The Wild Beyond the Witchlight** remains
3 because hag cruelty, loss, exploitation, corruption, and disturbing fairy-tale
material recur across Prismeer while wonder, whimsy, absurdity, eccentric social
play, and nonviolent fairy-tale problem solving remain comparably substantive.
**ADV-0303 — Storm King's Thunder** likewise remains 3 because cruelty,
captivity, predation, destruction, grotesquerie, and sinister cult material
recur across major campaign phases but coexist with enormous amounts of heroic
travel, exploration, politics, spectacle, and ordinary adventure. By contrast,
**ADV-0034 — Tomb of Horrors** reaches 4 because malevolent deathtrap framing,
macabre imagery, psychologically menacing deception, and supernatural threat
condition virtually the entire playable site rather than appearing as one
recurring register among several comparably substantial ones.

The **4/5** pressure test established that pervasiveness alone does not make an
adventure score 5. **ADV-0034 — Tomb of Horrors** remains 4 even though darkness
and menace saturate the tomb because substantive play is still fundamentally
organized around inspecting, interpreting, testing, and surviving Acererak's
adversarial puzzle/deathtrap architecture. Darkness strongly conditions that
activity without itself becoming the adventure's fundamental organizing
procedure. **ADV-0287 — House of Lament** reaches 5 because producing,
uncovering, escalating, confronting, and surviving the haunting **is itself the
organizing structure of the adventure**: exploration, séances, revelations,
awakening, entrapment, increasingly aggressive supernatural manifestations, and
the climax all operate as an escalating horror experience.

The working upper-boundary interpretation is therefore:

- **4 — High:** sustained darkness, horror, grimness, or menace strongly
  conditions most of the adventure, but substantive play remains fundamentally
  organized around another primary playable structure.
- **5 — Extreme / Sustained Horror:** creating, experiencing, uncovering,
  confronting, or surviving the dark or horrific condition is itself a
  fundamental organizing structure of the adventure.

This is **calibration guidance derived from the frozen anchors**, not replacement
anchor wording. Future scoring must continue to apply the normative score
meanings above rather than mechanically testing for a particular adventure
structure.

#### Blind Validation and Disagreement Adjudication

A subsequent **eight-case blind independent validation pass** applied the frozen
Darkness / Horror Intensity rubric without access to prior Darkness / Horror
scores, benchmark assignments, calibration rationales, boundary-test outcomes,
or adjudications. The blind reviewer independently reproduced **7 of the 8
then-current integer scores exactly**: **ADV-0062 — No Honour Among Thieves** at
1, **ADV-0053 — Call of the Wild** at 2, **ADV-0262 — Lost Mine of Phandelver**,
**ADV-0277 — The Wild Beyond the Witchlight**, and **ADV-0303 — Storm King's
Thunder** at 3, **ADV-0034 — Tomb of Horrors** at 4, and **ADV-0287 — House of
Lament** at 5. The sole score disagreement was **ADV-0040 — Expedition to the
Barrier Peaks**, scored 2 by the blind reviewer rather than the then-calibrated
3. The blind reviewer reported **no material rubric ambiguity**.

Focused full-source adjudication accepted the blind Barrier Peaks application
and moved the final benchmark from **3 to 2**. This was an application correction,
not a rubric correction: recurring dark content must be weighted by how strongly
it actually shapes expected experience rather than by its mere frequency or
presence in the source. After adjudication, the blind pass and final benchmark
set agree on **all eight integer scores**.

The blind pass also produced two path-sensitivity disagreements. For
**ADV-0277 — The Wild Beyond the Witchlight**, the calibrated flag changed from
Yes to **No** after adjudication. Different routes alter particular victims,
grotesqueries, bargains, confrontations, and local scenes, but the campaign-wide
mixture of dark fairy-tale material and substantial wonder/whimsy remains stable
enough that the Darkness / Horror experience is not materially path-sensitive.

For **ADV-0287 — House of Lament**, the blind reviewer proposed No, but focused
full-source adjudication retained **Path Sensitive: Yes**. The decisive evidence
is not merely which séance spirit is contacted. The published adventure supports
a meaningful state divergence between gradual dormant-house escalation and an
early awakened house whose horror becomes substantially more direct, aggressive,
and slasher-like. Both paths remain score 5, but path sensitivity does **not**
require supported paths to cross an integer boundary. The flag records
meaningful variation in the experience on the dimension, including variation
within an endpoint score.

The final working path-sensitivity judgments for the calibration set are:

| Adventure | Path sensitive? | Calibration note |
| --- | :---: | --- |
| **ADV-0062 — No Honour Among Thieves** | No | Dark material is isolated/localized within the same heist register. |
| **ADV-0053 — Call of the Wild** | Yes | Mutually exclusive quest paths materially vary exposure to supernatural/grave and ordinary wilderness menace. |
| **ADV-0040 — Expedition to the Barrier Peaks** | Yes | Traversal and Aphelion-related states can materially vary exposure to machine menace and darker derelict/biological material. |
| **ADV-0262 — Lost Mine of Phandelver** | Yes | Chapter 3 route selection materially varies undead/haunting exposure while the Redbrand and Wave Echo Cave phases preserve the score-3 baseline. |
| **ADV-0277 — The Wild Beyond the Witchlight** | No | Route details vary, but the campaign-scale darkness/whimsy mixture remains broadly stable. |
| **ADV-0303 — Storm King's Thunder** | Yes | Giant-lord choice materially changes the amount and character of cruelty, captivity, grotesquerie, and oppression encountered. |
| **ADV-0034 — Tomb of Horrors** | No | The tomb's sustained malevolent/macabre register is structurally stable across expected traversal. |
| **ADV-0287 — House of Lament** | Yes | Gradual haunting versus early awakened/slasher play materially changes horror intensity and presentation despite both remaining score 5. |

#### Application Guardrails

Several recurring false-positive and weighting patterns should be excluded in
future Darkness / Horror Intensity scoring:

- **Danger is not darkness.** Combat risk, traps, time pressure, powerful
  villains, or possible character death do not themselves establish a high
  Darkness / Horror score.
- **Lethality is not darkness.** A famously deadly adventure can remain low or
  moderate if death and failure are not presented with sustained disturbing,
  frightening, grim, or horrific experiential weight.
- **Seriousness is not darkness.** Earnest heroic drama can be non-dark, and
  horror can be campy, playful, or absurd. The dimensions must be scored
  independently.
- **Fantastic Weirdness is not darkness.** Bizarre, alien, surreal, or
  dreamlike material contributes only when it is actually presented with
  disturbing, frightening, horrific, grim, or emotionally dark weight.
- **Genre labels and gothic imagery are evidence, not scores.** A product can
  call itself horror or use haunted/gothic scenery without sustaining enough
  qualifying experience for a high placement.
- **Recurring dark facts are not automatically score 3.** Corpses, grim
  backstory, grotesque creatures, or catastrophic history can recur while
  remaining clearly secondary to a predominantly non-dark experiential frame,
  as demonstrated by the final Barrier Peaks adjudication.
- **Score the experienced material, not only the backstory.** Historical
  atrocities, dead populations, or villain lore matter in proportion to how
  strongly they become substantive player-facing experience.
- **Whimsy or comedy does not erase darkness automatically.** An adventure can
  sustain a score 3 or higher when dark material remains substantial despite
  recurring comic, whimsical, or absurd counter-registers.
- **Path sensitivity is independent of integer movement.** A supported path can
  materially intensify, soften, or alter the form of horror without changing
  the final 1--5 score; endpoint adventures can therefore still be
  path-sensitive.

Across full-source calibration, all four adjacent boundaries, blind independent
application, and focused disagreement adjudication, no surviving defect or
material ambiguity was found in the frozen Darkness / Horror Intensity rubric.

### 15. Fantastic Weirdness

**Definition:** How far the adventure departs from familiar/conventional fantasy
toward bizarre, surreal, dreamlike, or highly unusual material.

Fantastic Weirdness measures the **extent, recurrence, experiential dominance,
and structural centrality of convention-breaking fantastic material** in
expected substantive play. It does not measure the mere presence of magic,
monsters, Fey creatures, planar travel, horror, whimsy, spectacle, technology,
or unusual lore.

The following clarifications are normative application guidance for the frozen
rubric:

- **Fantasy is not automatically weird.** Dragons, giants, undead, magic,
  enchanted forests, demons, ruins, and other familiar fantasy material can be
  entirely conventional for D&D.
- **Rarity is insufficient.** A creature, location, object, or phenomenon is not
  Fantastic Weirdness merely because it is uncommon in the corpus or unusual
  within a particular setting.
- **Weirdness is not Darkness / Horror Intensity.** Bizarre, grotesque, alien,
  dreamlike, or reality-bending material contributes here because it departs
  from conventional fantasy expectations, not because it is frightening or
  disturbing.
- **Weirdness is not Seriousness.** Comic, playful, earnest, tragic, or absurd
  material can all be highly weird or entirely conventional.
- **Whimsy is not automatically weird.** Playfulness, fairy-tale imagery,
  colorful spectacle, and fanciful substitutions contribute only insofar as the
  actual player-facing phenomenon meaningfully departs from familiar fantasy
  expectations.
- **Science fiction and technology are not automatically score 5.** Their
  contribution depends on their extent, recurrence, experiential importance,
  and role in the adventure's playable identity.
- **Planar or exotic location is not automatically weird.** An unfamiliar plane
  can still support conventional fantasy play; score the reality and situations
  players substantively experience.
- **Weight player-facing experience over hidden bizarre lore.** Strange
  metaphysics, history, or explanations matter in proportion to how strongly
  they shape expected substantive play.

| Score | Meaning |
| ---: | --- |
| **1 — Conventional** | Adventure remains overwhelmingly within familiar fantasy conventions. Unusual elements, if present, are incidental, isolated, or readily understood through ordinary fantasy expectations. |
| **2 — Mildly Unusual** | Distinctive/unusual fantastic elements recur and matter, but most expected play still operates within recognizable conventional-fantasy assumptions. |
| **3 — Weird** | Bizarre, surreal, dreamlike, anachronistic, reality-bending, or otherwise highly unusual material is a substantial recurring part of the adventure alongside comparably substantial conventional fantasy material. |
| **4 — Highly Weird** | Fantastic weirdness is one of the adventure's dominant experiential characteristics. Players repeatedly encounter situations, environments, beings, or underlying realities that substantially depart from conventional fantasy expectations. |
| **5 — Fundamentally Weird** | Adventure fundamentally organized around bizarre, surreal, dreamlike, radically unfamiliar, or convention-breaking material. Sustained encounters with strange are central to playable identity; replacing most of that material with conventional fantasy would substantially transform the adventure. |

**Status:** Frozen calibration rubric. The definition, clarifications, and 1--5
anchors above were frozen unchanged for Pass 1 and retained unchanged through
full-source scoring of the familiar eight calibration adventures, targeted AVC
endpoint searches, pressure testing of all four adjacent boundaries, a nine-case
blind independent calibration pass, supplemental complete-source falsification
of candidate score-4 adventures, standalone blind tests of the disputed 4/5 and
3/4 candidates, and focused A/B/C adjudication of every integer-score blind
disagreement. Fantastic Weirdness is now **frozen, corpus-calibrated, and
blind-validated**. Future changes to the definition, clarification, or anchor
wording require an explicit ontology revision and revalidation against the
Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are the working reference exemplars produced
during Fantastic Weirdness calibration. They illustrate application of the
frozen rubric but do not redefine the score anchors; future adventures are
scored against the anchor meanings, not by relative similarity to these
examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Conventional** | **ADV-0053 — Call of the Wild**; **ADV-0062 — No Honour Among Thieves**; **ADV-0262 — Lost Mine of Phandelver**; **ADV-0303 — Storm King's Thunder** |
| **2 — Mildly Unusual** | **ADV-0185 — The Murkmire Malevolence**; **ADV-0287 — House of Lament** |
| **3 — Weird** | **ADV-0034 — Tomb of Horrors** |
| **4 — Highly Weird** | **ADV-0278 — Witchlight Carnival** |
| **5 — Fundamentally Weird** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0046 — Into Dreamland**; **ADV-0195 — Affair on the Concordant Express** |

#### Calibration Record and Boundary Guidance

Pass 1 applied the frozen rubric to the familiar eight Analysis Validation
Corpus cases. The initial placements were **ADV-0034 — Tomb of Horrors** at 4,
**ADV-0040 — Expedition to the Barrier Peaks** at 5, **ADV-0053 — Call of the
Wild** at 1, **ADV-0062 — No Honour Among Thieves** at 1, **ADV-0262 — Lost
Mine of Phandelver** at 1, **ADV-0277 — The Wild Beyond the Witchlight** at 5,
**ADV-0287 — House of Lament** at 3, and **ADV-0303 — Storm King's Thunder** at
2. Full-source lower-boundary testing subsequently moved **Storm King's
Thunder** from 2 to **1**, establishing that giants, dragons, exotic giant
strongholds, powerful magic, and spectacular fantasy situations remain
conventional when they operate through familiar heroic-fantasy assumptions.

The initial set left score 2 without a stable benchmark. A targeted full-AVC
search identified **ADV-0185 — The Murkmire Malevolence** as the strongest
candidate. Complete-source falsification placed it at **2 — Mildly Unusual**:
its museum-heist structure remains predominantly conventional, while the
eldritch egg creates recurring player-facing psychic and bodily distortions
that are central enough to matter but localized enough to remain secondary.
The later blind pass independently reproduced Murkmire at 2.

The **1/2** boundary therefore distinguishes isolated, incidental, or readily
conventionalized unusual material from an unusual fantastic strand that
**recurs and materially matters** while remaining clearly secondary to a
predominantly conventional-fantasy experience. Ordinary magic, monsters,
planar references, unusual treasure, or one spectacular set piece are not
sufficient by themselves.

The **2/3** boundary distinguishes recurring but still secondary weirdness from
weirdness that becomes a **substantial recurring experiential component**
alongside substantial conventional fantasy. **ADV-0287 — House of Lament** was
initially placed at 3 because its Domain-of-Dread metaphysics, collective
spirits, Entity, moving/overlaying reality, and other supernatural structure are
genuinely unusual. The blind reviewer instead scored it 2. Focused full-source
A/B/C adjudication found **A — the original AdventureFinder application was
wrong** and moved House of Lament to **2**. The original assessment had
substantially over-weighted familiar Gothic-haunting material and GM-facing
metaphysics relative to the player-facing experience, which remains primarily a
recognizable haunted-house adventure.

The same blind pass challenged the lower side of the **3/4** boundary by
scoring **ADV-0034 — Tomb of Horrors** at 3 rather than the initial 4. Focused
full-source adjudication again found **A — the original AdventureFinder
application was wrong**. Tomb contains repeated convention-breaking phenomena,
but substantial expected play remains conventional magical deathtrap/tomb
exploration: corridors, pits, secret doors, poison and fear effects, webs,
crypts, treasure traps, undead, and methodical dungeon probing. Weirdness is
therefore substantial and recurring alongside comparably substantial
conventional fantasy, making **3 — Weird** the calibrated placement.

A later search for a true score-4 benchmark tested several AVC candidates. Two
strong candidates falsified upward. **ADV-0046 — Into Dreamland** was tested
against the Tomb 3 and full-Witchlight 5 anchors and moved from prospective 4 to
**5 — Fundamentally Weird**. Its Great Vision is an equally real dream copy of
the temple; looping inhabitants, dream-state blessings and curses,
dream-shaped environments, death/return behavior, transformations, and the
physical manifestation of the dream copy make dream ontology part of what the
adventure fundamentally is rather than merely a dominant experiential texture.

**ADV-0195 — Affair on the Concordant Express** initially survived complete-
source review at 4, but a dedicated blind full-source assessment scored it 5.
Focused A/B/C adjudication found **A — the original AdventureFinder application
was wrong** and moved it to **5 — Fundamentally Weird**. The earlier 4
application had preserved only an abstract heist skeleton while under-weighting
that the sapient, treasure-burning, modron-operated interplanar train and its
reality-altering planar transitions constitute the principal authored site,
traversal structure, environmental behavior, encounter identity, and operating
reality of substantive play. Conventionalizing most of that material would
leave a generic prisoner-transport heist but would substantially transform the
adventure's playable identity.

The eventual score-4 candidate, **ADV-0278 — Witchlight Carnival**, received a
complete-source **Tomb 3 ↔ Carnival 4 ↔ full Witchlight 5** falsification and
was placed at 4. A subsequent dedicated blind review scored it 3. Focused A/B/C
adjudication found **B — the blind application was wrong** and retained
**4 — Highly Weird**. The blind review correctly discounted material that was
merely magical, Fey, whimsical, spectacular, or an unusual fantasy
substitution, but then applied that anti-proxy guidance too aggressively and
used recognizable activity forms such as races, rides, performances, games,
and social scenes as conventional-fantasy counterweight even where the actual
player-facing fictional experience remained bizarre. The Carnival's
mood-responsive reality, impossible physical construction, age/reflection
logic, dreamlike fear-demiplane, literalized hag-bargain transformation,
scale-changing Pixie Kingdom, spontaneous transformations, animate scenery,
and related phenomena make Fantastic Weirdness **one of the dominant
experiential characteristics** without making that weirdness fundamental to the
unit's playable identity.

The calibrated **3/4** distinction is therefore:

- **3 — Weird:** convention-breaking material is substantial and recurring,
  but substantial expected play also remains genuinely conventional in its
  player-facing fictional experience.
- **4 — Highly Weird:** convention-breaking material becomes **one of the
  dominant experiential characteristics** across expected play, even when the
  underlying activity forms remain familiar.

This is a qualitative weighting judgment, not a requirement that weirdness
constitute more than half of play or characterize virtually every scene.

The **4/5** boundary was pressure-tested repeatedly. A score-4 adventure can be
pervasively and dominantly weird while preserving a recognizable playable
identity if much of its convention-breaking material is replaced by
conventional fantasy. Score 5 requires the weirdness to be more constitutive:
**sustained convention-breaking material is central to what the adventure is in
play**, such that replacing most of it with conventional fantasy would
substantially transform its playable identity.

The calibrated upper-boundary interpretation is therefore:

- **4 — Highly Weird:** weirdness dominates repeated player-facing experience,
  but the adventure's operative situation and recognizable playable identity
  are not themselves substantially constituted by that weirdness.
- **5 — Fundamentally Weird:** weirdness is part of the adventure's fundamental
  operating reality, site, causal structure, progression, or other playable
  identity; conventionalizing most of it substantially transforms the
  adventure rather than merely making it less distinctive or memorable.

The replacement test must not be reduced to preservation of an abstract plot or
verb sequence. Nearly any adventure can retain a generic skeleton such as
“explore site,” “reach prisoner,” or “free ruler” after radical replacement.
The relevant question is whether the **substantive playable identity and
experienced operating reality** survive.

#### Blind Validation and Disagreement Adjudication

The initial **nine-case blind independent calibration pass** applied the frozen
Fantastic Weirdness rubric without access to prior scores, benchmark
assignments, calibration rationales, or expected results. It scored
**ADV-0185 — The Murkmire Malevolence** 2, **ADV-0034 — Tomb of Horrors** 3,
**ADV-0053 — Call of the Wild** 1, **ADV-0277 — The Wild Beyond the Witchlight**
5, **ADV-0062 — No Honour Among Thieves** 1, **ADV-0287 — House of Lament** 2,
**ADV-0040 — Expedition to the Barrier Peaks** 5, **ADV-0303 — Storm King's
Thunder** 1, and **ADV-0262 — Lost Mine of Phandelver** 1. It therefore
reproduced **7 of 9 then-current integer placements exactly** and disagreed only
on House of Lament and Tomb of Horrors. Focused full-source adjudication
accepted both blind corrections, producing **9/9 agreement** between the final
placements for that batch and the blind scores without changing the frozen
rubric.

Two later standalone blind tests directly pressure-tested the missing upper
benchmarks. The dedicated **Affair on the Concordant Express** blind review
scored it **5 rather than the then-calibrated 4**; focused adjudication accepted
the blind application and moved the final score to 5. The dedicated
**Witchlight Carnival** blind review scored it **3 rather than 4**; focused
adjudication rejected that application and retained the complete-source 4
because the reviewer had over-discounted qualifying weirdness occurring inside
recognizable carnival activities. These opposite-direction disagreements are
especially useful: Concordant tested and corrected the **upper edge of 4**,
while Carnival pressure-tested and ultimately preserved the **lower edge of 4**.

The supplemental score-5 benchmark **ADV-0046 — Into Dreamland** was established
through complete-source adjacent-anchor falsification rather than a separate
standalone blind reproduction. The dimension-level blind-validation claim rests
on the nine-case independent pass plus the later dedicated Concordant and
Carnival blind tests, which collectively pressure-tested every score level and
both sides of the narrow score-4 band.

No integer-score disagreement exposed a surviving defect in the frozen anchor
wording. Path-sensitivity disagreements from the blind work do not affect the
calibrated integer ladder and are not treated as unresolved numeric calibration
issues.

#### Application Guardrails

Several recurring false-positive and weighting patterns should be excluded in
future Fantastic Weirdness scoring:

- **“Not automatically weird” is an anti-proxy rule, not an exclusion rule.**
  Fey, whimsical, magical, technological, planar, horrific, or spectacular
  material must be assessed for what players actually experience. It should
  neither count merely because it belongs to one of those categories nor be
  discarded merely because it does.
- **Familiar activity structure does not make the fictional experience
  conventional.** Fighting, talking, racing, investigating, exploring, or
  riding an attraction can occur inside highly bizarre player-facing reality.
  At the 3/4 boundary, compare the prevalence and experiential weight of
  conventional versus convention-breaking **fictional experience**, not merely
  the familiarity of player verbs.
- **Do not require score 4 to be “most play” or “virtually the whole
  experience.”** The frozen anchor requires Fantastic Weirdness to be **one of
  the dominant experiential characteristics**. Several experiential
  characteristics can be dominant simultaneously.
- **Fantasy spectacle is evidence, not a score.** Dragons, giants, massive
  magic, impossible architecture, powerful artifacts, or exotic creatures can
  remain conventional fantasy when their role and causal logic fit familiar
  expectations.
- **Whimsy can qualify when the phenomenon itself is weird.** A pixie NPC or
  colorful magical performance may contribute little; independent reflections,
  literalized bargain transformations, emotion altering reality, or impossible
  scale/identity effects can contribute strongly even when playful or Fey in
  tone.
- **Technology and science-fiction imagery require extent and centrality.** A
  technological object, robot, firearm, or crashed vessel is not automatically
  score 5; sustained unfamiliar systems can reach 5 when they constitute the
  adventure's site and interaction logic, as in Expedition to the Barrier
  Peaks.
- **Planar travel or exotic location is not enough.** Score what the plane
  causes characters to substantively experience and how deeply that reality
  structures play.
- **Hidden metaphysics are weighted by player-facing consequence.** A bizarre
  explanation known mainly to the GM carries less weight than recurring
  reality-bending effects characters must experience and navigate.
- **The score-5 replacement test is about playable identity, not plot
  skeleton.** If conventionalization preserves only a generic objective or verb
  sequence while transforming the authored site, causal rules, traversal,
  encounter identity, or operating reality, score 5 can still be warranted.
- **Do not conflate weirdness with horror, seriousness, puzzle difficulty,
  tactical novelty, or rules novelty.** The same scene can contribute to more
  than one dimension for different reasons, but one dimension must not serve as
  a proxy for another.

Across full-source calibration, all four adjacent boundaries, targeted endpoint
searches, blind independent application, and focused disagreement adjudication,
no surviving defect or material ambiguity was found in the frozen Fantastic
Weirdness rubric.

### 16. GM Preparation Burden

**Definition:** How much work the GM ordinarily must perform **before play** to
run the adventure effectively.

Preparation includes reading and understanding upcoming material; identifying
relevant NPCs, locations, and events; understanding relationships and
dependencies; reviewing unusual mechanics or procedures; reconciling
information spread across the adventure; deciding among published options that
must be fixed before play; and making notes or organizational aids reasonably
needed to run the material effectively.

GM Preparation Burden does **not** measure invention, synthesis, reaction, or
adjudication beyond explicitly prepared material **during play**; that belongs
to GM Improvisation Demand. It also does not measure whether an inexperienced
GM can successfully perform the required preparation; that belongs to GM
Beginner Suitability.

#### Calibration Rules

- **Preparation burden is not adventure length.** A 200-page campaign is not
  automatically score 5, and a 10-page adventure is not automatically score 1.
  Score the work ordinarily necessary to run the canonical Adventure ID
  effectively, not raw page count or total reading volume merely because the
  adventure lasts longer.

- **Preparation burden is not improvisation demand.** An adventure can be easy
  to prepare while demanding substantial invention or reaction at the table;
  conversely, a high-preparation adventure can be explicit and well supported
  once play begins.

- **Preparation burden is not bad writing or beginner difficulty.** Dense
  organization, scattered dependencies, large casts, unusual systems, and
  advance branching can increase preparation burden. An inexperienced GM
  struggling with otherwise light preparation does not by itself make the
  adventure high-prep.

- **Score 1 does not mean zero preparation.** A brief but attentive read,
  compact localized procedures, and minor rules lookups can remain compatible
  with Minimal when the immediately relevant material is genuinely sufficient
  and little synthesis or organization is needed.

- **Alternatives need not interact to create score 3.** When substantially-as-
  published play requires several substantive alternatives to be ready before
  players select among them, the volume of significant upcoming material can
  itself create Moderate preparation burden even if the alternatives are
  cleanly compartmentalized.

- **Precision does not automatically create High preparation burden.** Exact
  traps, puzzle mechanisms, lethality, unusual adjudication, or neutral-referee
  demands can increase the amount of advance review required without by
  themselves establishing score 4. High still requires substantial overall
  advance preparation.

- **A consequential advance choice is not independently sufficient for score
  4.** Choosing among published options matters only insofar as it contributes
  to substantial overall advance preparation through broader dependencies,
  state management, cross-referencing, organization, or preparation work.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | The adventure can ordinarily be run effectively after very little advance work. A brief read or skim of the immediately relevant material is generally sufficient; important information is localized and the GM has little need to synthesize, organize, cross-reference, or make advance decisions. |
| **2 — Low** | Some deliberate prep is useful or expected, but the burden remains light. The GM should read the relevant material and may benefit from a small amount of note-taking, encounter review, or advance organization, but substantial synthesis or campaign-level understanding is unnecessary. |
| **3 — Moderate** | Effective play ordinarily requires meaningful advance preparation. The GM needs to understand several interacting elements, review significant upcoming material, and/or organize information before play, but the burden remains manageable without extensive reconstruction or campaign-wide mastery. |
| **4 — High** | Effective play ordinarily requires substantial advance preparation. The GM must understand or coordinate many interconnected elements, absorb a significant body of relevant material, make consequential advance choices, or create substantial organizational support from the published material. Running primarily from a short pre-session read is difficult. |
| **5 — Very High** | The adventure places exceptional preparation demands on the GM. Effective play ordinarily depends on extensive advance understanding, synthesis, cross-referencing, tracking, or organization across a large or unusually interconnected body of material. The GM is likely to need substantial preparation infrastructure or sustained advance mastery rather than ordinary session-by-session reading. |

**Status:** AFAO 1.6.1 candidate revision. The GM Preparation Burden definition,
calibration rules, and 1--5 score anchors remain unchanged from AFAO 1.6. This
revision changes only the **4/5 adjacent-boundary clarification** so that the
general blind-applicable wording is consistent with the already accepted
score-5 morphology of persistent cross-partition preparation infrastructure
inside a bounded adventure. No benchmark placement changes in this revision.
Acceptance of the revised 4/5 clarification requires targeted revalidation
before this version is frozen.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during GM
Preparation Burden calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0200 — Lake Monster** |
| **2 — Low** | **ADV-0288 — A Friend in Need** |
| **3 — Moderate** | **ADV-0034 — Tomb of Horrors**; **ADV-0053 — Call of the Wild**; **ADV-0062 — No Honour Among Thieves**; **ADV-0262 — Lost Mine of Phandelver** |
| **4 — High** | **ADV-0287 — House of Lament**; **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **5 — Very High** | **ADV-0303 — Storm King's Thunder**; **ADV-0032 — Dead in Thay** |

Initial full-source calibration applied the frozen Revision 1 rubric to the
familiar eight-adventure set, then searched the remaining Analysis Validation
Corpus for a score-1 endpoint and pressure-tested all four adjacent boundaries.
**ADV-0200 — Lake Monster** established the score-1 endpoint because its compact
procedures, minor lookups, and intelligent-monster resolution can genuinely be
run after a brief attentive read without meaningful synthesis or organization.

The initial blind independent pass reproduced **ADV-0062 — No Honour Among
Thieves** at 3, **ADV-0262 — Lost Mine of Phandelver** at 3, **ADV-0040 —
Expedition to the Barrier Peaks** at 4, **ADV-0277 — The Wild Beyond the
Witchlight** at 4, and **ADV-0303 — Storm King's Thunder** at 5. It disagreed on
**ADV-0200 — Lake Monster** (AdventureFinder 1 vs blind 2), **ADV-0034 — Tomb of
Horrors** (2 vs 4), **ADV-0053 — Call of the Wild** (2 vs 3), and **ADV-0287 —
House of Lament** (3 vs 4).

Focused full-source disagreement adjudication changed three AdventureFinder
applications and split the Tomb disagreement: **ADV-0034 — Tomb of Horrors**
moved 2→3 because the volume of precision-sensitive keyed mechanisms ordinarily
requires meaningful advance review, while the blind score 4 over-weighted
precision relative to substantial overall preparation; **ADV-0053 — Call of the
Wild** moved 2→3 because substantially-as-published one-shot play requires the
GM to be ready for three substantive player-selectable quest branches before
the choice is fixed; and **ADV-0287 — House of Lament** moved 3→4 because its
spirit selection, séance planning, Dormant/Awakened state, prepared hauntings,
revelation management, and climax dependencies together create substantial
advance preparation. **ADV-0200 — Lake Monster** remained at 1 because score 1
permits a brief attentive read and minor localized lookups rather than meaning
“zero preparation.” No score-anchor wording changed.

Those adjudications temporarily left score 2 without a benchmark. A targeted
AVC search identified **ADV-0288 — A Friend in Need**, and a complete canonical-
unit source analysis retained it at **2 — Low**: the GM benefits from a
deliberate read of the short mistaken-identity investigation and its few
cross-scene callbacks, but the publication supplies a single strongly authored
rescue chain, explicit clue fallbacks, and localized keyed encounters, keeping
synthesis and organization clearly light.

A supplemental blind lower-boundary pass then independently scored **ADV-0200 —
Lake Monster** 1, **ADV-0288 — A Friend in Need** 2, **ADV-0034 — Tomb of
Horrors** 3, and **ADV-0053 — Call of the Wild** 3, reproducing the repaired
**1↔2↔3** ladder **4/4** without being told the expected distribution. The same
pass also reproduced the final path-sensitivity judgments for those four cases.
This supplemental result validates both the score-1 interpretation that a brief
attentive read can still be Minimal and the score-2 distinction that light
whole-adventure familiarity can exceed skim-sufficient preparation without
becoming meaningful Moderate prep.

#### AFAO 1.6 Score-5 Benchmark Expansion and Blind Replication

A later length-independent Adventure Master Catalog search sought an additional
GM Preparation Burden score-5 morphology without assuming that Very High
preparation requires a full-book or campaign-length adventure. That search
identified **ADV-0032 — Dead in Thay** as the strongest compact upper-end
candidate because its Doomvault structure combines publisher-supported
partitioning with a persistent cross-partition preparation-management layer.

A dedicated pristine blind full-source assessment then applied only the frozen
GM Preparation Burden rubric and the canonical **Dead in Thay** source unit,
without access to prior AdventureFinder GM Preparation Burden scores, benchmark
placements, calibration outcomes, expected values, model results, candidate-
search conclusions, or outside sources. The independent reviewer assessed
**ADV-0032 — Dead in Thay = 5 — Very High**, with **94% confidence** and
**Path Sensitive: No**.

The blind review explicitly tested the strongest score-4 alternative. The
Doomvault is helpfully divided into nine sectors and four zones per sector, so a
score-4 reading is plausible if ordinary preparation can be reduced to the
forthcoming sector or zone plus modest continuity. The reviewer nevertheless
found that the published structure does not reset cleanly at those boundaries.
Effective preparation requires a durable Doomvault-wide operating model that
carries forward and interacts across otherwise bounded units, including:

- zone-specific and multi-attuned **glyph-key** access;
- white- and black-gate connectivity and accumulated nonlocal movement options;
- contact-stone attunement state and the exceptional keys required for the
  Temples of Extraction;
- explicitly recorded changed-area state, including explored rooms, defeated
  monsters, undiscovered secrets, removed treasure, and other alterations;
- a dungeon-wide **Alert Level** that changes with time and affects later random
  encounter procedures;
- encounter consequences and relocated or surviving creatures that can affect
  later play outside their original keyed locations;
- cross-Doomvault endgame progression requiring **six black gates in other
  sectors to be disrupted simultaneously** before the Temples can provide
  access to the Phylactery Vault; and
- a separately demanding Phylactery Vault preparation package whose unusual
  four-orientation gravity structure must be understood after those distributed
  prerequisites are satisfied.

The decisive 4/5 discriminator is therefore not publication length, raw dungeon
size, or the mere presence of many keyed areas. It is that ordinary
session-by-session preparation cannot reliably discard the accumulated
cross-Doomvault access, state, and progression model. The GM benefits
materially from sustained preparation infrastructure or advance mastery across
the canonical unit even though individual encounter content is publisher-
segmented.

This blind replication adds **Dead in Thay** as a second empirical score-5
benchmark alongside **Storm King's Thunder** and demonstrates a distinct compact
score-5 morphology: **persistent cross-partition preparation infrastructure
inside a bounded adventure**. It also directly reinforces the frozen anti-proxy
rule that GM Preparation Burden is not adventure length.

At AFAO 1.6, this benchmark expansion did not change the definition, calibration
rules, score anchors, or adjacent-boundary wording. Subsequent clean
benchmark-blind application exposed a narrower wording defect in the inherited
4/5 clarification: its references to **cross-campaign** understanding and a
**campaign-management layer** could be read as requiring campaign scale even
though the accepted score-5 anchor and Dead in Thay replication explicitly
permit a bounded but unusually interconnected canonical unit. AFAO 1.6.1
therefore corrects only that adjacent-boundary clarification. The definition,
calibration rules, score anchors, and benchmark placements remain unchanged.

The calibrated adjacent boundaries are therefore:

- **1/2 — skim-sufficient vs deliberate light preparation.** Score 1 permits a
  brief attentive read and minor localized procedures; score 2 begins when the
  GM ordinarily benefits from some preparation beyond that immediate read,
  such as light whole-unit familiarity, modest encounter review, note-taking,
  or organization.
- **2/3 — light preparation vs meaningful preparation.** Score 2 remains
  compact and easily managed; score 3 begins when significant upcoming
  material, recurring precision-sensitive mechanisms, several substantive
  alternatives, or interacting elements ordinarily require meaningful advance
  review or organization.
- **3/4 — meaningful but bounded prep vs substantial prep.** Score 3 remains
  manageable without extensive reconstruction or broad mastery; score 4 begins
  when the GM must absorb or coordinate enough material, dependencies, states,
  or advance tasks that relying primarily on a short pre-session read becomes
  unreliable.
- **4/5 — substantial but meaningfully partitionable prep vs sustained
  preparation infrastructure or mastery.** Score 4 can still be prepared in
  bounded sites, chapters, or publisher-supported segments whose preparation is
  largely independent once the relevant segment is known. Score 5 begins when
  effective play ordinarily requires sustained **cross-unit** understanding,
  synthesis, cross-referencing, state or dependency tracking, organization, or
  advance mastery that must persist across otherwise bounded preparation units
  and functions as an ongoing **preparation-management layer**. A bounded or
  self-contained canonical adventure can satisfy score 5; adventure length,
  campaign format, a bespoke tracking artifact, or simultaneous preparation of
  every possible branch is not required. Conversely, persistent state, a
  tracker, or callbacks alone do not establish score 5 when the substantive
  preparation remains meaningfully partitionable into largely independent
  upcoming units.

Calibration reaffirms that GM Preparation Burden must remain analytically
separate from adventure length, GM Improvisation Demand, GM Beginner
Suitability, Rules / System-Mastery Demand, Puzzle / Problem-Solving Emphasis,
and Lethality / Failure Severity. The calibrated result is the amount and
character of **pre-play work itself**, not how difficult the material is to
adjudicate or how much experience the GM possesses.

Across full-source calibration, score-endpoint search, all four adjacent-
boundary pressure tests, the initial blind independent pass, focused
source-grounded disagreement adjudication, replacement score-2 search and full-
source falsification, the supplemental 4/4 blind lower-boundary pass, and the
AFAO 1.6 pristine blind score-5 replication of **Dead in Thay**, no surviving
defect or material ambiguity was found in the GM Preparation Burden **score
anchors** themselves. AFAO 1.6.1 corrects the narrower under-generalization in
the 4/5 adjacent-boundary clarification described above. That clarification
change is pending targeted revalidation before AFAO 1.6.1 is accepted and
frozen.

### 17. GM Improvisation Demand

**Definition:** GM Improvisation Demand measures how much substantive play
requires the GM, at the table, to supply, extend, connect, or adjudicate
material that the published adventure does not sufficiently specify in
advance.

The core assessment question is:

> **During expected substantive play, how often and how consequentially must the
> GM create or resolve missing material at the table rather than primarily
> selecting, presenting, and applying material the adventure already provides?**

This dimension measures **runtime responsibility for substantive playable
material**, not merely how open the adventure is, how creative the players can
be, how difficult the adventure is to prepare, or how much ordinary description
and characterization the GM performs.

#### What Counts

Count substantive **at-the-table** demands such as:

- inventing NPC responses, motives, information, or consequences beyond useful
  published support;
- creating connective events or content because players pursue directions the
  adventure permits but does not substantively develop;
- synthesizing scattered published information into a playable response the
  text does not itself provide;
- extrapolating locations, factions, situations, or world states;
- adjudicating open-ended situations for which the adventure supplies goals or
  context but little practical resolution support;
- maintaining a reactive situation whose behavior must substantially emerge
  from player action rather than prepared branches; and
- making consequential rulings because the published material deliberately or
  practically leaves important details unresolved.

**Synthesis can count even when the ingredients being synthesized are
published.** An adventure can contain extensive locations, NPCs, factions,
motives, threats, encounters, tables, and procedures while still imposing very
high improvisation demand if it leaves the GM wide latitude to determine how
those ingredients combine into consequential playable situations during
ordinary play.

#### What Does Not Count by Itself

- **Preparation is not improvisation.** Advance reading, organization,
  annotation, encounter study, or restructuring belongs primarily to **GM
  Preparation Burden**. The relevant demand here occurs at the table.
- **Openness is not improvisation.** Structural freedom creates opportunities
  for unexpected play, but an open adventure can remain low-demand when the
  publication sufficiently specifies locations, actors, states, and responses.
- **Agency is not improvisation.** Players can make highly consequential
  choices among sufficiently specified branches, states, or outcomes.
- **Rules complexity is not improvisation.** Applying difficult published
  mechanics belongs primarily to **Rules / System-Mastery Demand**. Only
  substantive unresolved adjudication contributes here.
- **Ordinary roleplaying is not enough.** Phrasing dialogue, portraying a
  supplied personality, describing actions, and conversationally reacting do
  not count unless the GM must construct substantive information, consequences,
  or playable responses beyond useful published support.
- **Sparse publication is not automatically high improvisation demand.** A
  short or incomplete adventure scores highly only when ordinary substantially-
  as-published play actually expects the GM to supply the missing substance at
  runtime.
- **Optional embellishment is not demand.** Invitations to add encounters,
  atmosphere, foreshadowing, complications, or other material “if desired” do
  not raise the score unless ordinary published play actually depends on those
  additions.
- **Genre affordance is not demand.** Heists, mysteries, sandboxes, social
  adventures, and other forms may invite creative player action, but the genre
  itself does not establish how much unsupported runtime construction the GM
  must perform.

Published ingredients are therefore not automatically equivalent to specified
playable responses, but neither does the presence of a reactive actor or an
open choice automatically establish missing playable substance. The assessment
must examine what the publication actually gives the GM to execute likely
responses.

| Score | Meaning |
| ---: | --- |
| **1 — Minimal** | Expected substantive play is unusually well specified. The GM mostly presents, selects, and applies provided material. Ordinary description/dialogue aside, substantive invention, extrapolation, or unsupported adjudication is rare and readily avoidable. |
| **2 — Low** | Some substantive situations require modest extrapolation or invention, but these demands are bounded, occasional, or low-consequence. Published material normally gives the GM enough structure to recover quickly. |
| **3 — Moderate** | Improvisation is a recurring part of running the adventure. Meaningful stretches require the GM to synthesize, extrapolate, invent responses, or resolve underspecified situations, but substantial published support still constrains and carries play. |
| **4 — High** | Successful ordinary play regularly depends on substantial **at-the-table** invention, synthesis, extrapolation, or adjudication. Adventure supplies important foundations, but GM is **regularly** responsible for turning those foundations into playable responses/consequences. |
| **5 — Very High** | Significant improvisation is routinely expected in running the adventure. The published adventure supplies important content and constraints, while the GM is expected to exercise wide latitude in regularly synthesizing, extending, connecting, or resolving that material into consequential playable situations in response to player action. Large portions of ordinary play are expected to be carried by that runtime synthesis rather than primarily by explicitly specified responses or sequences. |

**Status:** Frozen calibration rubric. The Revision 2 definition, interpretation,
and 1--5 anchors above are locked for the current ontology version. Future
changes to their wording or meaning require an explicit ontology revision and
revalidation against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during GM
Improvisation Demand calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Minimal** | **ADV-0034 — Tomb of Horrors**; **ADV-0053 — Call of the Wild** |
| **2 — Low** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0062 — No Honour Among Thieves**; **ADV-0262 — Lost Mine of Phandelver** |
| **3 — Moderate** | **ADV-0287 — House of Lament**; **ADV-0277 — The Wild Beyond the Witchlight** |
| **4 — High** | **ADV-0303 — Storm King's Thunder** |
| **5 — Very High** | **ADV-0068 — Curse of Strahd** |

#### Adjacent-Boundary Guidance

The calibrated adjacent boundaries are:

- **1/2 — rare/readily avoidable vs genuine bounded missing substance.** Score 1
  applies when substantive invention beyond ordinary presentation is rare and
  readily avoidable. Score 2 begins when ordinary play contains some genuine
  substantive extrapolation or invention, but the demand remains occasional,
  bounded, or low-consequence and the GM normally returns quickly to specified
  material.
- **2/3 — bounded demand vs recurring operating demand.** Score 2 contains real
  improvisation without making it a recurring operating requirement. Score 3
  begins when meaningful substantive synthesis, extrapolation, invented
  response, or underspecified resolution recurs as an ordinary part of running
  the adventure.
- **3/4 — publication-carried play vs regular dependency.** Score 3 still has
  substantial published playable material carrying most ordinary play despite
  recurring improvisational episodes. Score 4 begins when successful ordinary
  play **regularly depends** on substantial at-the-table invention, synthesis,
  extrapolation, or adjudication and the GM regularly must turn published
  foundations into the actual playable response or consequence.
- **4/5 — regular high demand vs runtime synthesis carrying large portions of
  play.** Score 4 can contain extended high-improvisation phases while
  sufficiently specified material still carries substantial portions of
  expected play. Score 5 begins when the GM is routinely expected to exercise
  sufficiently wide latitude that runtime synthesis itself carries large
  portions of ordinary substantive play.

#### Score-5 Interpretive Guardrail

Score 5 does **not** require the adventure to be sparse, incomplete, a toolkit,
or mostly authored by the GM. A richly detailed published adventure can score
5. The relevant distinction is between **specified content** and **sufficiently
specified play**.

An adventure may provide extensive locations, NPCs, factions, motives, threats,
encounters, tables, and procedures while nevertheless expecting the GM to
exercise wide latitude in determining how those elements interact, develop,
respond, and become consequential playable situations after player intervention.

Therefore:

> **Do not ask whether the GM must “invent the adventure.” Ask how much of the
> adventure's actual substantive play must be synthesized at the table from the
> material the publication supplies.**

For difficult 4/5 cases, apply the **specified-material counterfactual**:

> **If the GM deliberately minimized substantial runtime invention and synthesis
> wherever the publication did not explicitly specify a response, could expected
> ordinary play still realize the adventure's intended form without significant
> degradation?**

For **4**, the adventure may become more rigid, less responsive, or less
satisfying, but sufficiently specified material still carries substantial
portions of ordinary play. For **5**, minimizing that synthesis cuts against a
major way the publication expects ordinary play to develop: large portions of
play depend on the GM exercising wide latitude to transform supplied material
into consequential situations in response to the players. This is **not** a
test of whether the adventure remains technically runnable or recognizable.

The calibrated upper boundary is exemplified by **ADV-0303 — Storm King's
Thunder** at 4 versus **ADV-0068 — Curse of Strahd** at 5. *Storm King's
Thunder* contains substantial and sometimes extended open-world runtime
construction, especially during the Savage Frontier phase, but that demand is
concentrated and repeatedly gives way to strongly authored sequences and sites.
*Curse of Strahd*, by contrast, overlays its extensive keyed content with a
campaign-wide reactive Strahd/PC relationship and evolving world state for which
the GM must persistently synthesize Strahd's goals, intelligence, mobility,
resources, and accumulated player actions into consequential interventions.
Reducing that synthesis leaves the campaign technically playable but
significantly degrades an intended campaign-wide operating mode.

#### Post-Blind Application Guardrails

Blind independent validation and focused source-grounded adjudication established
four additional application guardrails without changing the frozen anchors:

1. **Information-bearing roleplay can count.** Ordinary characterization,
   phrasing, and conversational texture do not count. Recurring open
   interactions do count when the publication requires the GM to construct
   substantive information-bearing answers or consequences from supplied facts
   and constraints. This distinction moved **ADV-0287 — House of Lament** from
   2 to 3 because its repeated séances require substantive answers to
   player-generated questions rather than merely delivery of fixed dialogue.
2. **Recurring reactivity is not automatically recurring improvisation.** A
   persistent actor can remain low-demand when the publication sufficiently
   specifies tasks, state transitions, practical responses, recovery
   mechanisms, and encounter behavior. This retained **ADV-0040 — Expedition to
   the Barrier Peaks** at 2 against a blind 3 despite Aphelion's campaign-long
   reactive role.
3. **Genre affordance is not improvisation demand.** A heist's invitation to
   clever plans does not establish score 3 unless ordinary expected play
   repeatedly forces the GM beyond useful published support. This moved
   **ADV-0062 — No Honour Among Thieves** from 3 to 2 because its maps, timer,
   defenses, keyed vault, and encounter structure normally keep unexpected
   plans bounded; the much less specified prison-break failure continuation is
   path-sensitive rather than baseline-determining.
4. **Optional embellishment is not improvisation demand.** Explicit invitations
   to add encounters, foreshadowing, atmosphere, or other enrichment do not
   establish score 2 when the supplied adventure itself is complete enough to
   run without them. This moved **ADV-0053 — Call of the Wild** from 2 to 1.

#### Calibration and Blind Validation Record

Initial Revision 1 calibration against the familiar eight placed **ADV-0034 —
Tomb of Horrors** at 1; **ADV-0040 — Expedition to the Barrier Peaks**,
**ADV-0053 — Call of the Wild**, **ADV-0262 — Lost Mine of Phandelver**, and
**ADV-0287 — House of Lament** at 2; **ADV-0062 — No Honour Among Thieves** and
**ADV-0277 — The Wild Beyond the Witchlight** at 3; and **ADV-0303 — Storm
King's Thunder** at 4. A targeted AVC and full Adventure Master Catalog endpoint
search found no defensible score-5 benchmark under the original Revision 1
wording.

That endpoint failure exposed a conceptual discontinuity in the original 4/5
model: score 5 had effectively required improvisational construction to be
“fundamental to how the adventure functions,” which risked selecting scenario
frameworks or barely specified products rather than the high end of runtime
improvisational responsibility within a fully published adventure. Revision 2
therefore retained the lower construct while redefining the upper endpoint
around **wide GM latitude and runtime synthesis carrying large portions of
ordinary play**, rather than requiring the GM to invent the adventure itself.

A complete-source Revision 2 review of **ADV-0068 — Curse of Strahd** moved it
from the prior Revision 1 score 4 to **5 — Very High**. A dedicated blind
full-source review independently reproduced score 5, the path-sensitivity
judgment, the closest alternative of 4, and the decisive specified-material
counterfactual. A subsequent full-source **Storm King's Thunder 4 ↔ Curse of
Strahd 5** pressure test confirmed the revised upper boundary without changing
the anchors.

A nine-case blind benchmark pass then produced exact integer agreement on
**ADV-0034 — Tomb of Horrors** 1, **ADV-0262 — Lost Mine of Phandelver** 2,
**ADV-0277 — The Wild Beyond the Witchlight** 3, **ADV-0303 — Storm King's
Thunder** 4, and **ADV-0068 — Curse of Strahd** 5. It disagreed on four lower
cases: **ADV-0287 — House of Lament** (AdventureFinder 2 vs blind 3),
**ADV-0040 — Expedition to the Barrier Peaks** (2 vs 3), **ADV-0062 — No Honour
Among Thieves** (3 vs 2), and **ADV-0053 — Call of the Wild** (2 vs 1).

Focused full-source adjudication accepted the blind correction for **House of
Lament** 2→3, rejected the blind increase for **Expedition to the Barrier
Peaks** and retained it at 2, accepted **No Honour Among Thieves** 3→2, and
accepted **Call of the Wild** 2→1. No adjudication required a rubric-wording
change. After adjudication, eight of the nine final benchmark integer placements
match the blind batch result; the sole surviving score disagreement is
*Expedition to the Barrier Peaks*, retained at 2 on source-grounded grounds.

The final calibrated ladder is therefore:

**Tomb of Horrors / Call of the Wild 1 → Expedition to the Barrier Peaks / No
Honour Among Thieves / Lost Mine of Phandelver 2 → House of Lament / The Wild
Beyond the Witchlight 3 → Storm King's Thunder 4 → Curse of Strahd 5.**

Calibration reaffirms that GM Improvisation Demand must remain analytically
separate from GM Preparation Burden, Structural Openness, Consequential Player
Agency, Rules / System-Mastery Demand, ordinary roleplaying, adventure length,
genre, and perceived adventure quality. Across Revision 2 endpoint testing,
upper-boundary full-source pressure testing, blind independent application, and
all four focused disagreement adjudications, no surviving defect or material
ambiguity was found in the frozen GM Improvisation Demand anchors.

### 18. Player Beginner Suitability

**Definition:** How well the adventure supports inexperienced players in
understanding objectives, making meaningful choices, learning expected modes of
play, and participating successfully.

Player Beginner Suitability measures the **fit between the published playable
experience and players who have little or no prior D&D experience**. It does not
measure whether the adventure is easy in an absolute sense, whether the GM is
inexperienced, or whether the adventure teaches the game through explicit
tutorial text alone.

A beginner-suitable adventure gives inexperienced players a reasonable basis
for understanding **what they are trying to accomplish, what kinds of actions
are available to them, how their choices affect play, and how to recover and
continue when their first attempts are imperfect**.

#### Calibration Rules

- **Low Rules / System-Mastery Demand is not automatically high Beginner
  Suitability.** An adventure can require little mechanical mastery while still
  confronting new players with unclear objectives, opaque assumptions, poorly
  signposted choices, or unfamiliar modes of play. Conversely, an adventure can
  introduce meaningful mechanical complexity while supporting beginners through
  clear context, progressive exposure, and forgiving opportunities to learn.

- **Difficulty and lethality are evidence, not proxies.** Challenging encounters
  or meaningful consequences do not automatically make an adventure unsuitable
  for beginners. They matter when inexperienced players are likely to suffer
  severe consequences **before they have had a reasonable opportunity to
  understand what is expected of them or learn from prior feedback**.

- **Clear objectives matter, but linearity is not required.** A structurally
  open adventure can be highly suitable for beginners when players receive
  understandable goals, actionable options, useful feedback, and manageable
  decision contexts. Structural Openness itself must not determine this score.

- **Meaningful choice is preferable to either helplessness or undirected
  freedom.** Beginner support is strongest when players can make genuine
  decisions while having enough information to understand the immediate problem
  and plausible courses of action.

- **Learning through play counts.** An adventure need not contain explicit
  tutorial text. Repeated situations that naturally introduce expected modes of
  play, demonstrate consequences, provide feedback, or progressively broaden
  player responsibility can support beginners.

- **Do not assume an expert GM will repair the adventure.** Score the player
  experience substantially as published under competent ordinary GMing. Do not
  increase the score because an experienced GM could rewrite unclear material,
  heavily coach the players, remove punishing elements, or construct a bespoke
  tutorial.

- **Do not score GM support here.** Read-aloud guidance, encounter organization,
  prep assistance, adjudication advice, and other GM-facing usability features
  contribute to Player Beginner Suitability only insofar as they materially
  produce a better supported **player-facing experience**. Their usefulness to
  an inexperienced GM belongs primarily to GM Beginner Suitability.

- **Player age and content appropriateness are outside this dimension.**
  “Beginner-friendly” is not the same as child-friendly, family-friendly, or
  suitable for a particular age group.

| Score | Meaning |
| ---: | --- |
| **1 — Poor** | The adventure is poorly suited to inexperienced players. Expected play substantially assumes prior familiarity with D&D conventions, leaves important objectives or actionable choices opaque, or exposes beginners to recurring situations where they are unlikely to understand what effective participation requires before serious setbacks occur. Significant player coaching or adaptation is ordinarily needed. |
| **2 — Challenging** | Beginners can participate, but meaningful recurring features of the adventure are difficult to navigate without prior experience. Objectives or immediate choices may usually be understandable, yet unfamiliar expectations, weak feedback, abrupt complexity, or unforgiving situations regularly create friction. Active GM guidance is likely to be important. |
| **3 — Adequate** | The adventure is reasonably workable for beginners. Most objectives and immediate choices are understandable, and inexperienced players can learn the expected modes of play through participation, but the adventure provides no unusually strong beginner scaffold and contains recurring moments where prior experience or GM guidance is helpful. |
| **4 — Strong** | The adventure is well suited to inexperienced players. Clear objectives, manageable decision contexts, useful feedback, progressive exposure to expected modes of play, or forgiving opportunities to learn allow beginners to participate meaningfully with limited special assistance. Some demanding or unfamiliar situations may occur without undermining the overall beginner-supportive experience. |
| **5 — Exceptional** | The adventure is exceptionally well suited to introducing inexperienced players to play. Across the adventure, beginners are consistently given clear purposes, understandable and meaningful choices, strong opportunities to learn through play, informative consequences or feedback, and room to recover from imperfect decisions. The playable structure itself functions as a sustained onboarding environment rather than merely being simple. |

**Status:** Frozen calibration rubric. The definition, calibration rules, and
anchors above are locked for the current ontology version. Future changes to
their wording or meaning require an explicit ontology revision and revalidation
against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during Player
Beginner Suitability calibration. They illustrate application of the rubric but
do not redefine the score anchors; future adventures are scored against the
anchor meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Poor** | **ADV-0034 — Tomb of Horrors** |
| **2 — Challenging** | **ADV-0062 — No Honour Among Thieves** |
| **3 — Adequate** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0303 — Storm King's Thunder** |
| **4 — Strong** | **ADV-0053 — Call of the Wild**; **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0287 — House of Lament** |
| **5 — Exceptional** | **ADV-0262 — Lost Mine of Phandelver** |

Initial full-source calibration applied the frozen Revision 1 rubric to the
familiar eight-adventure set and then pressure-tested every adjacent boundary.
The **1/2** boundary distinguished adventures where novices cannot reliably
learn what successful participation requires before serious punishment occurs
from adventures whose objectives remain legible but whose recurring demands
still make active guidance important. **ADV-0034 — Tomb of Horrors** anchors
score 1, while **ADV-0062 — No Honour Among Thieves** anchors score 2.

The **2/3** boundary was the principal post-blind pressure point. Initial
AdventureFinder application placed **ADV-0040 — Expedition to the Barrier
Peaks** at 2, while the blind independent reviewer placed it at 3. Focused
full-source A/B/C adjudication concluded **A — the original AdventureFinder
application was wrong**. The published 2024 adventure does not merely expose
novices to alien technology and high-level complexity: Aphelion 3000 provides
recurring authored objectives, navigation and hazard support, assistance and
rewards; technology is governed by explicit learn-by-doing procedures with
feedback and transferable learning; and the Aphelion relationship contains
published recovery mechanisms when characters distrust, reject, or offend it.
Those mechanisms make the adventure **reasonably workable for beginners through
participation**, while its 11th-level character complexity, deceptive guide,
alien hazards, and unfamiliar environment still create recurring moments where
experience or guidance is helpful. The final score is therefore **3 —
Adequate**, not 2 or 4.

This adjudication also establishes an application guardrail for the phrase
“active GM guidance”: **authored in-world guidance that is part of
substantially-as-published play counts as player-facing beginner support and is
not, by itself, evidence for score 2.** Score 2 instead concerns recurring need
for special player coaching or guidance beyond what the published playable
structure already supplies. This is application guidance under the frozen
rubric, not a change to the score anchors.

The **3/4** boundary distinguishes adventures that are broadly workable for
novices but contain recurring points where prior experience or guidance remains
helpful from adventures whose published structure provides strong recurring
beginner support through clear objectives, manageable decision contexts,
feedback, progressive exposure, or forgiving learning opportunities.
**ADV-0040 — Expedition to the Barrier Peaks** and **ADV-0303 — Storm King's
Thunder** anchor score 3; **ADV-0053 — Call of the Wild**, **ADV-0277 — The Wild
Beyond the Witchlight**, and **ADV-0287 — House of Lament** anchor score 4.

The **4/5** boundary is deliberately demanding. Score 5 does not mean merely
“excellent for beginners” or “simple.” It requires the **playable structure
itself to function as a sustained onboarding environment** across the
adventure. **ADV-0262 — Lost Mine of Phandelver** anchors score 5 because its
published progression moves novices from a simple mission through immediate
combat/investigation, a bounded initial lair, a town hub with legible NPC goals,
broader regional choices, and finally a larger dungeon while repeatedly
providing feedback, redundant leads, recovery from imperfect decisions, and
progressively broader responsibility. The calibrated score-4 cases provide
strong beginner support without sustaining that same onboarding function
across their complete playable structure.

A subsequent eight-case blind independent validation pass reproduced seven of
the eight initial integer scores exactly. The sole score disagreement was
**ADV-0040 — Expedition to the Barrier Peaks** at AdventureFinder 2 versus blind
3; the full-source adjudication described above moved the AdventureFinder score
to 3 while leaving the frozen rubric unchanged. The resulting final calibrated
benchmark set therefore agrees **8/8** with the blind independent integer-score
placements after adjudication.

Calibration also reaffirmed several analytical separations:

- **Rules / System-Mastery Demand is not Player Beginner Suitability.** A low
  mechanical-mastery adventure can still be opaque to novices, while a more
  mechanically demanding adventure can remain workable when the published
  experience supplies strong objectives, feedback, and learning mechanisms.
- **Character level is evidence, not destiny.** Starting at a high level can
  create novice friction, but it must not determine the score independently of
  the adventure's actual player-facing support.
- **Lethality / Failure Severity is not Player Beginner Suitability.** Severe
  consequences matter particularly when they arrive before novices have had a
  reasonable chance to understand expectations; difficulty alone is not a
  beginner-suitability score.
- **Structural Openness is not Player Beginner Suitability.** Open adventures
  can support beginners when goals and decision contexts remain legible, while
  linear adventures can still assume opaque conventions or provide weak
  feedback.
- **GM Beginner Suitability remains separate.** Player-facing support may be
  produced by material administered by the GM, but the ease with which an
  inexperienced GM can understand and run that material belongs to Dimension
  19.
- **Marketing labels are evidence, not scores.** “Starter,” “introductory,” or
  “beginner-friendly” framing does not replace full-source assessment of the
  playable structure.

Across full-source calibration, all four adjacent boundaries, blind independent
application, and the focused Barrier Peaks disagreement adjudication, no
surviving defect or material ambiguity was found in the frozen Player Beginner
Suitability rubric.


### 19. GM Beginner Suitability

**Definition:** How well the published adventure supports an inexperienced GM in
understanding, preparing, explaining, adjudicating, and successfully running it.

GM Beginner Suitability measures the adventure's **support for an inexperienced
GM**, not simply how little work or judgment the adventure requires. It considers
whether the published material makes the adventure's structure, objectives,
expected progression, important rules interactions, likely player choices, and GM
responsibilities understandable and manageable for someone with limited prior GM
experience.

It does **not** directly measure GM Preparation Burden, GM Improvisation Demand,
Rules / System-Mastery Demand, adventure quality, or Player Beginner Suitability.
Those factors may affect beginner suitability, but they should influence this score
only insofar as the published adventure successfully **supports an inexperienced GM
in handling them**.

#### Calibration Rules

- **Support, not raw simplicity, is the target.** A simple scenario can still score
  poorly when the publication leaves the GM to infer important structure or
  procedures. A complex scenario can score well when the publication makes that
  complexity operational through clear procedures, reactions, state handling,
  contingencies, and recovery guidance.

- **Do not use GM Preparation Burden as a proxy.** Material can require substantial
  reading or advance preparation while still being well scaffolded for an
  inexperienced GM. Conversely, a short or skim-friendly adventure can still leave
  critical operating gaps.

- **Do not use GM Improvisation Demand as a proxy.** Open or reactive play does not
  automatically reduce beginner suitability. What matters is whether the published
  adventure gives the inexperienced GM enough structure, information, and guidance
  to handle the improvisation it expects.

- **Do not use rules complexity as a proxy.** Unusual rules, high-level characters,
  technology, or other mechanical complexity can remain manageable when the source
  clearly explains the relevant procedures and provides usable recovery or
  contingency support.

- **An executable default path matters, but does not automatically earn score 3.**
  A coherent published progression can be enough to distinguish score 2 from score
  1. Score 3 additionally requires that **most important procedures and progression
  are adequately supported**.

- **Specified content is not automatically specified play.** A premise, map, NPC
  roster, goals, motivations, encounters, clues, or endpoint can all be clear while
  the GM still lacks the operating procedure needed to make ordinary expected play
  function.

- **Difficult execution is not the same as missing support.** Exacting refereeing,
  presentation technique, state tracking, or judgment can be hard for a novice while
  the publication nevertheless supplies the important procedures. Such difficulty
  is compatible with score 3 and, when central novice trouble spots are consistently
  operationalized, score 4.

- **Cognitive complexity is not evidence of poor beginner support.** Complicated
  identities, factions, or state structures can remain supportive when the source
  repeatedly supplies the information states, transitions, reactions, contingencies,
  and recovery mechanisms needed to operate them.

- **Do not assume an experienced GM will repair the adventure.** Score the published
  support actually provided. Do not increase the score because a veteran GM could
  invent missing procedures, reconstruct transitions, or redesign a weakly supported
  branch.

- **Path sensitivity applies when supported routes materially change novice-GM
  support.** A well-supported default route can coexist with a weakly supported
  alternate route; record Path Sensitive when those differences materially affect
  the dimension rather than averaging them away.

| Score | Meaning |
| ---: | --- |
| **1 — Poor** | The adventure provides little effective support for an inexperienced GM. Successfully running it substantially as published commonly depends on prior GM experience to understand its structure, identify what matters, resolve underspecified situations, or compensate for presentation or procedural gaps. |
| **2 — Challenging** | The adventure provides some usable guidance, but an inexperienced GM is likely to encounter recurring areas where important structure, procedures, transitions, or adjudications are insufficiently explained or assume experience. Beginner success is possible, but the adventure is not well scaffolded for it. |
| **3 — Manageable** | The adventure is reasonably understandable and runnable by an inexperienced GM. Most important procedures and progression are adequately supported, although some portions assume judgment, synthesis, or techniques that a beginner may find difficult. |
| **4 — Supportive** | The adventure consistently supports an inexperienced GM with clear structure, actionable guidance, understandable procedures, and useful support for likely situations. A beginner GM should usually be able to prepare and run it successfully without needing substantial prior experience to fill important gaps. |
| **5 — Exceptionally Supportive** | The adventure is deliberately or exceptionally effective at teaching and scaffolding the GM's job. It not only provides clear runnable material but actively helps an inexperienced GM understand what to do, why, and how to handle the adventure's important situations, making successful first-time or very-early GMing unusually well supported. |

**Status:** Frozen calibration rubric. The Revision 1 definition, clarification,
calibration rules, and 1--5 anchors above are locked for the current ontology
version. Future changes to their wording or meaning require an explicit ontology
revision and revalidation against the Analysis Validation Corpus.

#### Calibration Benchmarks

The following scored adventures are reference exemplars produced during GM Beginner
Suitability calibration. They illustrate application of the rubric but do not
redefine the score anchors; future adventures are scored against the anchor
meanings, not by relative similarity to these examples.

| Score | Calibrated benchmark adventures |
| ---: | --- |
| **1 — Poor** | **ADV-0168 — Blood Night** |
| **2 — Challenging** | **ADV-0132 — The Eyes of At'ar**; **ADV-0150 — A Restless Eternity** |
| **3 — Manageable** | **ADV-0034 — Tomb of Horrors**; **ADV-0062 — No Honour Among Thieves**; **ADV-0135 — Shadow of the Watch**; **ADV-0162 — The Dallabad Curse**; **ADV-0303 — Storm King's Thunder** |
| **4 — Supportive** | **ADV-0040 — Expedition to the Barrier Peaks**; **ADV-0053 — Call of the Wild**; **ADV-0092 — An Actor's Life**; **ADV-0262 — Lost Mine of Phandelver** |
| **5 — Exceptionally Supportive** | **ADV-0277 — The Wild Beyond the Witchlight**; **ADV-0287 — House of Lament** |

For concise score-to-score comparison, the preferred primary benchmark ladder is:

> **Blood Night 1 → The Eyes of At'ar 2 → Tomb of Horrors 3 → Expedition to
> the Barrier Peaks 4 → The Wild Beyond the Witchlight 5**

Supporting cases remain important for boundary interpretation, but the primary
ladder provides a compact baseline for production scoring.

#### Adjacent-Boundary Calibration

The **1/2** boundary distinguishes adventures where missing support is sufficiently
central or pervasive that prior GM experience must substantially construct or
reconstruct how ordinary expected play itself functions from adventures that provide
a coherent executable default adventure but still leave recurring important gaps.
**ADV-0168 — Blood Night** anchors score 1: after its opening premise, the central
dynamic murderous-house situation lacks a sufficient operating procedure for
movement, encounter triggering, victim progression, time passage, and ordinary state
handling. **ADV-0132 — The Eyes of At'ar** anchors score 2 because it supplies a
clear briefing, travel, cast, contact procedure, and path to the hostage exchange,
yet the central hostage/scroll resolution becomes under-proceduralized under ordinary
acceptance, refusal, rescue, or combat responses.

This establishes the application rule that **a badly unsupported branch is not by
itself sufficient for score 1 when the publication still provides a coherent,
executable default adventure**. Score 1 is reserved for cases where missing support
is central or pervasive enough that prior GM experience must supply the operating
engine of ordinary play.

The **2/3** boundary distinguishes an adventure with a runnable spine but recurring
important support gaps from one where the central procedure and resolution are
sufficiently authored and remaining difficulty is principally implementation,
judgment, or synthesis. **ADV-0132 — The Eyes of At'ar** remains the primary score-2
anchor. **ADV-0135 — Shadow of the Watch** and **ADV-0162 — The Dallabad Curse**
provide especially useful score-3 contrasts.

Focused adjudication of **Shadow of the Watch** established the following guardrail:
**an adventure can satisfy score 3 when it clearly establishes the important actors,
the concrete condition that resolves the central conflict, and the consequence of
satisfying that condition, even if the GM must synthesize some negotiation,
connective play, implementation, or aftermath needed to carry that condition out.**
Merely stating what an NPC wants is not enough; there must be a sufficiently concrete
causal link of **condition/action → defined consequential resolution**. If ordinary
play instead reaches the central conflict and the GM must still determine what the
substantive operating state or resolution itself is, score 2 remains appropriate.

**ADV-0162 — The Dallabad Curse** reinforces the same boundary from a procedural
direction. Its nonrepeating area-entry encounter procedure and Yharaskrik's authored
reaction chain supply a recognizable runtime engine. Random-state inconsistencies and
thin Khorin information require synthesis, but they occur around a supplied operating
mechanism rather than replacing it.

The **3/4** boundary distinguishes adventures that are basically runnable for a
beginner but still require recurring judgment or synthesis from adventures that
**consistently operationalize the central situations likely to trouble a novice**.
Complexity or a large amount of synthesis does not cap an adventure at 3 when the
source repeatedly supplies actionable procedures, reactions, state handling,
contingencies, or recovery support. **ADV-0303 — Storm King's Thunder** and
**ADV-0034 — Tomb of Horrors** illustrate score 3 in different ways;
**ADV-0040 — Expedition to the Barrier Peaks** anchors score 4 because its unusual
technology, robot, relationship, recovery, and antagonist procedures are repeatedly
made actionable for the GM.

Focused adjudication of **ADV-0092 — An Actor's Life** further established that
complicated identity/state tracking does not imply low beginner suitability when the
publication repeatedly supplies branch handling, failure recovery, state transitions,
and redundant fail-safes. Its original AdventureFinder score moved from 2 to 4 after
full-source adjudication.

The **4/5** boundary distinguishes excellent operational support from genuinely
pedagogical scaffolding. Score 5 requires the publication not merely to tell the GM
what the situation contains, but repeatedly to help an inexperienced GM understand
**what to do, why, and how** in the adventure's defining situations. Broad general
Dungeon Master instruction is one route to score 5, exemplified by **ADV-0277 — The
Wild Beyond the Witchlight**. It is not mandatory: **ADV-0287 — House of Lament**
qualifies through concentrated adventure-specific teaching about its flow, haunting
states, ambient haunt use, séance operation, spirit motivations, pacing, and
contingencies.

This establishes two legitimate score-5 architectures:

- **broad novice-GM instruction plus adventure-specific scaffolding**, and
- **exceptionally effective adventure-specific pedagogical scaffolding**.

Score 5 therefore does not require a general-purpose “how to be a Dungeon Master”
course.

#### Blind Validation and Adjudication Record

Calibration used multiple closed-source blind passes so that no single benchmark
search or disagreement could determine the full ladder.

A dedicated endpoint blind pass independently reproduced **ADV-0168 — Blood Night**
at **1** and **ADV-0277 — The Wild Beyond the Witchlight** at **5**. The endpoint
integer scores reproduced exactly; a supporting Path Sensitive disagreement for Blood
Night did not affect the score.

A separate interior blind pass assessed **ADV-0034 — Tomb of Horrors**,
**ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0287 — House of Lament**, and
**ADV-0303 — Storm King's Thunder**. The blind reviewer scored them **3, 4, 5, 3**.
Focused source-grounded A/B/C adjudication concluded that the original AdventureFinder
placements for Tomb (2), Barrier Peaks (3), and House of Lament (4) were application
errors and moved them to the blind scores; Storm King's Thunder reproduced 3 exactly.
No frozen anchor wording changed.

A supplemental lower-ladder blind pass challenged the provisional score-2 candidates
**ADV-0150 — A Restless Eternity** and **ADV-0092 — An Actor's Life**. The blind
reviewer scored them 3 and 4 respectively. Focused adjudication retained
**A Restless Eternity at 2**, because its own ordinary travel procedure can generate
an early cult encounter that leaves later central antagonist states under-specified,
while moving **An Actor's Life to 4** because the source repeatedly supplies explicit
branch continuations, recovery mechanisms, and redundant fail-safes. This pass showed
that score 2 required stronger independent validation rather than being preserved by
benchmark convenience.

A final fresh-candidate blind pass therefore assessed three previously unused
one-page adventures from the same sourcebook. **ADV-0132 — The Eyes of At'ar**
reproduced **2** exactly, **ADV-0162 — The Dallabad Curse** reproduced **3** exactly,
and the blind reviewer placed **ADV-0135 — Shadow of the Watch** at 3 against the
pre-blind AdventureFinder score of 2. Focused adjudication moved Shadow of the Watch
to 3, establishing the authored-resolution-condition versus missing-resolution
implementation guardrail above. This pass provided the clean independent score-2
reproduction that the calibration ladder previously lacked.

The blind reviewer in that final pass reported that the separate Adventure Master
Catalog and Adventure Boundary Detection Specification were not retrievable in its
closed-source environment. The three source boundaries were nevertheless
unambiguous heading-to-heading one-page units, and the reviewer did not supplement
externally. This source-package limitation was recorded but did not alter the integer
score adjudications.

Across full-source scoring, targeted endpoint searches, all four adjacent-boundary
pressure tests, multiple closed-source blind passes, and focused A/B/C disagreement
adjudications, no surviving defect or material ambiguity was found in the frozen
Revision 1 GM Beginner Suitability rubric. The remaining disagreements were resolved
as application differences under the frozen wording rather than as reasons to revise
the anchors.

## Working Status

The 19-dimension ontology and common analysis scoring framework are accepted as
Version 1.6.

The common analysis scoring framework and the Combat Emphasis rubric were
introduced in Version 0.2-draft as calibration scaffolding. All seventeen
interpretive analysis dimensions---Combat Emphasis, Exploration Emphasis, Social
Interaction Emphasis, Investigation Emphasis, Puzzle / Problem-Solving Emphasis,
Tactical Complexity, Lethality / Failure Severity, Rules / System-Mastery Demand,
Structural Openness, Consequential Player Agency, Seriousness, Darkness / Horror
Intensity, Fantastic Weirdness, GM Preparation Burden, GM Improvisation Demand,
Player Beginner Suitability, and GM Beginner Suitability---had frozen,
corpus-calibrated, blind-validated scoring rubrics through Version 1.2. Version
1.3 revises the Rules / System-Mastery Demand scores 3--5 and upper-boundary
guidance after a fresh source-grounded comparative review and pressure test.
Version 1.4 revises the Tactical Complexity definition and scores 3--5 around
live tactical decision load, coupled tactical pressure, and sustained dynamic
reassessment. Version 1.5 applies the post-blind Rules / System-Mastery Demand
continuity correction and moves Trobriand's Graveyard from 4 to 3 after two
clean blind assessments independently rejected the score-4 placement. Version
1.4.1 carries those semantics forward unchanged and completes the Tactical
Complexity Revision-3 blind revalidation and benchmark adjudication. The Rules
/ System-Mastery Demand Version-1.5 wording subsequently completed full blind
revalidation and source-grounded benchmark adjudication, as recorded below.
Version 1.6 expands the **GM Preparation Burden score-5 benchmark set** by adding
the pristine blind-reproduced **ADV-0032 — Dead in Thay = 5 — Very High**
result, preserving the frozen GMPB definition, calibration rules, anchors, and
adjacent-boundary semantics unchanged.

Version 1.0 therefore represents the first ontology version in which every
current matching and interpretive dimension has a calibrated production scoring
method. The ontology document as a whole received final editorial acceptance as
Version 1.0.

Version 1.1 carries that accepted ontology forward without changing any
dimension definition or scoring anchor. Its only substantive ontology change is
an expansion of the **Combat Emphasis score-5 calibration benchmark set** to add
**ADV-0032 — Dead in Thay** and **ADV-0033 — Against the Giants**, together with
their post-1.0 independent blind-replication record. Version 1.2 adds the frozen
**ADV-0230 — Salvage Operation** Combat Emphasis benchmark-application correction.

Version 1.3 adds the common **Empirically inhabited endpoints** scoring principle
and revises the **Rules / System-Mastery Demand** upper ladder so scores 3--5
distinguish recurring discrete mechanical problems, a continuing player-facing
mechanical layer, and mechanical mastery as a repeatedly progression-bearing
operating structure. The revised RSMD rubric is accepted based on the documented
source-grounded comparative review and boundary pressure tests.

Version 1.4 accepts **Tactical Complexity Revision 3**. It reframes the dimension
around live tactical decision load, preserves scores 1--2, revises score 3 around
recurring but bounded, stable, or separable tactical considerations, score 4
around coupled tactical pressure, and score 5 around dense, sustained coupled
tactical pressure across multiple major encounters or a dominant sustained
mandatory encounter sequence. Existing Tactical Complexity score-3 through
score-5 benchmark placements remain re-adjudication hypotheses under the new
semantics, and fresh independent blind revalidation remains pending.

Version 1.4.1 completes the post-acceptance work: two independent blind passes
over the ten-case 3--5 cohort, followed by focused source-grounded adjudication
of Storm King's Thunder, Expedition to the Barrier Peaks, and The Final Enemy,
establish the final fourteen-adventure benchmark ladder without changing the
Revision-3 definition or anchors.

Version 1.5 records the post-acceptance AFAO 1.3 RSMD blind revalidation outcome.
It corrects the upper-ladder continuity wording so persistent-state carry-forward
and repeated differentiated mechanical response are both legitimate sustained
mechanical morphologies rather than sequential prerequisite gates. It retains
the progression-bearing 4/5 distinction and initially carries **Obstacle Course**
and **Mad Wizard's Lair** as score-5 benchmark hypotheses under the corrected
semantics while moving **Trobriand's Graveyard** from 4 to **3 — Moderate** after
two clean blind assessments independently rejected 4. The corrected wording then
received a full fourteen-case blind benchmark pass, targeted lower-boundary
confirmation, and focused source-grounded adjudication; **Obstacle Course**
remains 5 while **Mad Wizard's Lair** is finalized at **4 — High**.

Version 1.6 carries all normative rubric semantics forward unchanged and expands
the **GM Preparation Burden** empirical upper endpoint. A length-independent
catalog search identified **ADV-0032 — Dead in Thay** as a compact score-5
candidate, and a pristine blind full-source review independently reproduced
**5 — Very High** at **94% confidence**, **Path Sensitive: No**. The result
establishes a second GMPB score-5 morphology in which persistent cross-partition
state, access, tracking, and progression dependencies create sustained
preparation infrastructure inside a bounded adventure. This strengthens the
existing 4/5 interpretation and the rule that preparation burden is not
adventure length; it does not revise the GMPB definition, calibration rules,
anchors, or boundary wording.

At this stage:

- **# of Sessions** and **Levels** remain editorially assessed matching
  dimensions outside the 1--5 interpretive scoring scale. **# of Sessions** has
  a frozen, calibrated, blind-validated normalized-duration rubric, and
  **Levels** has a frozen, calibrated, blind-validated Level Start / Level End
  assessment rubric.
- The seventeen interpretive dimensions are intended to use the provisional
  1--5 absolute scale.
- Fifteen interpretive dimensions retain frozen, corpus-calibrated,
  blind-validated scoring rubrics from Version 1.2. **Rules / System-Mastery
  Demand** is frozen, corpus-calibrated, independently blind-validated, and
  source-adjudicated under the accepted Version 1.5 semantics. **Tactical
  Complexity** is frozen, corpus-calibrated, and independently blind-validated
  under the accepted Revision-3 semantics as of Version 1.4.1.
- No current interpretive dimension remains without scoring anchors.
- **Insufficient Evidence** is represented by the reserved sentinel value `-1`;
  a blank score means **Not Yet Assessed**.


## Revision History

| Version | Date | Status | Summary |
| --- | --- | --- | --- |
| **1.6** | 2026-08-25 | Accepted | Expands the frozen **GM Preparation Burden** score-5 calibration benchmark set by adding **ADV-0032 — Dead in Thay = 5 — Very High** after a length-independent catalog search and pristine blind full-source reproduction at **94% confidence, Path Sensitive: No**; documents the distinct compact score-5 morphology in which persistent glyph-key/gate access, changed-area state, global alert, cross-location consequences, distributed black-gate prerequisites, and endgame preparation create sustained cross-partition preparation infrastructure inside a bounded adventure; strengthens the existing 4/5 distinction and the anti-proxy rule that preparation burden is not adventure length; and makes **no change** to the GMPB definition, calibration rules, 1--5 anchors, adjacent-boundary wording, assessment semantics, or any other dimension. |
| **1.5.1** | 2026-08-22 | Accepted | Adds canonical project-wide acronyms for all nineteen ontology dimensions; explicitly preserves the full canonical dimension names as authoritative and defines the acronyms as case-sensitive aliases only; records **LSLE** as shorthand for the single **Levels** dimension represented by **Level Start / Level End**; standardizes **RSMD** as **Rules / System-Mastery Demand**; and makes no changes to dimension definitions, scoring anchors, calibration guidance, assessment semantics, or matching behavior. |
| **1.5** | 2026-08-18 | Accepted | Applies the post-blind **Rules / System-Mastery Demand** correction after fresh independent AFAO 1.3 revalidation exposed a reproducible differentiated-response continuity defect and a likely benchmark-application error; clarifies that upper-score continuity may arise either through persistent mechanical information/state/tool carry-forward or through a sustained pattern of materially differentiated mechanical interpretation and adaptation; explicitly states that anchors are semantic placements rather than sequential morphology gates; revises scores 3--5 and the 3/4 guidance so a large collection of isolated bespoke mechanisms remains insufficient while repeated differentiated mechanical response can qualify when it materially shapes or carries substantive progression; preserves the progression-bearing 4/5 distinction and the score-5 morphologies; records two clean blind **Mad Wizard's Lair = 3** results as diagnosis of the AFAO 1.3 wording defect and a fresh targeted clean **Obstacle Course = 5** confirmation as evidence that the Extreme endpoint remains viable; moves **ADV-0335 — Trobriand's Graveyard** from **4 — High** to **3 — Moderate** after two clean blind assessments independently rejected 4 at scores 2 and 3 and source-grounded adjudication found recurring beyond-basic mechanical demand without a sufficiently sustained upper-score layer; records the corrected wording's subsequent full fourteen-case blind benchmark pass, targeted lower-boundary confirmation, and focused source-grounded adjudication of every surviving integer-score disagreement; finalizes benchmark-application corrections **ADV-0262 1→2**, **ADV-0277 2→3**, **ADV-0303 3→2**, **ADV-0062 3→4**, **ADV-0031 3→4**, and **ADV-0345 5→4**; and concludes with the RSMD rubric and benchmark ladder frozen, corpus-calibrated, blind-validated, and source-adjudicated. |
| **1.4.1** | 2026-08-18 | Accepted | Completes the post-acceptance calibration of **Tactical Complexity Revision 3** without changing its AFAO 1.4 definition or score anchors; records two separate blind full-source passes over the ten-adventure score-3 through score-5 cohort, with exact agreement on seven cases, only adjacent-score disagreement on the remaining cases, no reported Tactical Complexity contamination, and no material rubric ambiguity; records exact blind replication of **ADV-0262 — Lost Mine of Phandelver = 3**, **ADV-0287 — House of Lament = 3**, **ADV-0062 — No Honour Among Thieves = 5**, **ADV-0248 — Siege of Kalaman = 5**, **ADV-0223 — Sunblight = 4**, **ADV-0189 — Tockworth's Clockworks = 4**, and **ADV-0230 — Salvage Operation = 5**; resolves the three remaining applications by focused source-grounded adjudication at **ADV-0303 — Storm King's Thunder = 5**, **ADV-0040 — Expedition to the Barrier Peaks = 3**, and **ADV-0232 — The Final Enemy = 4**; records that the first Barrier Peaks blind pass followed an erroneous `171--224` target scope while the correct complete named unit is `157--189`, so that apparent 4/3 result is not treated as a clean same-scope blind disagreement; freezes the final fourteen-adventure benchmark ladder as **1:** ADV-0278; **2:** ADV-0053, ADV-0277, ADV-0034; **3:** ADV-0262, ADV-0287, ADV-0040; **4:** ADV-0232, ADV-0223, ADV-0189; **5:** ADV-0303, ADV-0062, ADV-0248, ADV-0230; and marks Tactical Complexity Revision 3 as accepted, corpus-calibrated, and independently blind-validated. |
| **1.4** | 2026-08-18 | Accepted | Accepts **Tactical Complexity Revision 3** as the current Tactical Complexity semantics; reframes the dimension around **live tactical decision load**, coupling among simultaneously relevant tactical factors, and dynamic reassessment as encounter state changes; preserves score 1 and score 2 from AFAO 1.3 while revising score 3 around recurring but bounded, relatively stable, or separable tactical considerations, score 4 around **coupled tactical pressure**, and score 5 around **dense, sustained coupled tactical pressure** across multiple major encounters or within a dominant sustained mandatory encounter sequence; strengthens the analytical separation from **Rules / System-Mastery Demand** by distinguishing understanding the mechanical option space from choosing among understood options during evolving encounter play; makes substantive encounter-play weighting explicit so a long central mandatory sequence can establish an upper score without a raw encounter-count or whole-adventure prevalence gate; removes "practical dependency," straightforward-plan impossibility, and whole-adventure prevalence as score-5 requirements; preserves the AFAO 1.3 Revision-2 calibration record as historical evidence while reopening existing Tactical Complexity score-3 through score-5 benchmark placements as re-adjudication hypotheses under the new semantics; records benchmark re-adjudication and fresh independent blind revalidation as post-acceptance validation tasks. |
| **1.3** | 2026-08-18 | Accepted | Adds Common Scoring Principle **3. Empirically inhabited endpoints**, requiring semantically defined ordinal endpoints to be inhabited by clear, reproducible examples from the broad target adventure corpus while explicitly prohibiting percentile-defined scores or predetermined score distributions; revises **Rules / System-Mastery Demand** scores 3--5 after a complete-source comparative review of nine compact upper-half calibration adventures and explicit 3/4 and 4/5 pressure tests; defines score 3 around recurring but chiefly localized, concentrated, or discrete mechanical problems, score 4 around a continuing player-facing mechanical environment or system whose information, state, rules, interactions, or tools remain consequential across substantive play, and score 5 around player-facing mechanical mastery repeatedly becoming a progression-bearing operating structure; adds guidance that teaching, discoverability, stable procedures, optionality, or the absence of one persistent subsystem do not automatically cap the score; reassigns **ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0227 — Doom of Ythryn**, and **ADV-0335 — Trobriand's Graveyard** to score 4 and **ADV-0032 — Dead in Thay**, **ADV-0337 — Obstacle Course**, and **ADV-0345 — Mad Wizard's Lair** to score 5 while retaining **ADV-0062 — No Honour Among Thieves**, **ADV-0303 — Storm King's Thunder**, **ADV-0031 — White Plume Mountain**, and **ADV-0034 — Tomb of Horrors** at score 3; records **Trobriand's Graveyard** as the weakest 3/4 boundary case and documents three distinct score-5 morphologies: persistent player-operated subsystem, recurring exact-rule environment, and repeated differentiated mechanical response; accepts the Version 1.3 ontology revision on the completed source-grounded comparative and pressure-test record while explicitly leaving fresh independent blind revalidation of the revised RSMD rubric as a post-acceptance validation task. |
| **1.2** | 2026-08-15 | Accepted | Carries forward accepted Version 1.1 unchanged except for the frozen **ADV-0230 — Salvage Operation Combat Emphasis benchmark-application correction** authorized by `combat-emphasis-ADV-0230-salvage-operation-readjudication-freeze-v0.2.md`; moves Salvage from **5 — Dominant** to **4 — High** at 93% human-adjudication confidence with Path Sensitive No; preserves the Combat definition, all 1--5 anchor wording, the 4/5 structural distinction, and the rule that the removal counterfactual is confirming rather than sufficient; records the independently progress-bearing box-retrieval and sinking-ship extraction structure as the decisive reason the adventure does not satisfy score 5; records the post-1.1 evidentiary change from grouped `4 / 5 / 4` instability to four focused single-dimension v0.7 assessments at **4 / 4 / 4 / 4**; retains **ADV-0032 — Dead in Thay** and **ADV-0033 — Against the Giants** as the two independently blind-replicated Combat-5 benchmarks; explicitly keeps Tomb of Horrors outside the correction; and preserves **Salvage Operation = 5 — Very High** for Tactical Complexity and all other non-Combat AFAO content unchanged. |
| **1.1** | 2026-08-15 | Accepted | Carries forward accepted Version 1.0 without changing any dimension definition or score-anchor wording; expands the **Combat Emphasis 5 — Dominant** calibration benchmark set by adding **ADV-0032 — Dead in Thay** and **ADV-0033 — Against the Giants** alongside **ADV-0230 — Salvage Operation**; records two separate blind full-source assessments for each new benchmark with exact **5/5** integer-score replication; records **Against the Giants** at 96% and 93% confidence with both reviewers path-sensitive and both selecting **4 — High** as the strongest adjacent alternative; records **Dead in Thay** at 88% and 96% confidence with both reviewers selecting **4 — High** as the strongest adjacent alternative and a supporting Path Sensitive disagreement of Yes versus No; documents the distinct stronghold-assault and Doomvault-assault structural rationales; and strengthens the empirical 4/5 boundary evidence while leaving the frozen Combat definition, anchors, and prior benchmark placements unchanged. |
| **1.0** | 2026-08-13 | Accepted | Carries forward accepted Version 0.20 and adds the frozen, calibrated, blind-validated **GM Beginner Suitability Revision 1** rubric; defines the dimension as published support for an inexperienced GM in understanding, preparing, explaining, adjudicating, and successfully running the canonical adventure while separating it from GM Preparation Burden, GM Improvisation Demand, Rules / System-Mastery Demand, adventure quality, and Player Beginner Suitability; adds the 1--5 anchors **Poor / Challenging / Manageable / Supportive / Exceptionally Supportive**; records the primary benchmark ladder **Blood Night 1 → The Eyes of At'ar 2 → Tomb of Horrors 3 → Expedition to the Barrier Peaks 4 → The Wild Beyond the Witchlight 5** plus supporting calibrated cases; documents the 1/2 distinction between missing central operating structure and an executable adventure with recurring important gaps, the 2/3 distinction between missing central resolution structure and synthesis required to implement an already authored resolution condition, the 3/4 rule that substantial complexity or synthesis does not cap an adventure at 3 when likely novice trouble spots are consistently operationalized, and the 4/5 requirement for repeated **what / why / how** pedagogical scaffolding; records focused application corrections **Tomb of Horrors 2→3**, **Expedition to the Barrier Peaks 3→4**, **House of Lament 4→5**, **An Actor's Life 2→4**, and **Shadow of the Watch 2→3**, while retaining **A Restless Eternity 2** against blind 3; records clean blind endpoint reproduction of **Blood Night 1** and **The Wild Beyond the Witchlight 5**, interior validation of the 3/4/5 ladder, and a fresh one-page blind pass with exact reproduction of **The Eyes of At'ar 2** and **The Dallabad Curse 3**; records the final Shadow of the Watch 2/3 adjudication and the rule that merely stating an NPC desire is not an authored resolution condition; finds no surviving rubric ambiguity; and updates Working Status to mark all seventeen interpretive dimensions frozen, calibrated, and blind-validated, making this the first complete 19-dimension production-scoring ontology. |
| **0.20** | 2026-08-13 | Accepted | Carries forward accepted Version 0.19 and adds the frozen, calibrated, blind-validated **Levels v2.1** editorial assessment rubric; replaces the conceptual single "Levels" range with two canonical discrete integer values, **Level Start** and **Level End**; defines Level Start as the primary intended character level at which ordinary substantially-as-published play begins and Level End as the character level the published adventure expects characters to have reached by completion of the same canonical Adventure ID; establishes that advancement explicitly awarded for completing the canonical adventure counts toward Level End while advancement triggered only by entering or beginning subsequent canonical material does not; separates primary values from alternate starts and scalable level support; adds evidence hierarchy, anti-proxy rules, multiple-advancement-method guidance, open-campaign guidance, matching guidance, and an explicit uncertainty state rather than reusing the interpretive `-1` sentinel; records calibrated reference cases **No Honour Among Thieves 10→11**, **The Wild Beyond the Witchlight 1→8**, **Dungeon of the Mad Mage 5→20**, **Lost Mine of Phandelver 1→5**, **House of Lament 1→3**, **Tomb of Horrors Uncertain→Uncertain**, **Expedition to the Barrier Peaks 11→13**, and **Witchlight Carnival 1→1**; records the focused Level End adjudication that established the completion-ownership rule; records exact blind reproduction of all eight primary outcomes and the primary-versus-scalable and canonical-transition rules; explicitly drops the experimental **Advancement Variable** supporting field from the rubric and production schema; and updates Working Status to mark Levels frozen, calibrated, and blind-validated. |
| **0.19** | 2026-08-12 | Accepted | Carries forward accepted Version 0.18 and adds the frozen, calibrated, blind-validated **# of Sessions** normalized-duration rubric; formalizes the 2.5--3.0 hour session baseline, whole-number best estimate, Practical Range, Confidence, Path Sensitive flag, substantially-as-published completion standard, probability-weighting of optional and mutually exclusive content, bypass handling, page-count and level-range anti-proxy rules, and the distinction between in-fiction time and table time; establishes five calibration regimes (1--2, 3--5, 6--11, 12--23, and 24+ sessions) as coverage bands rather than categorical scores; records calibrated reference estimates of **Lake Monster 1**, **Salvage Operation 2**, **No Honour Among Thieves 2**, **Call of the Wild 2**, **House of Lament 3**, **Tomb of Horrors 4**, **Expedition to the Barrier Peaks 7**, **Lost Mine of Phandelver 10**, **The Wild Beyond the Witchlight 18**, and **Storm King's Thunder 26**; records an independent blind pass with exact integer reproduction on eight of ten cases and practical reproduction of the two campaign-scale cases at 16 and 24 with strongly overlapping ranges and unchanged calibration regimes; records independent reproduction of the one-shot normalization, optional-content weighting, in-fiction-time, and 1-versus-2-session guardrails; notes supporting Path Sensitive disagreements for Salvage Operation and Tomb of Horrors without altering their calibrated integer benchmarks; and updates Working Status to mark # of Sessions frozen, calibrated, and blind-validated. |
| **0.18** | 2026-08-12 | Accepted | Carries forward accepted Version 0.17 unchanged and adds the frozen, corpus-calibrated, blind-validated **Fantastic Weirdness** rubric; preserves the exact frozen Revision 1 definition, clarifications, and 1--5 anchors unchanged through familiar-eight scoring, full-AVC candidate search, all four adjacent-boundary pressure tests, a nine-case blind independent pass, supplemental complete-source score-4 candidate falsification, dedicated blind tests of **ADV-0195 — Affair on the Concordant Express** and **ADV-0278 — Witchlight Carnival**, and focused A/B/C adjudication of every integer-score disagreement; records final calibrated benchmarks with **ADV-0053 — Call of the Wild**, **ADV-0062 — No Honour Among Thieves**, **ADV-0262 — Lost Mine of Phandelver**, and **ADV-0303 — Storm King's Thunder** at 1, **ADV-0185 — The Murkmire Malevolence** and **ADV-0287 — House of Lament** at 2, **ADV-0034 — Tomb of Horrors** at 3, **ADV-0278 — Witchlight Carnival** at 4, and **ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0277 — The Wild Beyond the Witchlight**, **ADV-0046 — Into Dreamland**, and **ADV-0195 — Affair on the Concordant Express** at 5; records post-blind application corrections **House of Lament** 3→2, **Tomb of Horrors** 4→3, and **Affair on the Concordant Express** 4→5 while retaining **Witchlight Carnival** at 4 against blind 3; records 7/9 exact initial blind reproduction and 9/9 agreement for that batch after adjudication; documents the 1/2, 2/3, 3/4, and 4/5 distinctions, including the rule that familiar activity verbs do not neutralize bizarre player-facing fictional experience and that the score-5 replacement test concerns substantive playable identity rather than abstract plot skeleton; adds the anti-proxy guardrail that “not automatically weird” is not an exclusion rule for Fey, whimsy, magic, technology, planar material, horror, or spectacle; records **Into Dreamland** as a complete-source rather than separately blind-reproduced score-5 benchmark; finds no surviving rubric ambiguity; and updates Working Status to mark Fantastic Weirdness frozen, corpus-calibrated, and blind-validated, leaving one interpretive dimension without anchors. |
| **0.17** | 2026-08-12 | Accepted | Carries forward accepted Version 0.16 unchanged and adds the frozen, calibrated, blind-validated **GM Improvisation Demand Revision 2** rubric; records the operational definition centered on substantive at-the-table invention, synthesis, extrapolation, and adjudication beyond sufficiently specified published material; distinguishes runtime improvisation from GM Preparation Burden, Structural Openness, Consequential Player Agency, Rules / System-Mastery Demand, ordinary roleplaying, genre affordance, sparse publication, and optional embellishment; preserves the revised 4 anchor and establishes the revised score-5 endpoint around wide GM latitude and runtime synthesis carrying large portions of ordinary substantive play rather than requiring the GM to “invent the adventure”; adds the specified-content versus specified-play guardrail and specified-material counterfactual for 4/5 adjudication; records final calibrated benchmarks with **ADV-0034 — Tomb of Horrors** and **ADV-0053 — Call of the Wild** at 1, **ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0062 — No Honour Among Thieves**, and **ADV-0262 — Lost Mine of Phandelver** at 2, **ADV-0287 — House of Lament** and **ADV-0277 — The Wild Beyond the Witchlight** at 3, **ADV-0303 — Storm King's Thunder** at 4, and **ADV-0068 — Curse of Strahd** at 5; records dedicated full-source and blind confirmation of **Curse of Strahd 5**, full-source **Storm King's Thunder 4 ↔ Curse of Strahd 5** upper-boundary pressure testing, and a nine-case blind benchmark pass; records focused post-blind adjudications changing **House of Lament** 2→3, **No Honour Among Thieves** 3→2, and **Call of the Wild** 2→1 while retaining **Expedition to the Barrier Peaks** at 2 against blind 3; documents the resulting application guardrails for information-bearing roleplay, recurring reactive actors, genre affordance, and optional embellishment; establishes calibrated 1/2, 2/3, 3/4, and 4/5 boundary distinctions; records no surviving rubric ambiguity; and updates Working Status to mark GM Improvisation Demand frozen, corpus-calibrated, and blind-validated, leaving two interpretive dimensions without anchors. |
| **0.16-draft** | 2026-08-12 | Accepted | Carries forward accepted Version 0.15 unchanged and adds the frozen, calibrated, blind-validated **GM Preparation Burden** rubric; preserves the exact frozen Revision 1 definition and 1--5 anchors through full-source scoring, targeted score-1 endpoint search, all four adjacent-boundary pressure tests, an initial nine-case blind independent pass, four focused disagreement adjudications, a targeted replacement score-2 search, complete-source falsification of **ADV-0288 — A Friend in Need**, and a supplemental four-case lower-boundary blind pass; records final calibrated benchmarks with **ADV-0200 — Lake Monster** at 1, **ADV-0288 — A Friend in Need** at 2, **ADV-0034 — Tomb of Horrors**, **ADV-0053 — Call of the Wild**, **ADV-0062 — No Honour Among Thieves**, and **ADV-0262 — Lost Mine of Phandelver** at 3, **ADV-0287 — House of Lament**, **ADV-0040 — Expedition to the Barrier Peaks**, and **ADV-0277 — The Wild Beyond the Witchlight** at 4, and **ADV-0303 — Storm King's Thunder** at 5; records the source-grounded post-blind corrections **ADV-0034** 2→3, **ADV-0053** 2→3, and **ADV-0287** 3→4 while retaining **ADV-0200** at 1 against blind 2, and records the Tomb adjudication rejecting both the original 2 and blind 4 in favor of 3; documents the application guardrails that score 1 does not mean zero prep, significant compartmentalized alternatives can create score 3, precision does not automatically create score 4, and a consequential advance choice is not independently sufficient for score 4; establishes the calibrated 1/2, 2/3, 3/4, and 4/5 boundary distinctions; records supplemental blind reproduction of **Lake Monster 1 ↔ A Friend in Need 2 ↔ Tomb of Horrors / Call of the Wild 3** at 4/4 exact scores and matching path-sensitivity judgments; corrects the Tomb calibration source attribution to *Tales from the Yawning Portal*; records no surviving rubric ambiguity; and updates Working Status to mark GM Preparation Burden frozen, corpus-calibrated, and blind-validated, leaving three interpretive dimensions without anchors. |
| **0.15** | 2026-08-12 | Accepted | Carries forward accepted Version 0.14 unchanged and adds the frozen, calibrated, blind-validated **Player Beginner Suitability** rubric; preserves the exact frozen Revision 1 definition, calibration rules, and 1--5 anchors unchanged through full-source scoring, all four adjacent-boundary pressure tests, and an eight-case blind independent validation pass; records final calibrated benchmarks with **ADV-0034 — Tomb of Horrors** at 1, **ADV-0062 — No Honour Among Thieves** at 2, **ADV-0040 — Expedition to the Barrier Peaks** and **ADV-0303 — Storm King's Thunder** at 3, **ADV-0053 — Call of the Wild**, **ADV-0277 — The Wild Beyond the Witchlight**, and **ADV-0287 — House of Lament** at 4, and **ADV-0262 — Lost Mine of Phandelver** at 5; records 7/8 exact initial blind integer-score reproduction and the sole focused score adjudication **ADV-0040 — Expedition to the Barrier Peaks** 2→3 under outcome **A — the original AdventureFinder application was wrong**, because Aphelion's recurring authored guidance, explicit technology-learning procedures, and recovery mechanisms make novice play basically workable while recurring unfamiliarity and complexity still keep it below 4; adds the application guardrail that authored in-world guidance counts as published player-facing support and does not itself satisfy the score-2 “active GM guidance” clause; documents the 1/2, 2/3, 3/4, and deliberately demanding 4/5 boundary distinctions, including the requirement that score 5's playable structure function as a sustained onboarding environment rather than merely being simple; records no surviving rubric ambiguity and 8/8 agreement between final integer benchmarks and the blind pass after adjudication; and updates Working Status to mark Player Beginner Suitability frozen, corpus-calibrated, and blind-validated, leaving four interpretive dimensions without anchors. |
| **0.14** | 2026-08-12 | Accepted | Adds the finalized-for-review **Darkness / Horror Intensity** rubric while carrying forward accepted Version 0.13 unchanged elsewhere; preserves the exact frozen Pass 1 definition, qualifying-material clarification, and 1--5 anchors unchanged through full-source scoring, all four adjacent-boundary pressure tests, an eight-case blind independent validation pass, and focused adjudication of every blind disagreement; records final calibrated benchmarks across all five score levels with **ADV-0062 — No Honour Among Thieves** at 1, **ADV-0053 — Call of the Wild** and **ADV-0040 — Expedition to the Barrier Peaks** at 2, **ADV-0262 — Lost Mine of Phandelver**, **ADV-0277 — The Wild Beyond the Witchlight**, and **ADV-0303 — Storm King's Thunder** at 3, **ADV-0034 — Tomb of Horrors** at 4, and **ADV-0287 — House of Lament** at 5; records 7/8 exact initial blind integer-score reproduction and the sole score correction **ADV-0040 — Expedition to the Barrier Peaks** 3→2 after adjudication found that the original application over-weighted recurring corpse/grotesque content relative to its clearly secondary experiential role; records the path-sensitivity adjudications changing **ADV-0277 — The Wild Beyond the Witchlight** Yes→No while retaining **ADV-0287 — House of Lament** at Yes because early awakened/slasher play can materially change horror intensity and presentation without crossing the score-5 endpoint; documents the 1/2 distinction between threatening/dangerous content and a meaningful dark experiential strand, the 2/3 distinction between bounded/secondary darkness and darkness as a substantial recurring component, the 3/4 distinction where darkness strongly conditions most substantive play, and the 4/5 distinction between pervasive darkness surrounding another primary playable structure and horror itself becoming a fundamental organizing structure; adds guardrails separating Darkness / Horror from Seriousness, lethality, danger, Fantastic Weirdness, genre labels, grim backstory, and mere recurrence of dark facts; records no surviving rubric ambiguity and 8/8 agreement between final integer benchmarks and the blind pass after adjudication; and updates Working Status to mark Darkness / Horror Intensity frozen, corpus-calibrated, and blind-validated, leaving five interpretive dimensions without anchors. |
| **0.13** | 2026-08-12 | Accepted | Finalizes **Seriousness** for review after full-source endpoint calibration, all four adjacent-boundary pressure tests, a ten-case blind independent validation pass, and focused adjudication of both resulting score disagreements; preserves the frozen definition, clarification, and 1--5 anchors unchanged; records 8/10 exact initial blind score reproduction with exact blind confirmation of **ADV-0013 — A Conspiracy Most Cracked** at 1, **ADV-0278 — Witchlight Carnival** at 2, **ADV-0040 — Expedition to the Barrier Peaks**, **ADV-0062 — No Honour Among Thieves**, and **ADV-0277 — The Wild Beyond the Witchlight** at 3, **ADV-0303 — Storm King's Thunder** at 4, and **ADV-0034 — Tomb of Horrors** and **ADV-0287 — House of Lament** at 5; records focused source-grounded adjudication retaining **ADV-0053 — Call of the Wild** at 4 against blind 3 and **ADV-0262 — Lost Mine of Phandelver** at 4 against blind 5, with no post-blind benchmark-application corrections and no rubric changes; adds the application guardrail that friendly, cozy, hopeful, or welcoming material is not automatically playful/lighthearted, and reaffirms that horror, lethality, objective stakes, Fantastic Weirdness, and game-like challenge are not proxies for Seriousness; documents the validated 3/4 distinction between no clear tonal hierarchy and earnest/dramatic predominance with meaningful lighter material, and the 4/5 distinction between meaningful lighter material and lighter material that is only rare, peripheral, or primarily contrastive; and updates Working Status to mark Seriousness frozen, corpus-calibrated, and blind-validated. |
| **0.12** | 2026-08-12 | Accepted | Finalizes **Consequential Player Agency** for review after full-source calibration, adjacent-boundary pressure testing, an eight-case blind independent pass, focused adjudication of all four initial score disagreements, replacement of an invalid *Sunken Isles* score-1 candidate after catalog-boundary revalidation, a full-source endpoint falsification of **ADV-0031 — White Plume Mountain**, a focused three-case blind lower-boundary confirmation, and final Tomb-only adjudication; preserves the frozen definition, clarification, and 1--5 anchors unchanged; records calibrated benchmarks across all five score levels with **ADV-0031 — White Plume Mountain** at 1, **ADV-0034 — Tomb of Horrors**, **ADV-0062 — No Honour Among Thieves**, **ADV-0053 — Call of the Wild**, and **ADV-0287 — House of Lament** at 2, **ADV-0262 — Lost Mine of Phandelver** at 3, **ADV-0040 — Expedition to the Barrier Peaks** and **ADV-0303 — Storm King's Thunder** at 4, and **ADV-0277 — The Wild Beyond the Witchlight** at 5; records initial blind/adjudication corrections **ADV-0034** 1→2, **ADV-0062** 1→2, and **ADV-0303** 3→4 while retaining **ADV-0040** at 4 against blind 3; documents the 1/2 distinction between consequentially inert route/method/survival/resource choice and at least one authored localized persistent consequence, the disjunctive score-3 major-outcome clause, the one-system-versus-multiple-thread routes to score 4, and the 4/5 distinction where cumulative decision history becomes a fundamental organizing feature; records removal of **ADV-0102 — Keyport in Danger** from calibration after boundary review invalidated it as a discrete adventure and excludes *Sunken Isles* calibration cases pending revalidation; records blind reproduction of **White Plume Mountain** at 1 and **No Honour Among Thieves** at 2 plus final retention of **Tomb of Horrors** at 2 after the blind pass omitted the decisive Siren consequence; and updates Working Status to mark Consequential Player Agency frozen, corpus-calibrated, and blind-validated. |
| **0.11.5** | 2026-08-12 | Accepted | Finalizes **Rules / System-Mastery Demand** for review after full-source calibration, repeated AMC endpoint searches, an upper-boundary rubric viability audit, adoption and pressure-testing of the final score-5 intensity-continuation wording, a twelve-case blind independent pass, and source-grounded adjudication of every actual blind disagreement; preserves the definition and score-1 through score-4 meanings while replacing the original overconstrained score-5 endpoint with the validated formulation centered on advanced mechanical understanding across the adventure, frequent selection/combination/adaptation/management of mechanical tools, and competent ordinary rules use often being insufficient; adds explicit clarifications that combat frequency/difficulty/lethality are not proxies and that authored mechanical teaching does not inherently reduce demand; records calibrated benchmarks across all five score levels with **ADV-0053 — Call of the Wild** and **ADV-0262 — Lost Mine of Phandelver** at 1, **ADV-0032 — Dead in Thay** and **ADV-0337 — Obstacle Course** at 4, and **ADV-0345 — Mad Wizard's Lair** at 5; records blind/adjudication corrections **ADV-0287** 1→2, **ADV-0277** 1→2, **ADV-0303** 2→3, **ADV-0031** 4→3, **ADV-0034** 4→3, and **ADV-0337** 5→4 while retaining **ADV-0040 — Expedition to the Barrier Peaks** at 3 against blind 4; documents the Puzzle/System-Mastery seam, taught/procedural bespoke systems, localized exact-rule gates, and the final 4/5 distinction between recurring strong mechanical demand and adventure-wide advanced mechanical dependence; records 10/12 agreement between final adjudicated scores and the blind pass with zero rubric-ambiguity outcomes; and updates Working Status to mark Rules / System-Mastery Demand frozen, corpus-calibrated, and blind-validated. |
| **0.11.4** | 2026-08-12 | Accepted | Finalizes **Tactical Complexity** after full-source calibration, endpoint search, upper-end rubric viability audit, Revision-2 re-adjudication, a dedicated six-case blind boundary pass, and focused adjudication of all three resulting score disagreements; preserves the original score-1 through score-4 wording and replaces only score 5 with the validated Revision-2 intensity continuation centered on dense tactical decision structures, dependence on coordinating multiple interacting factors, sustained adaptation, and straightforward default play being frequently inadequate; records calibrated benchmarks across all five score levels with **ADV-0278 — Witchlight Carnival** at 1 and **ADV-0230 — Salvage Operation** at 5; records the original blind corrections **ADV-0277 — The Wild Beyond the Witchlight** 1→2 and **ADV-0062 — No Honour Among Thieves** 5→4; records upper-end full-source negative controls including **ADV-0232 — The Final Enemy**, **ADV-0189 — Tockworth's Clockworks**, **ADV-0248 — Siege of Kalaman**, and **ADV-0223 — Sunblight**; records the Revision-2 blind disagreement adjudications retaining **ADV-0232** at 4 and correcting **ADV-0248** and **ADV-0223** from 5→4; documents the final 4/5 distinction between adaptation being materially rewarded and effective resolution depending on sustained coordination of interacting tactical factors; documents exclusions for combat volume, lethality, rules difficulty, puzzle/strategic planning, persistent state, optional extreme material, and raw encounter-count weighting; and updates Working Status to mark Tactical Complexity frozen, corpus-calibrated, and blind-validated while leaving Rules / System-Mastery Demand and Seriousness pending their remaining validation work. |
| **0.11.3** | 2026-08-12 | Accepted | Adds the frozen-for-calibration **Seriousness** rubric and consolidates its full-source calibration record while carrying forward accepted Version 0.11.2 unchanged elsewhere; preserves the exact frozen Pass 1 definition and 1--5 anchors distinguishing Playful, Light, Mixed, Serious, and Sustained Serious; records the full-AVC search that failed to produce a genuine score-1 endpoint, the full-AMC endpoint search and full-source confirmation of **ADV-0013 — A Conspiracy Most Cracked** at 1, and the full-source rejection of **ADV-0278 — Witchlight Carnival** as a 1 in favor of 2; records successful pressure testing of all four adjacent boundaries without changing the rubric wording; records calibration corrections **ADV-0277 — The Wild Beyond the Witchlight** 2→3, **ADV-0053 — Call of the Wild** 2→4, and **ADV-0034 — Tomb of Horrors** 4→5; records working benchmarks across all five score levels and the distinction between objective stakes/danger and the adventure's authored dramatic register; documents that game-like challenge, lethality, horror, or Fantastic Weirdness do not independently determine Seriousness; and updates Working Status to mark Seriousness as full-source calibrated but still pending blind independent validation. |
| **0.11.2** | 2026-08-12 | Accepted | Finalizes **Structural Openness** after endpoint expansion, full-source adjacent-boundary calibration, a twelve-case blind independent pass, and focused adjudication of all three score disagreements; restores the exact frozen Pass 1 definition and core clarifications, keeps the 1--5 anchors unchanged, and adds a narrow post-blind clarification distinguishing substantial site navigation from incidental room-to-room routing toward the same prescribed objective; records calibrated benchmarks across all five score levels, including **ADV-0288 — A Friend in Need** and **ADV-0200 — Lake Monster** at 1 and **ADV-0278 — Witchlight Carnival** and **ADV-0323 — Dungeon Level** at 5; records the pre-blind boundary correction **ADV-0053 — Call of the Wild** 3→2 and the blind adjudication corrections **ADV-0034 — Tomb of Horrors** 2→3 and **ADV-0040 — Expedition to the Barrier Peaks** 3→4 while retaining **ADV-0288 — A Friend in Need** at 1; documents the treatment of developed false/punitive routes, macro gates, scale weighting, and the 4/5 distinction between dominant openness and player-directed ordering as the fundamental organizing structure; records 9/12 initial blind score reproduction and 11/12 agreement with final benchmark scores after adjudication; leaves blind path-sensitivity disagreements outside this integer-score calibration update; and updates Working Status to mark Structural Openness as frozen, corpus-calibrated, and blind-validated. |
| **0.11.1** | 2026-08-12 | Accepted | Finalizes **Lethality / Failure Severity** after full-source calibration and blind validation; restores the exact frozen Pass 1 definition, clarifications, and 1--5 anchors as the normative rubric; records the targeted AVC score-1 endpoint **ADV-0278 — Witchlight Carnival** and calibrated benchmarks across all five score levels; records successful source-grounded testing of all four adjacent boundaries; records 9/9 exact blind reproduction of both scores and path-sensitivity judgments with no benchmark adjudications or wording changes required; documents the severity/readiness interaction, recovery and fail-forward weighting, campaign-scale density, recoverable death, and why ordinary theoretical combat lethality or an isolated TPK branch does not determine the score; updates Working Status to mark Lethality as frozen, corpus-calibrated, and blind-validated while leaving Tactical Complexity, Rules / System-Mastery Demand, and Structural Openness provisional. |
| **0.11-draft** | 2026-08-12 | Draft | Carries forward accepted Version 0.10 unchanged and consolidates the four parallel Challenge Character / Adventure Structure calibration tracks by adding frozen-for-calibration 1--5 rubrics for **Tactical Complexity**, **Lethality / Failure Severity**, **Rules / System-Mastery Demand**, and **Structural Openness**; records their current conceptual distinctions and boundary commentary, including Tactical Complexity's recurrence/layering/evolving-state distinctions, Lethality's severity/readiness and recovery-buffer weighting, System-Mastery's separation from tactics and puzzles plus the rules that basic checks/attacks are not mastery, level is evidence rather than destiny, and adventure-specific player-facing systems count, and Structural Openness's focus on player-directed major progression rather than local choice or Consequential Player Agency; explicitly leaves these four rubrics provisional at the ontology level pending completion/consolidation of calibration and independent validation rather than treating parallel working state as accepted ontology state. |
| **0.10** | 2026-08-11 | Accepted | Freezes the Puzzle / Problem-Solving Emphasis rubric after source-grounded adjacent-boundary calibration and nine-case blind validation; records calibrated benchmarks across all five score levels; records pre-blind source adjudications (**ADV-0040** 3→2, **ADV-0062** 3→2, **ADV-0277** 4→3); records the targeted AVC score-4 search and full-source placement of **ADV-0031 — White Plume Mountain** at 4; records blind 1/2 disagreements and final source adjudications (**ADV-0040** 2→1, **ADV-0262** 2→1, **ADV-0287** 1→2); documents the 1/2 boundary between ordinary opportunities for cleverness and authored substantive problem-solving; corrects the Working Status count of still-unanchored interpretive dimensions from eleven to twelve; and leaves the Puzzle / Problem-Solving definition, clarification, and 1--5 anchors unchanged. |
| **0.10-draft** | 2026-08-11 | Draft | Carries forward Version 0.9-draft unchanged and adds the provisional Puzzle / Problem-Solving Emphasis 1--5 rubric; defines substantive problem-solving as overcoming explicit noncombat obstacles, mechanisms, constraints, or challenges through reasoning, experimentation, resource/information combination, or supported creative solutions rather than puzzle count, difficulty, ability-check frequency, general cleverness, or combat tactics; distinguishes Puzzle / Problem-Solving from Investigation, Exploration, Tactical Complexity, and Rules / System-Mastery Demand while allowing the same scene to contribute to multiple dimensions for different reasons; and freezes the Puzzle / Problem-Solving definition, clarification, and anchors unchanged for the initial eight-adventure AVC calibration Pass 1 without declaring the rubric calibrated. |
| **0.9** | 2026-08-11 | Accepted | Freezes the Investigation Emphasis rubric after source-grounded adjacent-boundary calibration and nine-case blind validation; records calibrated benchmarks across all five score levels; records **ADV-0234 — The Styes** as the targeted score-5 endpoint; records final blind adjudications (**ADV-0062 — No Honour Among Thieves** 2→1 and **ADV-0040 — Expedition to the Barrier Peaks** 1→2) as benchmark-application corrections rather than rubric changes; documents the 1/2, 2/3, 3/4, and 4/5 boundary distinctions; records 9/9 agreement between the final source-grounded scores and the blind independent pass; corrects the Working Status count of still-unanchored interpretive dimensions to thirteen; and leaves the Investigation definition, clarification, and 1--5 anchors unchanged. |
| **0.9-draft** | 2026-08-11 | Draft | Carries forward accepted Version 0.8 unchanged and adds the provisional Investigation Emphasis 1--5 rubric; clarifies that Investigation measures substantive gathering, connecting, interpreting, and testing of information rather than mystery theme, hidden-information volume, clue count, search frequency, or isolated checks; distinguishes Investigation from Social Interaction, Exploration, and Puzzle / Problem-Solving while allowing the same scene to contribute to multiple dimensions for different reasons; and freezes the Investigation definition, clarification, and anchors unchanged for the initial eight-adventure AVC calibration Pass 1 without declaring the rubric calibrated. |
| **0.8** | 2026-08-11 | Accepted | Freezes the Social Interaction Emphasis 1--5 rubric after AVC calibration and blind validation; records calibrated benchmarks across all five score levels; records source-grounded blind adjudications (**ADV-0040** 2→3, **ADV-0053** 3→2, **ADV-0277** 4→5); records **ADV-0229 — Danger at Dunwater** as the targeted score-5 endpoint; records the targeted score-4 endpoint search, full-source review, and independent blind reproduction of **ADV-0257 — The Magister's Masquerade** at 4; and leaves the Social definition, clarification, and 1--5 anchors unchanged. |
| **0.7** | 2026-08-11 | Accepted | Records blind independent validation of the frozen Exploration Emphasis rubric; moves **ADV-0092 — An Actor's Life** from 1→2 after source-grounded adjudication and records it as path-sensitive; replaces the score-1 endpoint with source-reviewed **ADV-0170 — The Shadow Parliament**, **ADV-0169 — Clockwork Memories**, and **ADV-0198 — Cold-Hearted Killer** after a targeted Adventure Master Catalog endpoint search; and leaves the frozen Exploration definition, clarification, and 1--5 anchors unchanged. |
| **0.6** | 2026-08-11 | Accepted | Records blind independent validation of the frozen Combat Emphasis rubric; updates calibrated benchmark assignments after source-grounded adjudication (**ADV-0062** 2→3, **ADV-0277** 2→1, **ADV-0287** 3→2); records the corrected canonical-unit blind reassessment of **ADV-0262** at 4; and leaves the frozen Combat definition and 1--5 anchors unchanged. |
| **0.5** | 2026-08-10 | Accepted | Freezes the Exploration Emphasis 1--5 rubric after AVC calibration; records calibrated benchmark adventures across all five score levels; records successful adjacent-boundary testing, including the distinction between incidental environmental interaction at score 1 and meaningful but secondary exploration at score 2, and the distinction between high exploration and exploration as the adventure's primary organizing structure at score 5; and requires explicit ontology revision and revalidation for future changes to the Exploration anchors. |
| **0.5-draft** | 2026-08-10 | Draft | Adds the provisional Exploration Emphasis 1--5 rubric; clarifies that exploration measures substantive environmental discovery, navigation, traversal, and interaction rather than geographic scale, room count, travel alone, or Structural Openness; and freezes the rubric unchanged for the initial eight-adventure AVC calibration Pass 1. |
| **0.4** | 2026-08-09 | Accepted | Freezes the Combat Emphasis 1--5 rubric after AVC calibration; records calibrated benchmark adventures across all five score levels; records successful adjacent-boundary testing, including the 4/5 distinction; and requires explicit ontology revision and revalidation for future changes to the Combat anchors. |
| **0.3-draft** | 2026-08-09 | Draft | Locks assessment-state handling: blank score = Not Yet Assessed; `-1` = Insufficient Evidence; `1`--`5` = scored; confidence applies only to scored values; and `-1` must be excluded from numerical use of the 1--5 scale. |
| **0.2-draft** | 2026-08-09 | Draft | Adds the provisional common scoring framework for the seventeen interpretive dimensions; adopts a 1--5 absolute integer scale, 0--100% confidence, canonical Adventure ID scoring, expected-table-play and substantially-as-published principles, dimensional separation, and path-sensitivity flagging; records insufficient-evidence handling as an open question; and adds the first provisional rubric for Combat Emphasis. |
| **0.1-draft** | 2026-08-08 | Draft | Establishes the provisional 19-dimension AdventureFinder ontology: two editorially assessed matching dimensions and seventeen interpretive analysis dimensions. |
