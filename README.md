# maze_generator
This program generates mazes in a square with a given length. It can print them out to stderr or to files.
The only limit to the size of the maze is your computer.
The mazes are generated with Wilson's algorithm: [https://en.wikipedia.org/wiki/Maze_generation_algorithm]

## Examples
### 10x10
```bash
python3 maze_generator.py 10 -i 1 -p

# # # # # # # # # # # 
#   #           #   # 
#   # # #   # # #   # 
#           #       # 
# # #   # # #   #   # 
#   #           #   # 
#   #   #   # # # # # 
#   #   #   #       # 
#   #   #   # # #   # 
#       #           # 
# # # # # # # # # # # 
```

### 20x20
```bash
python3 maze_generator.py 20 -i 1 -p

# # # # # # # # # # # # # # # # # # # # # 
#       #   #                   #       # 
# # #   #   #   #   #   # # # # # # #   # 
#   #       #   #   #           #       # 
#   #   # # #   # # #   # # #   # # #   # 
#               #   #       #           # 
#   # # # # # # #   # # #   #   #   # # # 
#           #       #       #   #   #   # 
#   # # # # # # #   #   # # # # #   #   # 
#           #   #           #       #   # 
#   # # #   #   # # #   # # #   # # #   # 
#   #   #           #       #   #       # 
#   #   # # # # #   #   # # #   # # #   # 
#       #   #       #   #           #   # 
#   # # #   #   # # #   #   # # #   #   # 
#           #       #   #   #   #       # 
#   # # # # #   #   #   # # #   # # #   # 
#           #   #   #   #       #   #   # 
#   # # #   # # #   # # # # #   #   #   # 
#       #   #                       #   # 
# # # # # # # # # # # # # # # # # # # # # 
```

50x50
```bash
python3 maze_generator.py 50 -i 1 -p

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#           #   #   #               #           #   #           #                   #               # 
#   # # #   #   #   # # # # #   #   #   # # #   #   # # #   # # #   # # #   # # #   # # # # #   #   # 
#   #           #   #   #       #       #               #               #       #   #           #   # 
#   # # # # #   #   #   #   # # #   # # # # # # # # #   #   #   # # #   #   #   #   #   # # # # #   # 
#   #       #           #       #   #   #                   #   #   #   #   #   #   #   #           # 
# # # # #   # # #   # # # # #   # # #   #   # # # # # # # # #   #   # # #   #   # # #   # # # # #   # 
#                               #       #   #   #       #       #       #   #           #   #   #   # 
#   #   # # # # #   # # # # #   #   #   # # #   # # #   # # # # #   #   #   # # # # # # #   #   #   # 
#   #   #       #       #   #       #           #           #   #   #               #   #   #       # 
#   #   # # #   #   #   #   # # #   # # #   #   #   # # #   #   # # # # # # # # #   #   #   # # #   # 
#   #       #       #       #           #   #           #   #   #       #   #               #       # 
#   # # # # # # # # #   #   # # #   #   #   # # # # #   #   #   #   #   #   #   #   #   # # # # # # # 
#   #   #   #           #       #   #   #       #       #           #   #       #   #       #       # 
#   #   #   # # # # #   #   # # # # # # # # #   # # #   #   # # #   #   #   # # # # #   #   #   #   # 
#       #   #   #       #       #               #       #       #   #   #   #       #   #   #   #   # 
#   #   #   #   # # # # # # # # #   #   #   # # #   # # #   # # #   #   # # # # #   # # #   #   #   # 
#   #               #   #       #   #   #       #   #       #       #   #   #                   #   # 
# # #   # # # # # # #   #   #   #   # # #   # # # # #   # # # # # # #   #   # # #   # # # # # # # # # 
#   #               #       #           #           #   #   #       #       #       #               # 
#   # # #   #   #   # # # # # # # # #   #   # # #   # # #   # # #   # # # # #   # # # # #   #   #   # 
#           #   #               #       #   #       #       #               #   #       #   #   #   # 
# # #   # # # # #   # # # # # # #   # # #   #   # # # # #   # # # # #   #   # # #   # # #   # # # # # 
#       #           #           #   #   #   #                   #       #   #   #   #           #   # 
# # #   # # # # #   #   # # #   #   #   # # # # # # # # #   # # #   #   #   #   #   #   #   #   #   # 
#               #   #       #   #       #                       #   #   #   #   #       #   #   #   # 
#   # # # # # # # # # # #   #   # # # # #   #   # # #   #   # # #   #   # # #   # # #   # # #   #   # 
#       #   #               #   #       #   #   #   #   #   #       #       #               #       # 
#   # # #   # # # # #   #   # # #   # # # # #   #   #   #   #   # # #   # # # # #   # # #   #   #   # 
#                       #   #               #       #   #   #   #       #           #       #   #   # 
#   # # #   #   # # #   #   # # #   # # # # # # #   # # #   #   # # #   #   # # #   # # # # #   #   # 
#   #       #   #       #   #           #       #   #   #           #       #           #   #   #   # 
# # #   # # # # # # # # # # #   # # # # #   # # #   #   #   # # # # #   #   # # #   #   #   #   #   # 
#   #           #       #   #           #       #   #           #       #   #   #   #   #   #   #   # 
#   #   # # # # #   # # #   # # # # #   # # #   # # # # #   # # # # #   # # #   #   # # #   # # # # # 
#                       #           #               #   #       #           #               #       # 
#   # # # # # # # # # # #   # # # # # # #   # # #   #   # # # # #   #   # # # # #   #   # # #   # # # 
#           #                   #               #       #   #       #   #           #   #           # 
#   #   #   #   #   # # # # #   #   # # # # # # # # # # #   # # # # #   #   #   # # #   # # #   #   # 
#   #   #       #   #           #       #   #       #       #   #       #   #   #   #   #       #   # 
#   # # # # #   # # #   # # # # # # #   #   #   #   #   #   #   # # # # #   # # #   # # # # #   # # # 
#   #       #   #               #   #   #       #       #       #       #       #   #           #   # 
#   #   #   # # # # # # # # # # #   #   #   # # #   #   # # #   #   #   #   #   #   # # # # #   #   # 
#   #   #       #           #               #       #       #       #       #           #   #       # 
#   # # #   #   #   # # #   # # #   # # #   #   # # # # #   # # # # # # # # # # #   # # #   #   # # # 
#           #   #       #       #       #   #   #   #       #           #       #                   # 
#   # # # # #   #   # # # # #   #   # # #   # # #   # # #   # # # # #   #   # # # # # # # # # # #   # 
#   #       #   #       #   #       #       #           #   #                   #                   # 
#   #   #   #   # # #   #   # # # # # # #   # # #   #   # # #   # # # # # # #   # # # # #   # # # # # 
#   #   #       #       #                           #   #               #                           # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
```
