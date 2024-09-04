import pygame
import random
pygame.init()
WIDTH=850
HEIGHT=900
points=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("Background.PNG")
bg=pygame.transform.scale(bg,(1500,900))
candy_freq=1000
last_candy=pygame.time.get_ticks()-candy_freq
game=True
bg_x=0


class Snake(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("green_gummy_worm.PNG")
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        if self.rect.left < -40:
            self.rect.left = -40
class GummyWorm(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(300,200))
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        self.rect.x-=4
        if self.rect.x<0:
            self.kill()
class ExtraPoints(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image=pygame.image.load(img)
#Make the regular candies images list, resize the gummy bears, make other candies to display like the regular ones
        self.image=pygame.transform.scale(self.image,(64,105))
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        self.rect.x -= 4
        if self.rect.x<0:
            self.kill()
class RegularPoints(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        self.rect.y+=4
        if self.rect.y>900:
            self.kill()

#candy=ExtraPoints(400,300,img)
#making a group for the sprite
candies=pygame.sprite.Group()
gummies = pygame.sprite.Group()
#candies.add(candy)   

img=pygame.image.load("pink_gummy_worm.PNG")

snake=Snake(50,50)
round=pygame.sprite.Group()
round.add(snake)  
fps = 30   
clock=pygame.time.Clock()   

Extra=["gummy_bear_1.png","gummy_bear_2.png","gummy_bear_3.png"]
Regular=["big_cake.png","cake_slice.png",]

while True:
    clock.tick(fps)
    screen.blit(bg,(bg_x,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
    candies.draw(screen)
    gummies.draw(screen)
    round.draw(screen)
    round.update()

    bg_x=bg_x-0.7
    if abs(bg_x)>500:
        bg_x=0
    
    

    time_now=pygame.time.get_ticks()
    if time_now-last_candy>candy_freq:
        num=random.randint(50,850)
        
        img=pygame.image.load(random.choice(Regular))
        img2=random.choice(Extra)
        regular=RegularPoints(num,0,img)
        extra = ExtraPoints(WIDTH,num,img2)

        candies.add(regular)
        gummies.add(extra)
        last_candy = time_now
    #last_candy=time_now
    candies.update()
    gummies.update()
    pygame.display.update()
