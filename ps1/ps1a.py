###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Parameters:
    filename - the name of the data file as a string
    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    
    with open(filename) as f:
        for line in f:
            entry = line.strip()
            entry = entry.split(sep=',')
            cows[entry[0]] = int(entry[1])
    return cows

# Problem 2

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    selected_cows = []
    cows_copy = cows.copy()
    
    while cows_copy:
        trip = []
        rem_space = limit
        for cow in cows:
            if cows.get(cow) <= rem_space and cow not in selected_cows:
                trip.append(cow)
                selected_cows.append(cow)
                rem_space -= cows_copy.pop(cow)
        trips.append(trip)
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    partitions = get_partitions(cows.keys())
    less_trips = 0
    best_trip = None
    valid_trips = []
    
    for partition in partitions:
        weights_in_each_trip = []
        for combination in partition:
            weights = [cows.get(name) for name in combination]
            weights_in_each_trip.append(sum(weights))
        if max(weights_in_each_trip) < limit:
            valid_trips.append((partition, weights_in_each_trip))
#    with_less_trips = [trip[0] for trip in valid_trips]
    for trips in valid_trips:
        print(trips)

c = {"Jesse":6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(brute_force_cow_transport(c))
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
