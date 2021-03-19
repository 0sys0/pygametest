import copy
import random
class Shape():
    def __init__(self):
        self.shape0 = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.shape1 = [
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0]
        ]
        self.shape2 = [
            [1,1,0,0],
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.shape3 = [
            [1,0,0,0],
            [1,1,0,0],
            [1,0,0,0],
            [0,0,0,0]
        ]
        self.shape4 = [
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.shapes = [self.shape1,self.shape2,self.shape3,self.shape4]
        self.width = 4
        self.height = 4
    def random(self):
        return random.choice(self.shapes)
    def create(self,shape):
        return copy.deepcopy(shape)
    def rotate(self,shape,clockwise=True):
        shape_next = [[shape[self.height-1-i][j]for i in range(self.height)] for j in range(self.width)]
        for i in range(len(shape_next)):
            for j in range(len(shape_next[i])):
                shape[i][j] = shape_next[i][j]
    def print(self,shape):
        for line in shape:
            print(' '.join([str(each) for each in line]))
        print('')
    def run(self):
        shape = self.create(self.shape3)
        self.print(shape)
        self.rotate(shape)
        self.print(shape)
        self.rotate(shape)
        self.print(shape)
        self.rotate(shape)
        self.print(shape)
        self.rotate(shape)
        self.print(shape)

if __name__=='__main__':
    s = Shape()
    s.run()