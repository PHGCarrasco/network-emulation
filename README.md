# network-emulation

## Description
A simple and basic aplication that simulate a network on Linux using python

## How it Work
Using an tty no modem C source code, establish a conection with two virtual devices on Linux repositories.

Using an basic serial comunication python code, i can trade messages between those two virtual devices.


## Requirements
This project is built to run on any distro Linux 

[tty0tty Source code](https://github.com/freemed/tty0tty)

[Pyserial library](https://pypi.org/project/pyserial/) 

## How to run
Build the kernel module from provided source, detailed process on tty0tty [README.md](https://github.com/freemed/tty0tty/blob/master/README.md)

Run tty0tty exec 
  > ./tty0tty/pts/tty0tty
  
You should see wich serail ports are open

![Serial Ports](https://i.imgur.com/2b3o85T.png)
  
 You need to modify both codes with each port
 
 In different terminal sections, compile *first* rx.py and then tx.py
```
 python rx.py
 python tx.py
 ```
 
 ![network](https://i.imgur.com/c42dK8m.png)
