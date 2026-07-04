# AI Cognitive Architecture

**A distributed cognitive architecture for Multi-GPT systems.**

AI Cognitive Architecture is an experimental specification for organizing specialized AI systems as functional cognitive organs within a shared, observable, adaptive, and continuity-preserving cognitive system.

The project explores a shift from:

```text
many AI agents
```

to:

```text
distributed cognitive organs
+
explicit interfaces
+
adaptive routing
+
feedback evaluation
+
cognitive continuity
```

The architecture does not claim to reproduce the biological human brain.

Instead, it defines a functional model of distributed cognition in which sensing, semantic decomposition, memory, analysis, integration, verification, boundary control, language recomposition, human judgment, and structural rumination are treated as distinct but connected cognitive functions.

---

## Status

Current architecture arc:

**v0.1 → v0.5**

Current first-arc sequence:

```text
Observe
  ↓
Contract
  ↓
Route
  ↓
Evaluate
  ↓
Continue
  ↺
```

Current candidate release:

**v0.5.0-candidate**

---

## Core Idea

A conventional AI interaction is often represented as:

```text
Input
  ↓
Model
  ↓
Output
```

AI Cognitive Architecture instead defines a distributed cognitive cycle:

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
Cognitive Feedback
    ↓
Cognitive Continuity
    ↓
Next Cognitive Cycle
```

The central design principle is:

> Human language is first interpreted as explicit structure, processed across specialized cognitive organs, integrated, verified, translated back into human language, reviewed through human-facing boundaries, evaluated, and selectively carried into future cognition.

---

# Architecture Overview

## 1. Functional Differentiation

The architecture treats specialized AI systems as cognitive organs rather than generic interchangeable agents.

Examples include:

* sensing and retrieval
* semantic decomposition
* memory
* analysis
* structural integration
* verification
* boundary control
* human-language recomposition
* human decision support
* structural rumination
* feedback evaluation
* continuity preservation

Each function has its own role, inputs, outputs, boundaries, and observability requirements.

---

## 2. Structure Before Expression

The architecture does not assume that human-language input should immediately become human-language output.

Instead:

```text
Human Language
      ↓
Semantic Structure
      ↓
Distributed Cognition
      ↓
Integrated Structure
      ↓
