

def ice_brick_volume(radius, bottle_length, rim_length):
    return int(float(3.14159 * radius ** 2 * (bottle_length - rim_length)))

ice_brick_volume()