from gui import GUI
from data import Data
from controller import Controller
import tkinter as tk

root = tk.Tk()
root.title('Type your way up!')
app = GUI(root)
data = Data()
controller = Controller(data, app)
controller.start_session()

app.mainloop()
