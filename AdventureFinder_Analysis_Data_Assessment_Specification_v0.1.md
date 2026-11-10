# AdventureFinder

# Analysis Data / Assessment Specification

## Version 0.1

**Status:** Accepted  
**Date:** 2026-08-12  
**Assumed Ontology:** AdventureFinder Analysis Ontology (AFAO) 1.0  
**Purpose:** Canonical logical data contract and production assessment protocol for transforming AFAO-defined adventure characteristics into an auditable AdventureFinder analysis dataset.

---

## 1. Purpose

This specification defines how AdventureFinder analytical assessments are created, represented logically, reviewed, accepted, corrected, versioned, and retained as canonical analysis data.

The **AdventureFinder Analysis Ontology (AFAO)** defines what AdventureFinder measures and how each dimension is assessed. This specification defines how those measurements become production data.

In short:

> **AFAO defines the ruler. This specification defines how AdventureFinder uses the ruler and records the measurement.**

The specification has four primary responsibilities:

1. define the canonical **logical assessment model** linked to each Adventure ID;
2. define the **full-source production assessment procedure** used to create those assessments;
3. define **quality-control, review, correction, and adjudication rules**; and
4. define the **provenance and versioning requirements** needed to keep the dataset auditable over time.

This document intentionally does **not** choose the exact physical workbook layout, relational database schema, document store, file format, column naming convention, API representation, or search-index representation. Those are implementation decisions to be made after the logical semantics and production protocol are sufficiently stable.

---

## 2. Scope and Authority

This specification governs the AdventureFinder **analysis data layer**.

It applies to:

- editorially assessed matching values defined by AFAO;
- interpretive AFAO dimension scores;
- supporting confidence values;
- path-sensitivity flags;
- practical duration ranges where defined by AFAO;
- assessment state;
- source and evidence provenance;
- assessment rationales;
- review status;
- audit history;
- correction and supersession behavior; and
- AFAO-version migration.

This specification does **not** govern:

- which published works constitute canonical adventures;
- Adventure ID assignment;
- canonical adventure titles, source books, publishers, or page boundaries;
- the meaning or scoring anchors of AFAO dimensions;
- natural-language query interpretation;
- recommendation weighting or ranking;
- user preference modeling;
- community reviews or ratings; or
- overall adventure quality judgments unless a future ontology explicitly adds such a dimension.

Where responsibilities overlap, authority is divided as follows:

1. **Adventure Catalog Editorial Specification** — canonical Adventure ID and bibliographic/structural identity;
2. **Adventure Boundary Detection Specification** — determination of discrete playable adventure boundaries and nested-adventure identity;
3. **AFAO** — dimension definitions, scoring anchors, matching-dimension rules, calibration guidance, and dimension-specific assessment semantics;
4. **This specification** — production assessment procedure, logical assessment data model, provenance, acceptance, review, correction, and version lifecycle;
5. **Future Query Interpretation and Matching specifications** — translation of user requests into constraints/preferences and ranking of assessed adventures.

If this specification conflicts with AFAO about the meaning of a dimension or its permitted values, **AFAO controls**.

If this specification conflicts with the accepted Adventure Catalog or Boundary Specification about what material belongs to an Adventure ID, **the accepted catalog/boundary decision controls**.

---

## 3. Governing Principles

All production AdventureFinder assessments MUST preserve the following principles.

### 3.1 Canonical Adventure Identity

Every assessment applies to one canonical **Adventure ID**.

The analysis layer MUST NOT silently substitute:

- a containing source book;
- a parent campaign;
- an anthology;
- a chapter;
- a dungeon level;
- an adjacent adventure; or
- another playable unit

for the canonical Adventure ID being assessed.

Nested adventures are scored as their own canonical units when they have their own accepted Adventure IDs. Parent and child adventures MAY legitimately overlap in source pages and playable material. Such overlap does not erase either canonical identity.

### 3.2 Full-Source, Evidence-Based Assessment

Production assessments MUST be grounded in the published material relevant to the canonical Adventure ID.

Scores MUST NOT be assigned from title, reputation, product marketing, community consensus, memory of a different edition, prior AdventureFinder recommendation output, or superficial summaries when the full relevant source is available.

### 3.3 Substantially-as-Published Play

Assessments describe the adventure as it is ordinarily supported and expected to be played from the published material.

They do not describe:

- extensive rewrites;
- hypothetical GM improvements;
- homebrew transformations;
- unusually optimized or speed-run play;
- exhaustive completion of every technically available optional element; or
- a single rare path merely because it is possible.

### 3.4 Expected Table Play Over Document Form

AdventureFinder measures expected substantive play, not page count, encounter count, chapter count, keyed-room count, or other document-level proxies unless AFAO explicitly defines otherwise.

Document structure may provide evidence. It MUST NOT replace analysis of playable structure.

### 3.5 Dimension Independence

Each AFAO dimension MUST be assessed under its own frozen definition and anchors.

A score on one dimension MUST NOT be used as an implicit substitute for another dimension merely because the concepts correlate.

Examples include:

