# AdventureFinder Phase-4 Local-Model Acceptance Contract

## Version 0.1 — FROZEN

**Status:** Frozen for Phase 4 local-model auditions  
**Date:** 2026-08-21  
**Scope:** `af-cli-scoring-utility` local-model replacement / routing evaluation

---

## 1. Purpose

This contract governs how AdventureFinder evaluates local LLMs as possible replacements for the accepted Terra-based production scorer on individual AFAO dimensions.

The goal is **not** perfect reproduction of every Terra or regression-oracle score.

The goal is to determine whether a cheaper local scorer is **non-inferior enough for AdventureFinder production use**, while preserving the editorial integrity of the accepted ontology and assessment protocol.

A bounded adjacent disagreement may be acceptable. Serious scoring, grounding, source-boundary, or operational failures are not treated as equivalent to adjacent disagreements.

---

## 2. Governing frozen material

The following remain unchanged during model auditions:

1. accepted AFAO definitions, anchors, and calibration semantics;
2. production scoring prompt and dimension-specific guardrails;
3. structured-output schema and validator;
4. canonical Adventure IDs and source-boundary logic;
5. regression oracle / accepted benchmark values;
6. source material supplied to the scorer;
7. blindness and adjacent-anchor-falsification requirements; and
8. the prohibition on favorable stochastic reruns.

A transport-only compatibility change MAY be made when a provider/model cannot accept a semantically irrelevant API field, but it MUST be documented and MUST NOT alter the scoring instructions, rubric, evidence, source boundary, or output semantics.

---

## 3. Evidence hierarchy

### Tier A — Direct local-model evidence

Persisted local scoring artifacts produced under the frozen production contract are primary evidence.

### Tier B — Accepted Terra calibration evidence

The final accepted Terra calibration artifacts are the comparator for production quality. They establish the level of imperfection AdventureFinder already accepted for that dimension.

Terra is **not assumed to be perfect**.

Historical baseline or superseded Terra runs MAY be used to identify known failure modes, but MUST NOT replace the final accepted calibration profile when judging non-inferiority.

### Tier C — Product-impact evidence

Matcher/regression behavior MAY later be used to adjudicate whether a bounded systematic adjacent bias materially harms AdventureFinder recommendations.

---

## 4. Terra comparator record

Before a local model receives final production qualification for a dimension, a **Terra Comparator Record** MUST be frozen from existing archived data.

The record MUST identify:

- dimension;
- accepted Terra calibration version / artifact set;
- canonical cases represented;
- number of completed assessments;
- exact results;
- adjacent results, where applicable;
- non-adjacent / hard errors;
- malformed or unusable outputs;
- known residual directional or boundary bias;
- any accepted editorial caveats; and
- source artifact paths or repository references.

Existing archived Terra results MUST be reused. **Do not spend API money rerunning Terra solely to construct this comparator** unless the accepted archive is genuinely incomplete or unusable.

---

## 5. Error classes for the 17 interpretive 1–5 dimensions

### 5.1 Exact

Candidate score equals the accepted oracle value.

### 5.2 Adjacent

Candidate score differs from the oracle by exactly 1.

An adjacent result is **not automatically a failure**.

Its rationale and evidence must still be editorially coherent and grounded.

### 5.3 Non-adjacent / hard score error

Candidate differs from the oracle by 2 or more.

This is materially more serious than an adjacent disagreement.

### 5.4 Serious qualitative failure

The following are serious failures regardless of numeric distance:

- source contamination or material grounding hallucination;
- scoring the wrong canonical unit;
- conceptual inversion of the frozen rubric;
- systematic endpoint or central-scale collapse severe enough to erase meaningful distinctions;
- invalid / malformed structured output under the frozen validator;
- runaway or operationally pathological generation that makes production scoring impractical; or
- evidence fabricated outside the supplied canonical source.

A mild locator imprecision is not automatically a grounding failure when the cited underlying evidence is genuinely present in the canonical source.

---

## 6. Phase-4 tiny-audition gate

Phase 4 is a **small falsifiable audition**, not the final statistical qualification run.

For each model × dimension candidate:

1. Select the smallest predeclared discriminator set capable of exposing the known failure risk.
2. Prefer **1–3 new inference calls**.
3. Do not rerun a failed case merely to seek a favorable sample.
4. Stop immediately when a decisive serious failure makes further calls low-value.
5. Prefer shorter / cheaper source units when two cases answer the same question.

