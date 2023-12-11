# How to add a new challange?

1. Fork this project if you haven't done so

2. Determine how difficult the challenge is. There are 4 levels: **basic**, **intermediate**, **advanced**, and **extreme**.

3. Create a new directory under [`challenges/`](https://github.com/laike9m/Python-Type-Challenges/tree/main/challenges). The new directory's name should follow the pattern `[basic|intermediate|advanced|extreme]-name`.

   For example, say you want to add a new challenge about [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html). Since this is an advanced topic, you may name the directory `advanced-protocol`.

4. Put a `question.py` and a `solution.py` in the new directory. Here's an example `question.py`:

   ```python
   """
   TODO:
     foo should accept a dict argument, both keys and values are string.
   """

   def foo(x):
       pass

   ## End of your code ##
   foo({"foo": "bar"})
   foo({"foo": 1})  # expect-type-error
   ```

   You want to include several things in `question.py`:
   - Describe the challenge, make sure people understand what they need to accomplish (i.e. the `TODO:` part)
   - A comment `## End of your code ##`. This is mandatory, just copy and paste it.
   - Several test cases. Add a comment `# expect-type-error` after the lines where type errors should be thrown.

   `solution.py` contains the right solution, with everything else unchanged.

   **Rule of Thumb**: A challenge should *NEVER* ask users to write the actual implementation. Users are expected to write type hints and type hints only, and be able to pass the tests.

5. Test with [`pyright`](https://microsoft.github.io/pyright/#/installation?id=command-line) to make sure your new challenge works as expected.

6. *(Optional)* Add a hint message for the challenge,
   A well-written *HINT* sometimes makes the challenge even better. Steps:
   - Create a file named `hints.md` in the same directory.
   - Write hint message in markdown format, e.g: `Check out TypeVar, the constraints argument might be a good fit for this challenge.`.

7. Create a Pull Request.
