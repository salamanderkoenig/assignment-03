#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
from collections import deque
import numpy as np
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes,findPfad


def depth_first_search(maze_map, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [type]
        [description]
    start_pos : [type]
        [description]
    goal_pos : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """


    start = start_pos[0]
    goal = goal_pos
    queue = deque([start])

    # Fill in your DFS algorithm here
    completePfad = deque()
    smallPfad = deque()
    expMatrix = np.zeros((len(maze_map),len(maze_map[0])), dtype=int)
    expMatrix[start[0]][start[1]] = 1

    # the expMatrix saves the fiels, which are still given in the queue
    # in smallPfad the fields which the robot has to visid get saved

    mazeMapCopy = maze_map[:]
    try:
        while goal_pos > 0:
            # the while-loop runs until every goal was found

            mazeTree = maze_map_to_tree(mazeMapCopy)

            # mazeTree is a matrix which includes for every field a number,
            # which discribes which field is reachable

            tuple = queue.pop()
            smallPfad.append(tuple)
            print(mazeMapCopy)
            x = mazeTree[tuple[0]][tuple[1]]
            s = mazeMapCopy[tuple[0]][0:tuple[1]]
            ufree = expMatrix[(tuple[0]-1)][(tuple[1])] #+1
            rfree = expMatrix[(tuple[0])][(tuple[1]+1)] #+2
            bfree = expMatrix[(tuple[0]+1)][(tuple[1])] #+4
            lfree = expMatrix[(tuple[0])][(tuple[1]-1)] #+8

            if mazeMapCopy[tuple[0]][tuple[1]] == "*":
                goal_pos -= 1

            # in the following part the maze_map get a update in respect to the search-engine

            if x == 0:
                s += "\u22C5"
            elif x == 1:
                s += "\u2575"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
            elif x == 2:
                s += "\u2576"
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
            elif x == 3:
                s += "\u2514"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
            elif x == 4:
                s += "\u2577"
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
            elif x == 5:
                s += "\u2502"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
            elif x == 6:
                s += "\u250C"
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
            elif x == 7:
                s += "\u251C"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
            elif x == 8:
                s += "\u2574"
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 9:
                s += "\u2518"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 10:
                s += "\u2500"
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 11:
                s += "\u2534"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 12:
                s += "\u2510"
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 13:
                s += "\u2524"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 14:
                s += "\u252C"
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            elif x == 15:
                s += "\u253C"
                if ufree== 0:
                    queue.append(((tuple[0]-1),(tuple[1]))) #+1
                    expMatrix[(tuple[0]-1)][(tuple[1])] = 1
                if rfree == 0:
                    queue.append(((tuple[0]),(tuple[1]+1))) #+2
                    expMatrix[(tuple[0])][(tuple[1]+1)] = 1
                if bfree == 0:
                    queue.append(((tuple[0]+1),(tuple[1]))) #+4
                    expMatrix[(tuple[0]+1)][(tuple[1])] = 1
                if lfree == 0:
                    queue.append(((tuple[0]),(tuple[1]-1))) #+8
                    expMatrix[(tuple[0])][(tuple[1]-1)] = 1
            s += mazeMapCopy[tuple[0]][(tuple[1]+1)::]
            mazeMapCopy[tuple[0]] = s
    except IndexError:
        print("The Robot scanned the complete reachable area.")
        print("Some goals are outside the territorium of the robot.")

    print("The programm is calculating the way of the robot")

    #in this Part the programm recunstruct from smallPfad the real pfad of the robot
    tupleA = smallPfad.pop()
    completePfad.append(tupleA)
    while smallPfad:
        tupleB = smallPfad.pop()
        summe = (tupleA[0]-tupleB[0])*(tupleA[0]-tupleB[0]) + (tupleA[1]-
        tupleB[1])*(tupleA[1]-tupleB[1])
        if summe > 1:
            #findPfad calculate the route of the robot from A to B
            pfadAB = findPfad(tupleA,tupleB,maze_map)
            while pfadAB:
                completePfad.append(pfadAB.popleft())
        else:
            completePfad.append(tupleB)
        tupleA = tupleB
    return completePfad

    print(mazeMapCopy)
    return completePfad


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    # CALL THIS FUNCTIONS after filling in the necessary implementations
    start_pos_map1 = [(1,3)]
    start_pos_map2 = [(1,4)]
    start_pos_map3 = [(10,67)]
    goal_pos_map1 = 4
    goal_pos_map2 = 10
    goal_pos_map3 = 14

    path_map1 = depth_first_search(maze_map_map1, start_pos_map1, goal_pos_map1)
    write_to_file("dfs_map1", path_map1)

    path_map2 = depth_first_search(maze_map_map2, start_pos_map2, goal_pos_map2)
    write_to_file("dfs_map2", path_map2)

    path_map3 = depth_first_search(maze_map_map3, start_pos_map3, goal_pos_map3)
    write_to_file("dfs_map3", path_map3)
