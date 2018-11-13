try:
    # for Python2
    import Tkinter as tk   # notice capitalized T in Tkinter
except ImportError:
    # for Python3
    import tkinter as tk   # notice lowercase 't' in tkinter here

from collections import namedtuple


Coordinate = namedtuple('Coordinates', 'x y')


class App(tk.Tk):
    def __init__(self, coordinates_to_put_live, rng, delay=500, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.delay = delay
        self.rng = rng
        self.size = 10*self.rng
        self.canvas = tk.Canvas(self, width=self.size, height=self.size, borderwidth=0, highlightthickness=1)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.cellwidth = 10
        self.cellheight = 10
        self.oval = {}
        self.coordinates_to_put_live = coordinates_to_put_live

        for column in range(self.rng):
            for row in range(self.rng):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.oval[row, column] = self.canvas.create_rectangle(x1+2, y1+2, x2-2, y2-2, tags="rect")

        arena = [[0 for _ in range(self.rng)] for _ in range(self.rng)]

        for coordinate in self.coordinates_to_put_live:
            arena[coordinate.x][coordinate.y] = 1

        self.redraw(self.delay, arena)

    def redraw(self, delay, arena):

        need_to_make_change = []
          
        for i in range(len(arena)):
            for k in range(len(arena[i])):

                number_of_neighbor = 0
                neighbor_below_index = 0

                neighbor_above_index = len(arena) - 1 if i == 0 else i - 1

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

                # sum everything that is around current cell
                number_of_neighbor += arena[neighbor_above_index][neighbor_to_the_left_index]+arena[
                    neighbor_above_index][k]+arena[neighbor_above_index][neighbor_to_the_right_index]+arena[i][
                    neighbor_to_the_right_index]+arena[i][neighbor_to_the_left_index]+arena[neighbor_below_index][
                    neighbor_to_the_left_index]+arena[neighbor_below_index][neighbor_to_the_right_index]+arena[
                    neighbor_below_index][k]

                if (arena[i][k] == 1 and number_of_neighbor < 2) or (arena[i][k] == 1 and number_of_neighbor > 3):
                    need_to_make_change.append([i, k, "death"])
                elif (arena[i][k] == 0 and number_of_neighbor == 3) or arena[i][k] == 1:
                    need_to_make_change.append([i, k, "life"])
        for change in range(len(need_to_make_change)):
            alive = 0 if need_to_make_change[change][2] == "death" else 1
            arena[need_to_make_change[change][0]][need_to_make_change[change][1]] = alive

        self.canvas.itemconfig("rect", fill="white")
        for i in range(len(need_to_make_change)):

            row = need_to_make_change[i][0]
            col = need_to_make_change[i][1]
            item_id = self.oval[row, col]
            fill = "white" if need_to_make_change[i][2] == "death" else "black"
            self.canvas.itemconfig(item_id, fill=fill)

        self.after(delay, lambda: self.redraw(delay, arena))


if __name__ == '__main__':

    coordinate_1 = Coordinate(x=4, y=5)
    coordinate_2 = Coordinate(x=4, y=6)
    coordinate_3 = Coordinate(x=4, y=7)

    coordinates_to_put_live = [coordinate_1, coordinate_2, coordinate_3]

    app = App(coordinates_to_put_live=coordinates_to_put_live, rng=25)
    app.mainloop()

