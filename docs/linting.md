## Introduction
Git hook scripts are useful for identifying simple issues before submission to code review.
We run our hooks on every commit to automatically point out issues in code such as missing semicolons,
trailing whitespace, and debug statements.

pre-commit is built to solve our hook issues. It is a multi-language package manager for pre-commit hooks.
You specify a list of hooks you want and pre-commit manages the installation and execution of any hook
written in any language before every commit. pre-commit is specifically designed to not require root access.

## Installation

pre-commit exists in the requirements/base.txt . So, all you need to do is to source the venv.sh script as shown below:

        source scripts/venv.sh

This will create a new venv or switch to existing one and install the pre-commit hook script at `.git/hooks/pre-commit`

## Adding  new hooks
In order to add new hooks or modify the existing one's refer to file:

        .pre-commit-config.yaml

To add a new hook follow the format:
```
- repo:  # keyword local or the github url of the repo
  rev:   # version or branch name to clone. This arg is only need when using remote repo's url
  hooks:
  - id:  # name of the hook e.g pylint, flake8 etc
```

Three are other parameters available which can be modified as per needed.
Have a look at (https://pre-commit.com/) for further details.

## Adding configuration for hooks

To added configuration for hooks use `pyproject.toml` file in root directory.
Each hook's comes under the tag specified in '[ ]' brackets. The tag is listed on docs for the specific hook
For example: ```[tool.yapfignore]```
