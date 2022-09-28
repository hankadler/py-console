# py-console

A command-line interface

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Examples](#examples)
    - [Ask](#ask)
    - [Select](#select)
- [License](#license)

## Features

Console, once instantiated, provides methods for the following:

- Clearing the console screen.
- Persistently prompting the user for input.
- Persistently prompting the user to select an item from a list.

Options in the form of keyword arguments include:

- Clearing the console screen before the looping prompt.
- Constraining the input type to a specified type. If this requirement
  is violated, a warning is issued and the application repeats the
  prompt.
- Returning with a default value instead of prompting for it
  persistently, if no input is provided.

## Setup

```bash
# assumption: you're working on project with pipenv
pipenv shell
pipenv install -e git+https://github.com/hankadler/py-console#egg=console
```

## Examples

### Ask for ``x``, defaulting to ``2.2``:

```
>>> from console import Console
>>> console = Console()
>>> x = console.ask('Enter x: ', type=float, default=2.2)
Enter x:   # Nothing entered...
>>> x
2.2
```
> ``type=float`` ensures returned value is a ``float`` and not a ``str``.

### Select color(s) from a list of colors:

```
>>> from console import Console
>>> console = Console()
>>> colors = ['red', 'blue', 'yellow']
>>> color = console.ask('Select color: ', colors)
Select color:
    1. red
    2. blue
    3. yellow
Choice(s): 2
>>> color
'blue'
>>> colors = console.ask('Select colors: ', colors)
Select color:
    1. red
    2. blue
    3. yellow
Choice(s): 2 1  # Multiple choices are allowed...
>>> colors
['blue', 'red']
```

## License

[MIT](LICENSE)
