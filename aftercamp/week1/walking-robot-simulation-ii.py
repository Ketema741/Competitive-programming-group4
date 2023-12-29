class Robot:
    def __init__(self, width, height):
       self.x = 0
       self.y = 0
       self.w = width
       self.h = height
       self.dir = 0
       self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
       self.dlables = ["East", "North", "West", "South"]

    def step(self, num):
        num %= (self.w - 1 + self.h - 1)*2

        if num == 0:
            num += (self.w - 1 + self.h - 1)*2


        for _ in range(num):
            nx, ny = self.x + self.directions[self.dir][0], self.y  + self.directions[self.dir][1]

            while not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1)%4
                nx, ny = self.x + self.directions[self.dir][0], self.y + self.directions[self.dir][1]

            self.x = nx
            self.y = ny

           
    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dlables[self.dir]
