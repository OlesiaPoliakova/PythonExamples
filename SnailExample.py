import math


def get_snail_time(height, up_velocity, down_velocity):
    if up_velocity >= height:
        return 1
    return 1 + math.ceil((height - up_velocity) / (up_velocity - down_velocity))
