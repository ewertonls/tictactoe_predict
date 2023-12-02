# Tic-Tac-Toe Predict

Predict tic-tac-toe game result.

# Steps
I will assume you have `python 3.9` or newer installed.
If `python` or `pip` commands aren't available, try `python3` or `pip3` instead.
Also check if python is in your `PATH` in case of exotic installs.

## 1. Install dependencies

```sh
$ pip install -r requirements.txt
```

## 2. Run
You can run the script passing a game to it as args, where:
- `x` is cross
- `o` is circle
- `b` is blank

You can also pass multiple games, for a second, third, etc to be parsed the args
must be at least in length of `n*9`, the rest of input will be considered
a blank value.
Where the args `xxxbbboooxbo` will produce the two following games:

```
 x | x | x       x |   | o
---+---+---     ---+---+---
   |   |           |   |
---+---+---     ---+---+---
 o | o | o         |   |
```

```sh
$ python tictactoe.py xobooxx
...
 x | o |
---+---+---
 o | o | x
---+---+---
 x |   |

X will win: no
```