import os
import numpy as np
import random
import argparse
from tqdm import tqdm

"""
    Created by Benjamin Duncan
    Nov 24, 2023
    I'm using this to create randomly generated mazes and save them to text files
    
    Wilson's algorithm: https://en.wikipedia.org/wiki/Maze_generation_algorithm
"""

HALL = " "
WALL = "#"
START = "S"
END = "E"


class MazeGenerator:
    _size = 31
    _maze = None
    _potential_paths = None

    def generate_maze(self, size=100):
        if size % 2 == 0:
            size += 1

        self._size = size
        self._maze = np.full((self._size, self._size), [WALL], dtype=str)

        # assign starting point - (i, j)
        self._potential_paths = [(1, 1)]
        self._maze[self._potential_paths[0][0], self._potential_paths[0][0]] = HALL
        point = None
        # while there is a path in starting point
        while len(self._potential_paths) > 0:
            # verify point
            point = random.choice(self._potential_paths)
            self._potential_paths.remove(point)

            if not self._has_pot(*point):
                # print("Selected point has no pot")
                continue

            # generate path
            self._generate_path(*point, True)

        return self._maze

    def _generate_path(self, i, j, is_first=False):
        if not self._has_pot(i, j):
            return

        found_path = False
        while not found_path:
            rand: int = random.randint(0, 3)

            if rand == 0 and i - 1 > 0 and self._is_wall(i - 1, j):  # up
                if self._is_isolated(i - 2, j):
                    self._maze[i - 2, j] = HALL
                    self._maze[i - 1, j] = HALL
                    self._generate_path(i - 2, j)
                found_path = True
            if (
                rand == 1 and j + 1 < self._size - 1 and self._is_wall(i, j + 1)
            ):  # right
                if self._is_isolated(i, j + 2):
                    self._maze[i, j + 2] = HALL
                    self._maze[i, j + 1] = HALL
                    self._generate_path(i, j + 2)
                found_path = True
            if rand == 2 and i + 1 < self._size - 1 and self._is_wall(i + 1, j):  # down
                if self._is_isolated(i + 2, j):
                    self._maze[i + 2, j] = HALL
                    self._maze[i + 1, j] = HALL
                    self._generate_path(i + 2, j)
                found_path = True
            if rand == 3 and j - 1 > 0 and self._is_wall(i, j - 1):  # left
                if self._is_isolated(i, j - 2):
                    self._maze[i, j - 2] = HALL
                    self._maze[i, j - 1] = HALL
                    self._generate_path(i, j - 2)
                found_path = True

        if self._has_pot(i, j):
            self._potential_paths.append((i, j))

    def _has_pot(self, i, j):
        return self._is_hall(i, j) and (
            (i - 2 > 0 and self._is_isolated(i - 2, j))
            or (i + 2 < self._size and self._is_isolated(i + 2, j))
            or (j - 2 > 0 and self._is_isolated(i, j - 2))
            or (j + 2 < self._size and self._is_isolated(i, j + 2))
        )

    def _is_isolated(self, i, j):
        return (
            i > 0
            and i < self._size - 1
            and j > 0
            and j < self._size - 1
            and self._is_wall(i + 1, j)
            and self._is_wall(i - 1, j)
            and self._is_wall(i, j + 1)
            and self._is_wall(i, j - 1)
        )

    def _is_wall(self, i, j):
        return self._maze[i][j] == WALL

    def _is_hall(self, i, j):
        return self._maze[i][j] == HALL

    def print(self, pretty=True):
        m = ""
        for i in range(self._size):
            for j in range(self._size):
                m += self._maze[i][j] + (" " if pretty else "")
            m += "\n"
        print()
        print(m)


def main():
    parser = argparse.ArgumentParser(
        prog="maze_generator.py",
        description="This program generates mazes in a square with a given length. It can print them out to stderr or to files.",
    )
    parser.add_argument(
        "size",
        action="store",
        type=int,
        default=20,
        help="Size of maze - odd number. If even, 1 will be added.",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        type=str,
        help="The base filename to store the mazes to (./output/{filename}). If left empty, the mazes will be outputed to stderr.",
    )
    parser.add_argument(
        "-i",
        "--iterations",
        action="store",
        type=int,
        help="The amount of mazes to generate. If a filename is specified, '_i' will be appended to it, where 'i' is the iteration number, starting with 0.",
    )
    parser.add_argument(
        "-p",
        "--pretty",
        action="store_true",
        help="Pretty output to stderr and files. This just adds a space between characters",
    )

    args = parser.parse_args()
    base_path = "./output/"

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    generator = MazeGenerator()

    for i in range(args.iterations or 1):
        maze = generator.generate_maze(args.size)

        if args.file == None:
            print(f"\nMaze #{i}")
            generator.print()
        else:
            np.savetxt(
                f"{base_path}{args.file}_{i}.txt",
                maze,
                fmt="%s",
                delimiter=(" " if args.pretty else ""),
            )


if __name__ == "__main__":
    main()
