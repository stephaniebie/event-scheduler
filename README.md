# event-scheduler
CU Boulder DTSC 5501 Fall 2025 Group Project #1: Campus Event Scheduling System

# TODO: ADD ROLE DESCRIPTIONS HERE
Written and maintained by Group 10:
- Stephanie Bie
- Dnyanada Bhosale
- Augustine Joy

## Setup

Open a new terminal, navigate to a preferred directory, and clone the repository onto your local machine (for more information see this <a href="https://docs.github.com/en/get-started/git-basics/about-remote-repositories">tutorial</a>. I recommend following the "Cloning with SSH URLs" section):

```bash
git clone git@github.com:stephaniebie/event-scheduler.git
```

Create and enter a virtual environment (Windows):

```bash
python -m venv venv
source venv/Scripts/activate
```

Install a kernel for use with Jupyter notebooks:

```bash
python -m ipykernel install --user --name=scheduler
```

### For Developers

Once in the environment, install the package in editable mode:

```bash
pip install -e .[dev]
```

### For Users

Once in the environment, install the package:

```bash
pip install .
```

## Development

Navigate to the directory the local repo is located in, and open a terminal at this location.

For all developers, I recommend creating a new branch using the following command:

```bash
git checkout -b your-branch-name
```

It is generally bad practice to push to a main branch, especially in a collaborative environment.

Enter the virtual environment created earlier:

```bash
source venv/Scripts/activate
```

To open VSCode (if you haven't already, please install from <a href="https://code.visualstudio.com/download">here</a>):

```bash
code .
```

To open Jupyter Lab:

```bash
jupyter-lab .
```

To run tests:

```bash
pytest tests
```

After making a change you'd like to commit, run the following commands:

```bash
# This stages all of your recent changes
git add -A
# This commits your changes and allows you to write a message summarizing the change. It is good practice to write a message
git commit -m "Commit message here"
# This pushes your changes to the remote repository
git push
```

NOTE: if this is a new branch you may need to run

```bash
git push --set-upstream origin your-branch-name
```

To exit and close the notebook, open the terminal where you ran the above command, and press `Ctrl+C` a few times.

To exit the virtual environment, type `deactivate` in the terminal.

# TODO: ADD RESULTS DISCUSSION HERE
