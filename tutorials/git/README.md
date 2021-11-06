# git Tutorial

### Outline

The goal of this tutorial is to become familiar with some (of the vast) **git** functionality. It will cover the basics 
of version controlling and contributing to projects on GitHub. 

### Prerequisites

#### git + Python

This tutorial will require a familiarity with shells e.g. bash, and both a git & Python installs. See below to install 


|          |     Mac   |  Windows    |   Linux   |
|  :----:  |  :----:  |    :----:    |    :----: |
| git      |    n/a      |     Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/)         |     n/a      | 
| Python   |  `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && bash miniconda.sh`      |     Within WSL: `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && bash miniconda.sh`         |    `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh && bash miniconda.sh`    |

#### Python dependencies

Once Python is installed, add a couple of common Python packages (if they're not already installed)

```bash
conda install numpy matplotlib -c conda-forge
```

#### GitKraken

To interact with `git` using a graphical user interface (GUI) we'll be using GitKraken - download it [here](https://www.gitkraken.com/)
and sign in with your GitHub account.


### git by Example

The goal with this example will be to work together to solve a toy _research_ problem. Specifically, for a set of data 
points, what is the best fitting function? The true function and sample points (squares) are shown below.

![alt text](_common/true_function.png)


The sample points are:

```python
xs = [ 0.21121121, -0.4034034,  0.39139139, 0.78578579, -0.55155155, 0.56556557, 0.92392392, -0.6996997, 0.95795796, -0.91591592]
ys = [ 0.23533653, -0.31035679, 0.45911638, 0.31506996, -0.29502177, 0.60401143, -0.50146046, -0.04222024, -0.82460688, 1.27242725]
```

#### 0. Forking

To get started **fork** this repository, aka. create a copy ('clone') of it that is now associated with your GitHub 
account. On this page hit the `Fork` button in the top right and fork it to your account.

It's on this copy that changes will be made that can then be added to the [base repository](https://github.com/duartegroup/resources).

#### 1. Cloning

With GitKraken installed there are two ways to clone a repository either on the command line:

```bash
git clone https://github.com/duartegroup/resources.git
```

or through the GitKraken GUI with Clone → GitHub.com → Select appropriate repository → Clone the repo! 

#### 2. Making Changes

Finally, we're now ready to make some progress in solving the toy problem. Open up `fit_function.py` with your favourite 
text editor or IDE. Modify the trial function declaration to try and minimise the difference between your guess and 
the true values, subject to some simple regularisation. The 




