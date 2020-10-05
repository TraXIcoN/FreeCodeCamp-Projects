GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0,0,0)

colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, GREY, WHITE)


SCREENWIDTH=1400
SCREENHEIGHT=800

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
numdots=10

pygame.display.set_caption("dot mania")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

class Dot(pygame.sprite.Sprite):

    def __init__(self,xvel,yvel,color,size):

        super().__init__()
            
        #define the little image of the sprite
        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #initialize attributes
        self.xvel=xvel
        self.yvel=yvel
        self.color=color
        self.size=size

        #draw it
        #pygame.draw.ellipse(screen, self.color, [self.rect.x-self.size/2,self.rect.y-self.size/2,self.size,self.size], 0)
        pygame.draw.rect(self.image, self.color, [0, 0, self.size, self.size])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def move(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x > SCREENWIDTH-10:
            self.xvel = 0-(self.xvel)
            self.rect.x += self.xvel
            self.xvel=self.xvel+1
        if self.rect.y > SCREENHEIGHT-10:
            self.yvel = 0-(self.yvel)
            self.rect.y += self.yvel
            self.yvel=self.yvel+1

    def kick(self, hkick, vkick):
        self.xvel+=(hkick)
        self.yvel+=(vkick)

    def flash(self):
        for col in colorList:
            self.color=col
            all_sprites_list.draw(screen)
            pygame.display.flip()


listdots=[Dot(random.randint(-2,2),random.randint(-2,2),random.choice(colorList),random.randint(6,15)) for x in range(numdots)]

for spr in listdots:
    all_sprites_list.add(spr)

carryon = True


while carryon:


    #INPUT phase
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryon=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryon=False
    if keys[pygame.K_d]:
        for dotguy in listdots:
            for loop in range(100):
                 dotguy.flash()

    #UPDATE phase
    for dot in listdots:
        dot.kick(random.randint(0,1),random.randint(0,1))
        #dot.kick(1,1)
        dot.move()

    all_sprites_list.update()

    #DRAW phase

    screen.fill(BLACK)

    all_sprites_list.draw(screen)       

    pygame.display.flip()

pygame.quit()
