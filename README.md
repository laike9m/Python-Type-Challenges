# Python Type Challenges

Learn Python 🐍 typing (type hints) by completing online challenges.

🌟🌟 Click **[HERE](https://python-type-challenges.zeabur.app)** to start 🌟🌟

Happy typing!

## How to Contribute

You're more than welcome to contribute new challenges!

All existing [challenges](https://github.com/laike9m/Python-Type-Challenges/tree/main/challenges) live under the `challenges/` directory. Here's how to add a new one

1. Fork this project if you haven't done so

2. Determine how difficult the challenge is. There are 3 levels: basic, intermediate, and advanced.

3. Create a new directory under `challenges/`. The new directory's name should follow the pattern `[basic|intermediate|advanced]-name`.

   For example, say you want to add a new challenge about [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html). Clearly this is an advanced topic, so you may name the directory `advanced-protocol`.

4. Put a `question.py` in the new directory. Here's an example:
   ```python
   """
   TODO:
   
   foo should accept a dict argument, both keys and values are string.
   """
   
   def foo(x):
       pass
   
   def should_pass():
       foo({"foo": "bar"})
   
   def should_fail():
       foo({"foo": 1})
   ```

   You want to include several things in `question.py`

   - Describe the challenge, make sure people understand what they need to accomplish (the `TODO:` part)
   - Add two functions `should_pass` and `should_fail` as test cases. The **function names are mandatory**. With correct code, `should_pass` should pass type check, and `should_fail` should fail type check.

   Using the above challenge as an example, the correct answer is `def foo(x: dict[str: str]): pass`.

   This will pass type check:

   ```python
   def foo(x: dict[str: str]):
       pass
   
   def should_pass():
       foo({"foo": "bar"})
   ```

   This will fail type check

   ```python
   def foo(x: dict[str: str]):
       pass
     
   def should_fail():
       foo({"foo": 1})
   ```

5. Test with [`mypy`](https://mypy.readthedocs.io/) to make sure your new challenge works as expected.

6. Create a Pull Request. And that's it 🙂

## Got Questions?

For general questions, you can post them in [Discussions](https://github.com/laike9m/Python-Type-Challenges/discussions).

If you met issues or want to suggest a new feature/improvement, feel free to [open a new issue](https://github.com/laike9m/Python-Type-Challenges/issues/new).





