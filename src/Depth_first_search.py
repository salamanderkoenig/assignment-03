#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes


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
    queue = deque([("", start)])
    
    # Fill in your DFS algorithm here

    return


if __name__ == '__main__':

    maze_map =[]
    working_directory = os.getcwd()
    file_path = os.path.join(working_directory, 'maps/map2.txt')

    with open(file_path) as f:
        maze_map = f.readlines()

    # CALL THIS FUNCTION after filling in the necessary implementations
    # path = depth_first_search(maze_map, start_pos, goal_pos)
