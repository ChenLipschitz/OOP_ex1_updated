# OOP_Ex1

This project implements a smart elevator's, offline algorithm.

## **The Algorithm:**

The algorithm gets 2 files:
* file with the building's attributes
* file with the call's attributes
this algorithm is offline, which means all the details and parameters are given in advanced.
the algorithm allocates an elevator which travels to the source-floor's-call in the shortest time possible given the following conditions:
if there are several elevators in level-mode and have no calls the algorithm will assign the elevator which will arrive in the shortest time.
if there is no such elevator the algorithm will search for an elevator which is traveling in the same direction as the call's-type (up/down).
in addition the source floor and destination floor must be within the maximum/minimum set range parameters (ex: elevator A is from floor 21 to 35 only).
Out of the above conditions we will select the elevator that will reach it's source-call destination in the shortest time possible.

## **Literature review:**
* https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
* https://www.diva-portal.org/smash/get/diva2:668671/fulltext01.pdf
* https://www.researchgate.net/publication/331475872_Smart_Building's_Elevator_with_Intelligent_Control_Algorithm_based_on_Bayesian_Networks

The articles above inspired us and provided all the required information about elevators and its algorithm for this project.
