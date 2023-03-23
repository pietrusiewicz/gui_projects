from sys import argv
import math
import math_operations as mop
import numpy as np


class Recursion:
    def __init__(self, an_text, a=[]):
        self.a=a
        #self.an=lambda n: eval(an_text, {"n":n}, {"a":self.a})
        self.an_text = an_text
        self.n = len(self.a)


    def get_an(self, n):
        difference = len(self.an_text.split(',')) - len(self.a)
        if difference > 0:
            self.a = [0 for _ in range(difference)]
        result = sum(eval(self.an_text, {"n":n}, {"a":self.a}))
        self.a.insert(n,result)
        return result
    

    def get_x1_x2(self):
        b,c = [-eval(exp, {'n':1}, {"a":[1 for _ in self.a]} ) for exp in an_text[1:-1].split(',')][:2]
        # 1 is an
        self.x1,self.x2 = mop.get_x1_x2_delta(1, b,c)

        return self.x1,self.x2


    def fN_to_R(self):
        #ano = [for _ in self.a]
        fn = int(an_text[1:-1].split(',')[-1].split('*')[0])
        AB = [int(_.split('*')[0]) for _ in an_text[1:-1].split(',')[:-1]]
        print(AB)
        if len(AB) >2:
            A,B = AB
            print("An+B=")
            print(f"={A}(A(n-1)+B) + {B}(A(n-2)+B)=")
            print(f"={A}A*n + {-A}A + {A}B + {B}A*n + {-2*B}A + {B}B + {fn}*n")
            print(f"={A+B}A*n + {-A+-2*B}A + {A+B}B + {fn}*n")
            print(f"= An+B= n({A+B}A + {fn}) + ({-A+-2*B}A + {A+B}B)")

            print(f"{A+B}A + {fn} = A")
            print(f"{-A+-2*B}A + {A+B}B = B")

            print(f"{A+B}A + {fn} = A")
            print(f"{-A+-2*B}A + {A+B}B = B")
            #ans = A*fn.split('*')[-1]
            Lside = np.array( [[A+B-1, 0], [-A+-2*B, A+B-1]] )
            Rside = np.array([-fn, 0])
            self.A,self.B = list(np.linalg.solve(Lside,Rside))
            return f"An + B = {int(A)}n + {int(B)}"
        else:
            A = AB
            print(f"ans = An(n-1) + {fn}n")
            print(f"= An^2 + Bn")
            print(f"= A(n-1)^2 + B(n-1) + {fn}n")
            print(f"= A(n^2-2n+1) + Bn - B + {fn}n")
            print(f"= n^2(A) + n(-2A,B,{fn}) + (A-B)")
            Lside = np.array( [-2, 0], [1,-1] )
            Rside = np.array([fn, 0])
            self.A,self.B = list(np.linalg.solve(Lside,Rside))
            return f"An + B = {int(A)}n + {int(B)}"


    def An_plus_B(self):
        a,b,c = self.a.split(',')
        lenAn = sum(a,b,c)

    def an_ans_ano(self):
        try:
            Lside = [[1,1], [self.x1,self.x2]]
            Rside = [-self.B,-(self.A+self.B)+self.x1]
            print(f"\t1 + {self.x1}={-int(self.B)}")
            print(f"\t1 + {self.x2}={-int((self.A+self.B)+self.x1)}")
            self.C1,self.C2 = list(map(lambda x:int(x), np.linalg.solve(Lside,Rside)))
            print("C1 =",self.C1)
            print("C2 =",self.C2)
        except AttributeError:
            pass


if __name__ == '__main__':
    a = eval(argv[1])
    #an_text = argv[2]
    #an_text = "[12*(a[n-3]),-2*(a[n-2]),-9]"
    #an_text = "[7*a[n-1],-10*(a[n-2]),2*3**n]"
    #an_text = "[1*a[n-1],2*n]"
    #an_text = "[-2*a[n-1],15*a[n-2],36*n]"
    an_text = "[1*a[n-1],2*n]"
    r = Recursion(an_text)
    print(f"a0={r.get_an(0)}")
    print(f"a1={r.get_an(1)}")
    print(f"a2={r.get_an(2)}")
    print(f"a3={r.get_an(3)}")
    print(f"a4={r.get_an(4)}")
    print(f"a5={r.get_an(5)}")
    print(f"a6={r.get_an(6)}")
    print(f"a7={r.get_an(7)}")
    print(r.a)
    x = r.get_x1_x2()
    print(x)
    #x1,x2 = r.get_x1_x2()
    #ano = f"C1*{x}**n+C2*{x2}**n"
    #ano f"".format()
    # ano contains x,y
    ano = '*'.join([ f"C{i+1}*{item}**n" for i, item in enumerate(x) ])
    print("ano=", ano)

    ans = r.fN_to_R()
    print("ans=", ans)
    print("3. an = ano + ans")
    r.an_ans_ano()
    print(f"an={r.C1}*{r.x1}^n + {r.C2}*{r.x2}^n + {int(r.A)} + {int(r.B)}")