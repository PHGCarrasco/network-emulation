# network-emulation
## Description
A simple and basic aplication that simulate a network on Linux using python

## How it Work
Using an tty no modem C source code, establish a conection with two virtual devices on Linux repositories.

Using an basic serial comunication python code, i can trade messages between those two virtual devices.


## Requirements
This project is built to run in any common distro Linux 
tty0tty C Source code, i used this: https://github.com/freemed/tty0tty
Pyserial library isntalled

## How to run
Build the kernel module from provided source, detailed process on tty0tty README.md
Run tty0tty exec 
  > ./tty0tty/pts/tty0tty
  
