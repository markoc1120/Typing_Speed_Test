import random


class Data:
    def __init__(self):
        self.text = None
        self.data = ['Zelensky warned of great implications to global security if Russia isn’t stopped and also spoke '
                     'about what will come after the war, calling on nations and companies to invest in the restoration'
                     ' of Ukraine. Zelensky specifically spoke about the development of ports and cities on the Black'
                     ' Sea and rebuilding the naval sector.',
                     'There were soldiers who lived for this moment. The draft was an opportunity, they’d said. '
                     'Perseverance over preservation. Courage over cowardice. I saw it in their eyes, in the '
                     'direction of their boots as they stood and wrangled their rifles: one foot in front of the '
                     'other and you could bury your nose in that cut-flower honor our grandpas raised us on.']

    def get_random_text(self):
        self.text = self.data[random.randint(0, len(self.data) - 1)]
        return self.text
