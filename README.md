[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**<sup>(Let it scream at you)</sup>**

[![Build Status](https://travis-ci.com/ThatXliner/scratch-2-py.svg?branch=master)](https://travis-ci.com/ThatXliner/scratch-2-py)

# scratch-2-py

NOTE: README still under construction. And I'm also not done

## What is this?

**Scratch-2-py: The python implementation of PullJosh's Leopard.**

_TL;DR_: This turns scratch projects into python.

Inspired by PullJosh's [Leopard](https://github.com/PullJosh/leopard), and his [sb-edit](https://github.com/PullJosh/sb-edit), this implementation tries to convert the crazy ugly scratch JSON (which we call sb-JSON) into a cleaner, more generic, JSON (instead of JavaScript objects). Then, parsing the JSON, this program will make a [pygame](https://www.pygame.org/news) game.

**NOTE: I personally don't know pygame that much so any experts should contribute**

The parsing of JSON into much more easily readable (and usable) could be a separate repo.... :thinking:

You can use the JSON to a cleaner, more generic, JSON python script in

<u>
  <code>sbJSON2clean/GOOD_JSON.json</code>
</u>

or the scratchblocks representation in

<u>
  <code>sbJSON2clean/scratchblock_repr.txt</code>
</u>.

## Features

This project features the following:

- A decent sbJson to JSON converter (which may become it's separate Github repo in the future)
- A python API (since it's written in python)
- A decent README (WIP)
- And more!

---

## Future Features

In the future, we plan to add the following features:

[ ] A command line interface

[ ] A decent API

[ ] A better README

[ ] Documentation

[ ] Leopard integration

But for now, our highest priority is:

`Finishing this project`

# Contributing guidelines

TK

# Code style

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Black is pretty strict, and you can't configure it. Well, all we care about is the code, not the style.

**The only significant difference is that Black's max line length is `88` characters.** You should update your `flake8` settings accordingly. 

Also, it is recommended to use comments such as:

```python
# NOTE:
# TODO:
# HACK:
# DEBUG:
# OPTIMIZE:
```

These comments will be given special attention if you use the [MagicPython](https://github.com/MagicStack/MagicPython) python language syntax highlighting.

A little note: I personally prefer lots of inline comments in contrast to [PEP8](https://www.python.org/dev/peps/pep-0008/#inline-comments), I prefer lots of inline comments. I shouldn't 😔

**PLEASE USE [4 spaces](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)**

Black prefers double quotes. I'm not sure it'll switch to single quotes if necessary. It also will leave a space before the colon (`:`) in if statements, etc.

Use `try`/`excepts` over `if`-statements if possible. Same applies to `list`/`dict` comprehensions over for loops.

Also, **try to align statements as much as possible!**

Instead of this:
```
var1 = ["foo", "bar"]
long_name_var2 = 5
v3 = [float(x) for x in range(10)]
v4 = [x for x in rsnge(100)]
```

do
```
var1           = ["foo", "bar",]
long_name_var2 = 5
v3             = [float(x) for x in range(10)]
v4             = [x for x in rsnge(100)]
```
I think you'll need to configure `flake8` to ignore that, too.
Notice the hanging comma? Black did that.


Block comments, such as
```
################################################################
# This block comment ends at 79 characters #####################
################################################################
```

are used to seperate code into "paragraphs". It gives the reader an idea of what the next hundred/couple lines will be about. **Do not overuse.**

If you want more info on the black code style, see [here](https://black.readthedocs.io/en/stable/the_black_code_style.html)

## Naming conventions:
Variables and function names = `snake_case`

Class names and file names   = `camelCase`


# A little warning

:warning: THIS IS STILL HIGHLY IN-DEV. **THIS IS STILL IN IT'S _very_ EARLY STAGES OF DEVELOPMENT**.

You may contribute.

If you want to, email me at bryan.hu.cn@gmail.com
