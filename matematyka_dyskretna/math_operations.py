def get_x1_x2_delta(a,b,c):
    delta = b*b - 4*a*c
    sqrt_delta = delta**(1/2)
    x1 = (-b - sqrt_delta) / (2*a)
    x2 = (-b + sqrt_delta) / (2*a)
    return x1,x2
