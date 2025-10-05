# event-scheduler
CU Boulder DTSC 5501 Fall 2025 Group Project #1: Campus Event Scheduling System

# TODO: ADD ROLE DESCRIPTIONS HERE
Written and maintained by Group 10:
- Stephanie Bie
- Dnyanada Bhosale
- Augustine Joy

## Setup

Open a new terminal, navigate to a preferred directory, and clone the repository (for more information see this <a href="https://docs.github.com/en/get-started/git-basics/about-remote-repositories">tutorial</a>. I recommend following the "Cloning with SSH URLs" section):

```bash
git clone git@github.com:stephaniebie/event-scheduler.git
```

Create and enter a virtual environment (Windows):

```bash
python -m venv venv
source venv/Scripts/activate
```

### For Developers

Once in the environment, install the package in editable mode and install a kernel for use with Jupyter notebooks:

```bash
pip install -e .
python -m ipykernel install --user --name=scheduler
```

### For Users

Once in the environment, install the package and install a kernel for use with Jupyter notebooks:

```bash
pip install .
python -m ipykernel install --user --name=scheduler
```

## Development

Open a terminal and enter the virtual environment created earlier:

```bash
source venv/Scripts/activate
```

To open Jupyter Lab:

```bash
jupyter-lab .
```

To exit and close the notebook, open the terminal where you ran the above command, and press `Ctrl+C` a few times.

To exit the virtual environment, type `deactivate` in the terminal.

To run tests:

```bash
pytest tests
```

# TODO: ADD RESULTS DISCUSSION HERE