- Combat Emphasis is not Tactical Complexity;
- Lethality / Failure Severity is not Rules / System-Mastery Demand;
- Structural Openness is not Consequential Player Agency;
- Seriousness is not Darkness / Horror Intensity;
- GM Preparation Burden is not GM Beginner Suitability.

### 3.6 Best-Supported Assessment Rather Than Central-Tendency Bias

When evidence supports a score but uncertainty remains, the assessor MUST choose the best-supported permitted value and represent uncertainty through the supporting fields defined by AFAO.

Assessors MUST NOT drift toward middle values merely because they are uncertain.

### 3.7 Auditability

A later reviewer SHOULD be able to determine:

- what was assessed;
- under which AFAO version;
- under which production protocol version;
- from which source material;
- what value was assigned;
- why it was assigned;
- how confident the assessor was;
- whether material path variation was significant;
- whether the assessment was reviewed or corrected; and
- which value is currently canonical.

### 3.8 No Silent Mutation

Accepted assessments MUST NOT silently change.

Corrections, re-assessments, ontology migrations, and supersessions MUST leave an audit trail sufficient to distinguish the old state from the new state.

---

## 4. Canonical Assessment Unit

The fundamental production unit is an **Adventure Assessment Package**.

An Adventure Assessment Package represents the complete AdventureFinder analytical assessment of:

> **one canonical Adventure ID under one AFAO version, produced under one declared assessment-protocol version and source basis.**

Conceptually:

`Adventure ID + AFAO Version -> Adventure Assessment Package`

The package contains:

1. identity and provenance metadata;
2. the AFAO editorially assessed matching values;
3. one assessment for every interpretive AFAO dimension;
4. supporting rationale and evidence information;
5. package-level quality-control and review state; and
6. audit history sufficient to preserve corrections and supersession.

A physical implementation MAY store these elements in one table, multiple tables, workbook sheets, structured documents, or another representation. This specification does not prescribe that choice.

---

## 5. Logical Assessment Model

### 5.1 Adventure Assessment Package Metadata

Every completed or attempted Adventure Assessment Package MUST logically retain the following information:

| Logical element | Purpose |
| --- | --- |
| **Adventure ID** | Links the assessment to the canonical Adventure Catalog record. |
| **AFAO Version** | Identifies the ontology/rubric version whose meanings and anchors govern the values. |
| **Assessment Specification Version** | Identifies the production protocol used to create the assessment. |
| **Source Basis** | Identifies the source material actually used for assessment. |
| **Assessment Date** | Records when the assessment was completed or last substantively revised. |
| **Assessment Status** | Identifies whether the package is in draft, review, accepted, superseded, or another defined lifecycle state. |
| **Assessment Method / Assessor Provenance** | Records enough information to distinguish assessment runs or responsible editorial processes when needed for audit. |

The exact physical identifiers, timestamps, user IDs, model IDs, hashes, or storage formats are implementation choices and are not fixed by v0.1.

### 5.2 Canonical Matching Values

Under the assumed AFAO 1.0, the Adventure Assessment Package MUST logically support the following canonical matching values:

- **# of Sessions**
- **Level Start**
- **Level End**

These are not 1--5 interpretive scores.

Where AFAO defines supporting values for a matching dimension, those values remain part of the logical assessment. For # of Sessions, this includes the AFAO-defined supporting information such as Practical Range, Confidence, and Path Sensitive. For Levels, uncertainty and evidence-basis handling follow AFAO rather than the interpretive-score sentinel rules.

### 5.3 Interpretive Dimension Assessments

For each interpretive AFAO dimension, the package MUST logically retain one **Dimension Assessment**.

A scored Dimension Assessment contains at minimum:

| Logical element | Purpose |
| --- | --- |
| **Dimension Identity** | Identifies the AFAO dimension being assessed. |
| **Assessment State** | Distinguishes Not Yet Assessed, Scored, and Insufficient Evidence as defined by AFAO. |
| **Score** | The AFAO-permitted score when assessment state is Scored. |
| **Confidence** | 0%--100% confidence in the assigned score when AFAO requires confidence. |
| **Path Sensitive** | Indicates whether substantially supported published paths materially affect the dimension when AFAO defines this support field. |
| **Rationale** | Concise source-grounded explanation of the placement. |
| **Evidence Basis / Pointers** | Sufficient source information to support later audit or adjudication. |

A physical implementation MAY represent dimensions as fields, rows, documents, key-value entries, or other structures. The logical requirement is that each dimension's assessment remains separately addressable and auditable.

### 5.4 Evidence Items

An assessment MAY retain one or more separately addressable **Evidence Items**.

An Evidence Item conceptually identifies:

- the Adventure ID;
- the assessed dimension or matching value to which it applies;
- the source or source component;
- a locator such as page, chapter, section, encounter, table, appendix, or other stable reference when available;
- a concise description of what the evidence establishes; and
- when useful, the evidentiary character defined by the relevant AFAO rubric, such as explicit, derived, or editorially inferred.

This specification does not require exhaustive citation of every supporting passage. It requires enough retained evidence to make accepted assessments meaningfully auditable.

