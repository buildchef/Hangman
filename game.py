import word_logic
class Game:
    def __init__(self):
        self.word = word_logic.rand_word
        self.blink = word_logic.blink_word(self.word)
        self.chances = 6

    def validate_end(self):
        if self.chances <= 0:
            return True
        
        if self.blink == self.word:
            return True

        return False

    def __str__(self):
        return f'{self.word} | {self.blink}'        