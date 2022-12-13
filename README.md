# DS4400 Final Project

Zach O'Brien

December 2022

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
    source env/bin/activate
    ```

4. Install dependencies

    ```console
    # With environment activated
    python -m pip install -r requirements.txt
    ```

5. Create a new kernel for this environment to use with the Jupyter Notebook

    ```console
    # With environment activated
    python -m ipykernel install --user --name ds4400_final_obrien
    ```

6. Open Jupyter Lab

    ```console
    # With the env/ virtual environment activated:
    jupyter-lab
    ```


