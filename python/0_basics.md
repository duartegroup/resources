## 0. The Basics
We'll assume a working knowledge of the command line so if you're not familiar see the Unix tutorial in this 
repository.

***

### 0.0 Getting Set Up: Python Interpreters

Before we get into writing Python we need a program that will run our Python code, a 
[Python interpreter](https://docs.python.org/3.7/tutorial/interpreter.html). We'll be using Python version 3 rather than
2 for full support of scientific libraries like NumPy and some other nice features.

#### a. Mac OS and Linux 
Both Mac OS and Linux come with Python interpreters built in so if in your terminal you type 

```bash
which python3
```

and hit enter you should see a path like `/usr/local/bin/python3` or perhaps `/bin/python3`. While this Python is 
completely fine to use you may find later on that dependencies are difficult to satisfy, we'll therefore install
[miniconda](<https://docs.conda.io/en/latest/miniconda.html>) a 'conda' environment that makes dependency installation
simple. Download the installer and follow on the instructions after which running `which python3` should return 
something like `/your/home/dir/miniconda3/bin/python3` (**Note**: you may have to close and reopen your terminal).

#### b. Windows
Windows doesn't come with a Python interpreter so installing [miniconda](<https://docs.conda.io/en/latest/miniconda.html>)
is essential. After you do so you should have a _'Anaconda (command line)'_ program that will be referred to your 
'terminal' in the following.


### 0.1 Getting Set Up: Editors

All you need to write Python scripts is a text editor (or not even that with the interactive mode in Python) so you 
could use your favourite editor e.g. [Atom](https://atom.io/), [vi](https://www.vim.org/), 
[Notepad++](https://notepad-plus-plus.org/). Alternatively, you could use a [Jupyter Notebook](https://jupyter.org/)
which provides a way to integrate text, figures and code all in one place. My preferred method, however, is to use an 
Integrated Developer Environment (IDE), specifically [PyCharm](https://www.jetbrains.com/pycharm/). IDEs come with with
lots of nice features including auto-correct, syntax highlighting and debuggers and make writing code faster and more
accurate. Make your choice before you continue!


#### a. Setting up PyCharm

If you're using PyCharm on Mac or Linux you'll need to configure it to use the conda Python interpreter. To do so see 
the tutorial [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html), that is essentially following:
Settings → Project: YourDir → Project Interpreter → Project Interpreter (Show All) → + → System Interpreter → 
/your/home/dir/miniconda3/bin/python3. On Windows your conda Python should have already been detected

***

### 0.1 Variables and Data Types 

For this section we'll use the interactive mode in Python, so in your terminal type `python3` and hit enter. You 
should be greeted by something like

```bash
Python 3.7.7 (default, Mar 26 2020, 15:48:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

where we can write Python code and have it executed as its written. Python has a few key data types
that we'll introduce here (str, int, float, list) and others will be introduced when needed. The full list can be found in the 
[official documentation](https://docs.python.org/3/library/stdtypes.html). To exit use Ctrl-d or type `exit()` and hit 
enter.

#### a. Variables and Numerical Types

Objects can be assigned to variables to be used later e.g.

```
>>> a = 1
>>> b = 1
>>> print(a + b)
2
```
where a and b take the integer (int) value of 1 and the built-in `+` operator adds the values and _print()_ 
and displays the result. Mathematical operators are: `+` (sum), `-` (difference), `*` (product), `**` (power).

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) **Try**: Assign b to a non-integer (float) value and print
the product a × b.


#### b. Strings

Text in Python are strings (str) defined by text in single or double quotes i.e. `'hello'` and `"hello"` are equivalent. 
Strings can be added, not subtracted and variables introduced using f-strings e.g.

```
>>> first_word = 'hello'
>>> print(f'{first_word} world')
hello world
```

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) **Try**: Print a × b preceded by the string 
'The value of a×b ='.

**Note**: We can format an object in an f-string using the documentation [here](https://www.python.org/dev/peps/pep-0498/).
A particularly useful formatting option is to print a float with a certain precision with e.g. `{value:.4f}` for 4 dp.

#### c. Lists

Lists in Python are a collection of objects that can be indexed e.g. 

```
>>> first_word = 'hello'
>>> phrase = [first_word, 'world']
>>> print(phrase[0])
hello
```
where our phrase is a list of strings and the square brackets select the element with index 0 (lists are indexed from 0
in Python).

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) **Try**: Assign the sum a+b to a new variable and create a list
of the sum and product. Using the list print the sum and product in the form 'Sum = X, Product = Y'.

