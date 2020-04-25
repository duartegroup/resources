# Unix CLI

Computational chemistry requires a knowledge of command line interfaces 
([CLI](https://en.wikipedia.org/wiki/Command-line_interface)). Interacting with CLI only programs (most DFT/ab initio
software packages), using high performance computing resources and scripting common actions all require using a CLI.

This introduction should provides a very brief guide to using a CLI in  a Unix environment, specifically
[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) which is perhaps the most commonly used shell. Non-Unix
shells like [Windows PowerShell](https://en.wikipedia.org/wiki/PowerShell) work in much the same way, but as most
compute clusters are generally Linux-based we'll stick to bash.

**Note:** In Windows 10 a bash shell can be obtained by installing a Ubuntu subsystem as 
[here](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 

### Some Basic Commands

Opening up terminal in Mac OS or Linux will give you a window where you can type commands, providing a more primitive,
non-graphical way to interact with your computer. Some essential commands are:

```bash
ls
```
typing `ls` in the command line and hitting enter will _list_ all the current files and folders in the current folder
(also referred to as a directory). As an aside, Unix is case-sensitive so `Ls` won't give the same result. `ls` can also
take an argument of a path, for example `ls /` will list the contents of the root directory.

```bash
mkdir
```
_makes_ a _directory_ and takes one argument, the name of the directory you want to create. For example typing `mkdir tmp`
and hitting enter will make a directory called `tmp`; confirm it exists using `ls`.

```bash
cd
```
short for _change directory_ does exactly what you'd expect e.g. `cd tmp` will change directories to the just created
directory and running `ls` will give no output for this newly created empty folder. Changing directories
to one level up using `cd ..` should leave you in the same folder you started in.

```bash
rm
```
short for _remove_ is like right clicking on a file → Move to Trash, but more destructive. It will not, by default, move
files to an easily recoverable location like the Trash. Again, `rm` takes at least one argument of the file(s) or folder(s) 
to delete, however, `rm` won't remove directories without the `-r` recursive flag. To remove the empty directory: `rm -r tmp`

**Additional Hints**: Hitting Tab at any point as you're typing a command will autocomplete the command or path if there 
is only a single option. Hitting Tab twice in quick secession will give you all the available autocomplete options. 
`~` is short for your home directory (e.g. `ls ~` will list the contents of your home folder) while `*` is a wildcard 
(e.g. `ls ~/*.txt` will list all the files that end in .txt in the your home directory).  



![#1589F0](https://placehold.it/15/1589F0/000000?text=+) **Try**: Make a folder called 'test', change directories into it,
confirm that it's empty, change directories to one level up and delete the directory.

### More Complex Commands and vi

Moving around the directory tree creating folders and removing things is all well and good but we'll want to be able 
to make files, search, copy and move them. There are lots of command line text editors including 
[nano](https://en.wikipedia.org/wiki/GNU_nano), [emacs](https://en.wikipedia.org/wiki/Emacs) and 
[vi](https://en.wikipedia.org/wiki/Vi) with each choice being personal preference. Here we'll use vi as for making and
editing files.

```bash
vi
```
Running `vi test.txt` will make and open a test.txt text file. vi is powerful, but also probably unfamiliar. Using vi 
requires a few key commands: (1) `i` for _insert_ will allow you to enter text, (2) the escape key to exit
_insert_ mode, (3) `:wq` to write the file and quit vi, (4) `:u` undo, (5) `yy` to copy a line of text, (6) `p` to 
paste the _yanked_ lines, (7) `dd` to delete the current line. Both `yy` and `dd` can be preceded by a number, to copy
and delete a specified number of lines respectively. 

Quitting vi with `:wq` will return you to the command line and `ls` should show the just created 'test.txt' file. To 
copy this file use  

```bash
cp
```
short for _copy_ it takes two arguments, the source and destination. Running `cp test.txt test2.txt` will clone the 
file and make a new file called 'test2.txt'. To move rather than copy the file use
```bash
mv
```
in the same way as copy. Move the file to your home directory with `mv test2.txt ~/test2.txt`. Move also functions as
rename, if the destination is the same directory as the source file e.g. `mv test.txt test2.txt` will rename 
'test.txt' to 'test2.txt'. To remove both of the test files in the same command run `rm test2.txt ~/test2.txt`.

Searching files in the command line can be achieved with 

```bash
grep
```
or within vi. Make a new test file with `vi hello.txt`, insert 'hello' and quit out of vi. Running `grep 'hello' *` will
search all the files in the current directory for the word (also called a string) 'hello' and will return a list of where
it appears (hopefully in hello.txt!). To search a specific file use the `?` command in vi. For example, open hello.txt type
`?hello` and hit enter to search the file for that string, which will return a single instance. If there are multiple
instances you can use `n` to go to the next instance in the file.


![#1589F0](https://placehold.it/15/1589F0/000000?text=+) **Try**: Make an empty file called 'file.txt', change 
rename it to 'test.txt', edit the file to include the string 'hello', copy the file to 'test2.txt' and use grep
to find all the instances of 'hello' in the current directory then remove both of the files.


### Environment Variables and Useful tips 

Environment variables in bash are strings or lists that set the current shell environment. For example, the 0 environment
variable is the shell that is being used currently. Use 
```bash
echo
```
to show the 0 variable with `echo $0` and will probably print /bin/bash if you're using bash. Other useful environment
variables are 'PATH', 'LD_LIBRARY_PATH' and 'OMP_NUM_THREADS'. Running `echo $PATH` will show a colon separated list 
of the folders that bash is going to search for executable files. Adding folders to your PATH is useful if, for example,
you want to make a script executable from so it can be used from any folder. To make a script executable you will need
to first change the access permissions using 

```bash
chmod
```
with `chmod +x /path/to/your/script.py` and then add the folder to your PATH with `export PATH=/path/to/your/:$PATH`.
Note the ':$PATH' suffix is very important; without it `ls` and other core commands won't be available! (Opening a new
shell fixes this). However, when you close your current shell and open another the script will no longer be in your
'PATH'. To make the script available every time you open a terminal window you'll want to add the line
'export PATH=/path/to/your/:$PATH' to the end of your ~/.bash_profile file on Mac OS or ~/.bashrc file on Linux. You may
want to keep all your executable scripts in a dedicated folder; I use ~/.local/bin. 

The 'OMP_NUM_THREADS' environment variable is used in many computational chemistry packages to set the number of cores
(specifically number [OMP](https://www.open-mpi.org/) threads) that the code will use.

To run multiple commands in one line can be achieved by concatenating with '&&' e.g. `echo hello && sleep 2` will print
'hello' to the terminal and then sleep for 2 seconds. Bash one line for loops are very useful to perform actions on 
multiple files, and have the general structure

```bash
for iterable; do command $var; done
```
For example, `for i in {1..10}; do echo $i; done` will print the integers from 1 to 10, while 
`for item in *; do echo $item && sleep 5; done` will list all the files and folders in the current directory in 
intervals of 5 seconds. To quit this (or any undesired) currently running process hit Ctrl+c. 

Finally, a couple of useful shortcuts to go to the start and end of a line are Ctrl+a adn Ctrl+e respectively.

