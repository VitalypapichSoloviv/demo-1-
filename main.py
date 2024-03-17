import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))

class Player:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.color = color 
    def render(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h,)) 
    def upadate (self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
           self.y -= 0.8 
        if keystate [pygame.K_DOWN]:
            self.y += 0.8
        if keystate [pygame.K_LEFT]:
           self. x -= 0.8 
        if keystate[pygame.K_RIGHT]:
           self. x -= -0.8 
           
           
player = Player(250, 250, 50, 50, (250, 255,0))
 

                

while True: 
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

  screen.fill((255,255,255))
  player.render()
  player.upadate()
  pygame.display.update()
