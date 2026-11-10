# **AdventureFinder Scoring Calibration & Regression Guideline**

**v0.1  |  Human Operating Guide  |  August 2026**

**Purpose.** Keep prompt calibration accurate, cheap, reproducible, and finite. AFAO defines the ruler; the Human Regression Oracle defines accepted benchmark values; this guide defines how we develop and validate the scorer.

# **Core Rules**

**1\. Freeze the target before tuning.** Treat the current AFAO definition, anchors, and accepted oracle values as the target. Model disagreement alone does not reopen the ontology.

**2\. Diagnose before editing.** Classify the failure first: rubric misunderstanding, boundary discrimination, stochastic instability, source/context, wiring/formatting, or architectural limitation. Edit only against a plausible mechanism.

**3\. Use the cheapest valid test first.** Start with the smallest diagnostic set that can falsify the proposed fix. A candidate earns access to broader regression only by passing cheaper gates.

**4\. Separate development from validation.** Repeated tuning cases are development cases; preservation cases protect known behavior; holdouts test generalization and should not become tuning targets in the same cycle.

**5\. Replicate selectively.** Repeat runs when variance itself matters at a difficult boundary. Do not automatically run every adventure three times.

**6\. Predeclare pass / fail / adjudicate.** Before execution, state the hypothesis, cases, replicate count, preservation requirements, and acceptance condition. Passing freezes; failing triggers diagnosis before another edit.

**7\. Protect against regressions.** A local fix is not accepted merely because its target cases improve. Relevant low/middle/high controls must remain within declared bounds.

**8\. Treat API spend as an escalation signal.** Typical development envelopes: Easy $2–5; Normal $5–10; Hard $10–20. Crossing the hard envelope triggers an explicit architecture/value review—not automatic further tuning.

**9\. Freeze and reopen deliberately.** Record accepted prompt/profile version \+ hash, AFAO version, oracle version, test evidence, and known limitations. Reopen only for a systematic new failure, meaningful regression deterioration, ontology/source-pipeline change, or model migration—not one isolated miss.

# **Default Calibration Flow**

A. Smoke/diagnostic — 3–5 highly diagnostic cases, usually 1 run each.  B. Boundary \+ preservation — only cases needed to prove the fix and protect adjacent/anchor behavior.  C. Stability — replicate only where variance is material.  D. Broad regression — one pass over the wider oracle after the candidate earns it.  E. Holdout acceptance — previously unused/withheld cases as evidence of generalization.  F. Freeze — if declared criteria pass, stop tuning.

# **Decision Standard**

**Production-ready does not mean perfect deterministic agreement.** It means the scorer is accurate and stable enough on representative validated cases, preserves important controls, has no known systematic failure worth the expected cost of another iteration, and routes genuine uncertainty/disagreement to review.

**Working maxim:** What are we testing? What is the cheapest valid test? What constitutes success? When do we stop?