# What are skills

`https://anthropic.skilljar.com/introduction-to-agent-skills/434525`

## Key takeaways

- *Skills are folders of instructions* that Claude Code can discover and use to  handle
tasks more accurately. Each skills lives in a `SKILL.md` file with a name and
description in its frontmatter
- *Claude uses the dscription to match skills to requests.* When you ask Claude to do
something it compares your request against available skill descriptions and activates
the ones that match
- *Personal skills* go in `~/.claude/skills` and follow you across all projects.
*Project skills* go in `~/.claude/skills` inside a repository and follow you across all
projects.
- If you find yourself *explaining the same thing to claude repeatedly,* that's a skill
waiting to be written

### Some good skills to use when you are repeating yourself
- PR review format
- Commit message format