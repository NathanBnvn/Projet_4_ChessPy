# ChessPy
![code-in-python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python) ![flake-8](https://img.shields.io/badge/Styled%20with-Flake8-blueviolet?style=for-the-badge) ![mvc](https://img.shields.io/badge/MVC-Conception-black?style=for-the-badge) ![tiny-database](https://img.shields.io/badge/storing%20with-tinyDB-informational?style=for-the-badge)
![openclassrooms-project](https://user-images.githubusercontent.com/45998296/166692502-a22abdc0-e774-4ec6-8d7c-f86cb6e55825.svg)

![](https://images.unsplash.com/photo-1528819622765-d6bcf132f793?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80)
_Photo by Felix Mittermeier on Unsplash_

### Introduction
ChessPy is a chess tournament management program. 
With this project, you can create tournament, players and generate reports of registered tournaments, rounds, matchs and players
This project has been realised with python, according to the MVC structure and tinyDB. 
This program works in the terminal


### Download

To get the project from github
```bash
  git clone https://github.com/NathanBnvn/Projet_4_ChessPy.git

```


### Setup

First of all, you will need to create a virtual environement like so :

**on Mac or Linux**

```sh

$ python3 -m venv venv

```

once it's done, activate it

```sh

$ source venv/bin/activate

```


**on Windows**

```sh

$ py -m venv env

```

once it's done, activate it

```sh

$ .\env\Scripts\activate

```


### Usage

To launch the program :

```sh

$ python main.py

```

Then you can follow the different instructions in the menus

During an action, you can interrupt the process by typing in prompt command: 

```sh

$ quit

```



### PEP5 & Flake 8

This project respect PEP5 conventions and use flake8, so you can generate a HTML report with this command:

```sh

$ flake8 --format=html --htmldir=flake-report

```