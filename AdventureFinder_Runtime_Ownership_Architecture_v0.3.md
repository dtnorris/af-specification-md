# AdventureFinder Runtime Ownership Architecture v0.3

Status: accepted normative architecture for new production execution. This
version supersedes v0.2 for current architecture while preserving v0.1 and
v0.2 as accepted historical records. The component-owned low-level APIs linked below remain authoritative for their
wire formats. This specification owns project-level composition, not copied
schemas or runtime implementations.

| Public boundary | Authoritative owner and documentation |
| --- | --- |
| Generic execution plans | [WLO execution plan v0.3](https://github.com/dtnorris/workload-orchestrator/blob/main/contracts/wlo-execution-plan/v0.3/README.md) |
| Worker publication | [WLO dynamic-worker-registry/v0.1](https://github.com/dtnorris/workload-orchestrator/tree/main/contracts/dynamic-worker-registry/v0.1) |
| Capability requests | [WLO ollama-capability-request/v0.1](https://github.com/dtnorris/workload-orchestrator/tree/main/contracts/ollama-capability-request/v0.1) |
| Named source configuration | [WLO worker sources](https://github.com/dtnorris/workload-orchestrator/blob/main/docs/worker-sources.md) |
| Execution action admissibility | [WLO action-check](https://github.com/dtnorris/workload-orchestrator/tree/main/contracts/wlo-execution-action-check/v0.1) |
| Scorer environment and placement adaptation | [AFW producer contract](https://github.com/dtnorris/af-workloads/blob/main/docs/scorer-environment.md) |
| Campaign, budget and desired intent | [RPOF campaigns](https://github.com/dtnorris/runpod-ollama-fleet/blob/main/docs/CAPACITY_CAMPAIGN.md), [budget](https://github.com/dtnorris/runpod-ollama-fleet/blob/main/docs/CAMPAIGN_BUDGET.md), [desired-capacity contract](https://github.com/dtnorris/runpod-ollama-fleet/blob/main/contracts/rpof-desired-capacity/v0.1/README.md) |
| AF frozen handles, aliases and provenance | [AdventureFinder operator composition](https://github.com/dtnorris/adventure-finder), [provenance binding](https://github.com/dtnorris/adventure-finder/tree/main/contracts/adventurefinder-capability-provenance/v0.1) |

Copied conformance corpora are explicitly non-authoritative test material.
Independent validators are intentional; they do not import sibling runtime code.

The concise ownership rule is:

> **AFW defines work. LOW and RPOF expose workers. WLO matches work to workers.**

## Ownership

| Component | Owns | Does not own |
| --- | --- | --- |
| AFW (`af-workloads`) | AdventureFinder workload intent; source, model, input and scorer provenance; logical pools and exact capability requirements; jobs and scoring intent; the closed scorer environment | LOW or RPOF identity, endpoints, worker names, provider backends, fleet handles, placement, execution attempts or capacity budgets |
| LOW (`local-ollama-workers`) | Discovery and observation of configured operator-owned local Ollama capacity; stable logical local worker identity and concrete generation identity; local endpoint health/readiness; generation-bound capability evidence; durable publisher identity/revision state; provider-neutral `dynamic-worker-registry/v0.1` publication | Workload intent, pool requirements, job selection, scheduling, attempts, retries, execution state, result interpretation, provider lifecycle, paid-capacity safety or automatic workload execution |
| WLO (`workload-orchestrator`) | Generic plans, capability requests and read-only action admissibility; frozen `dynamic-worker-registry/v0.1` public provider API and canonical fixtures; independent named-source configuration and checkpoints; namespace-preserving registry union; capability matching and deterministic worker selection; one durable execution; pending/running/terminal state; claims; attempt creation, binding and evidence; worker-loss handling; runtime endpoint injection; retry, pause/resume, breakers and reporting | AdventureFinder semantics, proving worker capability, provider creation/replacement/teardown, paid-capacity admission or budget authority |
| RPOF (`runpod-ollama-fleet`) | Paid/provider-managed capacity campaigns; supervised desired-capacity reconciliation; provider resources; readiness, bootstrap and tunnels; cumulative/deadline/hourly/worker limits; scaling and replacement; independent guardian, teardown and provider-absence verification; provider-neutral `dynamic-worker-registry/v0.1` publication | Workload jobs, job assignment, commands, attempts, result interpretation or WLO execution state |
| AdventureFinder (`adventure-finder`) | AF-specific operator composition, frozen production context/handles, aliases, provenance bindings and short-handle presentation | Retained WLO execution-state interpretation, provider lifecycle or generic API authority |
| Specs (`md-specification-files`) | Project-level architecture and semantic composition | Component low-level API schemas or runtime implementation |

LOW is not “RPOF for localhost.” LOW and RPOF are symmetric only at their
publication boundary:

```text
LOW  -> dynamic-worker-registry/v0.1
RPOF -> dynamic-worker-registry/v0.1
```

Their capacity-lifecycle responsibilities are intentionally asymmetric. LOW
observes operator-owned local capacity. RPOF manages provider capacity and its
paid-resource safety lifecycle.

LOW therefore does not own AFW scoring semantics or scorer configuration,
logical pool requirements, job selection, scheduling or assignment, WLO
execution state, attempt creation or retry authorization, pause/resume,
circuit breakers, result interpretation, AFW environment mutation,
`AF_OLLAMA_BASE_URL` attempt binding, paid-capacity admission, RunPod or other
provider lifecycle, guardians, cumulative-cost enforcement, or automatic
workload execution.

## Production architecture

```text
AFW intent + provenance ---- wlo-execution-plan/v0.3 ----> WLO execution
LOW  ---- dynamic-worker-registry/v0.1 -------------------> / scheduler / store
RPOF ---- dynamic-worker-registry/v0.1 ------------------->       |
                                                                | bound endpoint
                                                                v
local scorer process --------------------------------> selected Ollama worker
```

AFW emits one plan containing all jobs and heterogeneous logical pools without
provider or placement decisions. WLO creates one execution, scheduler and store
for that plan. LOW, RPOF or future sources may independently supply conforming
registry snapshots. WLO accepts one or more named sources, retains each
publisher's namespace and checkpoint, and schedules across their worker union.
Neither publisher dispatches jobs, and WLO does not ask any publisher to do so.

This is the only architecture for newly compiled production work. AFW defaults
new workloads to v0.3 and requires explicit context and full-residency
capabilities. A v0.3 plan cannot be rebound through a WLO execution profile or
static worker configuration. WLO requires one or more provider-neutral worker
sources and fails closed when compatibility and dynamic-placement inputs are
mixed.

AFW remains provider- and placement-neutral. Its v0.3 plan expresses exact
model and digest requirements, context and residency requirements, optional
hardware identity requirements when semantically necessary, jobs, scoring
intent and provenance. It emits no publisher identity, endpoint, worker name,
provider backend, fleet handle or placement decision.

WLO remains the sole execution and scheduling authority. Registry publishers
do not create claims or attempts, authorize retries, inject runtime endpoints,
or interpret execution output.

Zero compatible workers is a normal live state. WLO records
`waiting_for_capacity`, continues bounded registry polling and dispatches no
work until a compatible READY worker appears. It does not fail merely because
capacity is currently zero.

## LOW observational publication

Ordinary LOW registry publication is observational. Obtaining a snapshot must
not implicitly:

- start or restart Ollama;
- pull or download a model;
- load or warm a model merely to satisfy polling;
- modify Ollama runtime configuration;
- change local capacity; or
- execute an inference workload.

A deliberate operation may establish or refresh generation-bound capability
evidence, but it must be separate and explicit. WLO polling the registry cannot
trigger such work as an incidental side effect. This architecture does not
freeze LOW command names or CLI design.

## Local worker identity and capability truth

For LOW, stable logical worker identity is distinct from concrete worker
generation. A local `worker_id` may survive an Ollama restart, but
`generation_id` identifies one observable local worker/runtime incarnation.
Endpoint reuse does not prove continuity. A restart, replacement or recreation
that could make the same endpoint address different concrete capacity requires
a new generation. Capability evidence belongs to the concrete generation it
describes. When LOW cannot establish continuity or capability evidence, it must
fail closed rather than invent either.

LOW publishes exact observed Ollama model identity and digest evidence, proven
runtime context capability, proven full accelerator-residency capability where
supportable, and a provider-neutral local hardware/runtime identity suitable
for `gpu_id`. It produces the capability fingerprint under the frozen registry
contract. This specification does not redefine `fully_gpu_resident`, Apple or
unified-memory evidence semantics.

The capability division remains:

```text
AFW says what a pool requires.
LOW or RPOF says what a worker can actually provide.
WLO decides whether the worker satisfies the pool.
```

LOW must not consume AFW requirements to manufacture favorable declarations.
Inability to prove a capability means it is not advertised as satisfied; it
does not relax exact model, digest, context, residency or GPU matching.

## Per-attempt path

For each dynamic dispatch WLO must:

1. validate the latest snapshot from every configured source and durably retain
   one independent checkpoint per publisher namespace;
2. match one pending job's logical-pool requirements to one compatible READY
   worker;
3. persist the attempt binding before launch using exactly
   `registry_id`, `worker_id`, `generation_id`, `endpoint` and
   `capability_fingerprint`, together with the accepted registry revision and
   snapshot hash;
4. start with the ordinary inherited process environment, apply the job
   environment, then inject the bound endpoint as `WLO_WORKER_ENDPOINT` last;
5. launch the opaque command locally and retain stdout, stderr, exit status and
   attempt metadata; and
6. commit terminal state or fail closed on worker loss/replacement.

AFW's scorer-controlled environment is closed: each recognized variable is
present with an exact string value or explicit null meaning absent.
AFW reserves both runtime endpoint names. WLO supplies only the generic
`WLO_WORKER_ENDPOINT`; AFW's scorer adapter translates that selected origin
into `AF_OLLAMA_BASE_URL`. AFW plan/scorer input cannot pin either runtime-owned
name. LOW and RPOF do not mutate AFW job environments. Result/scoring
interpretation remains in AFW and the scorer, outside WLO.

In the target production architecture, WLO validates and matches published
evidence; it does not discover local Ollama instances or prove local
capabilities itself.

## Worker continuity and loss

The five-field attempt binding is indivisible for LOW and RPOF workers alike.
Endpoint equality alone never proves continuity. Worker disappearance, a
changed generation, changed endpoint or changed capability fingerprint makes
the running outcome unknown. WLO records the attempt failed in doubt and halts
further dispatch. A late result is evidence only and cannot rewrite that state.

A replacement generation is a new worker. It may be selected for future work
after the prior loss transition is durable, but it cannot inherit, complete or
implicitly retry the old attempt. Retry remains an explicit audited WLO action
with a new attempt number.

## Paid-capacity safety

LOW and WLO are not paid-capacity safety boundaries. Starting, polling,
pausing, stopping or crashing them does not create, retain, resize, destroy or
widen provider capacity.

RPOF remains the sole owner of paid/provider-managed capacity: admission,
resources, campaigns, bootstrap/readiness, scaling, replacement, leases,
teardown and provider-absence verification. It binds each production campaign
to its original finite cumulative compute cap, absolute runtime deadline,
aggregate hourly-rate cap and worker limit. Its supervised controller continues
ordinary heartbeat and desired-capacity reconciliation after the
campaign-starting CLI, WLO, shell or terminal exits. Its independent guardian
separately continues safety enforcement and teardown. Scale and replacement
use the same durable authority and may not reset a deadline or create a second
budget.

RPOF desired capacity is mutable control-plane intent inside that fixed
authority. A declared profile may desire zero workers without losing its
authorized maximum or exact model/runtime/hardware requirements. Desired
changes retain the original campaign identity, parent budget, cumulative and
hourly limits, worker maxima, arm time and absolute deadline. Updating desired
state alone performs no provider reconciliation and cannot erase committed or
pending liability. Every later provider increase still passes ordinary RPOF
admission. The independent guardian remains a safety enforcer and teardown
owner, not a desired-capacity controller. The normative state and revision
rules are defined by `rpof-desired-capacity/v0.1`.

## Operator process ownership and human control

The following vocabulary is normative for WLO/RPOF help and operator
documentation:

- **FOREGROUND WORK OWNER**: the invoking process owns the active operation;
- **DETACHED WORK LAUNCHER**: the invoking process starts a separate process
  that continues after the command returns;
- **DETACHED/SUPERVISED CONTROLLER LAUNCHER**: the invoking process installs or
  starts an identity-bound controller that continues reconciliation after the
  command, shell or terminal exits;
- **READ-ONLY OBSERVER**: a continuing view that owns no workload or resource
  lifecycle;
- **ONE-SHOT INSPECTION/PUBLICATION**: a bounded read or registry publication
  that owns no workload or resource lifecycle;
- **CONTROL REQUEST**: a durable local execution/safety-state request, not
  provider teardown;
- **RESOURCE MUTATION**: a bounded provider or remote-state mutation client,
  not a continuing controller; and
- **TEARDOWN REQUEST**: an explicit resource-retirement request whose completion
  is governed by provider-absence verification.

Two lifecycle commands are not interchangeable. `wlo pause` is the intentional
graceful WLO workload-pause request: it stops new dispatch and lets already
running work finish under WLO's existing pause contract. It does not change
provider capacity. For production campaign capacity, `rpof campaign stop` is
the intentional paid teardown request. It does not pause WLO. Teardown is not
complete until RPOF records provider absence and the campaign budget is
`CLOSED`.

Foreground cancellation and graceful pause are distinct. Under FO-06, WLO
handles foreground interruption by stopping new dispatch and cancelling its
owned child process trees, preserving partial logs and interrupted evidence.
The signal/escalation rules are owned by WLO's
[operator workflow](https://github.com/dtnorris/workload-orchestrator/blob/main/docs/operator-workflow.md).
Abrupt runner death or terminal loss is not proof that all work stopped, and
no WLO cancellation performs provider teardown.

Current command syntax, classification and supervision guarantees belong with
[WLO](https://github.com/dtnorris/workload-orchestrator#readme),
[LOW](https://github.com/dtnorris/local-ollama-workers#readme) and
[RPOF](https://github.com/dtnorris/runpod-ollama-fleet#readme).
This architecture does not maintain a second copy of their CLI matrices.
RPOF's existing supervised controller reconciles desired capacity; its independent
guardian enforces safety and teardown. Neither owns WLO execution.

## Capability requests and AF front-door composition

AdventureFinder resolves an AF operator alias against the exact frozen AFW plan
and derives one generic WLO-owned capability request plus a separate AF provenance
binding. LOW and RPOF independently consume the generic request on explicit
bootstrap/campaign paths. Runtime identity excludes AF batch, alias, plan, pool
and label provenance. Provider/generation identity may additionally bind RPOF
bring-up evidence; it does not widen or reset original budget authority.

The generic capability contract preserves either exact residency boolean.
The current execution-plan and RPOF campaign policies require true when specified;
these are separate contracts, not boolean coercion or a request to widen policy.
Historical FO-10/FO-11 formats remain attributable to their recorded versions and
are not implicitly migrated by reads.

AdventureFinder verifies frozen provenance and resolves AF job short handles,
then calls WLO's read-only `action-check` for run/resume/retry/recovery/repair
admissibility. It validates the contract and presents WLO's disposition/reason.
WLO alone interprets retained execution state; the front door does not read its
state files, locks, pause state, breaker or dispatch-halt evidence. An action
check performs no action, retry authorization, repair or provider access.

## Registry composition boundary

`dynamic-worker-registry/v0.1` remains the frozen provider-neutral
cross-repository worker contract. LOW is another conforming publisher; it adds
no LOW-specific, provider-type or local-versus-remote fields and changes no
identity, fingerprint, state, freshness, revision or matching semantics.

One WLO execution may consume LOW, RPOF and future conforming publishers
simultaneously. WLO schedules over the union of workers while preserving every
publisher's exact `registry_id`, revision sequence and independent durable
checkpoint. The complete registry-qualified execution identity remains the
scheduling and attempt-binding key, so identical `worker_id` values in two
registries are distinct workers.

No publisher or AdventureFinder front door merges or republishes those streams,
and WLO creates no synthetic registry identity. A running attempt is reconciled
only against later checkpoints for its own `registry_id`; disappearance,
generation replacement, endpoint change or capability change in one namespace
cannot affect a same-named worker in another. Configured sources publishing
the same `registry_id` fail closed; source configuration cannot override a
publisher identity. Current `wlo-worker-sources/v0.2` configuration distinguishes
required and optional sources; historical v0.1 sources remain required. A required source
blocks dispatch when it lacks fresh accepted evidence. Optional failure is
isolated, and a still-fresh accepted snapshot may remain usable after a failed
poll under WLO's source policy. Publisher election and cross-publisher
deduplication remain outside this architecture.

## Compatibility boundary

Historical v0.1 static-worker and v0.2 execution-profile behavior remains
readable and, where current code still supports local/fixed execution,
runnable only for retained artifacts, recovery and rollback. Producers must
select those versions explicitly; they are never defaults for new work.

RPOF workload dispatch, dispatch admission/close and execution-pool
fulfillment commands are retired. Their frozen validators and historical
artifacts remain readable for audit, but current code cannot use them to run a
workload. RPOF publishes capacity; WLO executes jobs.

The following combinations fail closed:

- a v0.3 plan with any execution profile;
- a v0.3 plan without at least one dynamic worker source when execution is requested;
- dynamic worker-source options with a v0.1/v0.2 plan; and
- AFW v0.3 output containing worker names, endpoints, provider backends,
  concurrency, budgets, fleet handles or other placement authority.

Documentation may describe v0.1/v0.2 only under an explicit historical or
compatibility heading. No compatibility command or example may be presented
as a current production alternative.
