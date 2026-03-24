---
name: animal_battle_simulator
description: Writes animal battle descriptions. Use when determining which animal would
hypothetically win a battle.
allowed-tools: Read, Grep, Bash, Writes
model: sonnet
---

When providing an animal battle simulation:

1. If the user has not provided at least two animals ask a follow up about which
animals the user is referring to

2. Create a file in the `./assets/animal_battles/` directory with the 
animal_names_timestamp.md and output the simulation text there

3. If asked for a swarm/flock/multi animal battle without specific numbers given
execute the `./scripts/random_number.sh` using Bash to get a number to use in your
simulation

4. Before writing the simulation, use the Read tool to read `./assets/output_format.md` and follow its format exactly when writing the simulation