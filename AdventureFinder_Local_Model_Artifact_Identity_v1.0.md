# AdventureFinder Local Model Artifact Identity

## Version 1.0 — ACTIVE

**Date:** 2026-09-16  
**Scope:** Exact artifact identity and reproducible acquisition for AdventureFinder locally qualified Ollama models

---

## 1. Purpose

AdventureFinder local-model qualification applies to an **exact model artifact**, not merely to a human-readable Ollama model tag.

Ollama tags are convenient acquisition and runtime names, but registry tags can be repointed to different manifests over time. AdventureFinder therefore records the SHA-256 digest of the exact Ollama manifest that was present when the model artifact was qualified. That manifest digest is the project-level invariant for determining whether a newly acquired model is the same artifact covered by the existing qualification evidence.

This specification defines the identity fields, their ownership, and the fail-closed behavior required when a fetched artifact does not match the qualified artifact.

---

## 2. Identity fields

AdventureFinder distinguishes three model identifiers.

### 2.1 `ollama_model`

The AdventureFinder runtime/provenance identity used by scoring configuration, experiment manifests, and historical evidence.

Examples: `qwen3.6:27b`, `gpt-oss:20b`, `gemma4:26b`.

Existing historical evidence MUST retain the runtime model names that actually produced it. More precise acquisition identifiers introduced later MUST NOT rewrite historical provenance.

### 2.2 `pull_model`

The preferred public Ollama reference used to acquire the artifact on a fresh worker.

A `pull_model` is an **acquisition locator, not an immutable identity**. A more specific tag is preferred when Ollama publishes one that corresponds to the qualified artifact, but the tag alone does not prove that the fetched artifact is still qualified.

### 2.3 `qualified_manifest_sha256`

The lowercase 64-hex SHA-256 digest of the complete Ollama manifest file for the exact locally qualified artifact.

This is AdventureFinder's authoritative artifact-identity invariant. Qualification attaches to this manifest digest, subject to the scoring profile and other qualification conditions recorded elsewhere.

The manifest digest is distinct from the SHA-256 of the large GGUF/model-weight blob. The manifest references the configuration and model layers by their own content digests; hashing the manifest therefore commits AdventureFinder to the exact manifest composition that was qualified.

---

## 3. Qualified artifact registry

The following values were measured from the qualified local Ollama store used by AdventureFinder.

| AdventureFinder model alias | `ollama_model` | `pull_model` | `qualified_manifest_sha256` | Architecture | Parameters | Quantization | Native context |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `qwen` | `qwen3.6:35b-a3b` | `qwen3.6:35b-a3b-q4_K_M` | `07d35212591fc27746f0a317c975a6d68754fb38e9053d82e25f06057af28522` | `qwen35moe` | 36.0B | `Q4_K_M` | 262144 |
| `qwen27` | `qwen3.6:27b` | `dhiltgen/qwen3.6:27b-q4_K_M` | `a50eda8ed977ab48a12431878896b27ffd5cef552c17af3317d9623b939a7f1e` | `qwen35` | 27.8B | `Q4_K_M` | 262144 |
| `gptoss` | `gpt-oss:20b` | `gpt-oss:20b` | `17052f91a42e97930aa6e28a6c6c06a983e6a58dbb00434885a0cf5313e376f7` | `gptoss` | 20.9B | `MXFP4` | 131072 |
| `gemma` | `gemma4:26b` | `gemma4:26b-a4b-it-mtp-q4_K_M` | `08ae7ec1744bd7f451c4a530afb39d2673ad9d07a8369b8a33a3613b41212a68` | `gemma4` | 25.2B | `Q4_K_M` | 262144 |

The descriptive architecture, parameter, quantization, and context fields above document the measured qualified artifacts. They do not replace manifest-digest verification.

At the v1.0 freeze, the public `qwen3.6:27b-q4_K_M` library tag did **not** resolve to the qualified `a50eda8e...` manifest, while `dhiltgen/qwen3.6:27b-q4_K_M` did. The latter is therefore the preferred acquisition locator for the qualified Qwen 27B artifact. This is precisely why the locator remains subordinate to `qualified_manifest_sha256`.

---

## 4. Required verification behavior

Before a remote or newly provisioned worker is authorized to score under an existing AdventureFinder local-model qualification:

1. Acquire the requested model using the configured `pull_model` or another explicitly approved transport that is intended to reproduce the same artifact.
2. Resolve the resulting Ollama manifest.
3. Compute or obtain its exact SHA-256 digest.
4. Compare it with `qualified_manifest_sha256`.
5. Continue only on an exact match.

A mismatch MUST fail closed. The worker MUST NOT score under the existing local-model qualification merely because the model family, parameter count, quantization label, or human-readable tag appears compatible.

A successful tag pull plus a digest mismatch means **the fetched artifact is not the artifact covered by the existing qualification evidence**.

---

## 5. Artifact changes and requalification

A new manifest digest is a new AdventureFinder model artifact identity.

It MUST NOT silently inherit an existing `LOCAL_QUALIFIED` disposition. Adoption requires an explicit qualification-preservation or requalification decision supported by appropriate evidence under the project's current local-model acceptance rules.

Changing only the acquisition route does not require requalification if the resulting manifest digest is unchanged.

The project MUST NOT weaken or update `qualified_manifest_sha256` merely to make a newly fetched registry artifact pass bootstrap verification.

---

## 6. Repository ownership

### Normative definition — `md-specification-files`

This document defines what exact local-model artifact identity means for AdventureFinder and the required fail-closed behavior.

### Machine-readable source of truth — `af-workloads` (AFW)

`config/models.yml` records, for each locally qualified model alias:

- `ollama_model`
- `pull_model`
- `qualified_manifest_sha256`

AFW owns AdventureFinder model selection, qualification identity, reproducibility
requirements, and interpretation of whether a workload is authorized to use a
particular qualified model artifact. WLO carries the exact model/digest
requirement into execution and owns placement, state, retries, breakers and
paid-capacity lifecycle; it does not decide qualification.

### Remote enforcement — `runpod-ollama-fleet` (RPOF)

RPOF may receive the acquisition locator and expected digest and MUST fail closed when the provisioned worker does not contain the requested exact artifact. RPOF does not own AdventureFinder's model-selection or qualification semantics.

### Scoring runtime — `af-cli-scoring-utility`

The scoring runtime continues to use the AdventureFinder runtime model identity/profile required by the scoring contract. It does not become the authoritative store for model-distribution or artifact-supply metadata.

---

## 7. Measurement and audit

For a standard local Ollama installation, the qualified manifest digest can be independently reproduced with a command of the form:

```bash
shasum -a 256 "$HOME/.ollama/models/manifests/registry.ollama.ai/library/<repository>/<tag>"
```

The exact manifest path depends on the Ollama model namespace and locally stored tag.

The four v1.0 registry digests were measured directly from the local manifests, not inferred from model names or quantization labels.

---

## 8. Change control

Changes to a `pull_model` that preserve the same `qualified_manifest_sha256` are acquisition-maintenance changes and do not, by themselves, change the qualified artifact identity.

Changes to `qualified_manifest_sha256` are qualification-significant changes and require explicit evidence and project approval before production scoring under the new artifact.

Historical runs retain the model and artifact provenance that actually produced them; this registry governs current reproducible acquisition and future execution rather than rewriting historical evidence.
