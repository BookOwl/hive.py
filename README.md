# hive.py
A port of the Scratch game [Hive](https://scratch.mit.edu/projects/92205108/) to Python.
To run the game, use the following command: `python3 game.py` or on Windows if you have a recent Python installed: `py game.py`
## API
To programmatically play a Hive game, import the hive module and create a new game with the following code:
```python
import hive
game = hive.Hive()
```
Please see the source code or run `python -m pydoc hive` to see the whole API.

## Testing
I am using pytest for testing. To run the tests, install pytest, cd to the hive.py source directery, and run `python -m pytest -v`

## Changlog
### 1.1
Updated README and .gitignore, added a script to brute force winning sequences. Generalized the Hive class to create boards of any size.
### 1.0
Initial Release
