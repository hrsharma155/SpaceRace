import pygame.sprite

import assets
import configs
from layer import Layer


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.value = 0
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)


        #NEW
        self.au_font = pygame.font.SysFont('Courier', 37)  # Adjust the size as needed
        self.au_text_color = (255, 165, 0)  # White color, change as needed


        self.__create()

        super().__init__(*groups)

    def __create(self):
        self.str_value = str(self.value)

        self.images = []
        self.width = 0

        # Create images for each digit of the score
        for str_value_char in self.str_value:
            img = assets.get_sprite(str_value_char)
            self.images.append(img)
            self.width += img.get_width()

        # Check if there are any digits, to avoid errors
        if self.images:
            self.height = self.images[0].get_height()

        # Create the "Au" text surface
        au_surface = self.au_font.render("Au", True, self.au_text_color)
        self.images.append(au_surface)
        self.width += au_surface.get_width()

        # Create the combined surface for score and "Au" text
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH / 2, 30))

        # Blit the digit images and "Au" surface onto the score surface
        x = 0
        for img in self.images:
            self.image.blit(img, (x, 0))
            x += img.get_width()



    def update(self):
        self.__create()
