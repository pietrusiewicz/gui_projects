class Calculator:
    def __init__(self):
        pass

    def menu(self):
        arithmetic_signs = "+-*/%^"
        a = int(input("Enter value a"))
        b = int(input("Enter value b"))
        print("Select arithmetic operation:")
        for i,sign in enumerate(arithmetic_signs):
            print(f"\t{i}) {sign}")
        sign = arithmetic_signs[int(input())]
        print(sign)

        expression = f"{a}{sign}{b}".replace("^", "**")
        result = eval(expression)
        print(f"result: {result}")


if __name__ == "__main__":
    c = Calculator()
    c.menu()

