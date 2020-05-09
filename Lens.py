from tkinter import Canvas, Tk


class Lens:
    def __init__(self, root):
        self.root = root
        self.w = 1200.0
        self.h = 900.0
        self.f = 100.0

        self.canvas_create()

    def canvas_create(self):
        global w
        w = Canvas(self.root, height=self.h, width=self.w, background="yellow")
        w.grid(row=0, rowspan=10, column=0)


root = Tk()
L = Lens(root)
root.mainloop()
