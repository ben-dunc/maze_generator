# Python Maze Generator
This program generates mazes in a square with a given length. It can print them out to stderr or to files.
The only limit to the size of the maze is your computer.
The mazes are generated with [Wilson's algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm).

I created this program to generate environments to train a DeepRL model with.

## Usage

1. Download the program
```bash
git clone https://github.com/ben-dunc/maze_generator.git
```
2. Enter file
```bash
cd maze_generator
```
3. View Usage
```bash
python3 maze_generator.py -h
usage: maze_generator.py [-h] [-f FILE] [-i ITERATIONS] [-p] size

This program generates mazes in a square with a given length. It can print them out to stderr or to files.

positional arguments:
  size                  Size of maze - odd number. If even, 1 will be added.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The base filename to store the mazes to (./output/{filename}). If left empty, the mazes will be outputed to stderr.
  -i ITERATIONS, --iterations ITERATIONS
                        The amount of mazes to generate. If a filename is specified, '_i' will be appended to it, where 'i' is the iteration number,
                        starting with 0.
  -p, --pretty          Pretty output to stderr and files. This just adds a space between characters
```

## Examples

There are many examples in ./output/ as well in 10, 20, and 50 sizes.

### 10x10
```bash
python3 maze_generator.py 10 -i 1 -p
```
```text
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
```
```text
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
```
```text
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
