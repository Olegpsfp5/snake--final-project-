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

class Player(GameSprite):
    def __init__(self,image_name,x,y,width,height,speed,dmg):
        super().__init__(image_name,x,y,width,height)
        self.speed = speed
        self.dmg = dmg 
        self.fly = False
        

        
class Bird(Player):
    def __init__(self):
        super().__init__("bird1.png",100,467,30,30,10,20)


class Bird1(Player):
    def __init__(self):
        super().__init__("bird2.png",60,467,30,30,10,20 )


class Bird2(Player):
    def __init__(self):
        super().__init__("bird3.png",140,467,30,30,10,20 )
        self.speed = 7
        self.dmg = 30 

class Enemy(GameSprite):
    def __init__(self,image_name,x,y,width,height,hp):
        super().__init__(image_name,x,y,width,height)
        self.hp = hp

        
    
class Pig(Enemy):
    def __init(self):
        super().__init__("pig.png",400,467,30,30,10)



class Wall(GameSprite):
    def __init__(self,image_name,x,y,width,height,hp):
         super().__init__(image_name,x,y,width,height)
         



bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
beam = Wall("wood.png",580 ,440,10,60,30)
beam1 = Wall("beam.png",580 ,300,10,60,30)
bird = Bird()
bird1 = Bird1()
bird2 = Bird2()
pig = Pig("pig.png",600,467,30,30,30)
while True:

    window.blit(bg_image,(0,0))
    beam.draw()
    beam1.draw()
    pig.draw()
    bird.draw()
    bird1.draw()
    bird2.draw()
    display.update()
    clock.tick(60)