Human-Language Recomposition
```

This creates an explicit structural layer between interpretation and expression.

---

## 3. Cyclic Cognition

The architecture is not based on one-way processing.

Its basic assumption is:

```text
input
→ structure
→ analysis
→ integration
→ verification
→ expression
→ human judgment
→ feedback
→ continuity
→ next input
```

The output of one cognitive cycle may become structured input for the next.

---

## 4. Human-Centered Control

Human involvement is not treated as an external exception.

Human Gate, human feedback, and human review are architectural components.

The system may:

* prepare options
* surface uncertainty
* present unresolved conflicts
* request judgment
* preserve human corrections
* retain human preferences when explicitly provided
* require review before architecture-level change

The architecture supports human judgment rather than attempting to eliminate it.

---

## 5. Auditability

Important cognitive transitions should produce inspectable records.

The architecture therefore uses explicit artifacts such as:

* `CognitiveCycleRecord`
* `CognitiveOrganInterface`
* `CognitiveRoutingPlan`
* `CognitiveFeedbackRecord`
* `CognitiveContinuityTrace`

The goal is not exposure of hidden internal reasoning.

The goal is to preserve:

* observable inputs
* observable outputs
* structural summaries
* uncertainty
* conflicts
* routing decisions
* review decisions
* continuity lineage

---

# Cognitive Organs

## Finder

Role:

External sensing and retrieval.

Finder may gather information from:

* external sources
* documents
* logs
* archives
* databases
* environmental inputs

Primary output:

`RawInfoSet`

Finder should only activate when external information is actually needed.

---

## Yin Semantic Decomposer

Role:

Human Language → Structural Interpretation

The Yin Semantic Decomposer transforms human-language input into explicit semantic structure.

It may extract:

* primary intent
* secondary intent
* concepts
* relationships
* assumptions
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

The Yin function does not primarily answer.

It first asks:

> What is this question structurally asking?

---

## Memory Breathing

Role:

Selective contextual memory.

Memory Breathing provides historical context without treating all prior information as equally important.

Primary outputs:

* `ContextFrame`
* `HistoryTrace`

Its central question is:

> What should remain cognitively available now?

---

## Analyst

Role:

Structured reasoning, comparison, evaluation, hypothesis formation, and design.

Primary outputs:

* `AnalysisGraph`
* `HypothesisSet`
* `DesignProposal`

Analyst performs reasoning over explicit structures rather than replacing the entire cognitive architecture.

---

## Structural Core

Role:

Structural integration.

Structural Core integrates:

* semantic structures
* memory context
* analysis outputs
* conflicts
* priorities
* uncertainty

Primary outputs:

* `IntegratedStructure`
* `ConflictReport`
* `PriorityMap`

Its central question is:

> What do these structures mean together?

Structural Core is distinct from Human Gate.

Structural Core performs semantic integration.

Human Gate prepares information for human judgment.

---

## Verifier

Role:

Consistency and validation.

Verifier may examine:

* logical consistency
* specification compliance
* evidence sufficiency
* uncertainty handling
* unresolved conflicts
* validation conditions

Primary outputs:

* `ValidationReport`
* `RiskMap`

Verifier may return a task to Analyst or Structural Core when necessary.

---

## Boundary

Role:

Authority and output-boundary control.

Boundary may define:

* allowed actions
* prohibited actions
* filtering requirements
* escalation requirements
* authority limits

Primary outputs:

* `AllowedActionSet`
* `FilteredOutput`

Boundary must not invent missing evidence or silently replace the human goal.

---

## Yang Language Recomposer

Role:

Integrated Structure → Human Understanding

The Yang Language Recomposer transforms validated and bounded structures into human-readable language.

Primary outputs:

* `HumanText`
* `ExampleSet`
* `Reframing`

Its purpose is not mere simplification.

Its purpose is meaning-preserving recomposition.

It should preserve:

* uncertainty
* important constraints
* unresolved conflicts
* semantic nuance
* the central question epicenter

---

## Human Gate

Role:

Human-facing decision preparation.

Human Gate asks:

> What should the human see, compare, understand, or decide?

It may prepare:

* summaries
* options
* warnings
* unresolved issues
* confidence information
* explicit decision points

Primary output:

`HumanFacingBundle`

Human Gate does not silently substitute itself for human judgment.

---

## Structural Rumination

Role:

Meta-cognitive reflection.

Structural Rumination examines completed cognitive cycles and asks:

* What worked?
* What failed?
* Which route was inefficient?
* Which organ lacked information?
* Did translation lose meaning?
* Did verification miss something?
* Was Boundary overactive?
* Should memory or routing be reconsidered?

Primary outputs:

* `MetaStructureUpdate`
* `DesignReflection`

Structural Rumination evaluates one cycle or local structure.

Architecture-wide evaluation is handled by the Cognitive Feedback layer.

---

# First Architecture Arc

## v0.1 — Cognitive Cycle Record

### Observe

v0.1 defines one observable distributed cognitive cycle.

The primary artifact is:

`Cognitive Cycle Record`

It records:

* human input
* participating cognitive organs
* cognitive stages
* stage inputs
* stage outputs
* structural integration
* conflict records
* priority maps
* Human Gate output
* rumination output

Primary schema:

```text
schemas/cognitive-cycle-record.schema.json
```

Reference example:

```text
examples/cognitive-cycle-record.example.yaml
```

The central idea is:

> One cognitive cycle should be observable as a structured record.

---

## v0.2 — Cognitive Organ Interface

### Contract

v0.2 defines the machine-readable contracts of cognitive organs.

The primary artifact is:

`Cognitive Organ Interface`

Each interface may define:

* functional role
* responsibilities
* non-responsibilities
* consumed artifacts
* produced artifacts
* invocation mode
* preconditions
* skip conditions
* blocking conditions
* allowed predecessors
* allowed successors
* return routes
* semantic guarantees
* authority boundaries
* observability policy
* failure policy

Primary schema:

```text
schemas/cognitive-organ-interface.schema.json
```

Reference example:

```text
examples/cognitive-organ-interface.structural-core.example.yaml
```

The central principle is:

> A cognitive organ is defined by its contract, not by its model.

Different implementations may participate in the same architecture when they satisfy the same functional contract.

---

## v0.3 — Cognitive Routing Layer

### Route

v0.3 defines how tasks move through cognitive organs.

The primary artifact is:

`Cognitive Routing Plan`

It may define:

* input profile
* task type
* complexity
* uncertainty
* risk
* memory dependency
* external-information dependency
* required capabilities
* selected cognitive route
* required organs
* conditional organs
* optional organs
* fallback organs
* controlled loops
* return routes
* recovery policies
* termination conditions
* human escalation

Primary schema:

```text
schemas/cognitive-routing-plan.schema.json
```

Reference example:

```text
examples/cognitive-routing-plan.deep-structure.example.yaml
```

The central principle is:

> Activate the minimum sufficient cognitive route, then expand only when the task requires it.

---

## Routing Modes

### Minimal

For simple and low-risk tasks.

```text
Yin Semantic Decomposer
        ↓
