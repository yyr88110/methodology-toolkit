# 📚 Example Usage

This document provides practical examples of how to use the Methodology Toolkit in real-world scenarios.

## 🎯 Example 1: Decision Making

**Scenario:** User asks "Should we build this feature ourselves or use an existing library?"

**AI Response using Methodology Toolkit:**

```
Let me apply **Build vs Reuse** (Decide toolkit) and **Cost-Benefit Analysis** (Decide toolkit):

## Build vs Reuse Analysis

**Step 1: Check platform built-in capabilities**
- Does our framework already provide this? → [Check documentation]
- Is there a built-in module we can use? → [Search platform docs]

**Step 2: Check community solutions**
- Search GitHub for existing libraries → [Search results]
- Check popularity, maintenance status, compatibility
- Evaluate: Stars, recent commits, issue response time

**Step 3: Only if both are insufficient, consider building**
- Development time: X days
- Maintenance burden: Ongoing
- Opportunity cost: What else could we build with that time?

## Cost-Benefit Analysis

| Factor | Build | Reuse |
|--------|-------|-------|
| Initial cost | High (development time) | Low (integration time) |
| Maintenance | Ongoing (your team) | Community-driven |
| Customization | Full control | Limited by API |
| Risk | Bugs, delays | Dependency risk |
| Learning curve | High | Low |

**Conclusion:** [Specific recommendation based on analysis]
```

## 🔍 Example 2: Problem Diagnosis

**Scenario:** User asks "Why is our system running slowly?"

**AI Response using Methodology Toolkit:**

```
Let me apply **Bottleneck Analysis** (Diagnose toolkit) and **5 Whys** (Diagnose toolkit):

## Bottleneck Analysis

**Step 1: Identify the constraint**
- CPU usage: X% → [Is this the bottleneck?]
- Memory usage: Y% → [Is this the bottleneck?]
- Disk I/O: Z MB/s → [Is this the bottleneck?]
- Network: W Mbps → [Is this the bottleneck?]

**Step 2: Focus on the bottleneck**
The real constraint is: [Identified bottleneck]

## 5 Whys Analysis

1. **Why is the system slow?** → Database queries are slow
2. **Why are queries slow?** → Missing indexes on frequently queried columns
3. **Why are indexes missing?** → Schema was designed without considering query patterns
4. **Why wasn't this considered?** → No performance requirements were documented
5. **Why no requirements?** → We skipped the performance analysis phase

**Root Cause:** Missing performance requirements in the design phase

**Solution:** 
1. Add indexes for current performance issue (immediate)
2. Document performance requirements for future features (preventive)
```

## 🧠 Example 3: Creative Problem Solving

**Scenario:** User asks "How can we increase user engagement?"

**AI Response using Methodology Toolkit:**

```
Let me apply **Divergent-Convergent Thinking** (Create toolkit) and **Reverse Thinking** (Create toolkit):

## Phase 1: Divergent Thinking (Generate possibilities)

**No limits, all ideas welcome:**
1. Gamification (points, badges, leaderboards)
2. Personalization (AI-driven recommendations)
3. Social features (sharing, collaboration)
4. Notifications (push, email, in-app)
5. Content freshness (daily updates, new features)
6. Community building (forums, events)
7. Rewards (discounts, exclusive access)
8. Education (tutorials, webinars)
9. Feedback loops (surveys, user input)
10. Partnership (integrations, cross-promotion)

## Phase 2: Convergent Thinking (Filter and prioritize)

**Evaluation criteria:**
- Impact: High/Medium/Low
- Effort: High/Medium/Low
- Timeline: Immediate/Short-term/Long-term

**Prioritized ideas:**
1. **Quick wins** (High impact, Low effort): [Specific idea]
2. **Strategic investments** (High impact, High effort): [Specific idea]
3. **Fill-ins** (Low impact, Low effort): [Specific idea]
4. **Avoid** (Low impact, High effort): [Specific idea]

## Phase 3: Reverse Thinking (What would definitely fail?)

**How to guarantee user engagement drops:**
1. Ignore user feedback completely
2. Make the interface confusing
3. Never update content
4. Send spam notifications
5. Make it hard to find value

**Action:** Avoid these anti-patterns in our solution.
```

## 🔬 Example 4: Research Analysis

**Scenario:** User asks "Should we adopt this new JavaScript framework?"

**AI Response using Methodology Toolkit:**

```
Let me apply **5W1H Framework** (Research toolkit):

## 5W1H Analysis

### What
[Framework Name] is a [brief description] framework for [specific use case].

### Who
- **Author:** [Organization/Individual]
- **Stars:** [Number] (as of [date])
- **Forks:** [Number]
- **Contributors:** [Number]
- **Last commit:** [Date] (X days ago)
- **License:** [Type]

### Where
**Our specific use case:**
- We need: [Our requirements]
- This framework provides: [Matching features]
- Gap analysis: [What's missing]

### When
- **Initial release:** [Date]
- **Latest version:** [Version] (released [Date])
- **Release frequency:** [X releases per month]
- **Roadmap:** [Public roadmap? Next features?]

### Why
**Value proposition:**
- Solves: [Specific problem we have]
- Better than: [Current solution] because [reasons]
- Trade-offs: [What we give up]

### How
**Implementation plan:**
```bash
# Installation
npm install [package]