### 5.5 Audit Events

The logical model MUST be capable of preserving an **Audit Event** when an accepted assessment changes.

An Audit Event SHOULD be able to establish:

- what changed;
- the previous value or state;
- the new value or state;
- why the change occurred;
- whether the change was an assessment correction, adjudication, source correction, or ontology migration; and
- when the change became authoritative.

The exact storage mechanism for audit history is deferred.

---

## 6. Assessment States and Null Semantics

Assessment state MUST be represented explicitly enough that downstream systems cannot confuse missing work with negative evidence.

### 6.1 Interpretive Dimensions

Interpretive dimensions follow AFAO:

- **Not Yet Assessed** — no completed assessment exists;
- **Insufficient Evidence** — assessment was attempted but the available published evidence cannot responsibly support a 1--5 placement;
- **Scored** — the evidence supports a best assessment on the 1--5 scale.

Where a compatibility export uses the AFAO sentinel `-1` for Insufficient Evidence, that value remains a sentinel and MUST NOT participate in numerical interpretation of the 1--5 scale.

A physical database or workbook MAY represent state explicitly rather than relying solely on blank/`-1` conventions, provided exported data preserves AFAO semantics.

### 6.2 # of Sessions

# of Sessions follows the AFAO assessment-state rules for that matching dimension:

- Not Yet Assessed;
- Insufficient Evidence; or
- Assessed with a positive whole-number normalized session estimate.

The `-1` compatibility sentinel, where used, MUST NOT participate in duration arithmetic, ranking, filtering, averages, or other operations that treat it as an actual session count.

### 6.3 Level Start and Level End

Levels follows its own AFAO uncertainty semantics.

Each endpoint may be:

- Not Yet Assessed;
- an assessed discrete integer; or
- **Uncertain / Requires Source Verification** when the available evidence cannot responsibly establish that endpoint.

The interpretive `-1` sentinel MUST NOT be used as a Level Start or Level End value.

If one endpoint is supported and the other is not, the supported endpoint SHOULD remain assessed while the unresolved endpoint is explicitly uncertain.

### 6.4 Blank Is Not Zero

A blank, null, omitted, or Not Yet Assessed value MUST NOT be interpreted as:

- score 0;
- no combat;
- no exploration;
- no horror;
- zero sessions;
- level 0;
- low confidence; or
- negative evidence of any kind.

---

## 7. Source Basis and Evidence Requirements

### 7.1 Source Hierarchy

Production assessments SHOULD use evidence in the following order of authority:

1. **published source text and playable procedures belonging to the canonical Adventure ID**;
2. **adventure-specific maps, appendices, handouts, tables, stat blocks, and support material materially relevant to the assessed dimension**;
3. **shared source-book material explicitly required to understand or run the canonical adventure**;
4. **accepted Adventure Catalog and Boundary decisions needed to establish canonical identity and scope**;
5. **AFAO calibration benchmarks and accepted precedents**, only for rubric application checks rather than as substitutes for source evidence;
6. **editorial inference**, only when stronger evidence does not fully resolve the assessment.

External reviews, community discussions, actual-play reports, publisher marketing copy, and general reputation are not primary production evidence unless AFAO or a later specification explicitly authorizes them for a defined purpose.

### 7.2 Full Relevant Source Requirement

A production scorer MUST inspect the full relevant source body before finalizing an Adventure Assessment Package.

"Full relevant source" does not require identical attention to every sentence. It requires enough systematic coverage to understand:

- the adventure's beginning and resolution;
- its principal playable structure;
- expected routes and progression;
- major locations and encounter types;
- optional and mutually exclusive material;
- advancement and duration instructions;
- adventure-specific procedures;
- materially relevant appendices or shared rules; and
- supported alternate resolutions or paths.

For short adventures this will ordinarily mean reading essentially all substantive adventure material.

For long campaigns, structured full-source coverage MAY be used, but the scorer MUST NOT finalize the package from an introduction, synopsis, chapter summaries, or selected representative chapters alone.

### 7.3 Context Outside the Canonical Boundary

Material outside the canonical Adventure ID MAY be consulted when necessary to understand:

- an inherited hook;
- a parent-campaign premise;
- shared procedures;
- an explicitly referenced rule;
- terminal advancement ownership;
- a transition into or out of nested material; or
- another fact necessary to interpret the canonical unit.

Such context MUST NOT silently enlarge the scored unit.

### 7.4 Source Completeness

Before scoring, the assessor SHOULD determine whether the available source is sufficiently complete for responsible full-source assessment.

Potential source defects include:

- missing pages or sections;
- corrupted extraction;
- absent tables or maps whose contents materially affect play;
- incomplete appendices;
- ambiguous canonical boundaries; or
- conversion errors that remove important rules text.

A source defect does not automatically invalidate every dimension. The assessor SHOULD distinguish dimensions that remain responsibly assessable from those requiring Insufficient Evidence or Source Verification.

---

## 8. Production Assessment Protocol

A production Adventure Assessment Package SHOULD be created in the following order.

### Step 1 — Confirm the Canonical Target

Before scoring, establish:

- Adventure ID;
- Adventure Title for human verification;
- canonical source;
- accepted Start Page and End Page or equivalent canonical boundary;
- whether the adventure is nested inside a parent Adventure ID; and
- any accepted overlapping parent/child relationship relevant to source interpretation.

If the canonical target itself is unresolved, analytical scoring SHOULD pause until the boundary/identity problem is resolved or explicitly escalated.

### Step 2 — Confirm the Governing Versions

Record the AFAO version and the Assessment Specification version before beginning substantive scoring.

The scorer MUST use the definitions and anchors from the declared AFAO version throughout the package.

A single Adventure Assessment Package MUST NOT silently mix anchors from different AFAO versions.

### Step 3 — Establish the Source Basis

Identify the source material available for assessment and determine whether it supports full relevant-source coverage.

Record any material source limitations before final scoring.

### Step 4 — Perform Full-Source Structural Review

Read or systematically inspect the canonical adventure as a complete playable unit.

Before locking dimension values, establish a working model of:

- core/mandatory material;
- common optional material;
- rare or highly conditional material;
- mutually exclusive branches;
- supported bypasses;
- randomized structure;
- alternate resolutions;
- likely ordinary completion trajectory; and
- materially divergent published paths.

This working model is the common weighting basis for the later dimension assessments.

### Step 5 — Assess # of Sessions

Apply the frozen AFAO # of Sessions rubric to the canonical Adventure ID.

Record the AFAO-required primary and supporting values, including as applicable:

- best whole-number Normalized Sessions estimate;
- Practical Range;
- Confidence;
- Path Sensitive; and
- assessment state.

Do not estimate duration from page count, level range, publisher format label, or in-fiction time as a mechanical proxy.

### Step 6 — Assess Level Start

Apply the frozen AFAO Levels rubric.

Determine the primary intended character level at which ordinary substantially-as-published play of the canonical Adventure ID begins.

Explicit alternate starts or scalable support MUST NOT overwrite the primary Level Start merely because they are available.

### Step 7 — Assess Level End

Follow the canonical adventure through completion and determine the character level the published adventure expects characters to have reached by completion.

Include advancement explicitly awarded as part of completing the canonical Adventure ID.

Exclude advancement that occurs only upon entering, beginning, or undertaking subsequent canonical material outside the assessed Adventure ID.

If the endpoint cannot be responsibly established, use the AFAO Levels uncertainty state rather than inventing precision.

### Step 8 — Assess Each Interpretive Dimension Independently

For every interpretive AFAO dimension:

1. read the frozen definition and score anchors;
2. identify the source evidence materially relevant to that dimension;
3. weight expected substantially-as-published play rather than pages or raw counts;
4. assign the best-supported permitted score;
5. test the proposed score against the immediately lower and higher anchors when they exist;
6. assign Confidence;
7. determine Path Sensitive status; and
8. record a concise source-grounded rationale and sufficient evidence basis.

All interpretive dimensions SHOULD be attempted unless the production task explicitly scopes a partial assessment.

### Step 9 — Perform Adjacent-Anchor Falsification

Before finalizing a scored interpretive dimension, the assessor SHOULD be able to answer two questions:

> **Why does this adventure satisfy the assigned anchor rather than the immediately lower anchor?**

and, when a higher anchor exists:

> **What prevents the adventure from satisfying the immediately higher anchor?**

This is a falsification check, not a requirement to write long comparison essays.

If the assessor cannot distinguish the adjacent anchors after full-source review, the score MAY still be assigned when one remains best supported, but Confidence SHOULD reflect the unresolved boundary uncertainty.

### Step 10 — Perform Path-Sensitivity Review

For each dimension that supports a Path Sensitive flag, ask whether **substantially supported published paths** could materially change the experience on that dimension.

Path sensitivity MUST arise from authored structure, not merely from universal table-to-table variation or hypothetical GM rewriting.

When Path Sensitive is Yes:

- retain one best canonical score representing expected substantially-as-published play;
- record the flag;
- explain the material variation briefly; and
- do not silently average incompatible paths into a score that represents none of them well.

### Step 11 — Perform Confidence Review

Confidence expresses confidence in the correctness of the assessment under the frozen rubric, not the strength or intensity of the dimension.

The assessor SHOULD consider:

- clarity and completeness of source evidence;
- stability against adjacent anchors;
- degree of optionality or branching;
- source quality;
- dependence on editorial inference;
- whether materially supported paths pull toward different anchors; and
- whether the relevant AFAO calibration guidance yields a stable application.

Confidence MUST NOT be used to alter the score toward the middle of the scale.

### Step 12 — Record Rationale and Evidence

For each scored interpretive dimension, record a concise rationale sufficient to explain the placement to a future reviewer.

The rationale SHOULD normally identify:

- the dominant source-supported facts that drive the score;
- the decisive adjacent-anchor distinction when material; and
- any path-sensitive or uncertainty issue that materially affects interpretation.

Rationales SHOULD be concise. They are an audit trace, not a replacement for AFAO or a full adventure summary.

### Step 13 — Conduct Package-Level Quality Control