Yang Language Recomposer
        ↓
Human Gate
```

### Standard

For ordinary analytical tasks.

```text
Yin Semantic Decomposer
        ↓
Analyst
        ↓
Structural Core
        ↓
Verifier
        ↓
Yang Language Recomposer
        ↓
Human Gate
```

### Deep Structure

For complex design, philosophy, architecture, and long-context reasoning.

```text
Yin Semantic Decomposer
        ↓
Memory Breathing
        ↓
Finder
        ↓
Analyst
        ↓
Structural Core
        ↓
Verifier
        ↓
Boundary
        ↓
Structural Core
        ↓
Yang Language Recomposer
        ↓
Human Gate
        ↓
Structural Rumination
```

### Safety Review

For tasks dominated by risk, permissions, safety, or authority boundaries.

### Memory Intensive

For tasks requiring historical continuity and prior cognitive traces.

---

## v0.4 — Cognitive Feedback & Adaptation Layer

### Evaluate

v0.4 evaluates whether a completed cognitive route actually worked.

The primary artifact is:

`Cognitive Feedback Record`

It evaluates four levels.

### Outcome Quality

* goal completion
* semantic preservation
* human usability
* verification quality
* unresolved issues
* overall result quality

### Route Quality

* route fit
* route efficiency
* unnecessary organs
* missing organs
* loop count
* recovery count
* escalation quality

### Organ Quality

* input quality
* output quality
* contract compliance
* contribution score
* strengths
* issues
* recommended changes

### Human Feedback

* acceptance
* partial acceptance
* rejection
* correction requirements
* preferences
* notes

Primary schema:

```text
schemas/cognitive-feedback-record.schema.json
```

Reference example:

```text
examples/cognitive-feedback-record.example.yaml
```

The central rule is:

> Feedback may generate adaptation proposals, but adaptation proposals do not authorize automatic architecture change.

The controlled flow is:

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
  ↓
Possible Future Update
```

---

## v0.5 — Cognitive Continuity & Trace Layer

### Continue

v0.5 connects multiple cognitive cycles into an inspectable cognitive lineage.

The primary artifact is:

`Cognitive Continuity Trace`

It may preserve:

* question epicenters
* semantic structures
* important assumptions
* constraints
* unresolved conflicts
* design decisions
* memory anchors
* routing patterns
* repeated feedback patterns
* human corrections
* human preferences
* adaptation candidates

Primary schema:

```text
schemas/cognitive-continuity-trace.schema.json
```

Reference example:

```text
examples/cognitive-continuity-trace.example.yaml
```

The central principle is:

> Preserve significant structure, not all historical text.

---

# Memory, Trace, and Continuity

These concepts are related but distinct.

## Memory Breathing

Question:

> What should remain cognitively available?

Memory manages relevance and availability.

---

## Trace

Question:

> What is significant enough to pass forward?

Trace preserves importance.

---

## Cognitive Continuity

Question:

> What must be inherited to preserve the identity and direction of a cognitive lineage?

Continuity preserves lineage.

The relationship is:

```text
Memory
→ preserves availability

Trace
→ preserves significance

Continuity
→ preserves lineage
```

---

# Cognitive Continuity

A continuity trace may preserve, transform, defer, or retire inherited structure.

Supported transformations may include:

* preserve
* compress
* merge
* split
* reframe
* strengthen
* weaken
* retire

Important trace loss must not occur silently.

When an important trace is dropped or retired, the architecture should record:

* which trace changed
* why it changed
* whether review was required
* whether the change was approved

Human corrections and unresolved conflicts may receive explicit preservation protection.

---

# Next Cycle Seed

The output of continuity is not merely a historical summary.

A `Next Cycle Seed` may define:

* next question
* required context
* open conflicts
* priority targets
* routing hints
* activation conditions

Example:

```text
Current Cognitive Cycle
        ↓
Feedback
        ↓
Rumination
        ↓
Continuity Trace
        ↓
Next Cycle Seed
        ↓
Next Cognitive Cycle
```

This allows cognition to continue structurally rather than merely restarting from accumulated conversation text.

---

# Cognitive Economy

The architecture does not assume:

> more cognition is always better.

Instead, it asks:

> What is the minimum sufficient cognitive path for this task?

This connects the architecture to broader ideas of:

* specialized cognition
* selective memory
* computational breathing
* adaptive routing
* conditional verification
* bounded loops
* selective continuity

The architecture may evaluate questions such as:

* Was Finder necessary?
* Was Memory Breathing sufficient?
* Was Verifier activated too late?
* Was Boundary unnecessary?
* Did a return loop improve quality?
* Did translation lose meaning?
* Did Human Gate expose the correct decision points?

