# Changelog

All notable changes to this project will be documented in this file.

The project uses candidate releases during early architectural development.

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
