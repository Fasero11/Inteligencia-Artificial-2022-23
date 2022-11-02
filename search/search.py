# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from argparse import Action
from tokenize import ContStr
from turtle import st
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    actions = [] # List of actions Pac-Man will perform.
    explored = [] # List of explored nodes. (So they aren't expanded again).
    frontier = util.Stack() # LIFO queue of frontier nodes.

    # Each element in frontier has two attributes: (cost not included).
    # State: (X,Y). Node coordinates.
    # Actions: Array of all the previous actions needed to reach the State.
    start_state = problem.getStartState()
    start_node = (start_state, actions)
    frontier.push(start_node) # Add first node to the frontier
    
    while not frontier.isEmpty():
        current_state, actions = frontier.pop() # Expand node

        if current_state not in explored:
            explored.append(current_state) 

            if problem.isGoalState(current_state):
                #print("Actions: ",actions,'\n')
                break
            
            successors = problem.getSuccessors(current_state)
            # Each successor has three attributes: State, Action and Cost.
            # Example: ((5,5), 'South', 1) (Cost not used)
            for successor_state, successor_action, successor_cost in successors:
                # Add latest action to the list of actions.
                new_actions = actions + [successor_action] 
                successor_node = (successor_state, new_actions)
                frontier.push(successor_node) # Add successor to frontier

    return actions
    util.raiseNotDefined()    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = [] # List of actions Pac-Man will perform.
    explored = [] # List of explored nodes. (So they aren't expanded again).
    frontier = util.Queue() # FIFO queue of frontier nodes.

    # Each element in frontier has two attributes: (cost not included).
    # State: (X,Y). Node coordinates.
    # Actions: Array of all the previous actions needed to reach the State.
    start_state = problem.getStartState()
    start_node = (start_state, actions)
    frontier.push(start_node) # Add first node to the frontier
    
    while not frontier.isEmpty():
        current_state, actions = frontier.pop() # Expand node

        if current_state not in explored:
            explored.append(current_state) 

            if problem.isGoalState(current_state):
                #print("Actions: ",actions,'\n')
                break
            
            successors = problem.getSuccessors(current_state)
            # Each successor has three attributes: State, Action and Cost.
            # Example: ((5,5), 'South', 1) (Cost not used)
            for successor_state, successor_action, successor_cost in successors:
                # Add latest action to the list of actions.
                new_actions = actions + [successor_action]
                successor_node = (successor_state, new_actions)
                frontier.push(successor_node) # Add successor to frontier

    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    actions = [] # List of actions Pac-Man will perform.
    explored = [] # List of explored nodes. (So they aren't expanded again).
    frontier = util.PriorityQueue() # Priority queue of frontier nodes.

    total_cost = 0

    # Each element in frontier has three attributes:
    # State: (X,Y). Node coordinates.
    # Actions: Array of all the previous actions needed to reach the State.
    # Cost: n. the cost of reaching this State
    start_state = problem.getStartState()
    start_node = (start_state, actions, total_cost)
    frontier.push(start_node, total_cost) # Add first node to the frontier
    
    while not frontier.isEmpty():
        current_state, actions, current_cost = frontier.pop() # Expand node

        if current_state not in explored:
            explored.append(current_state) 

            if problem.isGoalState(current_state):
                #print("Actions: ",actions,'\n')
                break
            
            successors = problem.getSuccessors(current_state)
            # Each successor has three attributes: State, Action and Cost.
            # Example: ((5,5), 'South', 1)
            for successor_state, successor_action, successor_cost in successors:
                # Add latest action to the list of actions.
                new_actions = actions + [successor_action]
                total_cost = problem.getCostOfActions(new_actions)
                successor_node = (successor_state, new_actions, total_cost)
                frontier.push(successor_node, total_cost) # Add successor to frontier

    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Takes into account both the total cost of the previous actions and the heuristic
    actions = [] # List of actions Pac-Man will perform.
    explored = [] # List of explored nodes. (So they aren't expanded again).
    frontier = util.PriorityQueue() # Priority queue of frontier nodes.

    total_cost = 0

    start_state = problem.getStartState()
    start_node = (start_state, actions)
    start_cost = nullHeuristic(start_state, problem)
    frontier.push(start_node, start_cost) # Add first node to the frontier
    
    while not frontier.isEmpty():
        current_state, actions = frontier.pop() # Expand node

        if current_state not in explored:
            explored.append(current_state) 

            if problem.isGoalState(current_state):
                #print("Actions: ",actions,'\n')
                break
            
            successors = problem.getSuccessors(current_state)
            # Each successor has three attributes: State, Action and Cost.
            # Example: ((5,5), 'South', 1)
            for successor_state, successor_action, successor_cost in successors:
                # Add latest action to the list of actions.
                new_actions = actions + [successor_action]
                total_cost = problem.getCostOfActions(new_actions) + heuristic(successor_state, problem)
                successor_node = (successor_state, new_actions)
                frontier.push(successor_node, total_cost) # Add successor to frontier

    return actions
    util.raiseNotDefined()
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