The goal is not merely better answers.

The goal is better cognitive structure.

---

# Human Authority

Human authority is preserved across the architecture.

Human review may be required when:

* high-priority interpretations remain unresolved
* evidence is insufficient
* safety and task goals conflict
* architecture-level changes are proposed
* routing rules may change
* human corrections may be removed
* unresolved conflicts may be retired
* authority boundaries may change
* persistent cognitive lineage may be rewritten

The architecture follows the principle:

> The system may observe, evaluate, and propose.

> It does not automatically gain authority to rewrite its own architecture.

---

# No Hidden Reasoning Requirement

The architecture does not require disclosure of hidden internal reasoning.

Instead, it records inspectable structural information such as:

* input references
* output references
* summaries
* uncertainty
* conflicts
* priorities
* route decisions
* validation results
* adaptation proposals
* continuity transformations

The objective is observable cognition, not exposure of private internal computation.

---

# Repository Structure

```text
.
├─ .github/
│  └─ workflows/
│     └─ validate.yml
│
├─ schemas/
│  ├─ cognitive-cycle-record.schema.json
│  ├─ cognitive-organ-interface.schema.json
│  ├─ cognitive-routing-plan.schema.json
│  ├─ cognitive-feedback-record.schema.json
│  └─ cognitive-continuity-trace.schema.json
│
├─ examples/
│  ├─ cognitive-cycle-record.example.yaml
│  ├─ cognitive-organ-interface.structural-core.example.yaml
│  ├─ cognitive-routing-plan.deep-structure.example.yaml
│  ├─ cognitive-feedback-record.example.yaml
│  └─ cognitive-continuity-trace.example.yaml
│
├─ docs/
│  ├─ architecture-overview.md
│  ├─ cognitive-organ-interface.md
│  ├─ cognitive-routing-layer.md
│  ├─ cognitive-feedback-adaptation-layer.md
│  └─ cognitive-continuity-trace-layer.md
│
├─ scripts/
│  └─ validate_examples.py
│
├─ README.md
├─ CHANGELOG.md
└─ requirements.txt
```

---

# Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected validation targets:

```text
Cognitive Cycle Record
Cognitive Organ Interface
Cognitive Routing Plan
Cognitive Feedback Record
Cognitive Continuity Trace
```

Each example should validate against its corresponding JSON Schema.

GitHub Actions may run the same validation automatically on:

* push
* pull request
* manual workflow dispatch

---

# First Arc Summary

The first architecture arc is:

```text
v0.1
Observe

v0.2
Contract

v0.3
Route

v0.4
Evaluate

v0.5
Continue
```

Together:

```text
Observation
+
Functional Contracts
+
Adaptive Routing
+
Feedback Evaluation
+
Cognitive Continuity
=
Distributed Cognitive Architecture Foundation
```

The system can now represent:

* one cognitive cycle
* specialized cognitive organs
* explicit organ contracts
* adaptive cognitive routes
* controlled loops
* recovery paths
* human escalation
* outcome evaluation
* organ evaluation
* adaptation proposals
* multi-cycle continuity
* cognitive lineage

---

# Definition

> AI Cognitive Architecture is a distributed cognitive OS layer in which specialized AI systems participate as functional cognitive organs connected through explicit interfaces, adaptive routing, structural integration, verification, boundary control, human-language recomposition, human judgment, feedback evaluation, and continuity-preserving traces.

---

# Civilizational Position

The architecture reframes Multi-GPT systems.

Instead of:

```text
many GPTs
=
many tools
```

it explores:

```text
specialized cognitive organs
+
shared structural interfaces
+
adaptive routing
+
human review
+
feedback
+
continuity
=
distributed cognitive system
```

The long-term objective is not the multiplication of AI agents.

The objective is the emergence of a coherent, inspectable, modular, energy-aware, feedback-capable, and human-centered cognitive architecture.

---

# Scope Boundary

The current first arc does not define:

* autonomous architecture mutation
* autonomous prompt rewriting
* unsupervised route replacement
* self-approved Boundary modification
* autonomous permission expansion
* hidden memory modification
* automatic human-preference inference
* autonomous removal of unresolved conflicts
* permanent retention of all conversation history
* reinforcement-learning execution
* production deployment mechanisms

The current architecture defines explicit records, contracts, routes, feedback, adaptation proposals, and continuity structures.

---

# Motto

> Structure before expression.
> Contracts before orchestration.
> Minimum sufficient cognition before maximum activation.
> Evidence before adaptation.
> Continuity before repetition.
> Human judgment before architectural change.
