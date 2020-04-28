## 0. The Basics
We'll assume a working knowledge of the command line so if you're not familiar see the Unix tutorial in this 
repository.


### 0.0 Getting Set Up: Python Interpreters

Before we get into writing Python we need a program that will run our Python code, a 
[Python interpreter](https://docs.python.org/3.7/tutorial/interpreter.html). We'll be using Python version 3 rather than 2 for full support of scientific libraries like NumPy and 
some other nice features.

#### a. Mac OS and Linux 
Both Mac OS and Linux come with interpreters built in so if in your terminal you type 

```bash
which python3
```

and hit enter you should see a path like `/usr/local/bin/python3` or perhaps `/bin/python3`. While this Python is 
completely fine to use you may find later on that dependencies are difficult to satisfy, we'll therefore install
[miniconda](<https://docs.conda.io/en/latest/miniconda.html>) a 'conda' environment that makes dependency install
simple. Download the installer and follow on the instructions after which running `which python3` should return 
something like `/your/home/dir/miniconda3/bin/python3`.

#### b. Windows
Windows doesn't ship with a Python interpreter so installing [miniconda](<https://docs.conda.io/en/latest/miniconda.html>)
is essential. After you do so you should have a 'Anaconda (command line)' program where you should execute any 
`conda install` commands.


### 0.1 Getting Set Up: Editors

All you need to write Python scripts is a text editor (or not even that with the interactive mode in Python) so you 
could use your favourite editor e.g. [Atom](https://atom.io/), [vi](https://www.vim.org/), 
[Notepad++](https://notepad-plus-plus.org/). Alternatively, you could use a [Jupyter Notebook](https://jupyter.org/)
which provides a way to integrate text, figures and code in one place. My preferred method, however, is to use an 
Integrated Developer Environment (IDE), specifically [PyCharm](https://www.jetbrains.com/pycharm/). IDEs come with with
lots of nice features including auto-correct, syntax highlighting and debuggers and make writing code faster and more
accurate.
