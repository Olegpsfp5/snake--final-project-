from pygame import *
import pymunk as pm
from pymunk import Vec2d
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d
import math



pm.pygame_util.positive_y_is_up = False



mixer.init()
font.init()
WIDTH = 900
HEIGHT = 500
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Angry Birds")
clock = time.Clock()
mixer.music.load("angry-birds.ogg")


pm.pygame_util.DrawOptions(window)

space = pm.Space() # створюємо простір
space.gravity = (0.0, 700.0) #додаємо гравітацію


class Box: #клас "Коробка" - щоб елементи не вилітали за краї екрану
    def __init__(self, p0=(0, 0), p1=(WIDTH, HEIGHT), d=0):
        x0, y0 = p0
        x1, y1 = p1
        ps = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pm.Segment(space.static_body, ps[i], ps[(i+1) % 4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)

frame = Box() #рамка
run = True
start = False
finish = False
menu =  True 
  
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
    def __init__(self,image_name,x,y,width,height,speed):
        super().__init__(image_name,x,y,width,height)
        mass = 1 #маса пташки
        radius = 22 # радіус пташки
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia) #створюємо тіло
        body.position = x, y
        
        shape = pm.Circle(body, radius, (0, 0)) #додаємо форму кола
        shape.elasticity = 0.5 #задаємо пружність
        shape.friction = 0.5 #тертя
        shape.collision_type = 0
        space.add(body, shape) #додаємо в простір
        self.body = body 
        self.shape = shape
    def draw(self):
        angle = self.body.angle
        img = transform.rotate(self.image, math.degrees(angle))
        self.rect.center = to_pygame(self.body.position, window)
        window.blit(img, self.rect)

class StartButton(GameSprite):
    def __init__(self):
        super().__init__("start_btn.png",380,150,150,100)
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

    def play():
        if click[0]:
            x,y = mouse.get_pos()
        if self.rect.collidepoint(x,y) and level1 != True:
            level1()


    

            

class Bird(Player):
    def __init__(self):
        super().__init__("bird.png",100,452,45,45,10)
    


class Bird1(Player):
    def __init__(self):
        super().__init__("bird1.png",60,452,45,45,10)


class Bird2(Player):
    def __init__(self):
        super().__init__("bird2.png",145,452,45,45,10)
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
    #bird1 = Bird1()
    #bird2 = Bird2()
    birds.add(bird)
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
    #bird1 = Bird1()
    #bird2 = Bird2()
    bow = Bow()
    birds.add(bird)
    bows.add(bow)


active_bird = None
aim_pos1 = (175,420)
aim_pos2 = (220,420)
scoping = False
points = 0
spritecollide = False

#level1("background2.png")
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
            p = from_pygame(e.pos, window)
            x,y = e.pos
            for bird in birds:
                if bird.rect.collidepoint(x,y):
                    scoping = True
                    active_bird = bird
                    bird.body.position = p
        elif e.type == MOUSEMOTION:
            if active_bird and scoping:
                active_bird.body.position =from_pygame(e.pos,window)
        elif e.type == MOUSEBUTTONUP:
            if scoping:
                scoping = False
                p0 = Vec2d(aim_pos2)
                p1 = from_pygame(e.pos,window)
                impulse = 7 * Vec2d(p0-p1).rotated(-active_bird.body.angle)
                active_bird.body.apply_impulse_at_local_point(impulse)
        
    window.blit(bg_image,(0,0))
    if menu:
        start_btn.draw()
        start_btn.update()
    elif not menu and start:
        if not scoping:
            space.step(1 / 60)
        birds.update()
        walls.draw(window)
        pigs.draw(window)
        bows.draw(window)
        for bird in birds:
            collides = sprite.spritecollide(bird,walls,True)
            for hit in collides:
                points += 1
            collides = sprite.spritecollide(bird,pigs,True)
            for hit in collides:
                points +=10
            if scoping and bird == active_bird:
                x,y =  active_bird.rect.midleft
                p = (x+10,y+15)
                draw.line(window,(0,0,0),p, aim_pos1,3)
                bird.draw()
                draw.line(window,(0,0,0),p, aim_pos2,3)
            else:
                bird.draw()
        if len(pigs) == 0:
            space.remove(active_bird.body,active_bird.shape)
            walls = sprite.Group()
            pigs = sprite.Group()
            menu = True
            start = False
            start_btn.level +=1
    display.update()
    clock.tick(60)
