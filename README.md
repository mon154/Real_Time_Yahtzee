# Real Time Yahtzee
### Author: Keyanna Duker
## Overview:
### Description: 
I wanted to try dipping into video object detection and algorithm design, so this project will use OpenCV to identify rolled dice and use them in Yahtzee. I want the game to be between a minimum of one player and the computer, where the computer needs to choose whether or not to reroll to get a higher score and how to utilze chance and other boxes in a reasonable amount of time.

## Development Environment
* Microsoft Visual Studio Code
* Python 3.9.0
* OpenCV
* Logitech C615 HD Webcam (However any webcam should be sufficient)

## Useful Websites
* [This site](https://www.davidepesce.com/2019/09/06/dice-reader-part-1/ "Reading dice with OpenCV – Part 1") was essential for writing the OpenCV dice reader. However it is in C++
* [OpenCV Python Docs](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

## Future Work
* Need to fix bug for computer player. Currently once he begins to run out of top boxes to fill, instead of rolling for yahtzee with the most frequent number of dice rolled, he instead always asked to reroll everything except twos which is entertaining but not what I had intended. 
* Need to find a better way for the game to recognize Straights (sometimes it will miss one if there's a repeat number in the list of dice rolls)
* Give players the option to view their available score boxes at the beginning of their turn.
* I would eventually like to implement a GUI so the game is no longer played in the terminal.

