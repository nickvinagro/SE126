# function to pass in # of people and maximum capacity of a room. Returns over/under on capacity.
def difference(people: int, max_cap: int) -> int:
    return max_cap - people

# Example: If under capacity, there is room for extra attendees
# Example: If over capacity, there is no room for extra attendees and some need to be removed