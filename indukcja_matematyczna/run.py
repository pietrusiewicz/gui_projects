n = int(input("Podaj n: "))
a,b = int(input("Podaj a: ")), int(input("Podaj b: "))
print(f"1. Równanie: {a}x + {b}y = {n}")
for x in range(1,n):
    for y in range(1,n):
        if a*x + b*y == n:
            print(f"x={x}")
            print(f"y={y}")
            print(f"{n} = {a} * {x}(x) + {b} * {y}(y)")

print(f"2. Zakładam, że: n>={n} i n={a}x + {b}y dla pewnych x,y ∈ N")

print(f"3. Udowodnię że istnieje x',y'∈N n+1 = {a}x'+{b}y'")
print(f"Mamy:")
for x in range(1,n):
    for y in range(1,n):
        if a*-x + b*y == 1:
            print(f"1 = {a} * {-x}(x) + {b} * {y}(y)")
            x1,y1=-x,y
            #return x,y

print(f"= {x}x + {y}y + {x}({x1}) + {y}({y1}) =")
print(f"= {x}(x + ({x1})) + {y}(y + ({y1})) =")
print(f"x'=x+({x1})")
print(f"y'=y+({y1})")
