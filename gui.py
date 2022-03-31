import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.root = tk.Frame.__init__(self, *args, **kwargs)

        # IMAGE
        self.canvas = tk.Canvas(width=350, height=350)
        self.image = tk.PhotoImage(file='/Users/markoc1120/PycharmProjects/Typing_Speed_Test/logo.png')
        self.canvas.create_image(175, 175, image=self.image)
        self.canvas.grid(column=0, columnspan=3, row=0)

        # LABEL
        self.label_text = tk.Label()
        self.label_text.config(padx=20, pady=20, wraplength=600)
        self.label_text.grid(column=0, columnspan=3, row=1)

        # TEXT
        self.text = tk.Text(self.root, height=10, padx=20, pady=20)
        self.text.grid(column=0, columnspan=3, row=2)

        # FINISH BUTTON
        self.finish_b = tk.Button(text='Finish')
        self.finish_b.config(width=12, padx=10)
        self.finish_b.grid(column=1, row=3)

        # RESTART BUTTON
        self.restart_b = tk.Button(text='Restart')
        self.restart_b.config(width=12, padx=10)
        self.restart_b.grid(column=1, row=4)
