# Week 01 - Python Set Up and Intro

24th September 2021

## Python Overview
- Python terminal
- [VSCode](https://code.visualstudio.com/) IDE
- Running python scripts
- How to read exception messages
- [Jupyter notebooks](https://jupyter.org/) for interactive work
  - When starting new notebook you need to select which python environment to run the notebook in https://stackoverflow.com/a/44786736 solution for conda environments not showing up in jupyter 
- [Python package index](https://pypi.org/) aka pypi
- [Github](https://github.com/) for source code
- [Conda](https://docs.conda.io/en/latest/) for environment management
  - [Conda environment file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) for environment definition, example conda env file contents below;

```
name: test_env
dependencies:
 - python=3.7.9
 - pip=21.0.1
 - pip:
   - jupyter==1.0.0
   - pandas==1.3.3
```

## Exercises

### Set Up Development Environment

- Install VSCode
- Install Miniconda or Anaconda
- Create a conda environment using an environment file specifying exact versions for python, pandas, matplotlib, jupyter

### A Whirlwind Tour of Python

- Read [Real Python’s Introduction to Python 3](https://realpython.com/python-introduction/ )
- Read [Real Python’s How to Use Python: Your First Steps](https://realpython.com/python-first-steps/)
- [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
  - Follow sections 1 - 10, 14, 15, (17 - further reading) running the python commands

