class Induction:
    def __init__(self, a,b,n):
        self.a = a
        self.b = b
        self.n = n


    def krok_bazowy(self):
        print(f"1. Równanie: {self.a}x + {self.b}y = {self.n}")
        self.x,self.y = self.find_result("self.a*x + self.b*y == self.n")
        print(f"\t{self.n} = {self.a} * {self.x}(x) + {self.b} * {self.y}(y)")


    def find_result(self, exp):
        for x in range(1,self.n):
            for y in range(1,self.n):
                if eval(exp):
                    #print(f"{n} = {self.a} * {x}(x) + {self.b} * {y}(y)")
                    return x,y


    def krok_indukcyjny(self):
        print(f"2. Zakładam, że: n>={self.n} i n={self.a}x + {self.b}y dla pewnych x,y ∈ N")

        print(f"3. Udowodnię że istnieje x',y'∈N n+1 = {self.a}x'+{self.b}y'")
        print(f"\tMamy:")
        x1,y1 = self.find_result("self.a*x + self.b*-y == 1")
        x1 = -x1
        print(f"\t= {self.x}x + {self.y}y + {self.x}({x1}) + {self.y}({y1}) =")
        print(f"\t= {self.x}(x + ({x1})) + {self.y}(y + ({y1})) =")
        print(f"x'=x+({x1})")
        print(f"y'=y+({y1})")

if __name__ == '__main__':
    i = Induction(17, 11, 160)
    i.krok_bazowy()
    i.krok_indukcyjny()
