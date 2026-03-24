# Requirements
	- python 3.14.3

# Setup
1. create venv
	```bash
	python -m venv .venv
	```
2. use .venv
	```bash
	source .venv/bin/activate
	```
3. install dependencies
	```bash
	pip install anthropic python-dotenv black
	```
4. setup env file and put your info in there
	```bash
	cp .env.example .env
	```
5. Run the apps from the root of building_with_the_claude_api ex:
	```bash
	python 3_making_a_request/main.py
	```
	```bash
	python 5_chat_exercise/main.py
	```
	```bash
	python 7_system_prompts_exercise/main.py
	```
	```bash
	python 9_response_streaming/main.py
	```
6. Format your code
	```bash 
	black .
	```
