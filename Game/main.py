import pygame
import sys
from tank_class import Tank

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(16)
pygame.mixer.music.load("battlemusic.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
WIDTH = 1300
HEIGHT = 900
BORDER = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
arena = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Tanky")

clock = pygame.time.Clock()

boom_sound = pygame.mixer.Sound("boom.wav")
tank1 = Tank((255,0,0), 100, 450, 0, 1)
tank2 = Tank((0,255,0), 1200, 450, 180, 2)
explosions = []
"""
reset_button = pygame.Rect(WIDTH - 120, 20, 100, 40)
font = pygame.font.SysFont(None, 28)
"""
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tank1.reset()
                tank2.reset()
    keys = pygame.key.get_pressed()

    tank1.update(keys)
    tank1.update_bullets(WIDTH, HEIGHT)
    
    tank2.update(keys)
    tank2.update_bullets(WIDTH, HEIGHT)
    tank1.tank_x = max(BORDER, min(WIDTH-BORDER, tank1.tank_x))
    tank1.tank_y = max(BORDER, min(HEIGHT-BORDER, tank1.tank_y))

    tank2.tank_x = max(BORDER, min(WIDTH-BORDER, tank2.tank_x))
    tank2.tank_y = max(BORDER, min(HEIGHT-BORDER, tank2.tank_y))

    for bullet in tank1.bullets:
        if tank2.alive and tank2.get_rect().collidepoint(bullet[0], bullet[1]):
            tank2.lives -= 1
            tank1.bullets.remove(bullet)
            explosions.append([tank2.tank_x, tank2.tank_y, 1])
            boom_sound.play()
    for bullet in tank2.bullets:
        if tank1.alive and tank1.get_rect().collidepoint(bullet[0], bullet[1]):
            tank1.lives -= 1
            tank2.bullets.remove(bullet)
            explosions.append([tank1.tank_x, tank1.tank_y, 1])
            boom_sound.play()
    if tank1.lives == 0:
        tank1.alive = False
    
    if tank2.lives == 0:
        tank2.alive = False

    
    arena.fill((30,30,30))
    pygame.draw.rect(arena, (100,100,100), (0, 0, WIDTH, BORDER))  
    pygame.draw.rect(arena, (100,100,100), (0, HEIGHT-BORDER, WIDTH, BORDER))  
    pygame.draw.rect(arena, (100,100,100), (0, 0, BORDER, HEIGHT))  
    pygame.draw.rect(arena, (100,100,100), (WIDTH-BORDER, 0, BORDER, HEIGHT))


    tank1.draw(arena)
    tank2.draw(arena)
    for explosion in explosions:
        pygame.draw.circle(arena, (255,150,0), (int(explosion[0]), int(explosion[1])), explosion[2])
        pygame.draw.circle(arena, (255,200,0), (int(explosion[0]), int(explosion[1])), explosion[2]//2)
        explosion[2] += 2
    explosions = [e for e in explosions if e[2] < 40]
    """
    reset_color = (150,150,150) if reset_button.collidepoint(pygame.mouse.get_pos()) else (100,100,100)
    pygame.draw.rect(screen, reset_color, reset_button)
    
    text = font.render("Reset", True, (255,255,255))
    screen.blit(text, (reset_button.x + 20, reset_button.y + 10))
    """
    
    window_width, window_height = screen.get_size()
    scale = min(window_width / WIDTH, window_height / HEIGHT)
    scaled_width = int(WIDTH * scale)
    scaled_height = int(HEIGHT * scale)
    scaled_arena = pygame.transform.scale(arena, (scaled_width, scaled_height))
    offset_x = (window_width - scaled_width) // 2
    offset_y = (window_height - scaled_height) // 2
    screen.fill((0,0,0))
    screen.blit(scaled_arena, (offset_x, offset_y))
    pygame.display.flip()
    clock.tick(60)