# Changelog

All notable changes to this project will be documented in this file.

The project uses candidate releases during early architectural development.

## [0.4.0-candidate] - 2026-07-05

### Added

* `Cognitive Feedback Record` specification.
* Outcome-status evaluation.
* Goal-completion scoring.
* Semantic-preservation scoring.
* Human-usability scoring.
* Verification-quality scoring.
* Overall cognitive outcome scoring.
* Unresolved-issue recording.
* Route-fit evaluation.
* Route-efficiency evaluation.
* Unnecessary-organ detection.
* Missing-organ detection.
* Loop-count recording.
* Recovery-count recording.
* Human-escalation quality evaluation.
* Organ-level evaluation records.
* Input-quality scoring.
* Output-quality scoring.
* Interface-contract compliance scoring.
* Organ contribution scoring.
* Organ strengths and issue records.
* Human feedback records.
* Human correction records.
* User preference signals.
* Explicit adaptation proposals.
* Adaptation target layers.
* Adaptation proposal types.
* Evidence references for adaptation proposals.
* Proposal-priority scoring.
* Human-review requirements.
* Explicit prohibition of automatic architecture application.
* Cognitive Feedback & Adaptation Layer documentation.
* Extended multi-target validation for v0.1 through v0.4 artifacts.

### Architectural Meaning

v0.1 made cognition observable.

v0.2 defined cognitive organ contracts.

v0.3 introduced adaptive cognitive routing.

v0.4 evaluates whether the selected route and participating cognitive organs actually performed well.

The architecture can now distinguish between:

* successful outcomes with inefficient routes
* correct routes with weak organ output
* strong analysis with poor human-language translation
* useful output with excessive cognitive activation
* repeated route failures that justify future review

### Design Principle

> Feedback may generate adaptation proposals, but adaptation proposals do not authorize automatic self-modification.

v0.4 therefore introduces a controlled path from:

```text
Outcome
↓
Evaluation
↓
Evidence
↓
Adaptation Proposal
↓
Human Review
```

### Scope Boundary

v0.4 does not define:

* automatic architecture mutation
* autonomous prompt rewriting
* unsupervised route replacement
* automatic Boundary modification
* self-approved authority expansion
* reinforcement learning execution
* production deployment mechanisms

These remain outside the scope of this release.


## [0.3.0-candidate] - 2026-07-05

### Added

* `Cognitive Routing Plan` specification.
* Input profiling for cognitive task classification.
* Routing modes:

  * minimal
  * standard
  * deep structure
  * safety review
  * memory intensive
  * custom
* Route-step definitions.
* Required, conditional, optional, and fallback activation modes.
* Activation conditions.
* Skip conditions.
* Expected input and output artifacts.
* Controlled cognitive loops.
* Maximum loop-count limits.
* Optional parallel-branch declaration.
* Verification-before-output requirement.
* Boundary-before-output requirement.
* Preferred return routes.
* Explicit termination conditions.
* Missing-artifact recovery policy.
* Validation-failure recovery policy.
* Route-block recovery policy.
* Maximum recovery-attempt limits.
* Human escalation conditions.
* Human escalation presentation requirements.
* Deep Structure routing example.
* Cognitive Routing Layer documentation.
* Multi-target schema validation for v0.1, v0.2, and v0.3 artifacts.

### Architectural Meaning

v0.1 defined the record of one cognitive cycle.

v0.2 defined the contracts of the cognitive organs participating in that cycle.

v0.3 defines how a task selects and traverses a cognitive path.

The architecture can now represent:

* lightweight routes for simple tasks
* standard analytical routes
* memory-intensive routes
* safety-oriented routes
* deep-structure routes
* controlled return loops
* human escalation paths

### Design Principle

> Not every cognitive organ should be activated for every task.

The routing layer selects the minimum sufficient cognitive path and expands the route only when task complexity, uncertainty, risk, memory dependency, or missing evidence requires additional cognition.

### Scope Boundary

v0.3 does not yet define:

* automatic route scoring from historical outcomes
* cognitive energy cost metrics
* adaptive route optimization
* route-learning records
* cross-cycle continuity
* autonomous architecture mutation

These remain candidates for future versions.


## [0.2.0-candidate] - 2026-07-05

### Added

* `Cognitive Organ Interface` specification.
* Machine-readable organ identity and role contract.
* Explicit consumed and produced artifact definitions.
* Invocation modes:

  * always
  * conditional
  * on request
  * event driven
