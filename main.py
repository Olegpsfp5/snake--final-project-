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
        

        
class Bird(Player):
    def __init__(self):
        super().__init__("bird.png",100,452,45,45,10,20)


class Bird1(Player):
    def __init__(self):
        super().__init__("bird1.png",60,452,45,45,10,20)


class Bird2(Player):
    def __init__(self):
        super().__init__("bird2.png",145,452,45,45,10,20)
        self.speed = 7
        self.dmg = 30 

class Enemy(GameSprite):
    def __init__(self,image_name,x,y,width,height):
        super().__init__(image_name,x,y,width,height)

        
    
class Pig(Enemy):
    def __init(self):
        super().__init__(image_name,x,y,width,height)



class Wall(GameSprite):
    def __init__(self,image_name,x,y,width,height):
         super().__init__(image_name,x,y,width,height)
         

walls = sprite.Group()
pigs = sprite.Group()
birds = sprite.Group()
bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))

def level1(bg_img):
    global bg_image
    bg_image = transform.scale(image.load(bg_img),(WIDTH,HEIGHT))

    wood1 = Wall("wood.png",675 ,390,15,100)
    wood2 = Wall("wood2.png",575 ,390,100,15)
    wood3 = Wall("wood.png",560 ,390,15,100)

    wood4 = Wall("wood.png",675 ,290,15,100)
    wood5 = Wall("wood2.png",575 ,290,100,15)
    wood6 = Wall("wood.png",560 ,290,15,100)
    pigl1 = Pig("pig.png",605,445,45,45)
    pigl2 = Pig("pig.png",603,345,45,45)
    bird = Bird()
    bird1 = Bird1()
    bird2 = Bird2()
    birds.add(bird1,bird2,bird)
    walls.add(wood1,wood2,wood3,wood4,wood5,wood6)
    pigs.add(pigl1,pigl2)
    

def level2(bg_img):
    global bg_image
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
    walls.add(beam1,beam2,beam3,beam4,beam5,beam6,beam7,beam8,beam9,beam10,beam11,beam12,beam13,beam14,beam15)
    pig1 = Pig("pig.png",605,463,30,30)
    pig2 = Pig("pig.png",550,463,30,30)
    pig3 = Pig("pig.png",495,463,30,30)
    pig4 = Pig("pig.png",580,400,30,30)
    pig5 = Pig("pig.png",520,400,30,30)
    pig6 = Pig("pig.png",545,340,30,30)
    pigs.add(pig1,pig2,pig3,pig4,pig5,pig6)
    bird = Bird()
    bird1 = Bird1()
    bird2 = Bird2()
    birds.add(bird1,bird2,bird)


run = True
level2("background2.png")
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(bg_image,(0,0))
    walls.draw(window)
    pigs.draw(window)
    birds.draw(window)
    display.update()
    clock.tick(60)