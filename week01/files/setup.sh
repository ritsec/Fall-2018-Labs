#!/bin/bash

# Make ritsec user
useradd ritsec -d /home/ritsec/ -s /bin/bash
echo "ritsec:ritsec" | chpasswd

# Make hard user
useradd hard -d /home/hard/ -s /bin/bash
echo "hard:oopshunter2" | chpasswd

# Set Easy2 flag
useradd -d /usr/hackerman1337/ -s /bin/nologin hackerman1337

# Set Easy1 flag
echo "RS{EASY1_ETC_PA55WD}" >> /etc/passwd

# Set Medium1 flag
mkdir -p '/ /never/gonna/give/you/up/never/gonna/let/you/down/never/going/to/run/around/and/desert/you/why/did/i/type/this/out/'
echo "RS{MED1_5Y5T3M_W1D3_F1ND}" > "/ /never/gonna/give/you/up/never/gonna/let/you/down/never/going/to/run/around/and/desert/you/why/did/i/type/this/out/flag.txt"

# Set Medium2 flag
touch /tmp/2
touch /tmp/3

# Set Hard flag
echo "hard    ALL=(ALL) NOPASSWD: /usr/sbin/visudo" >> /etc/sudoers
