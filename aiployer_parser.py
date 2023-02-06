import nbformat
import re
from fastapi import FastAPI, Header

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

def main(notebook_filepath):
    with open(notebook_filepath) as f:
        nb = nbformat.read(f, as_version=4)

    cells_with_aiployer_decorator = find_cells_with_decorator(nb, 'aiployer')
    map_aiployer_function_to_openapi_spec = {}
    for cell in cells_with_aiployer_decorator:
        function_source = extract_function_from_cell(cell)
        function_name, parameters = parse_function_source(function_source)
        map_aiployer_function_to_openapi_spec[function_name] =  openapi_spec = generate_openapi_specification(function_name, parameters)

    return map_aiployer_function_to_openapi_spec
