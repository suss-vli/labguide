# CLI

Are you tired of running the virtual environment setup script? 
Or the git module commands to pull all modules? Or perhaps you have more multi-steps command that you have already written and lazy to type the full path?  

# Meet CLI

`cli` is a simple everyday cli with a simple mission. Save you keystroke and increase your project efficiency (& accuracy). Look at these benefits:

1. 📐Shorter. Better. Run shorter commands `setup`, `pull`, `module` with standardisation
2. 👯‍♂️ Same same! Stop saving script into dev/ or use different standardisation
3. ❌ No 3rd party script needed. Just use back the good default: `pip` and `python`
4. 🔋🔋🔋 Extra batteries will be included. Add on more scripts as you build along. Use an easy config file. 

# Installation
1. This method works. 
```
git clone https://github.com/ytbryan/cli
#then add the export CLI_PATH of cli path.
```
2. Add the repo to the PATH

```bash
export PATH="$PATH:<path_to_repo>/cli"
```

NOTE: Does not work yet
```
pip install git+http://github.com/ytbryan/cli.git
```

# Getting started

## Getting Started

## Set the CLI_PATH

```bash
export CLI_PATH="<path_to_this_cloned_project>"
```

## cli --help
```
cli --help
```

## TODO
- [x] ship it
- [x] add config.yml 
- [ ] add `show` to show the content of the file
- [ ] add alias to each command
- [ ] add `age` to show git commits and its age
- [ ] integrate with pyenv and pick up python version

## LICENSE
MIT
