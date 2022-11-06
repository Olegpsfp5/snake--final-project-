from pygame import *
<<<<<<< HEAD

=======
init()
>>>>>>> 17ae3a8b8344b6aa1a3718aedb27ee9fd839d45e
mixer.init()
font.init()
WIDTH = 900
HEIGHT = 500
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Angry Birds")
clock = time.Clock()
mixer.music.load("angry-birds.ogg")

<<<<<<< HEAD
run = True
start = False
finish = False
menu =  True 
=======
>>>>>>> 17ae3a8b8344b6aa1a3718aedb27ee9fd839d45e

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
    def update(self):
        click = mouse.get_pressed()
        
        if click[2]:
            x,y = mouse.get_pos()
            if self.rect.collidepoint(x,y) and self.rect.x != 170 and self.rect.y != 380:
                self.rect.x = 192
                self.rect.y = 395
    def move(self):
        click = mouse.get_pressed()
        if click[1]:
            x,y = mouse.get_pos()
            if self.rect.collidepoint(x,y):
                self.rect.x += 20




class StartButton(GameSprite):
    def __init__(self):
        super().__init__("start_btn.png",380,150,150,100)
<<<<<<< HEAD
        self.level = 1 
    def update(self):
        global menu, start
        click = mouse.get_pressed()
        if click[0]:
            x,y = mouse.get_pos()
            if self.rect.collidepoint(x,y) and not start:
                if self.level == 1:
                    level1()
                elif self.level == 2:
                    level2()
                else:
                    level1()
                
                menu = False
                start = True              
=======
    def play():
        if click[0]:
            x,y = mouse.get_pos()
        if self.rect.collidepoint(x,y) and level1 != True:
            level1()


    

            
>>>>>>> 17ae3a8b8344b6aa1a3718aedb27ee9fd839d45e


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


class Bow(GameSprite):
    def __init__(self):
         super().__init__("bow.png",170,400,70,90)


walls = sprite.Group()
pigs = sprite.Group()
birds = sprite.Group()
bows = sprite.Group()
bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
start_btn = StartButton()

def level1():
    global bg_image
    bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))

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
    bow = Bow()
    bows.add(bow)
    

def level2():
    global bg_image
    bg_image = transform.scale(image.load("background2.png"),(WIDTH,HEIGHT))

    beam1 = Wall("wood.png",840 ,440,10,50)
    beam2 = Wall("wood.png",790 ,440,10,50)
    beam3 = Wall("wood2.png",790 ,430,60,10)

    beam4 = Wall("wood2.png",730 ,430,60,10)
    beam5 = Wall("wood.png",730 ,440,10,53)

    beam6 = Wall("wood2.png",680 ,430,50,10)
    beam7 = Wall("wood.png",680 ,440,10,53)

    beam8 = Wall("wood.png",815 ,380,10,50)
    beam9 = Wall("wood2.png",765 ,370,60,10)
    beam10 = Wall("wood.png",760 ,380,10,50)

    beam11 = Wall("wood2.png",705 ,370,60,10)
    beam12 = Wall("wood.png",705 ,380,10,50)

    beam13 = Wall("wood2.png",730,310,60,10)
    beam14 = Wall("wood.png",730 ,320,10,50)
    beam15 = Wall("wood.png",780 ,320,10,50)
    walls.add(beam1,beam2,beam3,beam4,beam5,beam6,beam7,beam8,beam9,beam10,beam11,beam12,beam13,beam14,beam15)
    pig1 = Pig("pig.png",805,463,30,30)
    pig2 = Pig("pig.png",750,463,30,30)
    pig3 = Pig("pig.png",695,463,30,30)
    pig4 = Pig("pig.png",780,400,30,30)
    pig5 = Pig("pig.png",720,400,30,30)
    pig6 = Pig("pig.png",745,340,30,30)
    pigs.add(pig1,pig2,pig3,pig4,pig5,pig6)
    bird = Bird()
    bird1 = Bird1()
    bird2 = Bird2()
    bow = Bow()
    birds.add(bird1,bird2,bird)
    bows.add(bow)


<<<<<<< HEAD

=======
run = True
>>>>>>> 17ae3a8b8344b6aa1a3718aedb27ee9fd839d45e
#level1("background2.png")
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(bg_image,(0,0))
<<<<<<< HEAD
    if menu:
        start_btn.draw()
        start_btn.update()
    elif not menu and start:
        birds.update()
        walls.draw(window)
        pigs.draw(window)
        bows.draw(window)
        birds.draw(window)
=======
    start_btn.draw()
    birds.update()
    walls.draw(window)
    pigs.draw(window)
    birds.draw(window)
    bows.draw(window)
>>>>>>> 17ae3a8b8344b6aa1a3718aedb27ee9fd839d45e
    display.update()
    clock.tick(60)
