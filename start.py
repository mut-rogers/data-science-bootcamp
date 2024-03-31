
from typing import List



def create_users() -> List:
    """
    Creates and returns a dict of users
    """
    names: List = ["Hero", "Dunn", "Sue", "Chir", "Thor", "Cliff", "Hicks", "Devin", "Kate", "Klein"]

    users: List = list()

    for name in enumerate(names):
        output: dict = {
            "id": name[0],
            "name": name[1]
        }
        users.append(output)
    return users

######
from matplotlib import pyplot as plt 
from typing import List


movies: List = ["Criminal Code", "Blacklist", "Prison Break", "Money Heist", "Game of Thrones"]
num_oscars: List = [2, 8, 11, 6, 4] 

plt.bar(
    movies,
    num_oscars,
    edgecolor=(0,0,0),
    align="edge",
    width=0.8
)

# plt.ylabel("# of Oscars")
# plt.xlabel("Movies")
# plt.xticks(
#     minor=True,
#     ticks=[0.1 * i for i in range(11)]
# )
# plt.title("Distribution of Oscar Awards Accross Popular Movies")
# #plt.axis([0,20,0,12])
# plt.show()


Vector = List[float]

def add_vector(v: Vector, w: Vector) -> Vector: 
    """Adds two Vectors"""
    return [v_i + w_i for v_i, w_i in zip(v, w)] if len(v) == len(w) else []

def sub_vector(v: Vector, w: Vector) -> Vector:
    """Substracts two Vectors"""
    return [v_i + w_i for v_i, w_i in zip(v, w)] if len(v) == len(w) else []

def sum_vector(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements of the Vectors"""
    

result = add_vector([2,3], [4,4, 7])
print(result)

# Imports 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation

TWOPI = 2*np.pi 

fig, ax = plt.subplots()
t = np.arange(0.0, TWOPI, 0.001)
s = np.sin(t)
i = plt.plot(t, s)

ax = plt.axis([0, TWOPI, -1, 1])

redDot, = plt.plot([0], [np.sin(i)], 'ro')

def animate(i): 
    redDot.set_data(i, np.sin(i))
    return redDot

# Now creating animations 
myAnimation = animation.FuncAnimation(
    fig,
    animate,
    frames = np.arange(0.0, TWOPI, 0.1),
    interval=10,
    blit=True,
    repeat=True
)

plt.show()