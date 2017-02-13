# Cipher

## Description

I did this project as part of a Mathematics module. The goal was to crypt a message with a key.
I made two distinct matrix, one with the message and one with the key. The characters were ASCII. To encrypt I multiplied the matrix. I could decrypt the matrix with the inverse matrix of the key.

As the goal was to manipulate matrix on our own, we were not allowed use matrix's library as numpy, it would have been too easy !

As a bonus for this project, I did a brute force attack of the message (2*2 matrix). 
As the calculation could last long, I got the idea to use a socket server/client to use many computer to duplicate computing power.

So when we pitched this project for the school, 16 students took part of the experience to break one single message in less than one minute ! :)

## How to use

To crypt a message : ./cipher 0 "message" "key"

To decrypt a message : ./cipher 1 "23884 11009 26220 11615 22842 9797 10807 10201" "key"

To break a message :
   - server : ./cipher 2 "23884 11009 26220 11615 22842 9797 10807 10201"
   - client : ./client.py

*Tips : "23884 11009 26220 11615 22842 9797 10807 10201" is a encrypted message*