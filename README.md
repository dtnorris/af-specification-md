# AdventureFinder specifications

This is a proposed forward document set for content and publication review.
It supplies shared domain meaning; component repositories own loading, scoring,
workload policy and qualification. Importing these files does not accept a draft
method, qualify a runtime, migrate a caller or authorize publication.

| Selected document | Version / source status |
| --- | --- |
| [Catalog editorial rules](Adventure_Catalog_Editorial_Specification_Rev_2.0.md) | Rev 2.0 — Draft |
| [Boundary detection (ABDS)](Adventure_Boundary_Detection_Specification_ABDS_v1.4.md) | 1.4 — Accepted; selected for new work |
| [Analysis ontology (AFAO)](AdventureFinder_Analysis_Ontology_AFAO_v1.6.1.md) | 1.6.1 — Candidate; pending targeted GM Preparation Burden 4/5 revalidation |
| [Assessment methodology](AdventureFinder_Analysis_Data_Assessment_Specification_v0.1.md) | 0.1 — Accepted |
| [Scoring calibration and regression](AdventureFinder_Scoring_Calibration_Regression_Guideline_v0.1.md) | 0.1 — retained guideline |
| [Runtime ownership](AdventureFinder_Runtime_Ownership_Architecture_v0.3.md) | 0.3 — accepted normative architecture for new production execution |
| [Local model artifact identity](AdventureFinder_Local_Model_Artifact_Identity_v1.0.md) | 1.0 — ACTIVE |
| [Phase-4 local model acceptance](AdventureFinder_Phase4_Local_Model_Acceptance_Contract_v0.1.md) | 0.1 — FROZEN for its stated auditions |

These are complete, unchanged documents with their original basenames and
statuses. Internal historical versions, model registries and qualification
claims retain their original scope; they are not new installation defaults.
ABDS 1.3 is historical compatibility retained outside this forward set. Existing
operations must retain their exact frozen versions until deliberately migrated.

Run the standard-library-only preservation check with Python 3:

```sh
python3 verify_documents.py
```

[documents.json](documents.json) binds filenames, versions, modes, complete file
hashes and complete heading bodies, including nineteen dimensions, all 85 primary
anchors and ten assessment prompt sections. Whole-file hashes also protect common
and outside-section rules. The check refuses extra files as well as corruption;
keep generated output outside this directory. Verify the inventory and check
script against the reviewed patch before trusting them. This is extraction
integrity evidence, not editorial acceptance or publication clearance.

Use an explicit method root and exact paths. With the existing scorer installed,
its bounded native loaders can be invoked without running inference:

```sh
# Set SCORER_ROOT to the separately installed af-cli-scoring-utility checkout.
METHOD_ROOT="$PWD"
ruby -I "$SCORER_ROOT/lib" -r af_scoring -e '
  root = ARGV.fetch(0)
  ontology = AFScoring::AFAO.new(File.join(root, "AdventureFinder_Analysis_Ontology_AFAO_v1.6.1.md"))
  assessment = AFScoring::AssessmentSpec.new(File.join(root, "AdventureFinder_Analysis_Data_Assessment_Specification_v0.1.md"))
  abort "incompatible versions" unless ontology.version == "1.6.1" && assessment.version == "0.1"
  puts "Loaded AFAO #{ontology.version} and AssessmentSpec #{assessment.version}"
' "$METHOD_ROOT"
```

This example uses existing classes, not a new runtime interface. Scorer Runner
startup still has a separate regression-data dependency. SC/WL own its isolation,
profile selection and new method identity qualification. PL must bind boundary
guidance explicitly instead of choosing the largest version. FP must reconcile
its shorter ontology filename with the actual `_AFAO_` basename. AF owns installed
selection and integration. No fallback to a private specification directory is
part of this document set; old Git qualification does not transfer by relocation.

The AFAO references a standalone Salvage Operation adjudication freeze that is
retained privately as historical decision evidence. The operative Combat
correction, score-4 benchmark, rationale, unchanged anchors and non-Combat/Tomb
exclusions are already present in AFAO's “Post-1.1 Salvage Operation Benchmark
Re-Adjudication” section and version history. The cited private run archives and
oracle history support historical audit; they are not inputs to these bounded
loaders. Historical oracle/guardrail maintenance remains a separate owner action.
The private freeze is excluded from this proposed file set and publication history.

The retained [MIT license](LICENSE) applies to rights-cleared first-party material.
It does not grant rights to third-party source works or resolve embedded-content
clearance. Exact-candidate review remains required, including the AFAO's
source-derived calibration discussion and the outstanding original-source
comparison. Preserve its anchors and benchmark during that review. Application,
public release and public retrieval require separate operator acceptance.
