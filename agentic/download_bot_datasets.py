# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_download_bot_datasets.ipynb.

# %% auto 0
__all__ = ['download_file_from_url', 'download_from_huggingface', 'download_gsm8k', 'download_ambignq', 'download_humaneval',
           'download_game_of_24', 'download_python_programming_puzzles', 'download_bhb_tasks', 'sample_from_datasets']

# %% ../nbs/04_download_bot_datasets.ipynb 3
# load_dataset from the datasets library: Facilitates loading datasets from the Hugging Face Hub. (pip install datasets)
from datasets import load_dataset
from pathlib import Path
from typing import Optional
import requests
import zipfile
import io
import random
import json

# %% ../nbs/04_download_bot_datasets.ipynb 4
def download_file_from_url(
    url: str,
    path: Path,
):
    """
    Download a file from a URL.

    Parameters
    ----------
    url
        URL of the file to download.
    path
        Path where the downloaded file will be saved.

    Returns
    -------
    None
        This function performs file download but does not return any value.
    """
    if not path.exists():
        print(f"Downloading file from {url}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"File downloaded and saved to {path}.")
    else:
        print(f"File {path} already exists. Skipping download.")

# %% ../nbs/04_download_bot_datasets.ipynb 5
def download_from_huggingface(data_path: Path, path: str, name: Optional[str] = None):
    """
    Download a dataset from Hugging Face and save its splits to a specified directory.

    Parameters
    ----------
    data_path : Path
        The root directory where the dataset will be saved.
    path : str
        The dataset identifier on Hugging Face (e.g., "openai_humaneval").
    name :
        An additional name of the dataset. Will be used to create an extra directory. If None, no extra directory is created.

    Returns
    -------
    None
        This function downloads the dataset and saves it locally.
    """
    # Construct the target directory
    target_path = data_path / path
    if name:
        target_path = target_path / name

    # Check if the target directory exists and contains files
    if target_path.exists() and any(target_path.iterdir()):
        print(f"Dataset already exists in {target_path}. Skipping download.")
        return

    # Load the dataset from Hugging Face
    dataset = load_dataset(path=path, name=name)

    # Ensure the target directory exists
    target_path.mkdir(parents=True, exist_ok=True)

    # Save each split of the dataset to the target directory
    for split in dataset.keys():
        split_dataset = dataset[split]
        split_path = target_path / f"{split}.jsonl"
        split_dataset.to_json(split_path)
        print(f"Saved {split} split to {split_path}")

# %% ../nbs/04_download_bot_datasets.ipynb 7
def download_gsm8k(
    data_path: Path,
):
    """
    Download the GSM8k dataset into a specified folder.

    Parameters
    ----------
    path
        Directory path where the GSM8k dataset will be saved. If the directory does not exist, it will be created.

    Returns
    -------
    None
        This function downloads the dataset and saves it locally but does not return any value.
    """
    download_from_huggingface(data_path, "openai/gsm8k", "main")

# %% ../nbs/04_download_bot_datasets.ipynb 9
def download_ambignq(
    path: Path,
):
    """
    Download the AmbigNQ dataset into a specified folder.

    Parameters
    ----------
    path
        Directory path where the AmbigNQ dataset will be saved. If the directory does not exist, it will be created.

    Returns
    -------
    None
        This function downloads the dataset, extracts its contents, and saves them locally but does not return any value.
    """
    # URL for AmbigNQ dataset
    url = "https://nlp.cs.washington.edu/ambigqa/data/ambignq_light.zip"

    # Convert path to Path object and create directory if it doesn't exist
    ambignq_path = path / "ambignq"
    ambignq_path.mkdir(parents=True, exist_ok=True)

    # Download the ZIP file
    print(f"Downloading ZIP file from {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Open the ZIP file in memory and extract its contents
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        print("Unpacking ZIP file...")
        zip_file.extractall(ambignq_path)
    print(f"Unpacked contents to {ambignq_path}")

# %% ../nbs/04_download_bot_datasets.ipynb 11
def download_humaneval(data_path: Path):
    """
    Download the HumanEval dataset and save it to the specified directory.

    Parameters
    ----------
    data_path :
        The directory path where the HumanEval dataset will be saved. If the directory does not exist, it will be created.

    Returns
    -------
    None
        This function downloads the dataset and saves it locally but does not return any value.
    """
    download_from_huggingface(data_path, path="openai_humaneval")

# %% ../nbs/04_download_bot_datasets.ipynb 13
def download_game_of_24(data_path: Path):
    """
    Download the Game of 24 dataset using Hugging Face's `load_dataset` and save it to the specified directory.

    Parameters
    ----------
    path : Path
        The directory path where the Game of 24 dataset will be saved. If the directory does not exist, it will be created.

    Returns
    -------
    None
        This function downloads the dataset and saves it locally but does not return any value.
    """
    download_from_huggingface(data_path, path="nlile/24-game")

# %% ../nbs/04_download_bot_datasets.ipynb 15
def download_python_programming_puzzles(path: Path):
    """
    Download the Python Programming Puzzles (P3) dataset and save it to the specified directory.

    Parameters
    ----------
    path : Path
        The directory path where the P3 dataset will be saved. If the directory does not exist, it will be created.

    Returns
    -------
    None
        This function downloads the dataset and saves it locally but does not return any value.
    """
    # Ensure the target directory exists
    p3_path = path / "python_programming_puzzles"
    p3_path.mkdir(parents=True, exist_ok=True)

    # URL for the P3 dataset (update this URL if needed)
    url = "https://raw.githubusercontent.com/microsoft/PythonProgrammingPuzzles/main/puzzles/puzzles.json"

    download_file_from_url(url, p3_path / "train.json")

# %% ../nbs/04_download_bot_datasets.ipynb 17
def download_bhb_tasks(data_path: Path):
    """
    Download specific tasks from Google's BIG-Bench Hard (BBH) dataset and save them to the specified directory.
    Instead of downloading the entire dataset from the official repository, we download some examples from huggingface.

    Parameters
    ----------
    data_path : Path
        The root directory where the BBH tasks will be saved. Each task will be stored in a subdirectory
        based on its respective name.

    Returns
    -------
    None
        This function downloads the BBH tasks and saves them locally, with separate directories for each task.
    """
    for path, name in [
        ("maveriq/bigbenchhard", "boolean_expressions"),
        ("maveriq/bigbenchhard", "causal_judgement"),
        ("maveriq/bigbenchhard", "date_understanding"),
        ("maveriq/bigbenchhard", "word_sorting"),
    ]:
        download_from_huggingface(data_path, path, name)

# %% ../nbs/04_download_bot_datasets.ipynb 19
def sample_from_datasets(
    N: int, data_path: Path, path: Optional[str] = None, name: Optional[str] = None
) -> list[dict]:
    """
    Randomly samples N instances from the dataset(s) stored at the specified location.

    Parameters
    ----------
    N :
        Number of samples to retrieve.
    data_path :
        Root directory containing the datasets.
    path :
        Path to the specific dataset within the root directory. If None, `name` must also be None.
    name :
        Name of the dataset ('train' or 'test'). If None, samples from both datasets in `data_path/path`.

    Returns
    -------
    samples :
        A list of sampled instances.
    """
    if path is None and name is not None:
        raise ValueError("If 'path' is None, 'name' must also be None.")

    target_path = data_path / path if path else data_path
    target_path = target_path / name if name else target_path

    # Collect all json/jsonl files to sample from
    if target_path.exists():
        dataset_files = [
            file
            for file in target_path.rglob("*")
            if file.suffix in [".json", ".jsonl"]
        ]
    else:
        raise FileNotFoundError(f"The path '{target_path}' does not exist.")

    if not dataset_files:
        raise ValueError(
            f"No JSON or JSONL files found in the path '{target_path}'.")

    # Load data from the dataset files
    all_data = []
    for dataset_file in dataset_files:
        with open(dataset_file, "r", encoding="utf-8") as f:
            if dataset_file.suffix == ".jsonl":  # JSONL: Read line by line
                data = [json.loads(line.strip()) for line in f if line.strip()]
            elif dataset_file.suffix == ".json":  # JSON: Use json.load()
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError(
                        f"The JSON file '{
                            dataset_file}' does not contain a list of records."
                    )
            else:
                continue  # Skip unsupported file types
            all_data.extend(data)

    if not all_data:
        raise ValueError("No data found in the specified datasets.")

    # Randomly sample N instances
    if len(all_data) < N:
        raise ValueError(
            f"Not enough data to sample {
                N} instances. Found only {len(all_data)} records."
        )

    return random.sample(all_data, N)
