# Creating your first skill

`https://anthropic.skilljar.com/introduction-to-agent-skills/434527`

## Key takeaways

- A skill is a *directory containing a* `Skill.md` file with metadata(name,description)
in front matter and instructions below.
- Claude loads *only skill names and descriptions at startup,* then matches incoming
requests against those descriptions using the semantic matching
- You get a *confirmation prompt before Claude loads the full skill content into
context
- Priority for name conflicts`: Enterprise > Personal > Project > Plugins`
- To update a skill, edit its `SKILL.md`. To remove one, delete its directory. *Always
restart Claude Code* for changes to take effect

# We created a skill 
- its located in .claude/skills/animal_battle/SKILL.md
- `A parrot with sonar is an apex predator of the skies.`