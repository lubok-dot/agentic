---
description: Sample implementations of agentic research papers
output-file: index.html
title: agentic
---



```
# | hide
from agentic.core import *
```

# Agentic Workflows with LangGraph

This repository documents my experiments and learnings with **LangGraph** for implementing agentic workflows. My background in academia instilled in me a habit of understanding research papers by implementing them. As a result, this repository includes several implementations of research papers. These exercises extend beyond agentic workflows to cover various topics in mathematics and machine learning. You can find more examples on my personal [blog](https://lubok-dot.github.io/blog/).  

In addition to these implementations, I have also developed several auxiliary functions, primarily for downloading well-known benchmark datasets from various sources.  

I chose **nbdev** for development because it automatically generates high-quality documentation. Moreover, it separates code writing from packaging, making it easy to create standalone modules. This feature is particularly useful when deploying agents in [LangGraph Studio](https://studio.langchain.com). You can develop everything within Jupyter notebooks and export Python files that can be uploaded to LangGraph Studio at no cost.

## Developer Guide

If you are new to using `nbdev` here are some useful pointers to get you started.

### Install agentic in Development mode

```sh
# make sure agentic package is installed in development mode
$ pip install -e .

# make changes under nbs/ directory
# ...

# compile to have changes apply to agentic
$ nbdev_prepare
```

## Usage

### Installation

Install latest from the GitHub [repository][repo]:

```sh
$ pip install git+https://github.com/lubok-dot/agentic.git
```

[repo]: https://github.com/lubok-dot/agentic
[docs]: https://lubok-dot.github.io/agentic/
[pypi]: https://pypi.org/project/agentic/
[conda]: https://anaconda.org/lubok-dot/agentic

### Documentation

Documentation can be found hosted on this GitHub [repository][repo]'s [pages][docs]. 

[repo]: https://github.com/lubok-dot/agentic
[docs]: https://lubok-dot.github.io/agentic/
