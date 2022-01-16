level1_map = [
["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", "b", "b", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", "b", " ", " ", " ", " ", " ", " ", "3", " ", "c", " ", " ", " ", " ", " ", " ", " ", "3", " ", "c", " ", " ", " ", " ", " ", " ", " ", "c", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", "b", " ", " ", "b", "b", " ", "b", "b", "b", "b", " ", " ", " ", " ", " ", " ", "b", "b", "b", " ", " ", " ", " ", " ", " ", "b", "b", "b", " ", " ", " ", "b", "b", "b", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "3", " ", "c", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", "p", "c", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", "b", "b", "b", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", "b"], 
["b", " ", "b", "b", "b", "b", " ", " ", " ", " ", " ", " ", "c", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", "c", " ", "b", "b", "b", "b", " ", " ", " ", " ", "b", "b", "b", "b", "c", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", "b", " ", "c", "b"], 
["b", "c", " ", " ", " ", " ", " ", " ", "b", "b", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", "c", " ", " ", " ", " ", " ", " ", "b", "b"], 
["b", "b", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", "b", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", "b", "b", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", "b", "b", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "b"], 
["b", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "b"], 
["b", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "b"]
]

# b -> Normal metal block (collidable, acts as ground and walls)
# l -> Lava, kills player instantly
# c -> coin (collectable)
# 2 -> small enemy (moves 2 blocks to the right from initial position including spawnblock)
# 3 -> big enemy (moves 3 blocks ----)