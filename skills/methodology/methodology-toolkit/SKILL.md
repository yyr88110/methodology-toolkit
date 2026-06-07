---
name: methodology-toolkit
description: "52 thinking tools for AI agents — covering innovation, decision-making, diagnosis, research, systems thinking, and execution discipline. Transform AI from 'answering questions' to 'analyzing problems with structured methodology.'"
version: 1.0.0
author: Methodology Toolkit Contributors
license: MIT
metadata:
  hermes:
    tags: [methodology, thinking, decision-making, problem-solving, analysis]
    related_skills: [methodology-create, methodology-decide, methodology-diagnose, methodology-research, methodology-systems, execution-discipline]
---

# 🧠 Methodology Toolkit for AI Agents

> **52 thinking tools that transform AI from "answering questions" to "analyzing problems with structured methodology."**

## 🤔 What is this?

Most AI assistants just "give answers." But what's truly valuable isn't the answer—it's the **thinking process**. This toolkit encodes centuries of human thinking methodology into tools that AI can execute, making AI naturally apply these methods when answering questions.

## 🎯 Who is this for?

- **AI Agent developers** who want their agents to think more systematically
- **Knowledge workers** who want AI to help them analyze problems, not just answer them
- **Teams** looking to standardize how AI approaches complex decision-making
- **Anyone** who believes that "how you think" matters more than "what you know"

## 📦 What's included?

### 6 Categories, 52 Tools

| Category | Tools | Use Case |
|----------|-------|----------|
| **Create** | 12 | Brainstorming, solution design, breaking deadlocks |
| **Decide** | 15 | Making choices, weighing options, evaluating risks |
| **Diagnose** | 11 | Troubleshooting, analyzing causes, questioning arguments |
| **Research** | 1 | 5W1H structured analysis for external projects |
| **Systems** | 13 | Analyzing complex situations, understanding organizations |
| **Execute** | 9 | Execution discipline, task lifecycle, memory maintenance |

## 🚀 Quick Start

### Installation (Hermes Agent)

```bash
# Clone the repository
git clone https://github.com/your-username/methodology-toolkit.git

# Copy skills to your Hermes skills directory
cp -r methodology-toolkit/skills/methodology ~/.hermes/skills/

# Verify installation
hermes skills list | grep methodology
```

### Installation (Generic AI Agent)

1. Copy the `skills/methodology/` directory to your agent's skills location
2. Configure your agent to load skills from that directory
3. The toolkit will automatically activate when relevant triggers are detected

## 📚 Detailed Documentation

### Create Toolkit (12 tools)

**Purpose:** Brainstorming, solution design, breaking deadlocks.

**Key tools:**
- **Divergent-Convergent Thinking** — Generate possibilities first, then filter
- **Reverse Thinking** — Ask "how would this definitely fail?" then reverse
- **Counterfactual Thinking** — What if key conditions changed?
- **Problem Reframing** — Maybe the question itself is wrong
- **Constraint-Driven Thinking** — Acknowledge boundaries, find optimal within them
- **Falsifiability** — A claim that can't be disproven isn't scientific
- **Testability** — Can we design observations to test this?
- **Repeatability** — Does it hold under different conditions?
- **Evidence Hierarchy** — Not all evidence is equal
- **Underdetermination** — Same evidence can support multiple theories
- **Background Assumption Unpacking** — Separate data from assumptions
- **Prior-Posterior Distinction** — What did you believe before? How much did new evidence change it?

### Decide Toolkit (15 tools)

**Purpose:** Making choices, weighing options, evaluating risks.

**Key tools:**
- **Deductive/Inductive/Abductive/Causal/Analogical Reasoning** — Five reasoning types
- **Decision Theory** — Systematic choice-making framework
- **Expected Utility** — Probability × outcome, not just "most likely"
- **Cost-Benefit Analysis** — Systematic comparison of inputs/outputs
- **Opportunity Cost** — What do you give up by choosing this?
- **Build vs Reuse** — Before building, check: platform built-in? community solution?
- **Risk Stratification** — High-probability/low-loss vs low-probability/high-loss
- **Minimax Regret** — When uncertain, avoid the outcome you'd regret most
- **Bounded Rationality** — Perfect isn't possible; find "good enough"
- **Satisficing** — Not optimal, but executable now
- **Bayesian Updating** — Update beliefs with new evidence
- **Fallibilism** — Conclusions can be strong but remain revisable

### Diagnose Toolkit (11 tools)

**Purpose:** Troubleshooting, analyzing causes, questioning arguments.

