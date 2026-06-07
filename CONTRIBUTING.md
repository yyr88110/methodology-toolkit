# Contributing to Methodology Toolkit

Thank you for your interest in contributing to the Methodology Toolkit! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:
1. Check existing issues to avoid duplicates
2. Use the issue template provided
3. Include clear reproduction steps
4. Specify your environment (OS, AI agent version, etc.)

### Suggesting Enhancements

We welcome suggestions for:
- New thinking tools
- Improved explanations
- Better examples
- Domain-specific extensions
- Translation improvements

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-tool`)
3. Commit your changes (`git commit -m 'Add amazing thinking tool'`)
4. Push to the branch (`git push origin feature/amazing-tool`)
5. Open a Pull Request

## 📝 Content Guidelines

### Adding a New Thinking Tool

Each tool should follow this structure:

```markdown
### Tool Name

**Purpose:** One sentence describing what this tool does.

**When to use:**
- Trigger scenario 1
- Trigger scenario 2
- Trigger scenario 3

**How to use:**
Step-by-step instructions or explanation.

**Example:**
```markdown
User: "Should we use Tool A or Tool B?"
AI: "Let me apply **Cost-Benefit Analysis** (Decide toolkit)..."
```

**Common pitfalls:**
- Pitfall 1: Description and how to avoid
- Pitfall 2: Description and how to avoid
```

### Writing Style

- **Be concise** — Every word should add value
- **Use examples** — Show, don't just tell
- **Be practical** — Focus on actionable advice
- **Avoid jargon** — Explain technical terms when first used
- **Use active voice** — "Apply this tool" not "This tool should be applied"

### Quality Standards

- **Accuracy** — Verify all facts and claims
- **Clarity** — Can a new user understand this?
- **Completeness** — Are there any gaps in the explanation?
- **Consistency** — Does it match the existing style?

## 🔧 Technical Guidelines

### File Structure

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

### SKILL.md Format

Each SKILL.md should follow Hermes Agent conventions:

```yaml
---
name: methodology-toolkit
description: "52 thinking tools for AI agents..."
version: 1.0.0
author: Your Name
license: MIT
metadata:
  hermes:
    tags: [methodology, thinking, decision-making]
    related_skills: [methodology-create, methodology-decide]
---
```

### Validation

Before submitting, validate your SKILL.md:

```python
import yaml, re, pathlib

content = pathlib.Path("skills/methodology/<toolkit>/SKILL.md").read_text()
assert content.startswith("---"), "Must start with ---"
m = re.search(r'\n---\s*\n', content[3:])
fm = yaml.safe_load(content[3:m.start()+3])
assert "name" in fm, "Missing name field"
assert "description" in fm, "Missing description field"
assert len(fm["description"]) <= 1024, "Description too long"
assert len(content) <= 100_000, "File too large"
print("✅ Validation passed")
```

## 🧪 Testing

### Local Testing

1. Copy your changes to your Hermes Agent skills directory
2. Restart your agent or reload skills
3. Test with relevant triggers
4. Verify the tool activates correctly

### Integration Testing

Test your tool with:
- Simple questions (should not trigger)
- Complex questions (should trigger)
- Edge cases (ambiguous triggers)
- Multi-tool scenarios (tool combinations)

## 📚 Documentation Standards

### README Updates

When adding new tools:
1. Update the "What's included" section
2. Add the tool to the appropriate category table
3. Update the "Quick Start" section if needed
4. Add usage examples

### Code Examples

Use consistent formatting:

```markdown
**User:** "Should we build this ourselves or use an existing solution?"

**AI:** "Let me apply **Build vs Reuse** (Decide toolkit):

1. First, check what the platform already provides...
2. Then, check community solutions...
3. Only if both are insufficient, consider building..."
```

## 🎯 Contribution Ideas

### High Priority
- More domain-specific examples
- Better integration guides for other AI agents
- Translation to other languages
- Performance optimizations

### Medium Priority
- Additional thinking tools
- Improved documentation
- Better error messages
- More comprehensive examples

### Low Priority
- Cosmetic improvements
- Minor typo fixes
- Formatting adjustments

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments
- Release notes
- Contributor hall of fame
- Social media shoutouts

## 📞 Getting Help

- **Issues** — For bugs and feature requests
- **Discussions** — For questions and general discussion
- **Email** — For private inquiries

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make AI think better! 🧠**
