## the following is meant to solve the problem for when students add or delete a cell between questions.
## trying to solve problem for get_source_code when cell_idx is changed. 
## NOTE: this does not work

def test_for_none_cell_idx(desired_content, notebook_name, cell_idx, variable_name=None):
    try:
        cell_numbers = [int(idx) for idx in cell_idx.split(",")]

        for cell_number in cell_numbers:
            # Read the notebook content
            with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
                nb = nbformat.read(f, nbformat.NO_CONVERT)

            # Check if the cell number is valid
            if cell_number < 0 or cell_number >= len(nb["cells"]):
                raise Exception(f"Cell {cell_number} does not exist in the notebook.")

            # Get the source code of the specified cell
            cell = nb["cells"][cell_number] 
            cell_source = cell["source"]

            # Check for the presence of markers and empty or comment-only cells
            if (
                "check()" in cell_source
                or "hint()" in cell_source
                or "solution()" in cell_source
                or "### Question" in cell_source
            ):
                raise Exception(f"In cell {cell_number}, one of the markers (check(), hint(), solution(), ### Question) is present.")

            if not cell_source.strip() or cell_source.strip().startswith("#"):
                raise Exception(f"In cell {cell_number}, the cell is empty or contains only comments.")

            # If a variable name is provided, check for its existence in the cell
            if variable_name is not None:
                namespace = {}
                try:
                    exec(cell_source, namespace)
                    if variable_name not in namespace:
                        raise Exception(f"In cell {cell_number}, the variable '{variable_name}' is not defined.")
                except Exception as e:
                    raise Exception(f"Error in cell {cell_number}: {str(e)}")

    except Exception as e:
        # Handle exceptions and show context
        show_twenty_cells_around_this_cell(notebook_name, cell_number)
        raise e