**Key tools:**
- **Concept Clarification** — What exactly do you mean by X?
- **Socratic Questioning** — Continuous追问 definitions, premises, evidence
- **Necessary/Sufficient Conditions** — Is this required? Or just helpful?
- **Category Analysis** — Fact vs value vs causal judgment
- **Counterexample检验** — One strong counterexample can collapse a conclusion
- **Fallacy Recognition** — Straw man, false dichotomy, survivorship bias...
- **Cognitive Bias Correction** — Confirmation bias, anchoring, availability...
- **5 Whys** — Keep asking why until you reach root cause
- **Root Cause Analysis** — Formal method for engineering failures
- **Fault Tree/Causal Chain** — Map all possible paths to failure
- **Bottleneck Analysis** — Find the constraint that limits system output

### Research Toolkit (1 framework)

**Purpose:** 5W1H structured analysis for external projects.

**The framework:**

| Dimension | Question |
|-----------|----------|
| What | What does this project/tool do? One sentence core function |
| Who | Who made it? Author/org, Stars/Forks, activity level |
| Where | Where can we use it? Specific scenario analysis |
| When | When was it released? Update frequency? Maintenance status? |
| Why | Why is it worth using? What specific problem does it solve? |
| How | If worth using, how to install, integrate, design workflow? |

### Systems Toolkit (13 tools)

**Purpose:** Analyzing complex situations, understanding organizations and ecosystems.

**Key tools:**
- **Systems Thinking** — Don't just look at points; see structure, interdependencies
- **Feedback Loops** — Positive amplifies, negative stabilizes
- **Non-linear Thinking** — Small inputs can have disproportionate effects
- **Emergence** — Whole properties can't be predicted from parts
- **Self-Organization** — Systems can form stable patterns without central control
- **Level Analysis** — Individual, team, organization, institution
- **Path Dependence** — Why systems are locked into historical choices
- **Occam's Razor** — Prefer simpler explanations with fewer assumptions
- **Explanatory Power** — Which theory explains more, deeper, handles anomalies better?
- **Unification Principle** — One framework explaining multiple phenomena is powerful
- **Mechanistic Explanation** — Not just "correlated" but "how it works"
- **First Principles** — Break down to fundamental constraints, rebuild from there

### Execute Toolkit (9 modes)

**Purpose:** Execution discipline, task lifecycle management, memory maintenance.

**Key modes:**
- **Closure Discipline** — After creating anything, answer: who reads it? Where are the rules? Does parent reference it?
- **Task Lifecycle** — Before starting: check old tasks, progress, quotas, dependencies
- **Memory Maintenance** — Regular self-check: still accurate? Stored elsewhere? Long-term or temporary?
- **File Design Standards** — New MD files get methodology constraints in header comments
- **Progress Reporting** — Every 5 minutes during long operations, report status
- **Redundancy Cleanup** — Report only, don't delete. Confirm with boss first.
- **Cron Task Design** — Before creating: background, boundaries, side effects, failure modes
- **Reliability-First Degradation** — Prefer most reliable solution, not most feature-rich
- **Task-Level Business Constraints** — Each cron prompt starts with 3-5 iron laws

## 🔧 Integration Guide

### For Hermes Agent Developers

The toolkit follows Hermes Agent skill conventions:

```
skills/methodology/
├── methodology-toolkit/SKILL.md          # Main entry point
├── methodology-create/SKILL.md           # Create toolkit
├── methodology-decide/SKILL.md           # Decide toolkit
├── methodology-diagnose/SKILL.md         # Diagnose toolkit
├── methodology-research/SKILL.md         # Research toolkit
├── methodology-systems/SKILL.md          # Systems toolkit
└── execution-discipline/SKILL.md         # Execute toolkit
```

### For Other AI Agents

1. **Adapt the trigger system** — Map your agent's intent detection to the toolkit's trigger patterns
2. **Load on demand** — Only load relevant toolkits, not all 52 tools at once
3. **Integrate with your prompt system** — Add toolkit descriptions to your system prompt
4. **Customize for your domain** — The tools are general-purpose; add domain-specific examples

## 📖 Learning Resources

### Books
- **Thinking, Fast and Slow** (Daniel Kahneman) — Cognitive biases and decision-making
- **The Fifth Discipline** (Peter Senge) — Systems thinking
- **Superforecasting** (Philip Tetlock) — Bayesian reasoning and prediction
- **The Art of Thinking Clearly** (Rolf Dobelli) — Fallacies and biases

### Frameworks
- **MECE** (Mutually Exclusive, Collectively Exhaustive) — Structured problem decomposition
- **Pyramid Principle** — Conclusion-first communication
- **Issue Trees** — Breaking complex problems into manageable pieces

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hermes Agent** — The AI agent framework that inspired this toolkit
- **Daniel Kahneman** — For his groundbreaking work on cognitive biases
- **Peter Senge** — For systems thinking methodology
- **Philip Tetlock** — For Bayesian reasoning and forecasting
- **The AI Agent Community** — For continuous feedback and improvement

---

**Made with ❤️ by the AI Agent Community**

*"The goal is not to make AI smarter, but to make AI think better."*
