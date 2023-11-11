# Python Type Challenges

Learn Python 🐍 typing (type hints) by completing online challenges.

🌟🌟 Click **[HERE](https://python-type-challenges.zeabur.app)** to start 🌟🌟

![](docs/images/usage.gif)

Happy typing!

## How to Run Locally

This project use [PDM](https://pdm.fming.dev/latest/), a modern Python package and dependency manager, to manage dependencies. After you [have installed PDM](https://pdm.fming.dev/latest/#installation), you can run this project locally based on the following steps:

```bash
pdm plugin add pdm-autoexport
pdm install
pdm run dev # or more shorter: pdm dev
```

Alternatively, you can install dependencies just using `pip`:

```bash
pip install -r requirements.txt
flask run
```

## How to Contribute

- **Add a new challenge**

  Adding a new challenge is pretty simple: **you only need to create a new folder, add a `question.py` and a `solution.py`, and that's it**. See [here](docs/Contribute.md) for a detailed guidance.

- **Making code changes**

  If you want to fix a bug or add a new feature, follow the [guidance](docs/Development.md).

## Got Questions?

For general questions, you can post them in [Discussions](https://github.com/laike9m/Python-Type-Challenges/discussions).

If you met issues or want to suggest a new feature/improvement, feel free to [open a new issue](https://github.com/laike9m/Python-Type-Challenges/issues/new).

## Credits

This project is inspired [Type Exercise in Rust](https://github.com/skyzh/type-exercise-in-rust/) by [@skyzh](https://github.com/skyzh), and [type-challenges](https://github.com/type-challenges/type-challenges/) by [@antfu](https://github.com/antfu).
