from sys import argv
import math


class Recursion:
    def __init__(self, an_text):
        self.a=[]
        #self.an=lambda n: eval(an_text, {"n":n}, {"a":self.a})
        self.an_text = an_text
        self.n = len(a)


    def get_an(self, n):
        result = sum(eval(self.an_text, {"n":n}, {"a":self.a}))
        self.a.insert(n,result)
        return result
    

    def get_x1_x2(self):
        b,c,  a = [eval(exp, {'n':1}, {"a":[1 for _ in self.a]} ) for exp in an_text[1:-1].split(',')]
        a = 1
        #print([for exp in an_text[1:-1].split(',')])
        b,c = -b,-c
        delta = b*b - 4*a*c
        sqrt_delta = math.sqrt(delta)
        """
        print(f"x1={-b - sqrt_delta} / {2*a}")
        print(f"x2={-b + sqrt_delta} / {2*a}")
        """
        x1 = (-b - sqrt_delta) / (2*a)
        x2 = (-b + sqrt_delta) / (2*a)
        return x1,x2


    def fN_to_R(self):
        ano = ""
        A,n = an_text[1:-1].split(',')[-1].split('*')
        ans = An+B
        #ans = A*fn.split('*')[-1]
        print()


if __name__ == '__main__':
    #a = eval(argv[1])
    #an_text = argv[2]
    #an_text = "[12*(a[n-3]),-2*(a[n-2]),-9]"
    #an_text = "[7*a[n-1],-10*(a[n-2]),2*3**n]"
    an_text = "[1*a[n-1],2*n]"
    r = Recursion(a, an_text)
    print(f"a0={r.get_an(0)}")
    print(f"a1={r.get_an(1)}")
    print(f"a2={r.get_an(2)}")
    print(f"a3={r.get_an(3)}")
    print(f"a4={r.get_an(4)}")
    print(f"a5={r.get_an(5)}")
    print(f"a6={r.get_an(6)}")
    print(f"a7={r.get_an(7)}")
    print(r.a)
    #x1,x2 = r.get_x1_x2()
    ano = "C1*x1**n+C2*x2**n"
