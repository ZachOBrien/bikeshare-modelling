# Bikeshare Ridership Modelling

[![Python 3.10.5](https://img.shields.io/badge/python-3.10.5-blue.svg)](https://www.python.org/downloads/release/python-3105/)

Zach O'Brien

## Set up Environment

**This project was developed with Python version 3.10.5. You can attempt to install the packages and run the code with a different version of Python and it might work, but using version 3.10.5 is probably best.**

1. Install Python version 3.10.5 and use that version for the following steps

2. Create a new virtual environment for this project

    ```console
    python3 -m venv env/
    ```

3. Activate the virtual environment

    ```console
    # On windows:
    env\Scripts\activate.bat
    ```

    ```console
    # On Linux or MacOS:
    source env/bin/activate
    ```

4. Install dependencies

    On Apple silicon:
    ```
    # With the env/ virtual environment activated:
    python -m pip install -r requirements-apple-silicon.txt
    ```

    On all other platforms, including intel-based macs:
    ```
    # With the env/ virtual environment activated:
    python -m pip install -r requirements.txt

5. Create a new kernel for this environment to use with the Jupyter Notebook

    ```
    # With env/ virtual environment activated
    python -m ipykernel install --user --name bikeshare_modelling
    ```

6. Open Jupyter Lab

    ```
    # With the env/ virtual environment activated:
    jupyter-lab
    ```


