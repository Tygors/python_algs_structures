# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 假设迷宫分为很多格
# 每一格要么是空的，要么被墙堵上

# 初步思路
# 1. 从起始位置开始，首先向北移动一格，然后在新的位置再递归地重复本过程
# 2. 如果第1.步往北行不通，就尝试向南移动一格，然后递归地重复本过程
# 3. 如果向南也行不通，则尝试向西移动一格，然后递归地重复本过程
# 4. 如果向北、南、西都不行，就尝试向东移动一格，然后递归地重复本过程
# 5. 如果4个方向都不行，则意味着没有出路

# 思路修正
# 通过策略记住到过的地方（发现到过，则退回上一格，然后尝试递归下一步）

import turtle
from time import sleep

START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "O"
# 空 代表可走的区域

class Maze:
    def __init__(self, maze_fn):
        with open(maze_fn, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.strip("\n")] for line in maze_file.readlines()
            ]
            self.rows_in_maze = len(self.maze_list)
            self.columns_in_maze = len(self.maze_list[0])
            for row_idx, row in enumerate(self.maze_list):
                # 找到起始位置
                if START in row:
                    self.start_row = row_idx
                    self.start_col = row.index(START)
                    break

            self.x_translate = -self.columns_in_maze / 2
            self.y_translate = self.rows_in_maze / 2
            self.t = turtle.Turtle()
            self.t.shape("turtle")
            self.wn = turtle.Screen()
            self.wn.setworldcoordinates(
                -(self.columns_in_maze-1)/2-0.5,
                -(self.rows_in_maze-1)/2-0.5,
                (self.columns_in_maze-1)/2+0.5,
                (self.rows_in_maze-1)/2+0.5,
            )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate,
                        -y + self.y_translate,
                        "orange",
                    )

        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)
        # self.wn.exitonclick()

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()

        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        sleep(1)
        self.t.setheading(
            self.t.towards(
                x + self.x_translate,
                -y + self.y_translate
            )
        )
        self.t.goto(
            x+self.x_translate,
            -y+self.y_translate
        )

    def drop_bread_crumb(self,color):
        self.t.dot(10,color)

    def update_position(self, row, col, val=None):
        """标记路径并更新迷宫图景"""
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"

        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)



    # 检查是否已经到达迷宫边缘
    # 第0行，第0列 最后一行或最后一列
    def is_exit(self,row,col):
        return (
            row in [0,self.rows_in_maze-1] or col in [0,self.columns_in_maze-1]
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]

def search_from(maze, row, column):
    "对当前位置的四个方向逐一尝试，直到找到出口"
    maze.update_position(row, column)
    # 检查基本情况：
    #1. 遇到了障碍
    if maze[row][column] == OBSTACLE:
        return False

    #2. 遇到了已经访问过的位置
    if maze[row][column] in [TRIED, DEAD_END]:
        return False

    #3. 找到了出口
    if maze.is_exit(row, column):
        maze.update_position(row, column, PART_OF_PATH)
        return True
    maze.update_position(row,column,TRIED)

    # 使用逻辑or对各个方向进行逐一尝试
    found = (
        search_from(maze, row-1,column)
        or search_from(maze,row+1,column)
        or search_from(maze,row,column-1)
        or search_from(maze,row,column+1)
    )
    if found:
        maze.update_position(row,column,PART_OF_PATH)
    else:
        maze.update_position(row,column,DEAD_END)

    return found


if __name__ == "__main__":
    # a = Maze("./maze_data.txt")
    # for i in a.maze_list:
    #     print(i)
    new_maze = Maze("./maze_data.txt")
    new_maze.draw_maze()
    new_maze.update_position(new_maze.start_row,new_maze.start_col)
    search_from(new_maze,new_maze.start_row,new_maze.start_col)
    new_maze.wn.exitonclick()