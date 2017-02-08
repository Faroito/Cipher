# Cipher

## Description

I did this project in the Mathematics module. The goal was to crypt a message with a key by making two distinct matrix with the ASCII charactere and multiply the matrix. Then we had to decrypt the matrix with the inverse matrix of the key.

As the goal was to manipulate matrix, we couldn't use matrix's library as numpy, it would has be to easy !

As a bonus of this project I did a brute force attack of the message (2*2 matrix). Like this could be long I did a socket server/client to use many computer to duplicate computing power.

So when we pitch this project for the school, we invited 16 student to break a message ! :)

## How to use

To crypt a message : ./cipher 0 "message" "key"

To decrypt a message : ./cipher 1 "23884 11009 26220 11615 22842 9797 10807 10201" "key"

To break a message :
   - server : ./cipher 2 "23884 11009 26220 11615 22842 9797 10807 10201"
   - client : ./client.py

*Tips : "23884 11009 26220 11615 22842 9797 10807 10201" is a encrypt message*