import pygame.sprite
import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self,index, *groups):
        self._layer = Layer.BACKGROUND
        self.image = assets.get_sprite("background2")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index, 0))
        super().__init__(*groups)

    def update(self):
        # HOW fast the screen moves
        #.y for vertical change .x for horizontal change.
        #value for how fast
        self.rect.x -= 10

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH

