import json
class UnionFind:
    def __init__(self):
        self._structure = {}
    def __repr__(self):
        #print(self._structure)
        return json.dumps(self._structure)
    def __iter__(self):
        return iter(self._structure)
    def keys(self):
        return self._structure.keys()
    def values(self):
        return self._structure.values()
    def items(self):
        return self._structure.items()
    def union(self,*args):
        if len(args)==0:
            return
        m = min(args)
        if m not in self._structure:
            self._structure[m] = m
        for each in args:
            self._structure[each] = self._structure[self._structure[m]]
    def judge(self,a:int,b:int)->bool:
        return self._structure[a]==self._structure[b]
    def find(self,a):
        return [each for each in self._structure if self._structure[each]==self._structure[a]]

if __name__=='__main__':
    uf = UnionFind()
    uf.union(4,3)
    uf.union(3,8)
    uf.union(6,5)
    uf.union(9,4)
    uf.union(2,1)
    uf.union(5,0)
    uf.union(7,2)
    uf.union(6,1)
    for each in uf:
        print(each)
    print(uf)
    print(uf.judge(2,4))
    print(uf.judge(2,3))
    print(uf.find(2))