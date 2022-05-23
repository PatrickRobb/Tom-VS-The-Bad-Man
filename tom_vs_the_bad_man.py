import math
import pygame
from pygame.locals import *
import os
import random
from body_block import body_block

#from pygame.time import get_ticks

# main_dir = os.path.split(os.path.abspath(__file__))[0]
# data_dir = os.path.join(main_dir, "data")

pygame.init()
width = 700
height = 700

PLAYER_WIDTH, PLAYER_HEIGHT = 46, 46

body_color = (0, 255, 0)

tom_color = (0, 255, 0)

WIN = pygame.display.set_mode((width, height))

FPS = 60

BAD_MAN_HEAD_IMAGE = pygame.image.load(os.path.join('Assets', 'bad_man_4.png'))
#SNAKE_BODY_IMAGE = pygame.image.load(os.path.join('Assets', 'snake_body2.png'))
tom_head_image = pygame.image.load(os.path.join('Assets', 'tom_head_3.png'))

#SNAKE_BODY = pygame.transform.scale(
    #SNAKE_BODY_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
BAD_MAN_HEAD = pygame.transform.scale(
    BAD_MAN_HEAD_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
tom_head = pygame.transform.scale(tom_head_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

food_list = []
#snake_length = 0
speed = 3
angle = 0


def draw_window(bad_list, tom_list, angle, food_list):
    WIN.fill((35, 26, 196))
    bad_list[0].rects.pop(0)
    tom_list[0].rects.pop(0)
    WIN.blit(pygame.transform.rotate(BAD_MAN_HEAD, angle),
             (bad_list[0].rects[0].x, bad_list[0].rects[0].y))
    WIN.blit(tom_head, (tom_list[0].rects[0].x, tom_list[0].rects[0].y))
    #WIN.blit(tom_head, ((tom_list[0].rects[0].x-(PLAYER_WIDTH//4), tom_list[0].rects[0].y+(PLAYER_HEIGHT//4))))
    #pygame.draw.rect(WIN, (100, 100, 100), tom_list[0].rects[0])

    # for block in bad_list[1:]: # does not need to rotate
    #     WIN.blit(pygame.transform.rotate(
    #         SNAKE_BODY, angle), (block.rects.x, block.rects.y))
    for i in range(1, len(bad_list)):
        pygame.draw.circle(WIN, (bad_list[i].color), (bad_list[i].rects[0].x + (PLAYER_WIDTH//2), bad_list[i].rects[0].y + PLAYER_HEIGHT//2), PLAYER_WIDTH//2, PLAYER_HEIGHT//2)
        #WIN.blit(SNAKE_BODY, (bad_list[i].rects[0].x, bad_list[i].rects[0].y))
        bad_list[i].rects.append(pygame.Rect(bad_list[i-1].rects[0].x, bad_list[i-1].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
        bad_list[i].rects.pop(0)
    for i in range(1, len(tom_list)):
        #pygame.draw.rect(WIN, (200,200,200), tom_list[i].rects[0])
        pygame.draw.circle(WIN, (tom_list[i].color), (tom_list[i].rects[0].x + (PLAYER_WIDTH//2), tom_list[i].rects[0].y + PLAYER_HEIGHT//2), PLAYER_WIDTH//2, PLAYER_HEIGHT//2)
        #WIN.blit(SNAKE_BODY, (tom_list[i].rects[0].x, tom_list[i].rects[0].y))
        tom_list[i].rects.append(pygame.Rect(tom_list[i-1].rects[0].x, tom_list[i-1].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
        tom_list[i].rects.pop(0)
    # food = pygame.Rect(randx, randy, 20, 20)
    # pygame.draw.rect(WIN, (255,0,0), food)
    for p in bad_list[1:]:
        #for p in range(1, len(bad_list)):
            if p.rects[0].colliderect(tom_list[0].rects[0]):
                del tom_list[0:]
                tom_list.append(body_block(
                    [pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0))) 
    for p in bad_list[4:]:
        if p.rects[0].colliderect(bad_list[0].rects[0]):
            del bad_list[0:]
            bad_list.append(body_block(
                [pygame.Rect(520, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0)))
    for p in tom_list[1:]:
        #for p in range(1, len(tom_list)):
        if p.rects[0].colliderect(bad_list[0].rects[0]):
            del bad_list[0:]
            bad_list.append(body_block(
                [pygame.Rect(520, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0))) 
    for p in tom_list[4:]:
        if p.rects[0].colliderect(tom_list[0].rects[0]):
            del tom_list[0:]
            tom_list.append(body_block(
                [pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0)))
    for food in food_list:
        pygame.draw.rect(WIN, (255, 0, 0), food)
    pygame.display.update()


def player_movement(keys_pressed, bad_list, tom_list):
    angle = 0

    if tom_list[0].rects[0].x <= 0 or tom_list[0].rects[0].x >= width-PLAYER_WIDTH or tom_list[0].rects[0].y <= 0 or tom_list[0].rects[0].y >= height-PLAYER_HEIGHT:
        del tom_list[0:]
        tom_list.append(body_block(
            [pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0))) 
    if bad_list[0].rects[0].x <= 0 or bad_list[0].rects[0].x >= width-PLAYER_WIDTH or bad_list[0].rects[0].y <= 0 or bad_list[0].rects[0].y >= height-PLAYER_HEIGHT:
        del bad_list[0:]
        bad_list.append(body_block(
            [pygame.Rect(520, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0,0,0))) 
    if keys_pressed[pygame.K_a]:
        tom_list[0].rects.append(pygame.Rect(
            tom_list[0].rects[0].x - speed, tom_list[0].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
    elif keys_pressed[pygame.K_s]:
        tom_list[0].rects.append(pygame.Rect(
            tom_list[0].rects[0].x, tom_list[0].rects[0].y + speed, PLAYER_WIDTH, PLAYER_HEIGHT))
    elif keys_pressed[pygame.K_d]:
        tom_list[0].rects.append(pygame.Rect(
            tom_list[0].rects[0].x + speed, tom_list[0].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
    else:
        tom_list[0].rects.append(pygame.Rect(
            tom_list[0].rects[0].x, tom_list[0].rects[0].y - speed, PLAYER_WIDTH, PLAYER_HEIGHT))

    if keys_pressed[pygame.K_LEFT]:
        bad_list[0].rects.append(pygame.Rect(
            bad_list[0].rects[0].x - speed, bad_list[0].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
        angle = 90
    elif keys_pressed[pygame.K_DOWN]:
        bad_list[0].rects.append(pygame.Rect(
            bad_list[0].rects[0].x, bad_list[0].rects[0].y + speed, PLAYER_WIDTH, PLAYER_HEIGHT))
        angle = 180
    elif keys_pressed[pygame.K_RIGHT]:
        bad_list[0].rects.append(pygame.Rect(
            bad_list[0].rects[0].x + speed, bad_list[0].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
        angle = 270
    else:
        bad_list[0].rects.append(pygame.Rect(
            bad_list[0].rects[0].x, bad_list[0].rects[0].y - speed, PLAYER_WIDTH, PLAYER_HEIGHT))
        angle = 0
    return angle


# def snake_movement(keys_pressed, snake_rects):
#     speed = 3
#     if keys_pressed[pygame.K_SPACE]:
#         speed = 6
#     for i in range(len(snake_rects)):
#         if i > 0:
#             if snake_rects[i-1].x < snake_rects[i].x-PLAYER_WIDTH/1:
#                 snake_rects[i].x -= speed
#             elif snake_rects[i-1].x > snake_rects[i].x+PLAYER_WIDTH/1:
#                 snake_rects[i].x += speed
#             if snake_rects[i-1].y < snake_rects[i].y-PLAYER_HEIGHT/1:
#                 snake_rects[i].y -= speed
#             elif snake_rects[i-1].y > snake_rects[i].y+PLAYER_HEIGHT/1:
#                 snake_rects[i].y += speed
#     if keys_pressed[pygame.K_UP] and snake_rects[0].y > 0:
#         snake_rects[0].y -= speed
#     if keys_pressed[pygame.K_LEFT] and snake_rects[0].x > 0:
#         #BAD_MAN_HEAD_IMAGE = pygame.transform.rotate(BAD_MAN_HEAD_IMAGE ,90)
#         snake_rects[0].x -= speed
#         return 90
#     if keys_pressed[pygame.K_DOWN] and snake_rects[0].y < (height - PLAYER_HEIGHT):
#         snake_rects[0].y += speed
#         return 180
#     if keys_pressed[pygame.K_RIGHT] and snake_rects[0].x < (width - PLAYER_WIDTH):
#         snake_rects[0].x += speed
#         return 270
#     return 0

# def add_body(snake_rects):
# 	snake_rects.append(pygame.Rect(snake_rects[0].x-PLAYER_WIDTH, snake_rects[0].y-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))


def main():
    # snake_rects = []
    # snake_rects.append(pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT))
    clock = pygame.time.Clock()
    food_event = USEREVENT + 1
    pygame.time.set_timer(food_event, 1800)
    bad_list = []
    bad_list.append(body_block(
        [pygame.Rect(520, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0, 0, 0)))
    tom_list = []
    tom_list.append(body_block(
        [pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT)], (0, 0, 0))) 
    run = True
    while run:
        clock.tick(FPS)
        angle = player_movement(pygame.key.get_pressed(), bad_list, tom_list)
        #mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == food_event:
                rand_x = random.randint(50, 650)
                rand_y = random.randint(50, 650)
                food = pygame.Rect(rand_x, rand_y, 20, 20)
                food_list.append(food)
        for food in food_list:
            if food.colliderect(bad_list[0].rects[0]):
                food_list.remove(food)
                # snake_rects.append(pygame.Rect(snake_rects[len(
                #     snake_rects)-1].x-PLAYER_WIDTH, snake_rects[len(snake_rects)-1].y-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
                initial_moves_1 = []
                for _ in range(PLAYER_HEIGHT//speed):
                    initial_moves_1.append(
                        pygame.Rect(bad_list[-1].rects[0].x, bad_list[-1].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
                bad_list.append(body_block(initial_moves_1, ((150 + random.randint(-40, 80)), 0, 0)))
                # snake_rects.append(add_body(snake_rects))
        for food in food_list:
            if food.colliderect(tom_list[0].rects[0]):
                food_list.remove(food)
                initial_moves_2 = []
                for _ in range(PLAYER_HEIGHT//speed):
                    initial_moves_2.append(
                        pygame.Rect(tom_list[-1].rects[0].x, tom_list[-1].rects[0].y, PLAYER_WIDTH, PLAYER_HEIGHT))
                tom_list.append(body_block(initial_moves_2, (0, (150 + random.randint(-80, 80)), 0)))
        #if pygame.time.get_ticks() % 10000 == 0: draw_food()
        draw_window(bad_list, tom_list, angle, food_list)
        
    pygame.quit()


if __name__ == "__main__":
    main()
