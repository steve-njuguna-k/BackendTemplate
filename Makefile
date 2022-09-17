## Variables used in target commands
SHELL := /bin/bash
ENV ?= Local
SETTINGS ?= $(shell echo $(ENV) | tr '[:upper:]' '[:lower:]')

## Variables to make targets more readable
COMMAND = docker exec -it django-app bash -c
NON_INTERACTIVE_COMMAND = docker exec -i django-app bash -c
MANAGE = python manage.py
DOCKER_ENV_FILE = --env-file ./Docker/${ENV}/docker.env
DOCKER_COMPOSE_FILE = -f ./Docker/${ENV}/docker-compose.yml
DOCKER_FILE = docker-compose ${DOCKER_COMPOSE_FILE} ${DOCKER_ENV_FILE}
SETTINGS_FLAG = --settings=Project.settings.django.${SETTINGS}_settings

## Modules settings
TOML_PATH = ./Project/settings/pyproject.toml
BLACK_SETTINGS = --config="${TOML_PATH}"
ISORT_SETTINGS = --settings-path="${TOML_PATH}"

## Testing settings
DJANGO_TEST_SETTINGS = --ds=Project.settings.django.test_settings
PYTEST_FLAGS = --reuse-db -p no:cacheprovider -p no:warnings
PYTEST_SETTINGS = ${PYTEST_FLAGS} ${DJANGO_TEST_SETTINGS}
COVERAGE_SETTINGS = --cov --cov-config=.coveragerc
HTML_PATH = --cov-report=html:./Project/.htmlconv
HTML_COVERAGE_SETTINGS = ${COVERAGE_SETTINGS} ${HTML_PATH}

## Style to print targets in a nice format
STYLE = {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}


.PHONY: help
help:	## Show this help which show all the possible make targets and its description.
	@echo ""
	@echo "The following are the make targets you can use in this way 'make <target>': "
	@echo ""
	@awk ' BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / ${STYLE}' $(MAKEFILE_LIST)
	@echo ""
	@echo "You can change the environment with the ENV parameter in every target."
	@echo "* You can modify the settings with SETTINGS parameter."
	@echo "** You can grep a string with GREP parameter."
	@echo "*** You can modify the number of instances created with INSTANCES parameter."
	@echo "**** You can modify the path that will be tested with PATH parameter."
	@echo ""

ifeq (docker,$(firstword $(MAKECMDGOALS)))
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(ARGS):;@:)
endif
.PHONY: docker
docker: ## Runs docker compose command. You can pass it paramaters as normal. Eg: 'make docker ps'.
	@${DOCKER_FILE} $(ARGS)

.PHONY: bash
bash: ## Open a bash shell in the django container.
	@${DOCKER_FILE} exec app /bin/bash

.PHONY: shell
shell: ## Open the shell_plus of django. *
	${COMMAND} "${MANAGE} shell_plus ${SETTINGS_FLAG}"

.PHONY: show_urls
show_urls: ## Show the urls of the app. **
ifeq (${GREP},)
	@${COMMAND} "${MANAGE} show_urls"
else
	@${COMMAND} "${MANAGE} show_urls | grep ${GREP}"
endif

.PHONY: create-test-db
create-test-db: ## Create a test database.
	@${COMMAND} "${MANAGE} create_test_db"

.PHONY: flush
flush: ## Flush the database. *
	@${COMMAND} "${MANAGE} flush ${SETTINGS_FLAG}"

.PHONY: migrations
migrations: ## Creates and applies the django migrations. *
	@${COMMAND} "${MANAGE} makemigrations ${SETTINGS_FLAG}"
	@${COMMAND} "${MANAGE} migrate ${SETTINGS_FLAG}"

.PHONY: populate
populate: ## Populates the database with dummy data. ***
ifeq (${INSTANCES},)
	@${COMMAND} "${MANAGE} populate_db -i 50 ${SETTINGS_FLAG}"
else
	@${COMMAND} "${MANAGE} populate_db -i $(INSTANCES) ${SETTINGS_FLAG}"
endif

.PHONY: recreate
recreate: ## Recreate the the database with dummy data. *
	@make flush
	@make migrations
	@make populate
ifeq (${SETTINGS}, test)
	@create-test-db
endif

.PHONY: test
test: ## Run the tests. ****
	@make create-test-db
ifeq (${PATH},)
	@${COMMAND} "pytest . ${PYTEST_SETTINGS}"
else
	@${COMMAND} "pytest ${PATH} -s ${PYTEST_SETTINGS}"
endif

.PHONY: test-coverage
test-coverage: ## Run the tests with coverage.
ifeq (${ENV}, Ci)
	@${NON_INTERACTIVE_COMMAND} "${MANAGE} create_test_db"
	@${COMMAND} "pytest . ${PYTEST_SETTINGS} ${COVERAGE_SETTINGS}"
else
	@make create-test-db
	@${COMMAND} "pytest . ${PYTEST_SETTINGS} ${COVERAGE_SETTINGS}"
endif

.PHONY: test-coverage-html
test-coverage-html: ## Run the tests with coverage and html report.
	@make create-test-db
	@${COMMAND} "pytest . ${PYTEST_SETTINGS} ${HTML_COVERAGE_SETTINGS}"

.PHONY: fast-test
fast-test: ## Run the tests in parallel. ****
	@${COMMAND} "pytest ${PATH} ${PYTEST_SETTINGS} -n auto"

.PHONY: lint
lint: ## Run the linter
	@${COMMAND} "black . ${BLACK_SETTINGS}"

.PHONY: check-lint
check-lint: ## Check for linting errors.
	@${COMMAND} "black . ${BLACK_SETTINGS} --check"

.PHONY: sort-imports
sort-imports: ## Sort the imports
	@${COMMAND} "isort . ${ISORT_SETTINGS}"

.PHONY: check-imports
check-imports: ## Check for errors on imports ordering.
	@${COMMAND} "isort . ${ISORT_SETTINGS} --check"

.PHONY: format
format: ## Runs the linter and import sorter at once
	@make lint
	@make sort-imports
