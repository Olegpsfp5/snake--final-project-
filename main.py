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
        super()._init__()
        self.img = transform.scale(image.load(image_name),(width,height))
        self.rect = self,img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

class Bird(GameSprite):
    def __init__(self):
        super().__init__("bird1.png",140,140,75,75)
        self.speed = 5

bg_image = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
bird = Bird()
while True:
    bird.draw()
    window.blit(bg_image,(0,0))
    display.update()
    clock.tick(60)