After all values are assessed, conduct a separate package-level review for:

- canonical-unit contamination from parent or containing material;
- missed source sections;
- accidental dimension conflation;
- inconsistent application of substantially-as-published weighting;
- unsupported precision;
- confidence values inconsistent with the stated rationale;
- path-sensitive structure that was overlooked;
- invalid values or sentinel use;
- Level Start / Level End ownership mistakes;
- # of Sessions values inconsistent with the AFAO normalization rules; and
- rationales that do not actually support their scores.

This quality-control step MUST NOT force scores into a visually or conceptually "coherent" vector. Unusual combinations of dimension values may be correct.

### Step 14 — Determine Review Disposition

The completed package receives a production disposition under Section 12.

---

## 9. Confidence Guidance

### 9.1 Meaning

Confidence answers:

> **How strongly does the available published evidence support this specific assessment under the declared AFAO version?**

It does not answer:

- how intense the dimension is;
- how much the assessor likes the adventure;
- how reliable tabletop play is in general; or
- how similar the adventure is to a benchmark.

### 9.2 Confidence Is Supporting Metadata

Confidence MUST NOT replace the canonical score.

For interpretive dimensions, a low-confidence `5` remains a score of `5` until corrected or superseded. It MUST NOT be treated as a hidden `4`, `4.5`, or weighted midpoint unless a future matching specification explicitly defines a separate use of confidence.

### 9.3 Guidance Bands

Until empirically refined by production pilots, the following bands SHOULD be treated as descriptive guidance rather than hard statistical calibration:

| Confidence | Guidance |
| ---: | --- |
| **90--100%** | Source evidence and anchor application are very strong; adjacent alternatives are clearly inferior. |
| **75--89%** | Best assessment is well supported, with limited genuine interpretive uncertainty. |
| **60--74%** | Best assessment remains defensible, but an adjacent alternative is materially plausible or source evidence is incomplete/indirect. |
| **Below 60%** | Significant assessment uncertainty exists and editorial review will ordinarily be appropriate. |

These bands MAY be revised after production-pipeline validation without changing dimension meanings, provided any revision is versioned in this specification.

### 9.4 Review Threshold

Version 0.1 does **not** permanently freeze a universal automatic-review threshold.

The production pilot SHOULD measure confidence behavior across assessors and use those results to set or revise an operational threshold.

Until then, confidence below 60% SHOULD normally trigger review, while 60--74% MAY trigger review depending on the source of uncertainty and project policy.

---

## 10. Path-Sensitivity Guidance

### 10.1 Definition

Unless a dimension-specific AFAO rubric defines a narrower rule, record **Path Sensitive: Yes** when:

> **two or more substantially supported published paths through the canonical Adventure ID can produce meaningfully different experiences on the assessed dimension, and that variation is material to interpreting the canonical assessment.**

### 10.2 What Qualifies

Potential qualifying structures include:

- mutually exclusive major branches;
- faction choices producing materially different play;
- published violent and nonviolent resolutions with substantially different experiential consequences;
- optional regions or objectives whose omission materially changes the assessed dimension;
- randomized structures that produce materially different play bodies; or
- alternate endings or routes that cross or seriously pressure an AFAO anchor boundary.

### 10.3 What Does Not Qualify by Itself

The following do not automatically establish path sensitivity:

- ordinary player creativity;
- the possibility of bypassing one minor encounter;
- differences in table pacing;
- a GM's ability to rewrite the adventure;
- theoretical behavior not substantially supported by the source;
- minor encounter-order differences; or
- variation that does not materially affect the dimension.

### 10.4 Canonical Score Under Path Sensitivity

Path sensitivity does not eliminate the canonical score.

The assessor MUST still assign the best-supported canonical score when the evidence supports one, representing ordinary substantially-as-published play.

The flag and rationale preserve the material variation instead of replacing the score with an unbounded average.

---

## 11. Rationale and Evidence Provenance

### 11.1 Rationale Requirement

Every accepted scored interpretive Dimension Assessment SHOULD retain a concise rationale.

Every accepted # of Sessions and Levels assessment SHOULD retain enough source evidence to support later audit, especially when the value required editorial inference.

### 11.2 Rationale Content

A useful rationale ordinarily contains one to four concise sentences identifying:

- what the expected play actually does on this dimension;
- what source-supported features dominate the assessment;
- why the adjacent anchor is not a better fit when that distinction is non-obvious; and
- any important path-sensitive or confidence caveat.

### 11.3 Evidence Pointers

Evidence pointers SHOULD be retained when practical, especially for:

- explicit level or advancement instructions;
- explicit duration claims;
- unusual rules or procedures central to a score;
- decisive branching or bypass language;
- score-boundary adjudications;
- low-confidence assessments; and
- later corrections.

A source locator MAY refer to a page, section, chapter, encounter, keyed area, table, appendix, or another stable source location.

### 11.4 No Exhaustive Annotation Requirement

Version 0.1 does not require every paragraph or encounter to be exhaustively annotated.

Evidence capture should be sufficient for audit and adjudication without turning production scoring into full textual markup of every source.

