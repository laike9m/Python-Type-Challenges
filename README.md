# Python Type Challenges

Learn Python 🐍 typing (type hints) by completing online challenges.

🌟🌟 Click **[HERE](https://python-type-challenges.zeabur.app)** to start 🌟🌟

![](docs/images/usage.gif)

Happy typing!

## How to Run Locally

This project use [PDM](https://pdm.fming.dev/latest/), a modern Python package and dependency manager, to manage dependencies. After you [have installed PDM](https://pdm.fming.dev/latest/#installation), you can run this project locally based on the following steps:

```bash
pdm install
pdm run devserver
```

Optionally, the `requirements.txt` file is also provided for you if PDM doesn't exist in your environment.

You can use traditional `pip` to install dependencies and run the project manually:

```bash
pip install -r requirements.txt
flask --app app run --debug
```

## How to Contribute

You're more than welcome to contribute new challenges!

All challenges live under the [`challenges/`](https://github.com/laike9m/Python-Type-Challenges/tree/main/challenges) directory, and it's pretty easy to add a new one: **you only need to create a new folder, add a `question.py` and a `solution.py`, and that's it**. See [here](docs/Contribute.md) for a detailed guidance.

## Got Questions?

For general questions, you can post them in [Discussions](https://github.com/laike9m/Python-Type-Challenges/discussions).

If you met issues or want to suggest a new feature/improvement, feel free to [open a new issue](https://github.com/laike9m/Python-Type-Challenges/issues/new).

## Credits

This project is inspired [Type Exercise in Rust](https://github.com/skyzh/type-exercise-in-rust/) by [@skyzh](https://github.com/skyzh), and [type-challenges](https://github.com/type-challenges/type-challenges/) by [@antfu](https://github.com/antfu).
