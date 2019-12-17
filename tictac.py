from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from copy import deepcopy

cnt=0
class Board:

    def __init__(self, other=None):
        self.player = 'O'
        self.computer = 'X'
        self.empty = ''
        self.size = 3
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x,y] = self.empty
        # copy constructor
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self, x, y):
        board = Board(self)
        board.fields[x, y] = board.player
        (board.player,board.computer) = (board.computer,board.player)
        global cnt
        return board

    def __minimax(self, player):
        if self.won():
            if player:
                return (-1, None)
            else:
                return (+1, None)
        elif self.tied():
            return (0, None)
        elif player:
            best = (-2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(not player)[0]
                    if value > best[0]:
                        best = (value, (x, y))
            return best
        else:
            best = (+2, None)
            for x, y in self.fields:
                if self.fields[x, y] == self.empty:
                    value = self.move(x, y).__minimax(not player)[0]
                    if value < best[0]:
                        best = (value, (x, y))
            return best

    def best(self):
        return self.__minimax(True)[1]

    def tied(self):
        for (x, y) in self.fields:
            if self.fields[x, y] == self.empty:
                return False
        return True

    def won(self):
        # horizontal
        for y in range(self.size):
            winning = []
            for x in range(self.size):
                if self.fields[x, y] == self.computer:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # vertical
        for x in range(self.size):
            winning = []
            for y in range(self.size):
                if self.fields[x, y] == self.computer:
                    winning.append((x, y))
            if len(winning) == self.size:
                return winning
        # diagonal
        winning = []
        for y in range(self.size):
            x = y
            if self.fields[x, y] == self.computer:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # other diagonal
        winning = []
        for y in range(self.size):
            x = self.size - 1 - y
            if self.fields[x, y] == self.computer:
                winning.append((x, y))
        if len(winning) == self.size:
            return winning
        # default
        return None

    def __str__(self):
        string = ''
        for y in range(self.size):
            for x in range(self.size):
                string += self.fields[x, y]
            string += "\n"
        return string


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title('TicTacToe')
        self.root.geometry("450x450")
        self.root.resizable(width=False, height=False)
        self.topframe=Frame(self.root)
        self.topframe.pack()
        self.board = Board()
        self.font = Font(family="Helvetica", size=32)
        self.buttons = {}
        for x, y in self.board.fields:
            handler = lambda x=x, y=y: self.move(x, y)
            button = Button(self.topframe, command=handler, font=self.font, width=4, height=2)
            button.grid(row=y, column=x)
            self.buttons[x, y] = button
        handler = lambda: self.reset()
        self.bottomframe = Frame(self.root)
        self.bottomframe.pack()
        button = Button(self.bottomframe, text='reset',height=3,width=8,relief="raised",fg='green', command=handler)
        button.grid(row=self.board.size + 1, sticky=W+E)
        self.topframe.update()

    def reset(self):
        self.board = Board()
        self.update()

    def move(self, x, y):
        self.root.config(cursor="watch")
        self.root.update()
        self.board = self.board.move(x, y)
        self.update()
        move = self.board.best()
        if move:
            global  cnt
            cnt=cnt+1
            self.board = self.board.move(*move)
            self.update()
        self.root.config(cursor="")

    def update(self):
        for (x, y) in self.board.fields:
            text = self.board.fields[x, y]
            self.buttons[x, y]['text'] = text
            self.buttons[x, y]['disabledforeground'] = 'black'
            if text == self.board.empty:
                self.buttons[x, y]['state'] = 'normal'
            else:
                self.buttons[x, y]['state'] = 'disabled'
        winning = self.board.won()
        if winning:
            for x, y in winning:
                self.buttons[x, y]['disabledforeground'] = 'red'
            for x, y in self.buttons:
                self.buttons[x, y]['state']='disabled'
            messagebox.showinfo("Result", "Computer Won")

        for (x, y) in self.board.fields:
            self.buttons[x, y].update()


    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    gg=GUI()
    gg.mainloop()
