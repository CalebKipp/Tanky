import pygame

class Screen:
    def __init__(self, width, height):
        self.tank1_type = 1
        self.tank2_type = 2
        self.width = width
        self.height = height
        self.state = "title"
        self.title_font = pygame.font.SysFont(None, 120)
        self.menu_font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 32)
        self.tank1_button = pygame.Rect(self.width//2 - 200, self.height//2 + 40, 400, 50)
        self.tank2_button = pygame.Rect(self.width//2 - 200, self.height//2 + 110, 400, 50)
        #self.start_button = pygame.Rect(width//2 - 150, 400, 300, 60)

    def handle_event(self, event, screen, arena):
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            scale_x = arena.get_width() / screen.get_width()
            scale_y = arena.get_height() / screen.get_height()

            arena_mouse = (mouse_x * scale_x, mouse_y * scale_y)

            if self.tank1_button.collidepoint(arena_mouse):
                if self.tank1_type == 1:
                    self.tank1_type = "ai"
                else:
                    self.tank1_type = 1

            if self.tank2_button.collidepoint(arena_mouse):
                if self.tank2_type == 2:
                    self.tank2_type = "ai"
                else:
                    self.tank2_type = 2

            if self.start_button.collidepoint(arena_mouse):
                self.state = "game"
        if self.state == "title":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                scale_x = arena.get_width() / screen.get_width()
                scale_y = arena.get_height() / screen.get_height()
                arena_mouse = (mouse_x * scale_x, mouse_y * scale_y)

                if self.start_button.collidepoint(arena_mouse):
                    self.state = "game"
    def draw(self, surface):
        self.width = surface.get_width()
        self.height = surface.get_height()

        self.start_button = pygame.Rect(self.width//2 - 150, self.height//2 - 50, 300, 60)

        if self.state == "title":

            surface.fill((20,20,20))

            title = self.title_font.render("TANKY", True, (200,200,200))
            surface.blit(title, (self.width//2 - title.get_width()//2, 120))

            pygame.draw.rect(surface, (100,100,100), self.start_button)

            start_text = self.menu_font.render("Start Game", True, (255,255,255))
            surface.blit(start_text, (self.start_button.x + 60, self.start_button.y + 15))

            font = pygame.font.SysFont(None, 40)

            t1_label = "AI" if self.tank1_type == "ai" else "Player"
            t2_label = "AI" if self.tank2_type == "ai" else "Player"

            tank1_text = font.render(f"Tank 1: {t1_label}", True, (255,255,255))
            tank2_text = font.render(f"Tank 2: {t2_label}", True, (255,255,255))

            pygame.draw.rect(surface, (100,100,100), self.tank1_button)
            pygame.draw.rect(surface, (100,100,100), self.tank2_button)

            surface.blit(tank1_text, (self.tank1_button.x + 20, self.tank1_button.y + 10))
            surface.blit(tank2_text, (self.tank2_button.x + 20, self.tank2_button.y + 10))

            controls = [
                "Controls",
                "Player 1:",
                "W/S - Forward / Back",
                "A/D - Rotate",
                "SPACE - Shoot",
                "",
                "Player 2:",
                "Arrow Keys - Move",
                "L - Shoot",
            ]
            x = 60
            y = 520
            for line in controls:
                text = self.small_font.render(line, True, (180,180,180))
                surface.blit(text, (x, y))
                y += 30