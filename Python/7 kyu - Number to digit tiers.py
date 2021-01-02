def create_array_of_tiers(n):
    return [str(n)[slice(x+1)] for x in range(len(str(n)))]

### or i could use [:i] for slicing