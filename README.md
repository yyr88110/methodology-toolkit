# 🧠 Methodology Toolkit for AI Agents

> **52 thinking tools that transform AI from "answering questions" to "analyzing problems with structured methodology."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hermes Agent](https://img.shields.io/badge/Hermes-Agent-blue.svg)](https://github.com/hermes-agent/hermes-agent)

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

### Quick Example

**User asks:** "Should we use Tool A or Tool B?"

**Without methodology toolkit:** AI gives a generic comparison.

**With methodology toolkit:** AI naturally applies:
- **Cost-benefit analysis** (Decide) — systematic comparison of inputs/outputs
- **Opportunity cost** (Decide) — what do we give up by choosing each?
- **Risk stratification** (Decide) — high-probability/low-loss vs low-probability/high-loss
- **First principles** (Systems) — what are the fundamental constraints?

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

### Usage

Once installed, the toolkit activates automatically when you ask questions that match the trigger patterns:

| You say | Toolkit activates |
|---------|-------------------|
| "Help me analyze this problem" | Diagnose toolkit |
| "Which option should I choose?" | Decide toolkit |
| "What are some new approaches?" | Create toolkit |
| "Is this project worth using?" | Research 5W1H |
| "Why is this system designed this way?" | Systems toolkit |
| "How should I start this task?" | Execute toolkit |

## 📚 Detailed Documentation

### Create Toolkit (12 tools)

**Purpose:** Brainstorming, solution design, breaking deadlocks.

**Key tools:**
- **Divergent-Convergent Thinking** — Generate possibilities first, then filter
- **Reverse Thinking** — Ask "how would this definitely fail?" then reverse
- **Counterfactual Thinking** — What if key conditions changed?
- **Problem Reframing** — Maybe the question itself is wrong
- **Constraint-Driven Thinking** — Acknowledge boundaries, find optimal within them

**When to use:**
- "I need new ideas"
- "We're stuck"
- "How can we approach this differently?"

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

**When to use:**
- "Which option is better?"
- "What are the risks?"
- "How do I evaluate this trade-off?"

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

**When to use:**
- "What went wrong?"
- "Is this argument valid?"
- "Why is this happening?"

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

**When to use:**
- "Analyze this GitHub project"
- "Is this tool worth adopting?"
- "Help me evaluate this library"

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

**When to use:**
- "Analyze this complex system"
- "Why is the organization structured this way?"
- "What are the underlying dynamics?"

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

**When to use:**
- "How should I start this task?"
- "I created a new file/script"
- "I need to clean up the system"

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

### Customization

Each toolkit can be extended with:
- **Domain-specific examples** — Add your industry's common scenarios
- **Custom tools** — Add new thinking tools following the existing format
- **Integration hooks** — Connect tools to your agent's memory/knowledge systems

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

### Online Courses
- **Coursera: Model Thinking** — Multi-model approach to complex problems
- **edX: Critical Thinking** — Logic and argument analysis
- **MIT OpenCourseWare: Systems Thinking** — Complex system dynamics

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- **Add new thinking tools** — Follow the existing format
- **Improve existing tools** — Better examples, clearer explanations
- **Add domain-specific extensions** — Industry-specific applications
- **Fix bugs** — Typos, broken links, unclear instructions
- **Translate** — Make the toolkit accessible in other languages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hermes Agent** — The AI agent framework that inspired this toolkit
- **Daniel Kahneman** — For his groundbreaking work on cognitive biases
- **Peter Senge** — For systems thinking methodology
- **Philip Tetlock** — For Bayesian reasoning and forecasting
- **The AI Agent Community** — For continuous feedback and improvement

## 📞 Support

- **Issues** — [GitHub Issues](https://github.com/your-username/methodology-toolkit/issues)
- **Discussions** — [GitHub Discussions](https://github.com/your-username/methodology-toolkit/discussions)
- **Email** — your.email@example.com

---

**Made with ❤️ by the AI Agent Community**

*"The goal is not to make AI smarter, but to make AI think better."*
