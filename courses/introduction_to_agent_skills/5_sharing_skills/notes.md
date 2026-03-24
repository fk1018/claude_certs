# Sharing skills

`https://anthropic.skilljar.com/introduction-to-agent-skills/434529`

## Key Takeaways

- *Project skills* in `./claude/skills` can be shared if they are checked into git
- *Plugins* let you distribute skills across repositories via marketplaces for broader
community use
- *Enterprise managed settings* deploy skills organization-wide with the highest
priority, ideal for mandatory standards and compliance
- *Subagents don't automatically see your skills,* you must explicitly list skills in a
custom agent's frontmatter `skills` field
- Built-in agents (Explorer, Plan, Verify) *can't access skills at all,* only custom
subagents defined in `./claude/agents` can

## No updates