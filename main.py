class Node:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.next = None
        self.prev =None
class Game:
    def __init__(self):
        height = 20
        width = 30
        bitmap = [[0 for j in range(width)] for i in range(height)]

        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0:
                    bitmap[i][j] = -1
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}  # wsad

        head = Node(2, 5)
        cur = head
        cur.next = Node(2, 4)
        cur.next.prev = cur
        cur = cur.next
        cur.next = Node(2, 3)
        cur.next.prev = cur
        cur = cur.next
        cur.next = Node(2, 2)
        cur.next.prev = cur
        bitmap[2][5] = 1
        bitmap[2][4] = 1
        bitmap[2][3] = 1
        bitmap[2][2] = 1

        d = (0, 1)
    def on_button_press(self,button):
        d = directions[self,button]
    def game_over(self):
        pass
    def refresh():
        cur = head
        head_i = head.i+d[0]
        head_j = head.j+d[1]
        if abs(bitmap[head_i][head_j])==1:
            game_over()
        elif bitmap[head_i][head_j]==2:
            cur = Node(head_i,head_j)
            cur.next = head
            head.prev = cur
            head = cur
        else:
            while cur!=None:
                if cur!=head:
                    cur.i = prev_i
                prev_i = cur.i
            prev_j = cur.j

