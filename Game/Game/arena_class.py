import pygame
import random

class Arena:
    def __init__(self):
        self.arena_type = random.randint(1,9)
        
        self.walls = []

        if self.arena_type == 1:
            self.arena1()

        if self.arena_type == 2:
            self.arena2()

        if self.arena_type == 3:
            self.arena3()
        
        if self.arena_type == 4:
            self.arena4()

        if self.arena_type == 5:
            self.arena5()

        if self.arena_type == 6:
            self.arena6()

        if self.arena_type == 7:
            self.arena7()

        if self.arena_type == 8:
            self.arena8()

        if self.arena_type == 9:
            self.arena9()
        
    def arena1(self):

        self.spawn1 = (150, 450)
        self.spawn2 = (1150, 450)

        self.walls = [
            pygame.Rect(625, 250, 50, 400)
        ]
    
    def arena2(self):

        self.spawn1 = (200,200)
        self.spawn2 = (1100,700)

        self.walls = [
            pygame.Rect(500,420,300,60),
            pygame.Rect(620,250,60,350)
        ]


    def arena3(self):

        self.spawn1 = (200,700)
        self.spawn2 = (1100,200)

        self.walls = [
            pygame.Rect(400,300,150,150),
            pygame.Rect(750,450,150,150),
            pygame.Rect(600,150,200,100)
        ]
    
    def arena4(self):

        self.spawn1 = (100, 450)
        self.spawn2 = (1200, 450)

        self.walls = [
        pygame.Rect(300,100,50,700),
        pygame.Rect(500,0,50,600),
        pygame.Rect(700,300,50,600),
        pygame.Rect(900,0,50,600),
        pygame.Rect(1100,200,50,700),

        pygame.Rect(350,250,150,50),
        pygame.Rect(750,150,150,50),
        pygame.Rect(450,650,200,50),
        pygame.Rect(850,550,200,50)
        ]
    
    def arena5(self):

        self.spawn1 = (150,150)
        self.spawn2 = (1150,750)

        self.walls = [

        pygame.Rect(300,200,100,100),
        pygame.Rect(300,600,100,100),

        pygame.Rect(600,150,100,100),
        pygame.Rect(600,650,100,100),

        pygame.Rect(900,250,100,100),
        pygame.Rect(900,550,100,100),

        pygame.Rect(500,400,300,80)
        ]
    
    def arena6(self):

        self.spawn1 = (150,450)
        self.spawn2 = (1150,450)

        self.walls = [

        pygame.Rect(350,200,100,100),
        pygame.Rect(350,600,100,100),

        pygame.Rect(550,350,100,100),
        pygame.Rect(750,200,100,100),
        pygame.Rect(750,600,100,100),

        pygame.Rect(950,350,100,100),

        pygame.Rect(550,100,100,100),
        pygame.Rect(750,700,100,100)
    ]

    def arena7(self):

        self.spawn1 = (150,150)
        self.spawn2 = (1150,750)

        self.walls = [

        pygame.Rect(500,300,300,50),
        pygame.Rect(500,550,300,50),

        pygame.Rect(500,350,50,200),
        pygame.Rect(750,350,50,200),

        pygame.Rect(300,400,100,100),
        pygame.Rect(900,400,100,100)
    ]

    def arena8(self):

        self.spawn1 = (150,750)
        self.spawn2 = (1150,150)

        self.walls = [

        pygame.Rect(300,100,700,50),
        pygame.Rect(950,100,50,600),
        pygame.Rect(300,650,700,50),
        pygame.Rect(300,200,50,500),

        pygame.Rect(450,250,400,50),
        pygame.Rect(800,250,50,300),
        pygame.Rect(450,500,350,50),
        pygame.Rect(450,350,50,200)
    ]

    def arena9(self):

        self.spawn1 = (150,450)
        self.spawn2 = (1150,450)

        self.walls = []

        for x in range(300,1100,200):
            for y in range(200,800,200):
                self.walls.append(pygame.Rect(x,y,80,80))

    
    def draw(self, surface):

        for wall in self.walls:
            pygame.draw.rect(surface,(120,120,120),wall)