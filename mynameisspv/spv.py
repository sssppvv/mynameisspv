class Spv:
    """
    This class is about spv
    consists of page name,
    youtube name
    --------------------------
    Example:
    ss = Spv()
    ss.show_name()
    ss.show_page()
    ss.about()
    ss.picsart()
    --------------------------
    """

    def __init__(self):
        self.name = 'sssppvv'
        self.page = 'https://www.facebook.com/sssppvv'

    def show_name(self):
        print('Hi, my name is {}'.format(self.name))

    def show_music(self):
        print('Youtube = https://www.youtube.com/purpeech')

    def show_page(self):
        print('FB page : {}'.format(self.page))

    def about(self):
        text = '''
        Helloooooooooooooooooooooooo.
        '''
        print(text)

    def picsart(self):
        picc = ''''
        /^-----^\\
        V  o o  V
         |  Y  |
          \ Q /
          / - \\
          |    \\
          |     \\     )
          || (___\\====
        '''
        print(picc)
        

if __name__ == '__main__':
    ss = Spv()
    ss.show_name()
    ss.show_music()
    ss.show_page()
    ss.about()
    ss.picsart()