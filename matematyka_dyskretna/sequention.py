import math_operations as mop
import numpy as np

a = [1,-1]
sequence = [1, -2, 15, 24]
n = len(a)

if n == 2:
    x1,x2 = mop.get_x1_x2_delta(sequence[0], -sequence[1], -sequence[2])
    if x1 == x2:
        wzor = f"ano = C1*{x1}**n + n*C2*{x2}**n"
    else:
        wzor = f"ano = C1*{x1}**n + C2*{x2}**n"
    if len(sequence[3]) == 1:
        A = sequence[3]/(-sequence[1]+-sequence[2]+1)
        print(f"ans = {A}")

    print(f"an = {wzor} + {A}")
    Lside = np.array( [[1,1], [x1,x2]] )
    Rside = np.array( [a[0]-A, a[1]-A] )
    C1, C2 = list(np.linalg.solve(Lside,Rside))
    print(f"{C1} * {x1}**n, {C2} * {x2}**n + {A}")