# Integration steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

# Migration from current solution
- [Migration step 1]
- [Migration step 2]
```

## Conclusion

**Recommendation:** [Adopt / Wait / Don't adopt]

**Reasoning:**
- [Key factor 1]
- [Key factor 2]
- [Key factor 3]

**Trigger for re-evaluation:** [When should we reconsider?]
```

## 🏗️ Example 5: Systems Thinking

**Scenario:** User asks "Why is our team not shipping features fast enough?"

**AI Response using Methodology Toolkit:**

```
Let me apply **Systems Thinking** (Systems toolkit) and **Feedback Loops** (Systems toolkit):

## Systems Thinking Analysis

**Don't just look at points—see the structure:**

### Current System Structure
```
Product → Design → Development → Testing → Deployment
    ↓         ↓          ↓           ↓          ↓
 Feedback   Feedback   Feedback   Feedback   Feedback
```

### Interdependencies
- **Product → Design:** Requirements clarity affects design quality
- **Design → Development:** Design completeness affects development speed
- **Development → Testing:** Code quality affects testing time
- **Testing → Deployment:** Test coverage affects deployment confidence

## Feedback Loop Analysis

### Positive Feedback Loops (Amplifying)
1. **Technical debt accumulation:**
   - Quick fixes → More technical debt → Slower development → More quick fixes
   - **Result:** Speed decreases over time

2. **Knowledge silos:**
   - One person knows critical systems → Others can't help → More load on that person → More silos
   - **Result:** Bottlenecks increase

### Negative Feedback Loops (Stabilizing)
1. **Sprint retrospectives:**
   - Problems identified → Solutions implemented → Problems reduced → Less identification needed
   - **Result:** Continuous improvement

2. **Code reviews:**
   - Quality issues found → Fixes applied → Quality improves → Fewer issues found
   - **Result:** Quality stabilizes

## Root Causes (Not Just Symptoms)

**Layer 1: Symptoms**
- Features take too long
- Bugs in production
- Team burnout

**Layer 2: Process Issues**
- Unclear requirements
- Insufficient testing
- Poor communication

**Layer 3: Systemic Issues**
- No performance metrics
- No feedback loops
- No learning culture

**Layer 4: Cultural Issues**
- Fear of failure
- Blame culture
- Short-term thinking

## Recommendations

**Immediate (This sprint):**
1. [Action 1]
2. [Action 2]

**Short-term (Next month):**
1. [Action 1]
2. [Action 2]

**Long-term (Next quarter):**
1. [Action 1]
2. [Action 2]
```

## 🎓 Example 6: Execution Discipline

**Scenario:** User asks "I just created a new configuration file. What should I do?"

**AI Response using Methodology Toolkit:**

```
Let me apply **Closure Discipline** (Execute toolkit):

## Three-Question Self-Check

After creating any artifact, answer these three questions:

### 1. Who will read it, and under what circumstances?
- **Primary reader:** [Who]
- **Trigger:** [When will they read it?]
- **Purpose:** [Why will they read it?]

### 2. Where are the calling rules written?
- **Rule location:** [File path]
- **Rule content:** [What does the rule say?]
- **Example:** "Before [action], read [this file]"

### 3. Does the parent document have a back-reference?
- **Parent document:** [File path]
- **Reference:** [What does it say about this file?]
- **Status:** ✅ Present / ❌ Missing

## Action Items

If any answer is missing, complete these actions:

1. **Write calling rules:**
   ```
   File: [parent document]
   Content: "Before [action], read [this file]"
   ```

2. **Add back-reference:**
   ```
   File: [this file]
   Content: "Calling rules in [parent document] [section]"
   ```

3. **Verify:**
   - [ ] Can a new team member find this file?
   - [ ] Do they know when to read it?
   - [ ] Can they trace the rules?

## Example

**Scenario:** Created `config/database.yaml`

**Answers:**
1. **Who:** Developers setting up the project
   **When:** First time setting up the project
   **Why:** To configure database connection

2. **Rule location:** `README.md` → "Setup" section
   **Rule content:** "Copy `config/database.yaml.example` to `config/database.yaml` and update credentials"

3. **Parent reference:** `README.md` mentions this file ✅

**Result:** File is properly integrated into the system.
```

## 💡 Tips for Using These Examples

1. **Adapt to your context** — These are templates; customize for your specific situation
2. **Combine tools** — Real problems often need multiple tools
3. **Be practical** — Focus on actionable insights, not theoretical perfection
4. **Iterate** — First attempt may not be perfect; refine based on feedback
5. **Document** — Save successful applications for future reference

---

**Remember:** The goal is not to use all tools, but to use the right tools for the problem.
