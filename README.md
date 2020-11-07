# automatic_hangman_py
## Description
A program designed to play hangman better than any human and allow a human to play as well

## Usage
If installed on your system, you run it as `automatichangman`
If not installed, run `python3 -m automatichangman` from this git project root directory. 

## Installation
To install without a distro specific package, run `make install` from the project root directory

### Debian Package
You can install it from my [PPA](https://launchpad.net/~corruptedark/+archive/ubuntu/ppa).

#### On Ubuntu 20.04+ based distros 
To add the repository to your system, run:
```
sudo add-apt-repository ppa:corruptedark/ppa
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-automatichangman`

#### On Debian Buster
First install `software-properties-common`
	
Then to add the repository to your system, run:
```
sudo sh -c 'echo "deb http://ppa.launchpad.net/corruptedark/ppa/ubuntu groovy main\ndeb-src http://ppa.launchpad.net/corruptedark/ppa/ubuntu groovy main" > /etc/apt/sources.list.d/corruptedark.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E2BA18922C0D6991
sudo apt update
```
After adding the repository, install the package with: 

`sudo apt install python3-automatichangman`

### Red Hat Package
On Red Hat and Fedora based distros you can install the .rpm package once it is released.

## Packaging
To build a .deb package, first install the package `stdeb` either from apt or pip3. 
Next, run `make deb` from this project root directory.

To build a .rpm package, first install the package `rpmdevtools` from dnf.
Next, run `make rpm` from this project root directory.
