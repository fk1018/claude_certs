# Configuration and multi-file skills

`https://anthropic.skilljar.com/introduction-to-agent-skills/434526`

## Key takeaways
- `name` and `description` *are required*, `allowed-tools` and `model` are optional but
powerful additionals
- A good desription *answers two questions:* What does the skills do? When should
Claude use it?
- `allowed-tools` restricts which tools Claude can use when the skill is active, useful
for read-only or security-sensitive workflows
- *Progressive disclosure:* keep SKILL.md under 500 lines and link to supporting files
(references, scripts, assets) that Claude reads only when needed
- *Scripts execute without loading their contents into context,* only the output
consumes tokens, keeping context efficient

## We updated our animal_battle_simulator skill
- We added assets, references, and scripts directories documented here
`https://agentskills.io/specification`
- 