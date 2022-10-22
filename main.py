from pygame import *
mixer.init()
font.init()
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
        self.width = width
        self.height = height
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
        super().__init__("bird.png",100,467,30,30,10,20)


class Bird1(Player):
    def __init__(self):
        super().__init__("bird1.png",60,467,30,30,10,20 )


class Bird2(Player):
    def __init__(self):
        super().__init__("bird2.png",140,467,30,30,10,20 )
        self.speed = 7
        self.dmg = 30 

class Enemy(GameSprite):
    def __init__(self,image_name,x,y,width,height,hp):
        super().__init__(image_name,x,y,width,height)
        self.hp = hp

        
    
class Pig(Enemy):
    def __init(self):
        super().__init__(image_name,x,y,width,height)



class Wall(GameSprite):
    def __init__(self,image_name,x,y,width,height):
         super().__init__(image_name,x,y,width,height)
         


#beam2 = Wall("wood.png",630 ,440,10,50)
#beam3 = Wall("wood2.png",300 ,440,50,10)

bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
beam1 = Wall("wood.png",640 ,440,10,50)
beam2 = Wall("wood.png",590 ,440,10,50)
beam3 = Wall("wood2.png",590 ,430,60,10)

beam4 = Wall("wood2.png",530 ,430,60,10)
beam5 = Wall("wood.png",530 ,440,10,53)

beam6 = Wall("wood2.png",480 ,430,50,10)
beam7 = Wall("wood.png",480 ,440,10,53)

beam8 = Wall("wood.png",615 ,380,10,50)
beam9 = Wall("wood2.png",565 ,370,60,10)
beam10 = Wall("wood.png",560 ,380,10,50)

beam11 = Wall("wood2.png",505 ,370,60,10)
beam12 = Wall("wood.png",505 ,380,10,50)

beam13 = Wall("wood2.png",530,310,60,10)
beam14 = Wall("wood.png",530 ,320,10,50)
beam15 = Wall("wood.png",580 ,320,10,50)





bird = Bird()
bird1 = Bird1()
bird2 = Bird2()

pig1 = Pig("pig.png",605,463,30,30,30)
pig2 = Pig("pig.png",550,463,30,30,30)
pig3 = Pig("pig.png",495,463,30,30,30)
pig4 = Pig("pig.png",580,400,30,30,30)
pig5 = Pig("pig.png",520,400,30,30,30)
pig6 = Pig("pig.png",545,340,30,30,30)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(bg_image,(0,0))
    beam1.draw()
    beam2.draw()
    beam3.draw()
    beam4.draw()
    beam5.draw()
    beam6.draw()
    beam7.draw()
    beam8.draw()
    beam9.draw()
    beam10.draw()
    beam11.draw()
    beam12.draw()
    beam13.draw()
    beam14.draw()
    beam15.draw()
    pig1.draw()
    pig2.draw()
    pig3.draw()
    pig4.draw()
    pig5.draw()
    pig6.draw()
    bird.draw()
    bird1.draw()
    bird2.draw()
    display.update()
    clock.tick(60)