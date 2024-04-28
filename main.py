import pygame
from random import randint

HEIGHT = 700
WIDTH = 1300
SIZE = (WIDTH, HEIGHT)
FPS = 60

lost = 0
score = 0

window = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

background = pygame.transform.scale(
                pygame.image.load("galaxy.jpg"),
                SIZE)

pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play()

pygame.font.init()
font_big = pygame.font.Font(None, 70)
font_medium = pygame.font.Font(None, 35)
font_small = pygame.font.Font(None, 15)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image: str, coords: tuple[int,int], speed:int, size:tuple[int,int]):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image),
            size
        )
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect.topleft)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.x < WIDTH:
                self.rect.x += self.speed
            else:
                self.rect.x = 0
        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = WIDTH

    def fire(self):
        ...

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.rect.bottom = 0


player = Player("rocket.png", (WIDTH/2, HEIGHT-50), 8, (75,100))

test_enemy = Enemy("ufo.png", (randint(50,WIDTH-50),0), 5, (75,50))



game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        
        test_enemy




    text_lost = font_medium.render("Пропущено:" + str(lost), True, (255,255,255))
    text_score = font_medium.render("Рахунок:" + str(score), True, (255,255,255))

    window.blit(text_score, (0,0))
    window.blit(text_lost, (0, 40))





    pygame.display.update()
    clock.tick(FPS)