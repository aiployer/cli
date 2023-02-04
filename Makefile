ENV:=aiployer-cli-dev

build:
env: ## Make a dev environment
	conda create -y -n $(ENV) -c conda-forge --file requirements.txt
	conda activate $(ENV) && \
		pip install -e .


update-env: ## update env, usually for dependencies
	conda install -y -n $(ENV) -c conda-forge --file requirements.txt

activate:
	@echo "conda activate $(ENV)"
