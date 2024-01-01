import random
import pygame
import assets
import configs
from layer import Layer


class LowerMiddleObjects(pygame.sprite.Sprite):
    def __init__(self, *groups):


        #serves to overlap the column with floor
        #sees column as an obstacle that the floor has to cover
        self._layer = Layer.OBSTACLE
        #gap between the objects
        self.gap = 100
        possible_sprites = ["asteroid1", "asteroid2","asteroid3", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11"]
        num_objects =  4 #random.randint(1,4)
        self.sprites = []

        lower_middle_start = configs.SCREEN_HEIGHT *  (2/4)

        for _ in range(num_objects):
            sprite_name = random.choice(possible_sprites)
            sprite = assets.get_sprite(sprite_name)

            # randomness to x and y spawn
            y_position = random.uniform(lower_middle_start, configs.SCREEN_HEIGHT * 3/4 )  # NEW
            x_position = random.uniform(configs.SCREEN_WIDTH + 900, configs.SCREEN_WIDTH) # new

            sprite_rect = sprite.get_rect(midleft=(x_position, y_position))


            self.sprites.append((sprite, sprite_rect))
        self.image, self.rect = self.sprites[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.passed = False
        super().__init__(*groups)


    def update(self):
        # HOW fast the screen moves
        # .y for vertical change .x for horizontal change.
        # value for how fast
        self.rect.x -= 9

        if self.rect.right <= 10:
            self.kill()

