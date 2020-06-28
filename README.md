# automatic_hangman_py
## Description
A program designed to play hangman better than any human and allow a human to play as well

## Usage
If installed on your system, you run it as `automatichangman`
If not installed, run `python3 -m automatichangman` from this git project root directory. 

## Installation
To install without a distro specific package, run `make install` from the project root directory

### Red Hat Package
On Red Hat and Fedora based distros you can install the .rpm package once it is released.

## Packaging
To build a .deb package, first install the package `stdeb` either from apt or pip3. 
Next, run `make deb` from this project root directory.

To build a .rpm package, first install the package `rpmdevtools` from dnf.
Next, run `make rpm` from this project root directory.
