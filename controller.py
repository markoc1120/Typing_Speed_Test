from timeit import default_timer as timer


class Controller:
    def __init__(self, data, gui):
        self.start = None
        self.end = None
        self.text = None
        self.data = data
        self.gui = gui

    def get_time(self):
        return timer()

    def start_session(self):
        self.text = self.data.get_random_text()
        self.gui.label_text.config(text=self.text)
        self.gui.text.focus()
        self.gui.finish_b.config(command=self.end_session)
        self.gui.restart_b.config(command=self.restart_session)
        self.start = self.get_time()
        self.gui.restart_b.grid_forget()

    def end_session(self):
        self.end = self.get_time()
        time = round(self.end - self.start, 1)
        text_input = self.gui.text.get("1.0", "end-1c")

        spelling_rate = self.get_spelling_rate(text_input)
        if text_input:
            words_per_min = round(len(text_input.split(' ')) / (time / 60))
        else:
            words_per_min = 0

        self.gui.label_text.config(text=f'Your spelling rate is {spelling_rate}%, and your average typing speed is '
                                   f'{words_per_min} words per minute.')
        self.gui.text.grid_forget()
        self.gui.finish_b.grid_forget()
        self.gui.restart_b.grid(column=1, row=3)

    def get_spelling_rate(self, text_input):
        text = self.text.split(' ')
        text_input = text_input.split(' ')
        matches = [i for i, j in zip(text, text_input) if i == j]
        return round((len(matches) / len(text)) * 100, 1)

    def restart_session(self):
        self.gui.text.delete("1.0", "end-1c")
        self.start_session()
        self.end = None
        self.gui.text.grid(column=0, columnspan=3, row=2)
        self.gui.finish_b.grid(column=1, row=3)
