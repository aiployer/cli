ENV:=aiployer-cli-dev

build:
env: ## Make a dev environment
	conda create -y -n $(ENV) -c conda-forge --file requirements.txt
	conda activate $(ENV) && \
		pip install -e .
	conda install -c conda-forge jupyter_kernel_gateway


update-env: ## update env, usually for dependencies
	conda install -c conda-forge -y -n $(ENV) --file requirements.txt
	conda install -c conda-forge jupyter_kernel_gateway

activate:
	@echo "conda activate $(ENV)"
