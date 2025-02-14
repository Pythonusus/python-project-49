# Brain-games

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Pythonusus/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Pythonusus/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/11ea1330cdbde1ec50c6/maintainability)](https://codeclimate.com/github/Pythonusus/python-project-49/maintainability)


### Description:
Provides some cool games to play in console:
+ Brain-even. A game, where player needs to define if the given number is even.
+ Brain-calc. A game, where player needs to solve arithmetic problems.
+ Brain-gcd. A game, where player needs to find greatest common devisor of two numbers.
+ Brain-prime. A game, where player needs to define if the given number is prime.
+ Brain-progression. A game, where player needs to find missing number in progression.

### Requirements
Python >=3.8.1
poetry >= 1.2.0

### Quick start
1. Clone GitHub repo: `git clone https://github.com/Pythonusus/python-project-49`
2. Create virual environment and install dependencies.This comman should be executed in the root directory of the project: `make install`
3. Build project: `make build`
4. Install project on user level (`home/<user-name>/.local/bin` for Linux users): `make package-install`
5. Check `PATH` environmental variable. Path to the installation folder should be added to `PATH`.
6. Brain-games are ready to play!

### How to play
After installing the project, following commands will be available in the command line:
+ `brain-games` - shows welcome message
+ `brain-even` - starts brain-even game
+ `brain-calc` - starts brain-calc game
+ `brain-gcd` - starts brain-gcd game
+ `brain-progression` - starts brain-progression game
+ `brain-prime` - starts brain-prime game

### Brain-games asciinema demo
[![asciicast](https://asciinema.org/a/640811.svg)](https://asciinema.org/a/640811)

### Brain-even asciinema demo
[![asciicast](https://asciinema.org/a/634757.svg)](https://asciinema.org/a/634757)

### Brain-calc asciinema demo
[![asciicast](https://asciinema.org/a/635686.svg)](https://asciinema.org/a/635686)

### Brain-gcd asciinema demo
[![asciicast](https://asciinema.org/a/635756.svg)](https://asciinema.org/a/635756)

### Brain-progression asciinema demo
[![asciicast](https://asciinema.org/a/636056.svg)](https://asciinema.org/a/636056)

### Brain-prime asciinema demo
[![asciicast](https://asciinema.org/a/636305.svg)](https://asciinema.org/a/636305)

### Links
This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                        | "An extremely fast Python package and project manager, written in Rust"  |
| [Ruff](https://beta.ruff.rs/)                                         | "An extremely fast Python linter and code formatter, written in Rust" |
| [prompt](https://prompt.readthedocs.io/en/latest/)                          | "The prompt library provides functions that prompt for strings, numbers, and passwords." |