---

## 12. Quality Control and Review Disposition

### 12.1 Package Lifecycle States

The logical model SHOULD support at least the following package-level lifecycle states:

- **Draft** — assessment work is incomplete or has not passed production QC;
- **Review Required** — assessment is complete enough to inspect but one or more review triggers are present;
- **Accepted** — package is authorized for use as the canonical assessment under its declared AFAO version;
- **Superseded** — a later accepted assessment replaces this package for canonical use while preserving it for history.

A physical implementation MAY use additional operational states, but their meaning MUST NOT obscure which assessment is canonical.

### 12.2 Review Triggers

A completed package SHOULD enter review when one or more of the following is present:

- confidence below the current operational review threshold;
- Insufficient Evidence on a matching or interpretive value important to package completeness;
- Level Start or Level End marked Uncertain / Requires Source Verification;
- source corruption or incompleteness materially affects assessment;
- canonical boundary or nesting uncertainty remains;
- path-sensitive branches materially pressure or cross an anchor boundary and the canonical score remains difficult to stabilize;
- the scorer identifies apparent ambiguity in AFAO wording rather than ordinary application uncertainty;
- the scorer identifies a possible contradiction between AFAO rules;
- adjacent-anchor falsification cannot produce a stable best assessment;
- a regression case fails unexpectedly; or
- automated validation detects invalid state/value combinations.

### 12.3 Path Sensitivity Alone Is Not a Defect

Path Sensitive: Yes MUST NOT automatically require human review.

Path sensitivity is a legitimate property of published adventures. Review is warranted when the path variation makes the canonical assessment unstable or exposes a methodological problem, not merely because variation exists.

### 12.4 Acceptance Authority

An assessment becomes canonical only through an **authorized acceptance process**.

Version 0.1 deliberately does not require that every package be manually approved by a human editor. The production implementation MAY eventually authorize automatic acceptance for packages that pass defined quality criteria while routing exceptions to human review.

Whatever process is adopted MUST:

- distinguish Draft/Review results from Accepted results;
- preserve who or what authorized acceptance sufficiently for audit; and
- prevent unreviewed revisions from silently replacing accepted data.

---

## 13. Blindness and Anti-Bias Requirements

### 13.1 Production Scoring Independence

When assessing a new or independently re-assessed adventure, the scorer SHOULD ordinarily be blinded to prior target-adventure analytical outcomes that could bias rubric application.

The scorer SHOULD NOT be given, unless required for a defined review purpose:

- prior target-adventure scores;
- prior target-adventure confidence values;
- prior rationales;
- AdventureFinder recommendation rank;
- expected user matches;
- community ratings;
- popularity signals; or
- instructions that a particular score is expected.

### 13.2 Calibration Benchmarks

AFAO calibration benchmarks MAY be available as rubric-application guidance where AFAO intentionally includes them.

They MUST NOT be treated as substitutes for the score anchors or for full-source analysis.

The governing question remains whether the target adventure satisfies the frozen anchor meaning, not which benchmark it superficially resembles.

### 13.3 Regression Tests

Known calibrated adventures MAY be deliberately rescored in controlled regression tests.

In those tests, the scoring agent SHOULD be blinded to the expected result until after the assessment is locked.

Regression failures SHOULD trigger diagnosis of:

- source differences;
- canonical-unit mistakes;
- assessment-protocol drift;
- rubric-application drift; or
- genuine evidence that an accepted benchmark may require correction.

Regression results MUST NOT silently rewrite accepted AFAO calibration history.

---

## 14. Corrections, Adjudication, and Supersession

### 14.1 Assessment Correction

An **Assessment Correction** occurs when an accepted value is determined to have been incorrectly applied under the **same AFAO version**.

Examples include:

- overlooked source material;
- scoring the parent campaign instead of the canonical nested Adventure ID;
- misreading an advancement instruction;
- applying the wrong adjacent anchor;
- copying an incorrect value; or
- failing to account for a materially supported path required by the frozen rubric.

A correction changes the canonical assessment while preserving the previous accepted state in audit history.

The correction MUST NOT be misrepresented as an ontology change merely because the score changed.

### 14.2 Adjudication

An **Adjudication** resolves a substantive disagreement about how the frozen rubric applies to the source.

Adjudication SHOULD record:

- the competing interpretations;
- the decisive source evidence;
- whether the disagreement arose from application error, reviewer error, or genuine wording ambiguity; and
- the resulting canonical assessment or specification action.

If the adjudication reveals genuine AFAO wording ambiguity that cannot be resolved by application guidance without changing meaning, the issue SHOULD be logged for a future AFAO revision rather than silently altering the frozen ontology.

### 14.3 Ontology Migration

An **Ontology Migration** occurs when an adventure is assessed under a new AFAO version whose dimension definitions, anchors, or assessment rules differ materially.

The old assessment remains historically valid as an assessment under the older AFAO version unless separately corrected.

A new AFAO version therefore produces a new versioned assessment rather than silently overwriting the old one.

Conceptually:

`ADV-XXXX / AFAO 1.0 -> Assessment A`

