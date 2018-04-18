try:
    # for Python2
    import Tkinter as tk   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter as tk   ## notice lowercase 't' in tkinter here
import random
import time

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
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")
                self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2, fill="blue", tags="oval")

   

          arena = [[0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
          self.redraw(200, arena)

    def redraw(self, delay, arena):
          outputas = ""

          turiPakisti = []
          
          for i in range(0, len(arena)):
              for k in range (0, len(arena[i])):

                  if (k == len(arena[i]) -1) and (i == len(arena) -1):
                       outputas += str(arena[i][k]) + "\n"                    
                       print("\r"+outputas)
                  elif (k == len(arena[i]) -1):
                       outputas += str(arena[i][k]) + "\n"
                  else:
                       outputas += str(arena[i][k])
      
                  kaimynuSkaicius = 0
                  
                  kaimynaiVirsujeIndex = 0
                  kaimynaiApaciojeIndex = 0
                  if i == 0:
                      kaimynaiVirsujeIndex = len(arena) - 1
                  else:
                      kaimynaiVirsujeIndex = i - 1

                      
                  if i != len(arena)-1:
                      kaimynaiApaciojeIndex = i + 1



                  kaimynaiKairejeIndex = 0
                  kaimynaiDesnejeIndex = 0
                  
                  if k == 0:
                      kaimynaiKairejeIndex = len(arena[i])-1
                      kaimynaiDesnejeIndex = k +1
                  elif k == len(arena[i])-1:
                      kaimynaiDesnejeIndex = 0
                      kaimynaiKairejeIndex = k - 1
                  else:
                      kaimynaiDesnejeIndex = k +1
                      kaimynaiKairejeIndex = k - 1

                  kaimynuSkaicius +=arena[kaimynaiVirsujeIndex][kaimynaiKairejeIndex]+arena[kaimynaiVirsujeIndex][k]+arena[kaimynaiVirsujeIndex][kaimynaiDesnejeIndex]+arena[i][kaimynaiDesnejeIndex]+arena[i][kaimynaiKairejeIndex]+arena[kaimynaiApaciojeIndex][kaimynaiKairejeIndex]+arena[kaimynaiApaciojeIndex][kaimynaiDesnejeIndex]+arena[kaimynaiApaciojeIndex][k]
                  
                  if (arena[i][k] == 1 and kaimynuSkaicius < 2) or (arena[i][k] == 1 and kaimynuSkaicius > 3):
                       turiPakisti.append([i, k, "death"])
                  elif (arena[i][k] == 0 and kaimynuSkaicius == 3) or arena[i][k] == 1:
                       turiPakisti.append([i, k, "life"])
          try:
               for kitimas in range(0, len(turiPakisti)):
                    if turiPakisti[kitimas][2] == "death":
                         arena[turiPakisti[kitimas][0]][turiPakisti[kitimas][1]] = 0
                    else:
                         arena[turiPakisti[kitimas][0]][turiPakisti[kitimas][1]] = 1
          except:
               print("Neivyko jokiu pakitimu")
          self.canvas.itemconfig("rect", fill="blue")
          self.canvas.itemconfig("oval", fill="blue")
          for i in range(0, len(turiPakisti)):

                 row = turiPakisti[i][0]
                 col = turiPakisti[i][1]
                 item_id = self.oval[row,col]
                 if turiPakisti[i][2] == "death":
                      self.canvas.itemconfig(item_id, fill="blue")
                 else:
                      self.canvas.itemconfig(item_id, fill="green")
                      
          self.after(delay, lambda: self.redraw(delay,arena))
          

if __name__ == "__main__":
    app = App()
    app.mainloop()

