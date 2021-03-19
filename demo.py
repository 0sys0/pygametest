import pygame
import time
import sys
import a_star

class Demo:
    def __init__(self):
        self.a_star = a_star.AStar()
        self.map = self.a_star.run()
        self.max_i = len(self.map)
        self.max_j = len(self.map[0])
        self.block_width = 32
        self.block_height = 32

        self.screen = pygame.display.set_mode((self.max_j*self.block_width,self.max_i*self.block_height))

        self.white = pygame.image.load('white.png').convert()
        self.gray = pygame.image.load('gray.png').convert()
        self.red = pygame.image.load('red.png').convert()
        self.green = pygame.image.load('green.png').convert()
        self.blue = pygame.image.load('blue.png').convert()
        self.frame = pygame.image.load('frame.png').convert_alpha()
        self.background = [self.white,self.green,self.red,None,None,None,self.blue,None,None,self.gray]
    def run(self):

        
        while True:
            for event in pygame.event.get():
                if event.type==pygame.constants.QUIT:
                    pygame.quit()
                    sys.exit()
            for i in range(len(self.map)):
                for j in range(len(self.map[0])):
                    self.screen.blit(self.background[self.map[i][j]], (j*self.block_width, i*self.block_height))
                    self.screen.blit(self.frame, (j*self.block_width, i*self.block_height))
            pygame.display.update()
            #time.sleep(1)
        #time.sleep(60)

if __name__=='__main__':
    pygame.init()
    demo = Demo()
    demo.run()