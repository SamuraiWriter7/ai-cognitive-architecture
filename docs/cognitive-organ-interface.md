# Cognitive Organ Interface

## 1. Purpose

The Cognitive Organ Interface defines how specialized AI cognitive organs participate in a distributed cognitive architecture.

A cognitive organ is not defined primarily by its model provider, model size, prompt, or implementation language.

It is defined by its contract.

The contract specifies:

* what the organ consumes
* what the organ produces
* when the organ may run
* where information may be routed
* what meaning must be preserved
* what actions are prohibited
* what must be recorded
* how failure is handled

This enables cognitive organs to remain functionally distinct while participating in a shared architecture.

## 2. From Agent Collection to Cognitive System

A collection of AI agents is not automatically a cognitive architecture.

Without explicit interfaces, a system may contain many agents while remaining structurally opaque.

```text
Agent A
Agent B
Agent C
Agent D
```

becomes a cognitive architecture only when relationships are explicit.

```text
Input Artifact
      ↓
Cognitive Organ
      ↓
Output Artifact
      ↓
Next Cognitive Organ
```

The Cognitive Organ Interface defines these relationships.

## 3. Functional Identity

Each cognitive organ has a functional identity.

Examples include:

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

A concrete implementation may change.

For example, one Finder may use web search, another local documents, and another environmental sensors.

As long as each implementation satisfies the required interface contract, it may participate in the same cognitive architecture.

## 4. Artifact Contracts

Cognitive organs communicate through explicit artifacts.

Examples include:

* RawInfoSet
* SemanticStructure
* AssumptionSet
* ContextFrame
* HistoryTrace
* AnalysisGraph
* HypothesisSet
* IntegratedStructure
* ConflictReport
* ValidationReport
* FilteredOutput
* HumanText
* HumanFacingBundle
* MetaStructureUpdate

The architecture does not require every organ to understand every artifact.

An organ only needs to understand the artifacts defined by its own interface.

This reduces unnecessary coupling.

## 5. Invocation Policy

Not every cognitive organ must run in every cycle.

An interface may define one of four invocation modes:

### Always

The organ participates in every applicable cognitive cycle.

### Conditional

The organ runs when explicit preconditions are satisfied.

### On Request

Another organ or human participant explicitly invokes it.

### Event Driven

The organ runs when a specified architecture event occurs.

This distinction creates the foundation for later dynamic cognitive routing.

## 6. Routing Policy

Each organ declares:

* allowed predecessors
* allowed successors
* permitted return routes
* whether human escalation is allowed

This makes cognitive flow inspectable.

For example:

```text
Analyst
   ↓
Structural Core
   ↓
Verifier
   │
   ├─ valid → Boundary
   │
   └─ conflict → Structural Core
                     │
                     └→ Analyst
```

The architecture therefore supports loops without allowing unrestricted routing.

## 7. Guarantees

An interface may define semantic guarantees.

Examples:

* preserve uncertainty
* preserve source references
* preserve the original question epicenter
* report conflicts
* report missing evidence
* explain priority decisions

These guarantees are essential because a technically valid transformation may still damage meaning.

The architecture therefore treats semantic preservation as an interface responsibility.

## 8. Boundaries

Every organ has limited authority.

An Analyst may recommend but not gate.

A Verifier may validate but not rewrite the user's goal.

A Boundary organ may filter but should not invent evidence.

A Human Gate may prepare decisions but should not silently substitute itself for the human.

Explicit boundaries prevent functional roles from collapsing into one opaque agent.

## 9. Observability

Each organ declares which parts of its activity are recorded.

The interface may require records of:

* input references
* output references
* summary
* uncertainty
* conflicts
* decisions
* trace fields

Observability does not require disclosure of hidden internal reasoning.

The objective is to record inspectable outputs and decision-relevant structural information.

## 10. Failure Policy

Cognitive organs can fail.

A failure may cause the architecture to:

* stop the cycle
* skip the organ
* return to the predecessor
* route to Verifier
* route to Human Gate

Failure handling is therefore part of cognition rather than an external operational concern.

## 11. Architectural Meaning

v0.1 defined one cognitive breath.

v0.2 defines the interfaces between the organs participating in that breath.

Together:

```text
Cognitive Cycle Record
+
Cognitive Organ Interface
=
Observable Cognitive Flow
```

This is the foundation for future dynamic routing, multi-cycle cognition, cognitive trace receipts, and architecture adaptation.