### 6.1 Tiny-audition outcomes

**AUDITION_SURVIVED**  
All completed outputs are operationally valid and grounded, with only exact or adjacent scoring disagreements. The model remains eligible for qualification.

**AUDITION_SURVIVED_WITH_BIAS**  
The model remains within one score point, but two or more observations show a coherent repeated directional/boundary bias. This is a warning flag, **not an automatic rejection**.

**AUDITION_FAILED**  
A non-adjacent score error or serious qualitative failure occurs and is judged materially relevant to the dimension. Stop routine testing of that model × dimension unless there is a genuinely differentiated hypothesis for a future retest.

**INSUFFICIENT_EVIDENCE**  
The audition does not contain enough information to classify the candidate without another small discriminator.

### 6.2 Important rule

**Exact-match perfection is NOT a Phase-4 gate.**

An adjacent miss does not fail the audition merely because Terra or the oracle scored the case exactly.

---

## 7. Final local-production qualification for interpretive dimensions

A local candidate that survives Phase 4 is evaluated against the accepted Terra Comparator Record before production routing.

### 7.1 Mandatory integrity gates

The candidate MUST:

- preserve canonical source identity;
- produce validator-compliant structured output reliably;
- show no material grounding-hallucination pattern;
- show no conceptual inversion pattern; and
- avoid operational behavior that defeats the economic purpose of local scoring.

### 7.2 Severe-error non-inferiority

On the qualification benchmark, the candidate's count of non-adjacent / hard score errors MUST NOT exceed the accepted Terra comparator's count on the comparable test basis.

Where accepted Terra has zero hard errors, the local candidate is therefore expected to have zero hard errors for qualification.

A single hard error in a tiny audition is sufficient to stop that candidate early; this saves compute rather than requiring a larger run to reconfirm a serious failure.

### 7.3 Adjacent-error tolerance

Adjacent disagreements are permitted.

The candidate MAY have a lower exact-match rate than Terra provided that:

1. hard-error non-inferiority is preserved;
2. the remaining disagreement is bounded to adjacent scores;
3. the reasoning remains editorially defensible and source-grounded; and
4. the exact-match gap is not materially worse than Terra's accepted calibration behavior.

For a completed qualification set, **“materially worse” is provisionally defined as more than a 10 percentage-point exact-match deficit versus the accepted Terra comparator**.

Because small audition samples make percentages unstable, this 10-point rule applies to the later qualification set, **not** to the 1–3-case Phase-4 audition.

### 7.4 Boundary-bias flag

A repeated same-direction adjacent error at the same score boundary is recorded as a **BOUNDARY_BIAS**.

BOUNDARY_BIAS does not automatically disqualify the scorer if the model otherwise passes the non-inferiority gates.

Before production routing, a candidate with BOUNDARY_BIAS MUST receive product-impact review using the matcher/regression layer to determine whether that bias materially changes recommendations or hard-constraint behavior.

The bias is not to be “fixed” by prompt tuning during an audition against the frozen contract.

---

## 8. Product-impact adjudication

A model that is otherwise qualified but carries a bounded adjacent bias MAY be accepted only after a representative matcher shadow test shows that the bias does not create unacceptable product behavior.

At minimum, the shadow test MUST check:

- hard-constraint correctness;
- materially changed ranking/recommendation outcomes attributable to the biased dimension; and
- whether the bias systematically favors or suppresses a meaningful class of adventures.

A product-impact review MAY rescue a bounded-adjacent candidate; it MUST NOT rescue grounding hallucinations, invalid output, canonical-unit errors, or conceptual inversions.

---

## 9. Catalog dimensions: # of Sessions and Levels

AFAO treats **# of Sessions** and **Levels** as editorially assessed catalog dimensions rather than the seventeen interpretive 1–5 dimensions.

Therefore the exact/adjacent/non-adjacent rules above MUST NOT be mechanically imposed on them.

For these dimensions:

1. use the dimension's own accepted Terra calibration metrics and guardrails;
2. compare the local candidate against Terra using the same field-level / practical-range criteria used when the Terra implementation was accepted;
3. preserve hard matching consequences, especially level eligibility; and
4. record systematic over- or under-estimation as a bias requiring matcher-impact review.

