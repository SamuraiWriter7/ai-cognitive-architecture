# Changelog

All notable changes to this project are documented in this file.

The project uses candidate releases during early architectural development.

The first architecture arc follows:

```text
v0.1  Observe
v0.2  Contract
v0.3  Route
v0.4  Evaluate
v0.5  Continue
```

---

## [0.5.0-candidate] - 2026-07-05

### Cognitive Continuity & Trace Layer

v0.5 introduces explicit continuity across multiple cognitive cycles.

The architecture can now preserve, transform, defer, and retire important cognitive structures across an inspectable lineage.

### Added

* `Cognitive Continuity Trace` specification
* multi-cycle cognitive lineage records
* current-cycle references
* previous-cycle references
* routing-plan references
* feedback-record references
* parent-trace references
* lineage-depth tracking
* inherited cognitive trace records
* trace-type classification
* question-epicenter traces
* semantic-structure traces
* assumption traces
* constraint traces
* unresolved-conflict traces
* design-decision traces
* memory-context traces
* routing-pattern traces
* feedback-pattern traces
* human-correction traces
* human-preference traces
* adaptation-candidate traces
* trace importance scoring
* trace confidence scoring
* trace lifecycle states
* active trace state
* dormant trace state
* consumed trace state
* transformed trace state
* retired trace state
* continuity-role classification
* direct-context role
* constraint role
* warning role
* hypothesis role
* design-seed role
* routing-hint role
* memory-anchor role
* human-correction role
* explicit trace-preservation reasons
* related-trace references
* state-transition records
* preserved-element records
* transformed-element records
* dropped-element records
* trace transformation records
* preserve operations
* compress operations
* merge operations
* split operations
* reframe operations
* strengthen operations
* weaken operations
* retire operations
* dropped-trace reasons
* drop-review status
* feedback carryover records
* accepted adaptation proposals
* deferred adaptation proposals
* rejected adaptation proposals
* repeated-pattern records
* pattern occurrence counting
* evidence references for repeated patterns
* pattern importance scoring
* `Next Cycle Seed`
* next-question seeds
* required-context references
* open-conflict carryover
* priority targets
* routing hints
* activation conditions
* continuity policy
* maximum inherited-trace limits
* decay-mode selection
* relevance-based decay
* time-based decay support
* hybrid decay support
* minimum-importance thresholds
* human-correction preservation policy
* unresolved-conflict preservation policy
* required trace-origin policy
* explicit prohibition of silent trace dropping
* trace-compression policy
* periodic continuity-review intervals
* human-review records for continuity decisions
* Cognitive Continuity & Trace Layer documentation
* multi-target validation for v0.1 through v0.5 artifacts

### Architectural Meaning

v0.1 made one cognitive cycle observable.

v0.2 defined cognitive-organ contracts.

v0.3 introduced adaptive cognitive routing.

v0.4 introduced feedback evaluation and adaptation proposals.

v0.5 connects cognitive cycles into explicit lineage.

The architecture can now represent not only:

> what happened in one cognitive cycle

but also:

> what should survive, transform, remain unresolved, or seed the next cycle.

### Design Principle

> Preserve significant structure, not all historical text.

The continuity layer distinguishes between memory, trace, and lineage.

```text
Memory
→ preserves cognitive availability

Trace
→ preserves significance

Continuity
→ preserves lineage
```

### No Silent Trace Loss

Important cognitive traces should not disappear silently.

The architecture may record:

* which trace changed
* how it changed
* why it changed
* whether review was required
* whether the change was approved

Human corrections and unresolved conflicts may receive explicit preservation protection.

### First Arc Completion

v0.5 completes the first architecture arc:

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

Together, these layers establish the initial distributed cognitive architecture foundation.

### Scope Boundary

v0.5 does not define:

* autonomous trace rewriting
* automatic architecture mutation
* hidden memory modification
* automatic preference inference
* permanent storage of all conversation history
* autonomous identity formation
* unsupervised removal of unresolved conflicts
* self-approved architecture changes

---

## [0.4.0-candidate] - 2026-07-05

### Cognitive Feedback & Adaptation Layer

v0.4 introduces structured evaluation of completed cognitive cycles.

The architecture can now evaluate outcomes, routes, individual cognitive organs, and human feedback before generating reviewable adaptation proposals.

### Added

