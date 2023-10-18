import pygame
from pygame.color import Color
import sys

class Game:
    def __init__(self,parent):
        #create Welcome Screen
        self.parent = parent
        self.screen = pygame.display.set_mode([780,600])
        pygame.display.set_caption ('Hangman')
        pygame.init ()
        self.base_font = pygame.font.SysFont ("Impact", 32)
        self.display_image = pygame.image.load('hangman.jpg')
        self.input_rect = pygame.Rect ((340, 500), (52, 42))
        self.label = "Welcome to Hangman game. Click START to begin."
        self.user_text = "START"

    # Create an object to help track time
    clock = pygame.time.Clock
    """This function starts the game. When the game is over,
     it gets the user's input if user wants to keep playing or exit the game."""
    def run(self):
        while True:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    pygame.quit ()
                    sys.exit ()
                # event handler when clicking START button.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        new_game = self.parent.run()
                        if new_game == True:
                            return True
                        elif new_game == False:
                            return False
            #Draw START button frame
            self.screen.fill (Color ('white'))
            pygame.draw.rect (self.screen, Color('lightskyblue3'), self.input_rect, 4)
            #label
            label_surface = self.base_font.render (self.label, True, Color ('lightskyblue3'))
            self.screen.blit (label_surface, (54, 40))
            #button
            text_surface = self.base_font.render (self.user_text, True, Color ('black'))
            self.screen.blit (text_surface, (self.input_rect.x + 15, self.input_rect.y + 1))
            self.input_rect.w=text_surface.get_width() + 29
            #image
            self.screen.blit (self.display_image, (50, 100))
            pygame.display.flip ()
        clock.tick (60)