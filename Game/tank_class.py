import pygame
import math

class Tank:
    def __init__(self, tank_color, tank_x, tank_y, player_num):

        self.tank_width = 50
        self.tank_height = 30

        self.tank_x = tank_x
        self.tank_y = tank_y

        self.tank_angle = 0

        self.max_bullets = 5
        self.shoot_cooldown = 400
        self.last_shot_time = 0

        self.tank_color = tank_color

        self.tank_surface_size = 120
        self.tank_surface = pygame.Surface((self.tank_surface_size, self.tank_surface_size), pygame.SRCALPHA)

        self.player_num = player_num

        self.alive = True

        # tank body
        self.body_y_offset = 45
        self.body_x = self.tank_surface_size/2 - self.tank_width/2
        self.body_y = self.tank_surface_size/2 - self.tank_height/2

        # gun barrel
        self.gun_width = 40
        self.gun_length = 8
        self.gun_x = self.tank_width
        self.gun_y = self.body_y_offset + self.tank_height/2 - self.gun_length/2

        self.bullets = []

    def draw_tank(self):

        self.tank_surface.fill((0,0,0,0))

        pygame.draw.rect(
            self.tank_surface,
            self.tank_color,
            (self.body_x, self.body_y, self.tank_width, self.tank_height)
        )

        pygame.draw.rect(
            self.tank_surface,
            (180,180,180),
            (self.gun_x, self.gun_y, self.gun_width, self.gun_length)
        )

    def update(self, keys):
        if self.player_num == 1:
            if keys[pygame.K_w]:
                self.tank_x += math.cos(math.radians(self.tank_angle)) * 5
                self.tank_y -= math.sin(math.radians(self.tank_angle)) * 5

            if keys[pygame.K_s]:
                self.tank_x -= math.cos(math.radians(self.tank_angle)) * 5
                self.tank_y += math.sin(math.radians(self.tank_angle)) * 5

            if keys[pygame.K_a]:
                self.tank_angle += 5

            if keys[pygame.K_d]:
                self.tank_angle -= 5

            if keys[pygame.K_SPACE]:
                self.shoot()
        if self.player_num == 2:
            if keys[pygame.K_UP]:
                self.tank_x += math.cos(math.radians(self.tank_angle)) * 5
                self.tank_y -= math.sin(math.radians(self.tank_angle)) * 5

            if keys[pygame.K_DOWN]:
                self.tank_x -= math.cos(math.radians(self.tank_angle)) * 5
                self.tank_y += math.sin(math.radians(self.tank_angle)) * 5

            if keys[pygame.K_LEFT]:
                self.tank_angle += 5

            if keys[pygame.K_RIGHT]:
                self.tank_angle -= 5

            if keys[pygame.K_l]:
                self.shoot()


    def shoot(self):

        current_time = pygame.time.get_ticks()

        if len(self.bullets) < self.max_bullets and current_time - self.last_shot_time > self.shoot_cooldown:

            self.bullets.append([self.tank_x, self.tank_y, self.tank_angle])

            self.last_shot_time = current_time


    def update_bullets(self, WIDTH, HEIGHT):

        for bullet in self.bullets:

            bullet[0] += math.cos(math.radians(bullet[2])) * 8
            bullet[1] -= math.sin(math.radians(bullet[2])) * 8

        self.bullets = [b for b in self.bullets if 0 < b[0] < WIDTH and 0 < b[1] < HEIGHT]


    def draw(self, screen):
        if self.alive != True:
            return

        self.draw_tank()

        rotated_tank = pygame.transform.rotate(self.tank_surface, self.tank_angle)

        rect = rotated_tank.get_rect(center=(int(self.tank_x), int(self.tank_y)))

        screen.blit(rotated_tank, rect)

        for bullet in self.bullets:
            pygame.draw.circle(screen, (255,255,0), (int(bullet[0]), int(bullet[1])), 5)

    def get_rect(self):
        return pygame.Rect(self.tank_x - self.tank_width/2, self.tank_y - self.tank_height/2, self.tank_width, self.tank_height)