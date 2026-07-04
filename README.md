# AI Cognitive Architecture

**A distributed cognitive architecture for Multi-GPT systems.**

AI Cognitive Architecture defines a functional architecture in which specialized AI systems are treated not merely as task agents, but as cognitive organs participating in a shared processing cycle.

The architecture organizes semantic decomposition, memory, analysis, structural integration, verification, boundary control, human-language recomposition, human review, and structural rumination into one distributed cognitive system.

## Status

Current version:

**v0.1 — Cognitive Cycle Record**

The project is currently an experimental architecture specification.

It does not claim to reproduce the biological human brain.

Instead, it explores how functional differentiation, structural translation, cyclic processing, memory, verification, and human judgment can be organized into an auditable AI cognitive architecture.

## Core Idea

A conventional AI interaction is often represented as:

```text
Input
  ↓
Model
  ↓
Output
```

AI Cognitive Architecture instead defines a cognitive cycle:

```text
Human Input
    ↓
Finder
    ↓
Yin Semantic Decomposer
    ↓
Memory Breathing
    ↓
Analyst
    ↓
Structural Core
    ↓
Verifier / Boundary
    ↓
Yang Language Recomposer
    ↓
Human Gate
    ↓
Structural Rumination
    ↓
Next Cognitive Cycle
```

The central design principle is simple:

> Human language is first lowered into explicit structure, processed across specialized cognitive organs, integrated, verified, translated back into human language, and then returned to human judgment.

## Cognitive Organs

### Finder

Collects external information, documents, logs, observations, and environmental context.

Primary output:

`RawInfoSet`

### Yin Semantic Decomposer

Decomposes human-language input into explicit semantic structures.

It may identify:

* intention
* assumptions
* concepts
* relations
* constraints
* ambiguity
* uncertainty
* question epicenter
* reusable traces

Primary outputs:

* `SemanticStructure`
* `AssumptionSet`
* `ConstraintSet`
* `AmbiguityMap`

### Memory Breathing

Provides historical context without treating all memory as equally important.

Primary outputs:

* `ContextFrame`
* `HistoryTrace`

### Analyst

Performs comparison, reasoning, hypothesis formation, evaluation, and design analysis.

Primary outputs:

* `AnalysisGraph`
* `HypothesisSet`
* `DesignProposal`

### Structural Core

Integrates structures from multiple cognitive organs.

Its responsibility is semantic integration rather than final presentation.

Primary outputs:

* `IntegratedStructure`
* `ConflictReport`
* `PriorityMap`

### Verifier

Checks logical consistency, specification compliance, uncertainty, and validation conditions.

Primary outputs:

* `ValidationReport`
* `RiskMap`

### Boundary

Applies operational, safety, technical, and policy boundaries.

Primary outputs:

* `AllowedActionSet`
* `FilteredOutput`

### Yang Language Recomposer

Transforms integrated and bounded structures into human-readable language.

Primary outputs:

* `HumanText`
* `ExampleSet`
* `Reframing`

### Human Gate

Prepares information for human understanding and decision.

The Human Gate does not replace human judgment.

It organizes:

* summaries
* options
* warnings
* unresolved issues
* decision points

Primary output:

`HumanFacingBundle`

### Structural Rumination

Reviews the completed cognitive cycle and identifies possible changes to:

* memory
* routing
* cognitive strategy
* architecture

Primary outputs:

* `MetaStructureUpdate`
* `DesignReflection`

## v0.1 Scope

v0.1 introduces the `Cognitive Cycle Record`.

The record captures one complete distributed cognitive cycle, including:

* original human input
* participating cognitive organs
* processing stages
* structural integration
* conflicts
* priorities
* Human Gate output
* rumination updates

The primary schema is:

```text
schemas/cognitive-cycle-record.schema.json
```

A complete example is available at:

```text
examples/cognitive-cycle-record.example.yaml
```

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Cognitive Cycle Record
  schema : schemas/cognitive-cycle-record.schema.json
  example: examples/cognitive-cycle-record.example.yaml
