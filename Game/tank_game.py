import pygame
import sys
import math

pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Game")

clock = pygame.time.Clock()

tank_width = 50
tank_height = 30
tank_x = 400
tank_y = 300 - (tank_height//2)
tank_angle = 0
max_bullets = 3 
shoot_cooldown = 600
last_shot_time = 0
tank_color = (255,0,0)

tank_surface_size = 120
tank_surface = pygame.Surface((tank_surface_size, tank_surface_size), pygame.SRCALPHA)

# tank body
body_y_offset = 45
body_x = tank_surface_size/2 - tank_width/2
body_y = tank_surface_size/2 - tank_height/2

pygame.draw.rect(tank_surface, tank_color, (body_x, body_y, tank_width, tank_height))

# gun barrel
gun_width = 40
gun_length = 8

gun_x = tank_width
gun_y = body_y_offset + tank_height/2 - gun_length/2

pygame.draw.rect(tank_surface, (180,180,180), (gun_x, gun_y, gun_width, gun_length))

bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    rotated_tank = pygame.transform.rotate(tank_surface, tank_angle)
    rect = rotated_tank.get_rect(center=(int(tank_x), int(tank_y)))
    screen.blit(rotated_tank, rect)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        print("pressed w")
        tank_x += math.cos(math.radians(tank_angle)) * 5
        tank_y -= math.sin(math.radians(tank_angle)) * 5
    if keys[pygame.K_s]:
        print("pressed s")
        tank_x -= math.cos(math.radians(tank_angle)) * 5
        tank_y += math.sin(math.radians(tank_angle)) * 5
    if keys[pygame.K_a]:
        tank_angle += 5
        print("pressed s")
    if keys[pygame.K_d]:
        tank_angle -= 5
        print("pressed d")
    if keys[pygame.K_SPACE]:
        print("pressed space")
        current_time = pygame.time.get_ticks()
        if len(bullets) < max_bullets and current_time - last_shot_time > shoot_cooldown:
            bullets.append([tank_x, tank_y, tank_angle])
            last_shot_time = current_time
    
    for bullet in bullets:
        bullet[0] += math.cos(math.radians(bullet[2])) * 8
        bullet[1] -= math.sin(math.radians(bullet[2])) * 8

        pygame.draw.circle(screen, (255,255,0), (int(bullet[0]), int(bullet[1])), 5)

    bullets = [b for b in bullets if 0 < b[0] < WIDTH and 0 < b[1] < HEIGHT]

    pygame.display.flip()
    clock.tick(60)