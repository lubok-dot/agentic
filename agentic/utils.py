# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_utils.ipynb.

# %% auto 0
__all__ = ['extract_python_blocks', 'markdown_to_json', 'json_to_markdown']

# %% ../nbs/05_utils.ipynb 3
import re

# %% ../nbs/05_utils.ipynb 5
def extract_python_blocks(text: str) -> list[str]:
    """
    Extracts the content between ```python ... ``` blocks from the given string.

    Parameters
    ----------
    text
        The input string containing Python code blocks.

    Returns
    -------
    code
        A list of strings, each containing the content of a Python code block.

    """
    # Regex to match content between ```python ... ```
    pattern = r"```python\n(.*?)```"
    # Use re.DOTALL to match across newlines
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

# %% ../nbs/05_utils.ipynb 6
def markdown_to_json(markdown_text: str) -> dict:
    """
    Splits a markdown file along its ## headers and organizes content in a dictionary.

    Parameters
    ----------
    markdown_text
        The markdown file content as a string.

    Returns
    -------
    json
        A dictionary where keys are transformed headers and values are paragraph text.
    """

    # Regular expression to match `##` headers
    header_pattern = re.compile(r"^##\s*(.+)$", re.MULTILINE)

    # Find all headers and their positions
    headers = [
        (match.start(), match.group(1))
        for match in header_pattern.finditer(markdown_text)
    ]

    # Dictionary to store the processed headers and content
    content_dict = {}

    for i, (start_pos, header) in enumerate(headers):
        # Determine the start and end of the content for this header
        end_pos = headers[i + 1][0] if i + \
            1 < len(headers) else len(markdown_text)

        # Extract content for the current header
        content = markdown_text[start_pos:end_pos]

        # Remove the header itself from the content
        content = header_pattern.sub("", content, count=1).strip()

        # Transform header: casefold, strip whitespace, and replace spaces with underscores
        transformed_header = header.casefold().strip().replace(" ", "_")

        # Add the header and its corresponding content to the dictionary
        content_dict[transformed_header] = content

    return content_dict


def json_to_markdown(content_dict: dict) -> str:
    """
    Reconstructs a markdown string from a dictionary where keys are headers
    and values are paragraph text.

    Parameters
    ----------
    content_dict
        A dictionary with transformed headers as keys and content as values.

    Returns
    -------
    markdown
        The reconstructed markdown string.
    """
    markdown_lines = []

    for header, content in content_dict.items():
        # Transform the key back into a header: replace underscores with spaces, capitalize
        original_header = header.replace("_", " ").title()
        # Add the header and its content in markdown format
        markdown_lines.append(f"## {original_header}")
        markdown_lines.append(content)
        markdown_lines.append("")  # Add a blank line for spacing

    # Join the lines to form the complete markdown text
    return "\n".join(markdown_lines)
