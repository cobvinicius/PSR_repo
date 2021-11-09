import tkinter as tk

class Paint():
    def __init__(self):
        self.window = tk.Tk()
        self.sizex = 500
        self.sizey = 500
        self.canvas = tk.Canvas(self.window, width=self.sizex,
                             height=self.sizey, highlightthickness=0)
        # Set canvas background color so you can see it
        self.canvas.config(bg="thistle")
        self.canvas.pack()

        self.img = tk.PhotoImage(width=self.sizex, height=self.sizey)
        self.canvas.create_image((0,0), image=self.img, state="normal",
                                 anchor='nw')
        # Set image color so you can see it
        self.img.put('khaki',to=(0, 0, self.sizex, self.sizey))
        self.canvas.bind("<Button-1>",self.color_in)

    def color_in(self, event):
        # Paint a 2x2 square at the mouse position on image
        x, y = event.x, event.y
        self.img.put("black", to=(x-2, y-2, x+2, y+2))

paint = Paint()
paint.window.mainloop()