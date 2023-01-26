ENV:=aiployer-cli-dev

build:
env: ## Make a dev environment
	conda create -y -n $(ENV) -c conda-forge --file requirements.txt
	conda activate $(ENV) && \
		pip install -e .

activate:
	@echo "conda activate $(ENV)"
