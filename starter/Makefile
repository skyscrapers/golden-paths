.PHONY: requirements

PIP_TOOLS_VERSION = 7.7.0
PYTHON_313 ?= python3.13

# Regenerate the pins in app/requirements.txt from app/requirements.in (needs Python 3.13)
requirements:
	tmp=$$(mktemp -d) \
	&& $(PYTHON_313) -m venv $$tmp \
	&& $$tmp/bin/pip install -q pip-tools==$(PIP_TOOLS_VERSION) \
	&& cd app \
	&& CUSTOM_COMPILE_COMMAND="make requirements" $$tmp/bin/pip-compile -q --strip-extras requirements.in \
	; status=$$?; rm -rf $$tmp; exit $$status
