# Cognitive Routing Layer

## 1. Purpose

The Cognitive Routing Layer defines how a cognitive task is routed across specialized cognitive organs.

Earlier layers define:

* how one cognitive cycle is recorded
* how each cognitive organ declares its interface contract

The routing layer defines:

* which organs should participate
* in what order they should run
* which organs are optional
* when a route should loop
* where a failed route should return
* when human escalation is required

The routing layer therefore converts a collection of available cognitive organs into an adaptive cognitive flow.

## 2. Why Routing Matters

Not every task requires the same cognitive path.

A simple explanation task may require only semantic decomposition, language recomposition, and Human Gate presentation.

A complex architecture design task may require:

* semantic decomposition
* memory retrieval
* external information retrieval
* analysis
* structural integration
* verification
* boundary review
* re-integration
* language recomposition
* human presentation
* structural rumination

Running every cognitive organ for every task would create unnecessary complexity and computational overhead.

The routing layer therefore follows the principle:

> Activate the minimum sufficient cognitive path, then expand only when the task requires it.

## 3. Input Profiling

Before route selection, a task may be described by an input profile.

The profile may include:

* task type
* complexity
* uncertainty
* risk level
* memory dependency
* external information dependency
* required capabilities

These values do not represent biological cognition.

They are architectural signals used to select and justify an appropriate route.

## 4. Routing Modes

### Minimal Route

Used for low-complexity and low-risk tasks.

Typical route:

```text
Yin Semantic Decomposer
        ↓
Yang Language Recomposer
        ↓
Human Gate
```

### Standard Route

Used for ordinary analytical work.

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

### Deep Structure Route

Used for complex design, philosophy, architecture, and long-context reasoning.

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

### Safety Review Route

Used when risk, authority, or safety boundaries dominate the task.

### Memory-Intensive Route

Used when historical continuity and prior trace retrieval are central.

## 5. Controlled Loops

The Cognitive Routing Layer allows loops, but loops must be explicit and bounded.

Examples:

```text
Verifier
   ↓ validation failure
Structural Core
```

```text
Verifier
   ↓ insufficient evidence
Analyst
```

```text
Structural Core
   ↓ insufficient history
Memory Breathing
```

```text
Boundary
   ↓ structure modified
Structural Core
```

Every loop should define:

* source organ
* destination organ
* activation condition
* maximum repetition limit

This prevents uncontrolled cognitive circulation.

## 6. Conditional Activation

An organ may be activated only when required.

For example, Finder may be invoked when:

* external information is required
* evidence is missing
* the task depends on unstable current information

Boundary may be invoked when:

* risk exceeds a defined threshold
* authority boundaries are affected
* Verifier reports safety-sensitive conditions

Structural Rumination may be required only for:

* architecture updates
* repeated failures
* high-complexity tasks
* route redesign

Conditional activation creates an energy-aware cognitive architecture.

## 7. Fallback Policy

A routing plan must define behavior for incomplete or failed routes.

Examples include:

* invoke Finder when evidence is missing
* invoke Memory Breathing when historical context is missing
* return to Analyst when reasoning is insufficient
* return to Structural Core when validation fails
* route to Human Gate when automated resolution is inappropriate
* stop the cycle when no safe route remains

Failure recovery is therefore part of cognitive routing.

## 8. Human Escalation

Human escalation is a first-class route.

The system should route to Human Gate when:

* high-priority interpretations remain unresolved
* available evidence is insufficient
* safety constraints conflict with task objectives
* recovery attempts are exhausted
* the task affects human authority
* the architecture cannot justify one route over another

Human escalation is not a system failure.

It is a valid cognitive route.

## 9. Routing and Cognitive Economy

The routing layer supports a broader architectural principle:

> Not every cognitive organ must be activated for every question.

This enables:

* lower computational cost
* reduced unnecessary reasoning
* clearer trace records
* smaller failure surfaces
* better specialization
* explainable cognitive paths

The routing layer therefore acts as both an orchestration layer and a cognitive economy layer.

## 10. Architectural Progression

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
```

Together, these layers establish:

```text
Observable Cycle
+
Contracted Organs
+
Explicit Routing
=
Distributed Cognitive Architecture Foundation
```

## 11. Scope Boundary

v0.3 defines route selection and route representation.

It does not yet define:

* automatic route optimization from historical performance
* cognitive load balancing
* energy cost measurement
* route mutation learning
* multi-cycle state continuity
* architecture self-modification

These may be introduced in later versions.
