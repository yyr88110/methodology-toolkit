#!/usr/bin/env python3
"""
Validate all SKILL.md files in the methodology toolkit.

Checks:
1. Frontmatter starts with --- and closes with ---
2. Required fields present (name, description)
3. Description length <= 1024 chars
4. Total file size <= 100,000 chars
5. Body content exists after frontmatter
"""

import sys
import re
import yaml
from pathlib import Path

# Constants
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_CONTENT_CHARS = 100_000
REQUIRED_FIELDS = ["name", "description"]

def validate_skill_file(filepath: Path) -> list[str]:
    """Validate a single SKILL.md file. Returns list of errors."""
    errors = []
    
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Failed to read file: {e}"]
    
    # Check file size
    if len(content) > MAX_SKILL_CONTENT_CHARS:
        errors.append(f"File too large: {len(content)} chars (max {MAX_SKILL_CONTENT_CHARS})")
    
    # Check starts with ---
    if not content.startswith("---"):
        errors.append("File must start with '---'")
        return errors  # Can't parse frontmatter if it doesn't start correctly
    
    # Find closing ---
    match = re.search(r'\n---\s*\n', content[3:])
    if not match:
        errors.append("Missing closing '---' for frontmatter")
        return errors
    
    # Parse frontmatter
    try:
        frontmatter_text = content[3:match.start() + 3]
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML frontmatter: {e}")
        return errors
    
    if not isinstance(frontmatter, dict):
        errors.append("Frontmatter must be a YAML mapping")
        return errors
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    # Check description length
    description = frontmatter.get("description", "")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"Description too long: {len(description)} chars (max {MAX_DESCRIPTION_LENGTH})")
    
    # Check body exists
    body = content[match.end():]
    if not body.strip():
        errors.append("Empty body after frontmatter")
    
    return errors

def main():
    """Validate all SKILL.md files."""
    # Find skills directory
    skills_dir = Path("skills/methodology")
    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return 1
    
    # Find all SKILL.md files
    skill_files = list(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        print(f"❌ No SKILL.md files found in {skills_dir}")
        return 1
    
    print(f"🔍 Found {len(skill_files)} SKILL.md files to validate\n")
    
    all_passed = True
    results = []
    
    for skill_file in sorted(skill_files):
        skill_name = skill_file.parent.name
        errors = validate_skill_file(skill_file)
        
        if errors:
            all_passed = False
            results.append((skill_name, "❌", errors))
        else:
            results.append((skill_name, "✅", []))
    
    # Print results
    for name, status, errors in results:
        print(f"{status} {name}")
        if errors:
            for error in errors:
                print(f"   - {error}")
    
    print()
    
    if all_passed:
        print("✅ All SKILL.md files passed validation!")
        return 0
    else:
        print("❌ Some SKILL.md files failed validation")
        return 1

if __name__ == "__main__":
    sys.exit(main())