* Precondition, skip condition, and blocking condition support.
* Allowed predecessor and successor routing rules.
* Return-route definitions.
* Human escalation permission.
* Semantic preservation guarantees.
* Mandatory reporting requirements.
* Cognitive authority levels.
* Explicit prohibited-action boundaries.
* Observability requirements.
* Cognitive-organ failure policies.
* Structural Core reference interface example.
* Multi-target schema validation.
* Cognitive Organ Interface documentation.

### Architectural Meaning

v0.1 introduced the observable record of one distributed cognitive cycle.

v0.2 defines the contract of the cognitive organs participating in that cycle.

The architecture can now describe not only:

> what happened during one cognitive cycle

but also:

> what each cognitive organ is allowed and required to receive, produce, preserve, report, and route.

This is the first step toward a loosely coupled distributed cognitive system.

### Design Principle

> A cognitive organ is defined by its contract, not by its model.

Different implementations may participate in the same architecture when they satisfy the same interface requirements.

### Scope Boundary

v0.2 does not yet define:

* dynamic route selection
* route scoring
* cognitive load balancing
* organ capability discovery
* multi-cycle state continuity
* semantic diff receipts
* autonomous architecture mutation

These remain candidates for future releases.


## [0.1.0-candidate] - 2026-07-05

### Added

* Initial AI Cognitive Architecture specification.
* `Cognitive Cycle Record` as the first canonical architecture record.
* JSON Schema for one complete distributed cognitive cycle.
* YAML example demonstrating:

  * human input
  * Finder
  * Yin Semantic Decomposer
  * Memory Breathing
  * Analyst
  * Structural Core
  * Verifier
  * Boundary
  * Yang Language Recomposer
  * Human Gate
  * Structural Rumination
* Explicit separation between semantic integration and human decision presentation.
* Conflict reporting and priority mapping.
* Rumination outputs for:

  * memory updates
  * routing updates
  * architecture updates
* Python validation script.
* GitHub Actions validation workflow.
* Initial architecture overview documentation.

### Architectural Position

v0.1 establishes the minimum observable unit of the architecture:

> one human input passing through a distributed cognitive cycle and producing an auditable record of interpretation, analysis, integration, verification, translation, human presentation, and rumination.

### Scope Boundary

This release does not yet define:

* dynamic routing
* executable orchestration
* autonomous architecture mutation
* cognitive organ service protocols
* multi-cycle continuity
* semantic translation diff records
* cognitive trace receipts

These remain candidates for future versions.

## [0.3.0-candidate] - 2026-07-05

### Added

* `Cognitive Routing Plan` specification.
* Input profiling for cognitive task classification.
* Routing modes:

  * minimal
  * standard
  * deep structure
  * safety review
  * memory intensive
  * custom
* Route-step definitions.
* Required, conditional, optional, and fallback activation modes.
* Activation conditions.
* Skip conditions.
* Expected input and output artifacts.
* Controlled cognitive loops.
* Maximum loop-count limits.
* Optional parallel-branch declaration.
* Verification-before-output requirement.
* Boundary-before-output requirement.
* Preferred return routes.
* Explicit termination conditions.
* Missing-artifact recovery policy.
* Validation-failure recovery policy.
* Route-block recovery policy.
* Maximum recovery-attempt limits.
* Human escalation conditions.
* Human escalation presentation requirements.
* Deep Structure routing example.
* Cognitive Routing Layer documentation.
* Multi-target schema validation for v0.1, v0.2, and v0.3 artifacts.

### Architectural Meaning

v0.1 defined the record of one cognitive cycle.

v0.2 defined the contracts of the cognitive organs participating in that cycle.

v0.3 defines how a task selects and traverses a cognitive path.

The architecture can now represent:

* lightweight routes for simple tasks
* standard analytical routes
* memory-intensive routes
* safety-oriented routes
* deep-structure routes
* controlled return loops
* human escalation paths

### Design Principle

> Not every cognitive organ should be activated for every task.

The routing layer selects the minimum sufficient cognitive path and expands the route only when task complexity, uncertainty, risk, memory dependency, or missing evidence requires additional cognition.

### Scope Boundary

v0.3 does not yet define:

* automatic route scoring from historical outcomes
* cognitive energy cost metrics
* adaptive route optimization
* route-learning records
* cross-cycle continuity
* autonomous architecture mutation

These remain candidates for future versions.

