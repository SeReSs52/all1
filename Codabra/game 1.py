
import pygame
import sys
import random

def finish():
    pygame.quit()
    sys.exit(0)

H = 500
W = 500
SIZE_A = 15
SIZE_B = 45

Display = pygame.display.set_mode((W, H))

FPS = 20
fpsClock = pygame.time.Clock()

def main ():
    hero = pygame.Rect(W / 2, H - 40, SIZE_B, SIZE_A)
    enemy = pygame.Rect((W / 2), 40, SIZE_B, SIZE_A)
    ball = pygame.Rect(W / 2, H / 2, 15, 15)

    x_ball_speed = 0
    y_ball_speed = 0
    while not x_ball_speed:
        x_ball_speed = random.randint(-10, 10)
    while not y_ball_speed:
        y_ball_speed = random.randint(-1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            hero.move_ip(-15, 0)
        elif keys[pygame.K_RIGHT] :
             hero.move_ip(15, 0)

        if keys[pygame.K_a] :
            enemy.move_ip(-15, 0)
        elif keys[pygame.K_d] :
            enemy.move_ip(15, 0)

        ball.move_ip(x_ball_speed, y_ball_speed)


        if ball.x > W - 15:
            x_ball_speed = random.randint(-10, -1)
        if ball.x < 0:
            x_ball_speed = random.randint(1, 10)

        if ball.y > H:
            return
        if ball.y < -15:
            return

        if ball.colliderect(enemy):
            y_ball_speed = 10
        if ball.colliderect(hero):
            y_ball_speed = - 10

        if hero.x > W - 15:
            hero.move_ip(-15, 0)
        if hero.x < 0:
            hero.move_ip(15, 0)

        if enemy.x > W - 15:
            enemy.move_ip(-15, 0)
        if enemy.x < 0:
            enemy.move_ip(15, 0)


        Display.fill((36, 255, 0))
        pygame.draw.rect(Display, (255, 0, 0), hero)
        pygame.draw.rect(Display, (0, 0, 0), enemy)
        pygame.draw.rect(Display, (0,0,255), ball)
        pygame.display.update()
        fpsClock.tick(FPS)
main()
finish()
