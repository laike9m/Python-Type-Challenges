- Step 1. Install PDM

  The project uses [PDM](https://pdm-project.org/latest/) for managing dependencies, executing commands, and other stuff. Follow the [instructions](https://pdm-project.org/latest/) to install PDM if you haven't.

- Step 2. Clone the project

  ```bash
  git clone git@github.com:laike9m/Python-Type-Challenges.git
  ```

- Step 3. Install dependencies

  ```bash
  # Inside the project directory
  pdm install && pdm install --plugins
  pdm venv activate
  pre-commit install
  ```

If you encounter any issues in the above steps, please file a bug and I'll fix it as soon as I can.
