#coding=utf-8
import random
import pygame
from pygame.locals import *
import sys
import time
import json

class Node:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.next = None
        self.prev = None
class Game:
    def generate_food(self):
        while True:
            i = random.randint(0,self.height-1)
            j = random.randint(0,self.width-1)
            if self.bitmap[i][j] == 0:
                self.bitmap[i][j] = 2
                break
    def change_direction(self,button):
        self.next_d = self.directions[button]
    def game_over(self):
        sys.exit()
    def refresh(self):
        if abs(self.next_d[0])==abs(self.d[0]) and abs(self.next_d[1])==abs(self.d[1]):
            pass
        else:
            self.d = self.next_d
        next_i = self.head.i+self.d[0]
        next_j = self.head.j+self.d[1]
        if abs(self.bitmap[next_i][next_j])==1 and not (next_i==self.tail.i and next_j==self.tail.j):
            print(next_i)
            print(next_j)
            print(self.bitmap[next_i][next_j])
            self.game_over()
        elif self.bitmap[next_i][next_j]==2:
            self.bitmap[next_i][next_j] = 1
            cur = Node(next_i,next_j)
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
            self.fps *= 1.2
            self.generate_food()
        else:
            self.bitmap[self.tail.i][self.tail.j] = 0
            self.tail = self.tail.prev
            cur = Node(next_i,next_j)
            cur.next = self.head
            self.head.prev = cur
            self.head = cur
            self.bitmap[self.head.i][self.head.j] = 1
    def __init__(self):
        self.height = 20
        self.width = 30
        self.bitmap = [[0 for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1:
                    self.bitmap[i][j] = -1
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # wsad
        self.head = Node(2, 5)
        cur = self.head
        cur.next = Node(2, 4)
        cur.next.prev = cur
        cur = cur.next
        cur.next = Node(2, 3)
        cur.next.prev = cur
        cur = cur.next
        cur.next = Node(2, 2)
        cur.next.prev = cur
        self.tail = cur.next
        self.bitmap[2][5] = 1
        self.bitmap[2][4] = 1
        self.bitmap[2][3] = 1
        self.bitmap[2][2] = 1
        self.d = (0, 1)
        self.next_d = self.d
        self.fps = 3.0
        self.generate_food()
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode([800,600])
        pygame.display.set_caption('helloworld')
        characters = {-1:'□',0:'　',1:'■',2:'♥'}
        font_size = 24

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    button = ''
                    if event.key == pygame.K_LEFT:
                        button = 'left'
                    elif event.key == pygame.K_RIGHT:
                        button = 'right'
                    elif event.key == pygame.K_UP:
                        button = 'up'
                    elif event.key == pygame.K_DOWN:
                        button = 'down'
                    if button!= '':
                        self.change_direction(button)
            self.refresh()
            string = []
            #string = ''
            for i in range(self.height):
                temp = ''
                for j in range(self.width):
                    temp+=characters[self.bitmap[i][j]]
                #string = temp+'\n'
                string.append(temp)
            #print(json.dumps(string,indent=4,ensure_ascii=False))
            fontObj = pygame.font.Font('font.ttf', font_size)
            # render方法返回Surface对象
            screen.fill((0, 0, 0))
            for i in range(len(string)):
                textSurfaceObj = fontObj.render(string[i], True, (255,255,255), (0,0,0))
                screen.blit(textSurfaceObj,(0,0+i*font_size))
            # get_rect()方法返回rect对象
            #textRectObj = textSurfaceObj.get_rect()
            #textRectObj.center = (200, 150)
            pygame.display.update()
            time.sleep(1/self.fps)
if __name__=='__main__':
    game = Game()
    game.run()
