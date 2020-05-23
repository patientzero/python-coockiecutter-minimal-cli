# Python coockiecutter minimal cli template

This is an absolute minimal boilerplate cli code as I use it in many of my projects
where fast iteration and exploration is the key while maintaining order and versioning commands
as well as writing outputs is important.
I prefer this way of working to the use of iPython notebooks, especially as soon as it comes
to experimenting.
Command line arguments with proper help texts are somewhat "self documenting" which can be useful, especially if you wrote
the code a while back.
## Features:
* logging namespace
* set log level on cli
* boilerplate cli generation
## Requirements:

You need cookiecutter installed (for example from here https://github.com/cookiecutter/cookiecutter)
Install with conda or pip:
```
pip install --user cookiecutter
# or
conda install cookiecutter
```
or when you're on Mac you can use homebrew
```
brew install cookiecutter
```

To make the template work you will need the click library:
```
pip install click
```


## Usage:

### **Directly from github**
```
cookiecutter -o outdir https://github.com/patientzero/python-cockiecutter-minimal-cli
```
### **From the cloned directory:**
```
git clone https://github.com/patientzero/python-cockiecutter-minimal-cli.git
cd python-cockiecutter-minimal-cli
cookiecutter -o outdir ~/projects/python-cockiecutter-minimal-cli

```
### **Options && default values**:
```
    "module_name": "command",
    "command_group_name": "cli",
    "cli_name": "my_cli",
    "first_command_name": "helloworld",
    "file_name": "cli.py"
```
* module name: name of the module containing your cli
* command_group_name: Name of the method on which the @click.group decorator is placed, used for adding more commands
* cli_name: Internal name for your program. Mainly used for logging.
* first_command_name: Name of first example/boilerplate method
* file_name": Name of the file containing your cli definition

## General use of generated cli:
```
python -m module_name --option1 someinput --option2 somemoreinput
```
## Example call of first generated method:
```
cd outdir
python -m command -l INFO helloworld --log-dir /test/logs
# output:
# [2020-03-23 15:39:41,881] INFO cli.py: use pathlib to write to /test/logs
```

You can make new commands based on the provided example (helloworld).
For more options visit the [click docs](https://click.palletsprojects.com/en/7.x/).
