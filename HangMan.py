import pygame
from wonderwords import RandomWord
from pygame.color import Color
import time

class HangMan:
    def __init__(self):
        # create Welcome Screen
        self.screen = pygame.display.set_mode ([700, 600])
        pygame.display.set_caption ('Hangman')
        pygame.init ()
        self.base_font = pygame.font.SysFont ("Impact", 32)
        self.base_fo = pygame.font.SysFont ("Arial", 25)
        self.input_rect = pygame.Rect ((410,500),(52,42))
        self.label = "Please enter your guess here: "
        self.user_text = ""
        self.random_word = RandomWord ().random_words ()[0]
        self.letters = [0 for _ in range(len(self.random_word))]
        print(self.random_word)
        self.wrong = ""
        self.user_tex=""
        self.flag = False

    #draw gallow
    def draw_gallows(self):
        pygame.draw.rect (self.screen, Color('black'), [0, 450, 100, 10])
        pygame.draw.rect (self.screen, Color('black'), [100, 450, 100, 10])
        pygame.draw.rect (self.screen, Color('black'), [200, 450, 100, 10])
        pygame.draw.rect (self.screen, Color('black'), [50, 350, 10, 100])
        pygame.draw.rect (self.screen, Color('black'), [50, 250, 10, 100])
        pygame.draw.rect (self.screen, Color('black'), [50, 150, 10, 100])
        pygame.draw.rect (self.screen, Color('black'), [50, 150, 150, 10])
        pygame.draw.rect (self.screen, Color('black'), [150, 150, 100, 10])
        pygame.draw.rect (self.screen, Color('black'), [150, 150, 10, 50])
        pygame.draw.line (self.screen, Color('black'), [55, 405], [100, 450], 10)
        pygame.draw.line (self.screen, Color('black'), [100, 150], [55, 195], 10)
        pygame.draw.line (self.screen, Color('black'), [55, 405], [10, 450], 10)

    #specify position on screen wrong of correct letters guessed by player
    def draw_guess_letters(self):
        start = 360
        for i in range(len(self.random_word)):
            end = (start + i * 20) + 15
            pygame.draw.line(self.screen, Color('black'), (start + i * 20, 220), (end, 220), 3)
            if self.letters[i]:
                text = self.base_fo.render(self.random_word[i], False, Color('darkgreen'))
                self.screen.blit(text, (start + i * 20, 185))
    #specify position on screen of wrong letters guessed by player
    def draw_wrongs(self):
        index = 0
        for i in self.wrong:
            text = self.base_fo.render(i, True, Color('red'))
            self.screen.blit(text, (360 + index * 20, 400))
            index += 1

    def draw_leg_one(self):
        pygame.draw.line (self.screen, Color ('red'), (200, 300), (150, 350), 10)

    def draw_leg_two(self):
        pygame.draw.line (self.screen, Color ('red'), (200, 300), (250, 350), 10)

    def draw_arm_one(self):
        pygame.draw.line (self.screen, Color ('red'), (150, 250), (200, 250), 10)

    def draw_arm_two(self):
        pygame.draw.line (self.screen, Color ('red'), (200, 250), (250, 250), 10)

    def draw_body(self):
        pygame.draw.line (self.screen, Color ('red'), (200, 200), (200, 300), 10)

    def draw_head(self):
        pygame.draw.circle (self.screen, Color ('red'), (200, 200), 10, 10)

    def draw_hangman(self):
        self.draw_gallows ()
        if len (self.wrong) >= 1:
            self.draw_head ()
        if len (self.wrong) >= 2:
            self.draw_body ()
        if len (self.wrong) >= 3:
            self.draw_arm_one ()
        if len (self.wrong) >= 4:
            self.draw_arm_two ()
        if len (self.wrong) >= 5:
            self.draw_leg_one ()
        if len (self.wrong) >= 6:
            self.draw_leg_two ()
        self.draw_wrongs ()
    """Keep track of wrong letters and correct letters by drawing the hangman accordingly."""
    def run(self):
        run = True
        clock = pygame.time.Clock ()
        while run:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    pygame.quit ()
                    sys.exit ()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                        self.user_tex=self.user_text
                    else:
                        self.user_text += event.unicode
                        self.user_tex=self.user_text
                    # Exit game when esc key is pressed.
                    if event.key == pygame.K_ESCAPE :
                        pygame.quit ()
                        sys.exit ()

            self.screen.fill (Color ('white'))

            # track wrong guessed letters
            if len (self.wrong) == 6:
                lost_text = self.base_font.render ("You Lost, Please Press N To Start a New game or Esc to Quit", True, Color ('red'))
                self.screen.blit (lost_text, (10, 40))
                # if 6<len(self.wrong)<8:
                if self.user_tex.lower()=="n":
                    return True
                    run = False
            # track correct guessed letters
            for i in self.letters:
                if int(i) !=0:
                    if all(self.letters):
                        self.flag = True
                else:
                    self.flag = False

            if self.flag == True:
                lost_text = self.base_font.render ("You Won, Please Press N To Start a New game or Esc to Quit", True, Color ('darkgreen'))
                self.screen.blit (lost_text, (10, 40))

                if self.user_tex.lower()=="n":
                    return True
                    run = False

            pygame.draw.rect (self.screen, Color ('lightskyblue3'), self.input_rect, 4)

            # label
            label_surface = self.base_font.render (self.label, True, Color ('lightskyblue3'))
            self.screen.blit (label_surface, (10, 500))
            # button
            text_surface = self.base_font.render (self.user_text, True, Color ('black'))
            self.screen.blit (text_surface, (self.input_rect.x + 15, self.input_rect.y + 1))
            time.sleep(0.25)
            self.user_text = ""
            # draw guessed letters
            self.draw_guess_letters()
            # draw hangman
            self.draw_hangman()
            # keep track of wrong and right guessed letters
            def click():
                word = str (self.random_word)
                if self.user_tex in word:
                    for index in [i for i, x in enumerate (word) if x == self.user_tex ]:
                        self.letters[index] = 1
                else:
                    if self.user_tex not in self.wrong:
                        self.wrong += self.user_tex

            click()
            #update the screen
            pygame.display.flip ()

        clock.tick (60)
