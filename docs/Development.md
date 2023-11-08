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

## Common commands

- Run test

  ```
  pdm test
  ```

- Format files

  ```
  pdm format
  ```
  Note: The project uses [djhtml](https://github.com/rtts/djhtml) to format HTML, which may conflicts with your editor's default formatter.

- Start a development server

  ```
  pdm devserver
  ```

  Then visit http://127.0.0.1:5000/ to access the app in your local browser.

If you encounter any issues in the above steps, please file a bug and I'll fix it as soon as I can.
