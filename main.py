from pygame import *
mixer.init()
font.init()
init()
WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Angry Birds")
clock = time.Clock()
mixer.music.load("angry-birds.ogg")

class GameSprite(sprite.Sprite):
    def __init__(self,image_name,x,y,width,height):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
    def draw(self):
        window.blit(self.image, self.rect)

        
class Bird(GameSprite):
    def __init__(self):
        super().__init__("bird.png",100,467,30,30)
        self.speed = 10
        self.dmg = 20 

class Bird1(GameSprite):
    def __init__(self):
        super().__init__("bird1.png",60,467,30,30)
        self.speed = 30
        self.dmg = 10

class Bird2(GameSprite):
    def __init__(self):
        super().__init__("bird2.png",140,467,30,30)
        self.speed = 7
        self.dmg = 30 

        
    
class Pig(GameSprite):
    def __init(self):
        super().__init__("pig.png",400,467,30,30)
        self.hp = 10


#class Wall(sprite.Sprite):
    #def __init(self,x,y,width,height):
       # super().__init__("beam.png",x,y,width,height)
        #self.rect.




bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
bird = Bird()
bird1 = Bird1()
bird2 = Bird2()
pig = Pig("pig.png",600,467,30,30)
while True:

    window.blit(bg_image,(0,0))
    pig.draw()
    bird.draw()
    bird1.draw()
    bird2.draw()
    display.update()
    clock.tick(60)