The same general principle applies: **the local model need not be perfect; it must be non-inferior enough to the accepted Terra behavior for AdventureFinder's actual matching use.**

---

## 10. Cost discipline and escalation

Testing order MUST optimize information gained per unit of time/cost.

1. Reuse archived Terra evidence; do not rerun paid baselines unnecessarily.
2. Use the smallest local discriminator set that can falsify viability.
3. Stop after a decisive hard failure.
4. Do not expand a local benchmark merely to chase a better exact percentage.
5. Do not test a more expensive model/tier until a cheaper plausible candidate has either failed the relevant gate or there is a concrete reason it cannot answer the question.
6. Before any premium/API escalation, estimate the expected production cost and compare it to the savings from local routing.
7. Sunk cost is not evidence for continuing an approach.

---

## 11. Frozen result vocabulary

Use the following labels going forward:

- **LOCAL_QUALIFIED** — passed Terra-relative qualification and any required matcher-impact review.
- **LOCAL_QUALIFIED_WITH_BIAS** — passed qualification; known bounded adjacent bias has been reviewed and accepted.
- **AUDITION_SURVIVED** — passed tiny Phase-4 kill test; full qualification not yet established.
- **AUDITION_SURVIVED_WITH_BIAS** — passed tiny kill test with a repeated bounded adjacent bias.
- **AUDITION_FAILED** — serious failure; current model × dimension candidate rejected.
- **CURRENT_LOCAL_POOL_UNSUITABLE** — multiple materially different local candidates have failed and no untested cheap hypothesis currently justifies more model-carousel spend.
- **UNTESTED** — no direct local evidence.

Do not use “failed” to describe a model solely because it produced one or more defensible adjacent disagreements.

---

## 12. Retroactive classification of evidence gathered before this freeze

The already-completed Phase-4 CONFIRM evidence is reclassified under this contract without rerunning any model.

### Tactical Complexity — qwen3.6:35b-a3b

**AUDITION_FAILED**

Reason: the deliberately selected ADV-0189 discriminator produced **expected 4 → proposed 2**, a non-adjacent error. The response was operationally valid and grounded, so the miss represents substantive scoring failure rather than transport noise.

No further routine Qwen Tactical audition is warranted under the current hypothesis.

### Darkness / Horror Intensity — qwen3.6:35b-a3b

**AUDITION_SURVIVED_WITH_BIAS**

Observed local ladder to date:

- 1 → 1 exact
- 2 → 2 exact
- 3 → 2 adjacent — Lost Mine of Phandelver
- 3 → 2 adjacent — The Wild Beyond the Witchlight
- 4 → 4 exact
- 5 → 5 exact

This is a repeated **2/3 downward BOUNDARY_BIAS**, but there are no non-adjacent errors in the observed Darkness set. Witchlight's reasoning was substantially grounded and the disagreement is a weighting judgment rather than a gross misunderstanding of the adventure.

Under the frozen Phase-4 contract, this is **not a failed audition**. Qwen remains eligible for later Terra-relative qualification / matcher-impact evaluation on Darkness.

No additional Witchlight-scale confirmation call is justified at this stage.

### Rules / System-Mastery Demand — current tested local pool

**CURRENT_LOCAL_POOL_UNSUITABLE**

Reason: direct evidence across multiple local candidates contains non-adjacent errors, conceptual scale failures, grounding failure, malformed/pathological output behavior, and repeated inability to preserve the difficult upper-ladder distinctions.

This status applies to the **current tested pool**, not to all conceivable future local models.

---

## 13. Change control

This v0.1 contract is frozen before beginning Wave-A auditions.

Changes to the acceptance criteria after observing future candidate results MUST be versioned and justified independently of whether the change would help or hurt a particular model.

Do not move the acceptance threshold after seeing a result.

---

## 14. Source basis

Normative AdventureFinder sources:

- AdventureFinder Analysis Ontology v1.5
- AdventureFinder Analysis Data / Assessment Specification v0.1

Historical comparator sources:

- `https://github.com/dtnorris/llm-response-data`
- `https://github.com/dtnorris/af-cli-scoring-utility`

The final accepted Terra calibration artifact for each dimension controls its Terra Comparator Record; superseded calibration attempts are historical evidence only.