* `Cognitive Feedback Record` specification
* outcome-status evaluation
* successful status
* partially successful status
* unsuccessful status
* inconclusive status
* human-review-pending status
* goal-completion scoring
* semantic-preservation scoring
* human-usability scoring
* verification-quality scoring
* overall cognitive outcome scoring
* unresolved-issue recording
* route-fit evaluation
* route-efficiency evaluation
* unnecessary-organ detection
* missing-organ detection
* cognitive-loop counting
* recovery-attempt counting
* escalation-quality evaluation
* route-issue records
* route-strength records
* organ-level evaluation records
* participation status
* input-quality scoring
* output-quality scoring
* interface-contract compliance scoring
* organ contribution scoring
* organ strengths
* organ issues
* recommended organ changes
* human feedback records
* human correction records
* acceptance status
* partial-acceptance status
* rejection status
* pending status
* user preference signals
* adaptation proposals
* adaptation target layers
* memory adaptation target
* routing adaptation target
* organ-interface adaptation target
* verification adaptation target
* boundary adaptation target
* translation adaptation target
* Human Gate adaptation target
* rumination adaptation target
* architecture adaptation target
* adaptation proposal types
* add
* remove
* strengthen
* weaken
* reorder
* reroute
* clarify
* split
* merge
* observe
* evidence references for adaptation proposals
* proposal-priority scoring
* automatic-application prohibition
* human-review requirements
* feedback-record retention policy
* Cognitive Feedback & Adaptation Layer documentation
* extended multi-target validation for v0.1 through v0.4 artifacts

### Architectural Meaning

v0.4 allows the architecture to ask:

> How well did the cognitive cycle actually work?

The architecture can distinguish between:

* successful outcomes with inefficient routes
* correct routes with weak organ output
* strong analysis with poor language recomposition
* useful output with excessive cognitive activation
* repeated failures that justify future review

### Four Evaluation Levels

#### Outcome Quality

Evaluates:

* goal completion
* semantic preservation
* human usability
* verification quality
* unresolved issues

#### Route Quality

Evaluates:

* route fit
* route efficiency
* unnecessary organs
* missing organs
* loop count
* recovery count
* escalation quality

#### Organ Quality

Evaluates:

* input quality
* output quality
* contract compliance
* contribution score
* strengths
* issues

#### Human Feedback

Records:

* acceptance
* partial acceptance
* rejection
* correction requirements
* preferences
* notes

### Design Principle

> Feedback may generate adaptation proposals, but adaptation proposals do not authorize automatic self-modification.

The controlled path is:

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
* automatic Boundary modification
* unsupervised route replacement
* self-approved permission expansion
* reinforcement-learning execution
* automatic deployment of architecture changes

---

## [0.3.0-candidate] - 2026-07-05

### Cognitive Routing Layer

v0.3 introduces explicit route selection across cognitive organs.

The architecture can now select different cognitive paths according to task type, complexity, uncertainty, risk, memory dependency, and external-information requirements.

### Added

* `Cognitive Routing Plan` specification
* input-profile structure
* task-type classification
* simple-answer task type
* translation task type
* summarization task type
* analysis task type
* design task type
* verification task type
* decision-support task type
* open-research task type
* safety-sensitive task type
* custom task type
* complexity scoring
* uncertainty scoring
* risk-level scoring
* memory-dependency scoring
* external-information-dependency scoring
* required-capability declarations
* routing modes
* minimal routing mode
* standard routing mode
* deep-structure routing mode
* safety-review routing mode
* memory-intensive routing mode
* custom routing mode
* route-step definitions
* required activation
* conditional activation
* optional activation
* fallback activation
* activation conditions
* skip conditions
* expected input artifacts
* expected output artifacts
* controlled cognitive loops
* maximum loop-count limits
* optional parallel-branch declarations
* verification-before-output policy
* boundary-before-output policy
* preferred return routes
* route-return conditions
* explicit termination conditions
* missing-artifact recovery policy
* validation-failure recovery policy
* route-block recovery policy
* maximum recovery-attempt limits
* human escalation
* human escalation conditions
* human escalation presentation requirements
* Deep Structure routing example
* Cognitive Routing Layer documentation
* extended multi-target validation for v0.1 through v0.3 artifacts

### Architectural Meaning

v0.1 answered:

> What happened during one cognitive cycle?

v0.2 answered:

> What can each cognitive organ receive, produce, preserve, and route?

v0.3 answers:

> Which cognitive organs should participate in this task, and how should cognition move between them?

### Routing Principle

> Activate the minimum sufficient cognitive route, then expand only when the task requires it.

Not every task should activate every cognitive organ.

### Routing Modes

#### Minimal

Typical route:

```text
Yin Semantic Decomposer
        ↓
Yang Language Recomposer
        ↓
Human Gate
```

#### Standard

Typical route:

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

#### Deep Structure

Typical route:

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

### Controlled Cognitive Loops

v0.3 allows explicit bounded loops.

Examples:

```text
Verifier
    ↓
Structural Core
```

```text
Verifier
    ↓
Analyst
```

```text
Structural Core
    ↓
Memory Breathing
```

```text
Boundary
    ↓
Structural Core
```

Loops must be:

* explicit
* condition-based
* observable
* bounded

### Human Escalation

Human escalation is treated as a valid route rather than a system failure.

The architecture may escalate when:

* high-priority interpretations remain unresolved
* evidence is insufficient
* recovery attempts are exhausted
* safety constraints conflict with task objectives
* one route cannot be justified over another
* human authority may be affected

### Scope Boundary

v0.3 does not define:

* automatic route optimization
* route-performance learning
* energy-cost accounting
* adaptive route mutation
* cognitive load balancing
* multi-cycle continuity
* autonomous architecture self-modification

---

## [0.2.0-candidate] - 2026-07-05

### Cognitive Organ Interface Contract

v0.2 introduces machine-readable interface contracts for cognitive organs.

The architecture now defines not only that cognitive organs exist, but how they receive, produce, preserve, route, observe, and recover.

### Added

* `Cognitive Organ Interface` specification
* cognitive-organ identity
* functional-role definitions
* responsibilities
* non-responsibilities
* consumed-artifact declarations
* produced-artifact declarations
* artifact schema references
* required-artifact flags
* invocation policies
* always invocation mode
* conditional invocation mode
* on-request invocation mode
* event-driven invocation mode
* preconditions
* skip conditions
* blocking conditions
* routing policies
* allowed predecessors
* allowed successors
* return routes
* human escalation permissions
* semantic guarantees
* required preserved elements
* mandatory reporting requirements
* quality conditions
* cognitive authority levels
* observe authority
* interpret authority
* recommend authority
* validate authority
* filter authority
* gate authority
* meta-update authority
* prohibited actions
* human-review requirements
* observability policy
* input-recording policy
* output-recording policy
* summary-recording policy
* uncertainty-recording policy
* trace-field declarations
* failure policies
* stop-cycle failure behavior
* skip-organ failure behavior
* return-to-predecessor behavior
* route-to-Verifier behavior
* route-to-Human-Gate behavior
* fallback-organ definitions
* failure-artifact definitions
* Structural Core reference interface example
* Cognitive Organ Interface documentation
* multi-target schema validation

### Architectural Meaning

v0.1 defined the record of one cognitive cycle.

v0.2 defines the contracts of the cognitive organs participating in that cycle.

The architecture can now describe:

* what each organ receives
* what each organ produces
* what meaning it must preserve
* what it must report
* where it may route
* what it must not do
* how failure should be handled

### Design Principle

> A cognitive organ is defined by its contract, not by its model.

Different implementations may participate in the same architecture when they satisfy the same interface requirements.

For example, different Finder implementations may use:

* web search
* local documents
* databases
* environmental sensors
* archived logs

while preserving the same functional role.

### Scope Boundary

v0.2 does not define:

* dynamic route selection
* route scoring
* cognitive load balancing
* capability discovery
* multi-cycle continuity
* semantic translation diffs
* autonomous architecture mutation

---

## [0.1.0-candidate] - 2026-07-05

### Cognitive Cycle Record

v0.1 introduces the initial AI Cognitive Architecture specification.

The release defines the first canonical architecture record:

`Cognitive Cycle Record`

The record captures one complete distributed cognitive cycle.

### Added

* initial AI Cognitive Architecture specification
* `Cognitive Cycle Record`
* JSON Schema for one complete distributed cognitive cycle
* YAML reference example
* architecture identifier
* cycle identifier
* creation timestamp
* human input record
* environment references
* log references
* cognitive-organ registry
* Finder organ record
* Yin Semantic Decomposer organ record
* Memory Breathing organ record
* Analyst organ record
* Structural Core organ record
* Verifier organ record
* Boundary organ record
* Yang Language Recomposer organ record
* Human Gate organ record
* Structural Rumination organ record
* organ activation status
* organ input references
* organ output references
* cognitive-cycle stage records
* stage ordering
* stage status
* stage summaries
* structural integration record
* integrated structure
* conflict report
* conflict status
* priority map
* weighted priority records
* Human Gate output record
* human-facing summary
* options
* warnings
* decision-required flag
* rumination record
* memory-update candidates
* routing-update candidates
* architecture-update candidates
* Python validation script
* GitHub Actions validation workflow
* initial architecture overview documentation

### Architectural Meaning

v0.1 establishes the minimum observable unit of the architecture:

> one human input passing through a distributed cognitive cycle and producing an auditable record of interpretation, memory, analysis, integration, verification, boundary control, translation, human presentation, and rumination.

### Core Cycle

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
```

### Design Principles

v0.1 establishes the initial principles of:

* functional differentiation
* structure before expression
* cyclic cognition
* human-centered control
* auditability
* uncertainty preservation

### Scope Boundary

v0.1 does not define:

* dynamic routing
* executable orchestration
* autonomous architecture mutation
* cognitive-organ service protocols
* multi-cycle continuity
* semantic translation diff records
* cognitive trace receipts

These are addressed or prepared for in later versions.

---

# First Arc Summary

The first architecture arc is now:

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

The progression can also be described as:

```text
Record one cognitive breath
        ↓
Define the organs
        ↓
Select the cognitive path
        ↓
Evaluate the path
        ↓
Preserve the lineage
```

Together:

```text
Observation
+
Contracts
+
Routing
+
Feedback
+
Continuity
=
AI Cognitive Architecture First Arc
```

The first arc establishes the foundation of an observable, modular, adaptive, feedback-aware, continuity-preserving, human-centered distributed cognitive architecture.
