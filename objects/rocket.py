import pygame
import assets
import configs
from layer import Layer
from objects.lowerMidObjects import LowerMiddleObjects
from objects.lowerObjects import LowerObjects
from objects.upperMidObjects import UpperMiddleObjects
from objects.upperObjects import UpperObjects


class Rocket(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER

        self.images = [
            assets.get_sprite("rocket-straight"), #rocket when no input
            assets.get_sprite("rocket-up"), #rocket image when going up
            assets.get_sprite("rocket-down") #rocket image when going down
        ]




        self.image = self.images[0]
        self.image = assets.get_sprite("rocket-straight") #midflap
        self.rect = self.image.get_rect(topleft=(-50,50))

        self.mask = pygame.mask.from_surface(self.image)

        self.vertical_speed = configs.VERTICAL_SPEED
        self.horizontal_speed = configs.HORIZONTAL_SPEED

        self.flap = 0


        super().__init__(*groups)

    def update(self):
        if pygame.key.get_pressed()[pygame.K_a]:
            self.image = self.images[1]
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.image = self.images[2]
        else: self.image = self.images[0]

        if self.rect.x < 50:
            self.rect.x += self.horizontal_speed
           


    def update_movement(self, moving_up, moving_down):
        if moving_up:
            self.rect.y -= self.vertical_speed
        elif moving_down:
            self.rect.y += self.vertical_speed
        else:
            self.rect.x += self.horizontal_speed

    def move_up(self):
        # Prevent the rocket from moving above the top of the screen
        new_y_position = self.rect.y - self.vertical_speed
        if new_y_position < 0:
            self.rect.y = 0
        else:
            self.rect.y = new_y_position



       

    def move_down(self):
        # Prevent the rocket from moving below the bottom of the screen
        new_y_position = self.rect.y + self.vertical_speed
        if new_y_position > configs.SCREEN_HEIGHT - self.rect.height:
            self.rect.y = configs.SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.y = new_y_position
        

    def stay_still_y(self):
        # No vertical movement, rocket stays still in y direction
        pass

    def move_forward_x(self):
        # Continuously move the rocket in x direction
        self.rect.x += self.horizontal_speed



    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 5

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is UpperObjects or type(sprite) is LowerObjects or type(sprite) is LowerMiddleObjects or type(sprite) is UpperMiddleObjects) and sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y) or self.rect.bottom < 0)):
                return True

        return False

    def set_death_image(self):
        death_image = assets.get_sprite("death-image")  # Assuming you have a death image
        self.image = death_image