`ADV-XXXX / AFAO 1.1 -> Assessment B`

Both MAY coexist historically even though only one is current for a given production context.

### 14.4 Supersession

When a new accepted assessment replaces a prior accepted assessment for the same Adventure ID and AFAO version, the prior assessment becomes **Superseded** rather than deleted.

The system MUST be able to determine which assessment is currently canonical.

---

## 15. Versioning Requirements

AdventureFinder MUST distinguish at least three independent forms of version identity.

### 15.1 AFAO Version

Identifies what the dimensions mean and how their values are assessed.

A change to dimension meaning, anchors, or frozen matching-dimension rules requires an AFAO revision under AFAO's own revision policy.

### 15.2 Assessment Specification Version

Identifies how production assessment is conducted and recorded.

Changes such as the following may require a new version of this specification:

- source-coverage requirements;
- confidence guidance;
- review triggers;
- evidence-retention requirements;
- acceptance workflow;
- anti-bias protocol; or
- correction/audit behavior.

A methodology revision does not automatically imply that AFAO meaning changed.

### 15.3 Source Version / Source Basis

The source basis identifies what published or converted source material was actually assessed.

This matters when:

- a source conversion is corrected;
- a revised printing changes adventure text;
- missing pages are restored;
- OCR/extraction defects are repaired; or
- a different source representation materially changes available evidence.

A source change MAY justify re-assessment even when both AFAO and this specification remain unchanged.

---

## 16. Canonical Data Versus Derived Representations

The **canonical logical assessment data** defined here is distinct from derived representations created for convenience.

Derived forms MAY include:

- wide spreadsheet exports;
- normalized database tables;
- denormalized search-index documents;
- embedding/vector representations;
- recommendation feature vectors;
- display-oriented formatted level ranges;
- duration categories derived from numeric sessions;
- API response objects; or
- cached ranking features.

Derived representations MUST NOT silently change canonical semantics.

Examples:

- `Level Start = 1` and `Level End = 5` may be displayed as `1--5`, but the formatted range is derived presentation;
- a # of Sessions calibration regime may be derived for validation, but it does not replace the numeric session estimate;
- a `-1` Insufficient Evidence export value remains a sentinel and must not become a numerical low score;
- confidence MAY be used later by a matching system only under an explicit matching specification, not by silently modifying the canonical score.

---

## 17. Production Validation and Regression

Before full-corpus scoring begins, AdventureFinder SHOULD validate this production protocol against a controlled pilot.

### 17.1 Pilot Corpus

The pilot SHOULD contain a deliberately diverse set of adventures that exercise:

- short and long duration;
- low and high levels;
- nested and standalone canonical units;
- linear and open structure;
- path-sensitive and path-stable adventures;
- low- and high-confidence calibration cases;
- multiple score anchors across interpretive dimensions; and
- known historical application traps.

Where possible, cases with previously blind-validated AFAO outcomes SHOULD be included because they provide known expected results without requiring new rubric calibration.

### 17.2 What the Pilot Tests

The pilot is not primarily another AFAO calibration exercise.

It tests whether the production process reliably reproduces accepted AFAO application while producing clean, auditable data.

The pilot SHOULD evaluate:

- canonical-target accuracy;
- source completeness handling;
- score reproduction;
- confidence consistency;
- path-sensitivity consistency;
- rationale quality;
- evidence sufficiency;
- review-trigger usefulness;
- rate of false review escalation;
- rate of missed genuine problems; and
- operational cost.

### 17.3 Regression Suite

After acceptance, a subset of stable calibration cases SHOULD become a recurring regression suite for future scoring-pipeline changes.

Pipeline changes that materially reduce benchmark reproduction SHOULD be investigated before broad deployment.

---

## 18. Partial Assessments

AdventureFinder MAY support intentionally partial assessments, such as scoring only one dimension for calibration or adjudication.

A partial assessment MUST clearly identify its scope.

It MUST NOT be mistaken for a complete Adventure Assessment Package.

Unassessed dimensions remain **Not Yet Assessed**, not Insufficient Evidence.

A later complete assessment MAY incorporate or supersede the partial work under the project’s acceptance policy.

---

## 19. LLM Application Guidance

When an LLM is used as a production assessor, reviewer, or adjudication assistant, it MUST treat the accepted Catalog, Boundary Specification, AFAO, and this specification as normative within their respective scopes.

The LLM SHOULD:

1. confirm the exact canonical Adventure ID before scoring;
2. inspect the full relevant source rather than rely on summaries or reputation;
3. distinguish source fact from editorial inference;
4. apply each AFAO dimension independently;
5. use substantially-as-published expected play as the weighting basis;
6. perform adjacent-anchor falsification before locking interpretive scores;
7. assign confidence to the assessment rather than to dimension intensity;
8. flag materially supported path sensitivity without treating all optionality as path sensitivity;
9. use AFAO's correct uncertainty state for the relevant value type;
10. preserve concise rationale and evidence sufficient for audit;
11. surface source defects or genuine rubric ambiguity instead of inventing certainty;
12. avoid using prior target-adventure scores as evidence during independent production scoring; and
13. distinguish corrections under the same AFAO version from migrations to a new AFAO version.

An LLM MUST NOT:

- invent missing source facts;
- score the containing product merely because it is easier than isolating the canonical Adventure ID;
- average dimensions together;
- infer interpretive scores from page count or encounter count alone;
- convert low confidence into a middle score;
- treat `-1` as part of the 1--5 scale;
- use `-1` for Level Start or Level End;
- silently alter accepted assessments; or
- treat recommendation outcomes as evidence of the correct underlying AFAO score.

---

## 20. Explicitly Deferred Physical-Schema Decisions

Version 0.1 intentionally leaves the following questions unresolved:

- whether the production source of truth is a workbook, relational database, document database, or another store;
- whether interpretive dimensions are stored wide or normalized;
- whether evidence items use separate records or embedded structures;
- exact field and column names;
- internal assessment IDs;
- primary-key implementation;
- timestamp format;
- assessor/model identifier format;
- source hash format;
- JSON or API serialization;
- workbook sheet organization;
- search-index representation;
- embedding strategy;
- whether confidence is stored as integer percent or decimal proportion;
- exact enum encoding for lifecycle states; and
- audit-log storage mechanics.

Those decisions SHOULD be made only after the logical model and production pilot reveal what information must be operationally convenient.

Any physical schema MUST preserve the semantics defined by this specification and AFAO.

---

## 21. Conceptual AdventureFinder Data Flow

The intended architecture is:

```text
Published Source
      |
      v
Adventure Boundary Detection
      |
      v
Canonical Adventure Catalog
      |
      | Adventure ID
      v
AFAO + Analysis Data / Assessment Specification
      |
      v
Canonical Adventure Analysis Dataset
      |
      +------------------+
      |                  |
      v                  v
Query Interpretation   Derived Search / Index Representations
      |                  |
      +--------+---------+
               |
               v
       Matching / Ranking
               |
               v
       AdventureFinder Results
```

The Analysis Dataset is therefore a versioned measurement layer between canonical adventure identity and downstream recommendation behavior.

---

## 22. Minimum Conditions for a Canonical Production Assessment

An Adventure Assessment Package SHOULD NOT be marked Accepted unless all of the following are true:

1. the canonical Adventure ID is confirmed;
2. the governing AFAO version is declared;
3. the governing Assessment Specification version is declared;
4. the source basis is identified and sufficiently complete for the values being accepted;
5. # of Sessions has been assessed or explicitly assigned its correct non-assessed/evidence state;
6. Level Start has been assessed or explicitly assigned its correct uncertainty state;
7. Level End has been assessed or explicitly assigned its correct uncertainty state;
8. every in-scope interpretive dimension has a valid assessment state;
9. every scored interpretive dimension has a valid score and confidence value;
10. every dimension supporting path sensitivity has been considered for it;
11. concise rationale/evidence is retained at the level required by this specification;
12. package-level quality control has been completed;
13. all triggered review conditions have been resolved or explicitly accepted by authorized policy; and
14. the package has passed the applicable acceptance process.

---

## 23. Relationship to Future Recommendation Systems

This specification creates descriptive assessment data. It does not decide how AdventureFinder should rank adventures for a user.

Future matching systems MAY use:

- Level Start as an entry-level compatibility signal;
- Level End as a completion/progression property;
- # of Sessions as a duration constraint or preference;
- interpretive dimension scores as preference-match features;
- path sensitivity as explanatory or uncertainty metadata;
- confidence as a quality-control or matching-support signal if explicitly specified; and
- assessment state to exclude unavailable values from inappropriate calculations.

However, such use belongs in a separate Matching / Recommendation Specification.

The analysis layer MUST remain independently meaningful even if recommendation algorithms change.

---

## 24. Revision Policy

Changes to any of the following require an explicit revision of this specification:

- the canonical logical assessment model;
- required assessment states;
- source-coverage requirements;
- production scoring procedure;
- confidence guidance;
- path-sensitivity production handling;
- rationale/evidence requirements;
- review and acceptance rules;
- anti-bias requirements;
- correction/supersession behavior; or
- versioning semantics.

Changes limited to physical workbook/database implementation do not require a revision of this specification unless they alter these semantics.

Accepted production assessments MUST NOT silently change meaning when this specification changes.

Where a methodological revision materially affects prior assessments, AdventureFinder SHOULD define an explicit review or migration plan.

---

## 25. Revision History

| Revision | Date | Status | Description |
| --- | --- | --- | --- |
| **0.1** | 2026-08-12 | Accepted | Initial AdventureFinder Analysis Data / Assessment Specification. Establishes the logical Adventure Assessment Package, separates matching values from interpretive Dimension Assessments, preserves AFAO-specific assessment-state semantics, defines full-source production scoring, adjacent-anchor falsification, confidence and path-sensitivity handling, rationale/evidence provenance, review triggers, anti-bias rules, corrections versus ontology migrations, auditability, versioning, pilot/regression requirements, and explicit deferral of physical workbook/database schema decisions. |

