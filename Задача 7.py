class MinMaxWordFinder:
    def __init__(self) -> None:
        pass
    def add_sentence(self, string):
        self.n=string
        self.y=self.n.split()
        print(self.y)
    def shortest_words(self, string):
        self.n=string
        self.y=self.n.split()
        self.min = self.y[0]
        self.lst=[]
        for j in range(0, len(self.y)):
            if len(self.min) >= len(self.y[j]):
                self.min = self.y[j]
        for j in range(0, len(self.y)):
            if len(self.min) == len(self.y[j]):
                self.lst.append(self.y[j])
        self.lst.sort()
        print(self.lst)
    def longest_words(self, string):
        self.n=string
        self.y=self.n.split()
        self.max = self.y[0]
        self.lst=[]
        for j in range(0, len(self.y)):
            if len(self.max) <= len(self.y[j]):
                self.max = self.y[j]
        for j in range(0, len(self.y)):
            if len(self.max) == len(self.y[j]):
                    self.lst.append(self.y[j])
        self.final=list(set(self.lst))
        self.final.sort()
        print(self.final)

finder=MinMaxWordFinder()
finder.add_sentence("hello abc world ayu")
finder.shortest_words("hello abc e world ayu ttt ui o")
finder.longest_words("world abc e hello ayu hello ttt ui o hello")


