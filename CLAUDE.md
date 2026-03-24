# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a learning repository for the Anthropic "Introduction to Agent Skills" certification course. It contains course notes and a working example skill.

## Structure

- `courses/` — Course notes organized by course and lesson:
  - `introduction_to_agent_skills/` — (in progress)
  - `building_with_the_claude_api/`
  - `claude_code_in_action/`
  - `introduction_to_model_context_protocol/`
- `animal_battles/` — Example project for skill exercises
- `.claude/animal_battle/SKILL.md` — A project skill that handles animal battle descriptions

## Skills

Project skills live in `.claude/<skill-name>/SKILL.md` with a `name` and `description` in the frontmatter. Claude matches skills to user requests by comparing the request against skill descriptions.
