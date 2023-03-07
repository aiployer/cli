import nbformat
import re
from fastapi import FastAPI, Header
import subprocess
import sys

def find_cells_with_decorator(nb, decorator):
    cells = []
    for cell in nb.cells:
        if cell.cell_type == 'code':
            lines = cell.source.splitlines()
            for line in lines:
                if line.startswith('@' + decorator):
                    cells.append(cell)
                    break
    return cells

def extract_function_from_cell(cell):
    source = cell.source
    # Find the start and end of the function
    start = source.find('def ')
    end = source.rfind('return')
    function_source = source[start:end]
    return function_source

def parse_function_source(function_source):
    function_name = re.search(r'def (\w+)\(', function_source).group(1)
    # Extract the function parameters
    parameters = re.findall(r'(\w+):', function_source)
    return function_name, parameters

def generate_openapi_specification(function_name, parameters):
    app = FastAPI()

    @app.get(f"/{function_name}")
    async def function_handler(*args, **kwargs):
        pass

    for parameter in parameters:
        app.dependency_functions[function_handler].append(Header(parameter))

    openapi_spec = app.openapi()
    return openapi_spec

def run_jkg(notebook_filepath):
    command = ['jupyter', 'kernelgateway', "--ip='0.0.0.0'", "--KernelGatewayApp.api='kernel_gateway.notebook_http'", "--KernelGatewayApp.seed_uri='{}'".format(notebook_filepath)]

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip())

def main(notebook_filepath):
    run_jkg(notebook_filepath)

if __name__ == '__main__':
    main('test.ipynb')
