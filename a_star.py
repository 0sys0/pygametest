import time
import json
class AStar:
    def __init__(self):
        #显示地图
        self._map = [
            [0,0,0,0,0,0,0],
            [0,0,0,9,0,0,0],
            [0,0,0,9,0,0,0],
            [0,1,0,9,0,2,0],
            [0,0,9,9,0,0,0],
            [0,0,0,0,0,0,0]
            ]        
        self._start = [3,1]
        self._target= [3,5]
        #方向        
        self._d = [[[0,0] for each in row]for row in self._map]
        #f g h
        self._f = [[0 for each in row]for row in self._map]
        self._g = [[0 for each in row]for row in self._map]
        self._h = [[0 for each in row]for row in self._map]
        self._d1 = [[1,0],[0,1],[-1,0],[0,-1]] #右下左上
        self._d2 = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]] #右下左下左上右上
        self._cost1=[10,10,10,10]
        self._cost2 = [10,10,10,10,14,14,14,14]
        self._arrow = {str([1,0]):'↓',str([0,1]):'→',str([-1,0]):'↑',str([0,-1]):'←',str([1,1]):'↘',str([-1,1]):'↗',str([-1,-1]):'↖',str([1,-1]):'↙',str([0,0]):'○'}

        self._open_list = []
        self._close_list = []
        self._open_list.append(self._start)
    def run(self):
        while len(self._open_list)!=0:
            # find the smallest one
            current = min(self._open_list,key=lambda x:self._f[x[0]][x[1]])
            print(current)
            if current==self._target:
                break
            current_i = self._open_list.index(current)
            self._open_list = self._open_list[:current_i]+self._open_list[current_i+1:]

            self._close_list.append(current)
            for i in range(len(self._d2)):
                d = self._d2[i]
                cost = self._cost2[i]
                nex = [current[0]+d[0],current[1]+d[1]]
                if nex[0]>=0 and nex[0]<6 and nex[1]>=0 and nex[1]<7 and self._map[nex[0]][nex[1]]!=9 and nex not in self._close_list:
                    if nex not in self._open_list:
                        self._open_list.append(nex)
                        self._g[nex[0]][nex[1]] = self._g[current[0]][current[1]]+cost
                        self._h[nex[0]][nex[1]] = self._distance(nex,self._target)
                        self._d[nex[0]][nex[1]] = str([-d[0],-d[1]])
                    else:
                        if self._g[current[0]][current[1]]+cost<self._g[nex[0]][nex[1]]:
                            self._g[nex[0]][nex[1]] = self._g[current[0]][current[1]]+cost
                            self._d[nex[0]][nex[1]] = str([-d[0],-d[1]])
                    self._f[nex[0]][nex[1]] = self._g[nex[0]][nex[1]]+self._h[nex[0]][nex[1]]
            print('\n'.join(' '.join(['%2d' % i for i in row]) for row in self._f))
            print('')
            print('\n'.join(' '.join(['%2d' % i for i in row]) for row in self._g))
            print('')
            print('\n'.join(' '.join(['%2d' % i for i in row]) for row in self._h))
            print('')
            print('\n'.join(' '.join([self._arrow[str(i)] for i in row]) for row in self._d))
            #print(self._open_list)
            #print(self._close_list)
            #time.sleep(0.5)
        current = self._target
        while current!=self._start:
            if self._map[current[0]][current[1]]==0:
                self._map[current[0]][current[1]] = 6
            d = json.loads(self._d[current[0]][current[1]])
            current = [current[0]+d[0],current[1]+d[1]]
        print('')
        print('\n'.join(' '.join(['%2d' % i for i in row]) for row in self._map))
        return self._map
        
            

    def _distance(self,a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])
    def __repr__(self):
        return '\n'.join(' '.join(['%2d' % i for i in row]) for row in self._map)

if __name__=='__main__':
    a_star = AStar()
    print(a_star)
    a_star.run()