[ok] cognitive-cycle-record.example.yaml is valid
```

GitHub Actions also validates the example automatically.

## Design Principles

### Functional Differentiation

Different cognitive functions should be represented explicitly instead of being hidden inside one undifferentiated response process.

### Structure Before Expression

Human-language input should be interpretable as explicit semantic structure before final explanation is generated.

### Cyclic Cognition

The architecture assumes repeated cycles of:

```text
input
→ structure
→ analysis
→ integration
→ verification
→ expression
→ human judgment
→ rumination
→ next input
```

### Human-Centered Control

The architecture supports human judgment rather than removing it.

### Auditability

Important transformations should leave inspectable structural records.

### Uncertainty Preservation

Translation and simplification must not transform uncertainty into false certainty.

## Repository Structure

```text
.
├─ .github/
│  └─ workflows/
│     └─ validate.yml
├─ schemas/
│  └─ cognitive-cycle-record.schema.json
├─ examples/
│  └─ cognitive-cycle-record.example.yaml
├─ docs/
│  └─ architecture-overview.md
├─ scripts/
│  └─ validate_examples.py
├─ README.md
├─ CHANGELOG.md
└─ requirements.txt
```

## Development Direction

Possible future layers include:

* dynamic cognitive routing
* organ-level interface schemas
* bidirectional verification loops
* cognitive trace receipts
* semantic translation diffs
* memory weight updates
* multi-cycle continuity
* architecture mutation records
* Human Gate decision receipts

These are not yet part of v0.1.

## Definition

> AI Cognitive Architecture is a distributed cognitive OS layer in which specialized AI systems operate as functional cognitive organs connected through semantic decomposition, memory, analysis, integration, verification, boundary control, translation, human judgment, and structural rumination.

## Motto

> Structure before expression.
> Integration before conclusion.
> Human judgment before closure.

## v0.2 — Cognitive Organ Interface Contract

v0.2 introduces a machine-readable interface contract for cognitive organs participating in the architecture.

While v0.1 defined the record of one complete cognitive cycle, v0.2 defines how individual cognitive organs connect to that cycle.

Each interface declares:

* functional role
* consumed artifacts
* produced artifacts
* invocation conditions
* routing permissions
* semantic guarantees
* authority boundaries
* observability requirements
* failure behavior

The primary schema is:

`schemas/cognitive-organ-interface.schema.json`

The first reference example defines the Structural Core interface:

`examples/cognitive-organ-interface.structural-core.example.yaml`

### Architectural Progression

```text
v0.1
Cognitive Cycle Record
        ↓
Observe one cognitive breath

v0.2
Cognitive Organ Interface
        ↓
Define how cognitive organs connect
```

The purpose of v0.2 is to move the architecture from a fixed conceptual pipeline toward a replaceable, loosely coupled distributed cognitive system.

A cognitive organ is defined by its interface contract rather than by a specific model, vendor, prompt, or runtime.

This creates the foundation for future dynamic cognitive routing and multi-organ orchestration.

## v0.3 — Cognitive Routing Layer

v0.3 introduces explicit cognitive route selection.

While v0.1 records one cognitive cycle and v0.2 defines the interface contracts of cognitive organs, v0.3 defines how a task moves through those organs.

The Cognitive Routing Layer determines:

* which cognitive organs participate
* the order of activation
* required, conditional, optional, and fallback organs
* return routes
* verification loops
* boundary-triggered re-integration
* recovery behavior
* human escalation conditions

The primary schema is:

`schemas/cognitive-routing-plan.schema.json`

The first reference example defines a deep-structure cognitive route:

`examples/cognitive-routing-plan.deep-structure.example.yaml`

### Architectural Progression

```text
v0.1
Cognitive Cycle Record
        ↓
Observe one cognitive breath

v0.2
Cognitive Organ Interface
        ↓
Define cognitive organ contracts

v0.3
Cognitive Routing Layer
        ↓
Select the required cognitive path
```

The central principle of v0.3 is:

> Activate the minimum sufficient cognitive route, then expand the route only when evidence, uncertainty, risk, memory dependency, or structural complexity requires it.

This enables the architecture to move from a fixed cognitive pipeline toward adaptive distributed cognition.

## v0.4 — Cognitive Feedback & Adaptation Layer

v0.4 introduces structured evaluation of completed cognitive cycles.

While v0.3 selects a cognitive route, v0.4 evaluates whether that route, its participating organs, and its final human-facing outcome actually performed well.

The new `Cognitive Feedback Record` captures:

* outcome quality
* semantic preservation
* human usability
* verification quality
* route fit
* route efficiency
* unnecessary organ activation
* missing cognitive organs
* loop and recovery counts
* organ-level contribution
* human corrections
* adaptation proposals
* review requirements

The primary schema is:

`schemas/cognitive-feedback-record.schema.json`

The reference example is:

`examples/cognitive-feedback-record.example.yaml`

### Architectural Progression

```text
v0.1
Cognitive Cycle Record
        ↓
Observe cognition

v0.2
Cognitive Organ Interface
        ↓
Define cognitive organs

v0.3
Cognitive Routing Layer
        ↓
Select cognitive paths

v0.4
Cognitive Feedback & Adaptation Layer
        ↓
Evaluate outcomes and propose improvements
```

The central rule of v0.4 is:

> The architecture may generate adaptation proposals, but it must not automatically apply architecture changes.

This creates a reviewable path from cognitive outcome to future improvement while preserving human authority over architectural change.

