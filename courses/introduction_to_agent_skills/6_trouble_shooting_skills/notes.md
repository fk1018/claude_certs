# Troubleshooting skills

`https://anthropic.skilljar.com/introduction-to-agent-skills/434530`

## Key Takeaways

- Start with the *skills validator tool,* it catches structural problems before you
spend time debugging other things
- If a skill *doesn't trigger,* the cuase is almost always the description, add trigger
phrases that match how you actually phrase requests
- If a skill *doesn't load,* check the `SKILL.md` is inside a named directory(not at 
the skills root) and the file name is exactly `SKILL.md`
- If the *wrong skill gets used,* your descriptions are too similar, make them more 
distinct
- For *runtime errors,* check dependencies, file permissions(`chmod +x`), and path
seperators (use forward slashes everywhere)

## Notes
- A good place to start triaging a skill is using the `uv` command. Install based on os