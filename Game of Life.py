try:
    # for Python2
    import Tkinter as tk   # notice capitalized T in Tkinter
except ImportError:
    # for Python3
    import tkinter as tk   # notice lowercase 't' in tkinter here


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        self.oval = {}
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="rect")
                self.oval[row, column] = self.canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill="blue", tags="oval")

        arena = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.redraw(200, arena)

    def redraw(self, delay, arena):

        need_to_make_change = []
          
        for i in range(0, len(arena)):
            for k in range(0, len(arena[i])):

                number_of_neighbor = 0
                neighbor_below_index = 0

                if i == 0:
                    neighbor_above_index = len(arena) - 1
                else:
                    neighbor_above_index = i - 1

                if i != len(arena)-1:
                    neighbor_below_index = i + 1

                if k == 0:
                    neighbor_to_the_left_index = len(arena[i])-1
                    neighbor_to_the_right_index = k + 1
                elif k == len(arena[i])-1:
                    neighbor_to_the_right_index = 0
                    neighbor_to_the_left_index = k - 1
                else:
                    neighbor_to_the_right_index = k + 1
                    neighbor_to_the_left_index = k - 1

                number_of_neighbor += \
                    arena[neighbor_above_index][neighbor_to_the_left_index]+arena[neighbor_above_index][k]+arena[neighbor_above_index][neighbor_to_the_right_index]+arena[i][neighbor_to_the_right_index]+arena[i][neighbor_to_the_left_index]+arena[neighbor_below_index][neighbor_to_the_left_index]+arena[neighbor_below_index][neighbor_to_the_right_index]+arena[neighbor_below_index][k]

                if (arena[i][k] == 1 and number_of_neighbor < 2) or (arena[i][k] == 1 and number_of_neighbor > 3):
                    need_to_make_change.append([i, k, "death"])
                elif (arena[i][k] == 0 and number_of_neighbor == 3) or arena[i][k] == 1:
                    need_to_make_change.append([i, k, "life"])
        try:
            for change in range(0, len(need_to_make_change)):
                if need_to_make_change[change][2] == "death":
                    arena[need_to_make_change[change][0]][need_to_make_change[change][1]] = 0
                else:
                    arena[need_to_make_change[change][0]][need_to_make_change[change][1]] = 1
        except:
            raise Exception("No changes made")
        self.canvas.itemconfig("rect", fill="blue")
        self.canvas.itemconfig("oval", fill="blue")
        for i in range(0, len(need_to_make_change)):

            row = need_to_make_change[i][0]
            col = need_to_make_change[i][1]
            item_id = self.oval[row, col]
            if need_to_make_change[i][2] == "death":
                self.canvas.itemconfig(item_id, fill="blue")
            else:
                self.canvas.itemconfig(item_id, fill="green")

        self.after(delay, lambda: self.redraw(delay, arena))
          

if __name__ == "__main__":
    app = App()
    app.mainloop()

