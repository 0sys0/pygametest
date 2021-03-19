import shape
import time
import copy
class Tetris():
    def __init__(self):
        self.width = 10
        self.height = 20
        self.background = []
        for i in range(self.height):
            self.background.append([0 for j in range(self.width)])
        self.shape = shape.Shape()
        self.now = self.shape.create(self.shape.random())
        self.x = 0
        self.y = 4
        self.next = self.shape.create(self.shape.random())
        self.mark = {0:'□',1:'■'}
    def render(self):
        self.canvas = copy.deepcopy(self.background)
        for i in range(4):
            for j in range(4):
                self.canvas[self.x+i][self.y+j]|=self.now[i][j]
        for i in range(self.height):
            for j in range(self.width):
                self.canvas[i][j] = self.mark[self.canvas[i][j]]
        self.print(self.canvas)
    def print(self,canvas):
        for line in canvas:
            print(' '.join([str(each) for each in line]))
        print('')
    def move(self):
        self.x+=1
    def collision_detect(self,x,y):
        for i in range(4):
            for j in range(4):
                if (x+i<self.height and y+j<self.width and self.canvas[x+i][y+j]==1) and self.now[i][j]==1:
                    return True
        return False
    def run(self):
        while True:
            self.render()
            self.move()
            time.sleep(1)
if __name__=='__main__':
    m = Tetris()
    m.run()