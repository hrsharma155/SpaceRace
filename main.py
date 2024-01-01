import random

import pygame
import configs
from objects.lowerObjects import LowerObjects #NEW
from objects.lowerMidObjects import LowerMiddleObjects
from objects.upperMidObjects import UpperMiddleObjects

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
import pygame
import assets
import configs
from objects.background import Background
from objects.rocket import Rocket
from objects.upperObjects import UpperObjects
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score


pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
obstacle_create_event = pygame.USEREVENT
astronaut_create_event = pygame.USEREVENT #NEW
running = True
gameover = False
gamestarted = False

assets.load_sprites()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)

    return Rocket(sprites), GameStartMessage(sprites), Score(sprites)


rocket, game_start_message, score = create_sprites()
helperDistance = 0


while running:




    keys = pygame.key.get_pressed()
    if not gameover:
        if keys[pygame.K_a]:
            rocket.move_up()
        elif keys[pygame.K_d]:
            rocket.move_down()
        else:
            rocket.stay_still_y()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == obstacle_create_event:
            UpperObjects(sprites)
            LowerObjects(sprites)
            LowerMiddleObjects(sprites)
            UpperMiddleObjects(sprites)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_message.kill()
                pygame.time.set_timer(obstacle_create_event, 1500)
                pygame.time.set_timer(astronaut_create_event, 1500) #new
            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                rocket, game_start_message, score = create_sprites()

        keys = pygame.key.get_pressed()



    screen.fill(0)

    sprites.draw(screen)

    #update game logic
    if gamestarted and not gameover:
        sprites.update()

    #this creates the game over message
    if rocket.check_collision(sprites) and not gameover:
        gameover = True
        gamestarted = False
        rocket.set_death_image()
        GameOverMessage(sprites)
        pygame.time.set_timer(obstacle_create_event, 0)
        pygame.time.set_timer(astronaut_create_event, 1500)  # new

        assets.play_audio("death")


    helperDistance += 1
    if helperDistance == 100:
        score.value += 1
        helperDistance = 0


    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
