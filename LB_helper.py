#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time
from collections import deque
import numpy as np



def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    mazeMatrix = np.zeros((len(maze_map),len(maze_map[0])), dtype=int)
    for i in range(1,len(maze_map)-1):
        for j in range(1,len(maze_map[i])-1):
            if (maze_map[i-1][j] == "s") or (maze_map[i-1][j] == "*") or (
            maze_map[i-1][j] == " "):
                mazeMatrix[i][j] += 1
            #Proofs the field above xy

            if (maze_map[i][j+1] == "s") or (maze_map[i][j+1] == "*") or (
            maze_map[i][j+1] == " "):
                mazeMatrix[i][j] += 2
            #Proofs the field right from xy

            if (maze_map[i+1][j] == "s") or (maze_map[i+1][j] == "*") or (
            maze_map[i+1][j] == " "):
                mazeMatrix[i][j] += 4
            #Proofs the field below xy

            if (maze_map[i][j-1] == "s") or (maze_map[i][j-1] == "*") or (
            maze_map[i][j-1] == " "):
                mazeMatrix[i][j] += 8
            #Proofs the field left from xy

    return mazeMatrix
    #raise NotImplementedError

def findPfad(ziel,start,maze_map):

    #start = tupleB
    #ziel = tupleA
    queue = deque([start])
    walkMatrix = np.zeros((len(maze_map),len(maze_map[0])), dtype=int)
    walkMatrix[start[0]][start[1]] = 1

    mazeMapCopy = maze_map[:]
    tuple = start
    while tuple != ziel:
        mazeTree = maze_map_to_tree(mazeMapCopy)
        tuple = queue.pop()
        queue.appendleft(tuple)
        x = mazeTree[tuple[0]][tuple[1]]
        s = mazeMapCopy[tuple[0]][0:tuple[1]]
        ufree = walkMatrix[(tuple[0]-1)][(tuple[1])] #+1
        rfree = walkMatrix[(tuple[0])][(tuple[1]+1)] #+2
        bfree = walkMatrix[(tuple[0]+1)][(tuple[1])] #+4
        lfree = walkMatrix[(tuple[0])][(tuple[1]-1)] #+8

        if x == 0:
            s += "\u22C5"
        elif x == 1:
            s += "\u2575"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
        elif x == 2:
            s += "\u2576"
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
        elif x == 3:
            s += "\u2514"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
        elif x == 4:
            s += "\u2577"
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
        elif x == 5:
            s += "\u2502"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
        elif x == 6:
            s += "\u250C"
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
        elif x == 7:
            s += "\u251C"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
        elif x == 8:
            s += "\u2574"
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 9:
            s += "\u2518"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 10:
            s += "\u2500"
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 11:
            s += "\u2534"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 12:
            s += "\u2510"
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 13:
            s += "\u2524"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 14:
            s += "\u252C"
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        elif x == 15:
            s += "\u253C"
            if ufree== 0:
                queue.appendleft(((tuple[0]-1),(tuple[1]))) #+1
                walkMatrix[(tuple[0]-1)][(tuple[1])] = 1
            if rfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]+1))) #+2
                walkMatrix[(tuple[0])][(tuple[1]+1)] = 2
            if bfree == 0:
                queue.appendleft(((tuple[0]+1),(tuple[1]))) #+4
                walkMatrix[(tuple[0]+1)][(tuple[1])] = 4
            if lfree == 0:
                queue.appendleft(((tuple[0]),(tuple[1]-1))) #+8
                walkMatrix[(tuple[0])][(tuple[1]-1)] = 8
        s += mazeMapCopy[tuple[0]][(tuple[1]+1)::]
        mazeMapCopy[tuple[0]] = s

    tuple = ziel
    pfad = deque(ziel)
    while tuple != start:
        if walkMatrix[tuple[0]][tuple[1]] == 1:
            pfad.append(((tuple[0]+1),tuple[1]))
            tuple = ((tuple[0]+1),tuple[1])
        elif walkMatrix[tuple[0]][tuple[1]] == 2:
            pfad.append(((tuple[0]),tuple[1]-1))
            tuple = ((tuple[0]),tuple[1]-1)
        elif walkMatrix[tuple[0]][tuple[1]] == 4:
            pfad.append(((tuple[0]-1),tuple[1]))
            tuple = ((tuple[0]-1),tuple[1])
        elif walkMatrix[tuple[0]][tuple[1]] == 8:
            pfad.append(((tuple[0]),tuple[1]+1))
            tuple = ((tuple[0]),tuple[1]+1)
    return pfad

def assign_character_for_nodes(maze_map, current_node, prev_node):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map : [type]
        [description]
    current_node : [type]
        [description]
    prev_node : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """


    raise NotImplementedError


def write_to_file(file_name, path):
    """Function to write output to console and a txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.
    path : [type]
        [description]

    """

    file = open(file_name,"w")
    file.write(str(path))
    file.close()

    return
    #raise NotImplementedError
