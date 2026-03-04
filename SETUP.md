# Setup
## Environment Setup Guide
Before using this repo, make sure you have installed the following core tools:

- Git
- Git Bash (for Windows)
- UV

## Necessary Packages
This "Predict Customer Spending Score" repo uses its own isolated environment called `pcss-env` so that packages don’t conflict with other projects. 
We use UV to create this environment, activate it, and install the required packages listed in the module’s `pyproject.toml`.  

This setup only needs to be done **once**, after that, you just activate the environment whenever you want to work in this repo.  

Open a terminal (macOS/Linux) or Git Bash (Windows) in this repo, and run the following commands in order:

1. Create a virtual environment called `pcss-env`:
    ```
    uv venv pcss-env --python 3.11
    ```

2. Activate the environment:
    - for macOS/Linux:
        ```
        source pcss-env/bin/activate
        ```
        
    - for windows (git bash):    
        ```
        source pcss-env/Scripts/activate
        ```

3. Install all required packages from the [pyproject.toml](./pyproject.toml)
    ```bash
    uv sync --active
    ```

## Environment Usage
In order to run any code in this repo, you must first activate its environment.
- for macOS/Linux:
    ```
    source pcss-env/bin/activate
    ```
    
- for windows (git bash):    
    ```
    source pcss-env/Scripts/activate
    ```

When the environment is active, your terminal prompt will change to show:  
```
(pcss-env) $
```
This is your **visual cue** that you’re working inside the right environment.  

When you’re finished, you can deactivate it with:  
```bash
deactivate
```

> **👉 Remember**   
> Only one environment can be active at a time. If you switch to a different repo, first deactivate this one (or just close the terminal) and then activate the new repo’s environment.

---