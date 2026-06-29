""" Advent of Code 2025 - Day 7: Laboratories
Author: Pika4ndy

Part I:


Part II:


Difficulties encountered:
- Memoization
"""

sample = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

sample_test = """..S..
.....
..^..
.....
.^.^.
.....
"""

class Scene:
    """
    """
    def __init__(self, playground: list[list[str]]):
        self.scene = playground
        self.split_number = 0
        self.timelines = {}

        for i, row in enumerate(self.scene):
            for j, _ in enumerate(row):
                self.timelines[(i, j)] = 0

    def joinedScene(self) -> str:
        joined_scene = []

        for line in self.scene:
            joined_line = "".join(line)
            joined_scene.append(joined_line)

        joined_scene = "\n".join(joined_scene)
        
        return joined_scene

    def reconstructScene(self):
        new_scene = []

        for line in self.scene:
            char_list = []
            for char in line:
                char_list.append(char)

            new_scene.append(char_list)

        return new_scene

    def update(self):
        self.updated_scene : list[list[str]] = self.reconstructScene()

        for i, line in enumerate(self.scene): # row
            for j, char in enumerate(line): # column
                match char:
                    case ".":
                        continue

                    case "S":
                        if i+1 < len(self.scene) and self.scene[i+1][j] == ".":
                            self.timelines[(i+1, j)] = 1
                            self.updated_scene[i+1][j] = "|"

                    case "|":
                        if i+1 < len(self.scene):
                            self.updated_scene[i][j] = "."
                            # if self.scene[i+1][j] == "|":
                            #     continue

                            self.timelines[(i+1, j)] += 1
                            
                            if self.scene[i+1][j] == ".":
                                self.updated_scene[i+1][j] = char

                            elif self.scene[i+1][j]== "^":
                                self.timelines[(i+1, j-1)] += 1
                                self.timelines[(i+1, j+1)] += 1
                                if self.scene[i+1][j-1] == "." and self.scene[i+1][j+1] == ".":
                                    self.split_number += 1

                                match self.scene[i+1][j-1]:
                                    case ".":
                                        self.updated_scene[i+1][j-1] = char

                                    case "|":
                                        continue


                                match self.scene[i+1][j+1]:
                                    case ".":
                                        self.updated_scene[i+1][j+1] = char

                                    case "|":
                                        continue

        self.scene = self.updated_scene
                                
    def showScene(self) -> None:
        print(self.joinedScene())

def sampleTest() -> None:
    global sample
    global sample_test

    lines = sample.splitlines()

    sample_input = []

    for line in lines:
        sample_input.append([char for char in line])

    sample_scene = Scene(sample_input)

    
    for _ in range(15):
        sample_scene.update()

    sample_scene.showScene()
    print(f"{sample_scene.split_number = }")
    print(f"{sample_scene.timelines = }")
    last_row_list = list(filter(lambda x: x[0] == 15, sample_scene.timelines.keys()))
    # print(sum(map(lambda x: sample_scene.timelines[x], last_row_list)))

def main():
    with open("Day7/Day7_input") as file:
        reader = file.read()

    lines = reader.splitlines()

    grid_input = []

    for line in lines:
        grid_input.append([char for char in line])

    # print(sample_input)
    # print(numpy.array(sample_input))

    grid_scene:Scene = Scene(grid_input)

    
    grid_scene.update()
    grid_scene.showScene()
    print(grid_scene.split_number)

if __name__ == '__main__':
    sampleTest()