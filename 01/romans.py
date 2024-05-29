def int_to_roman(num):
  #encoding: utf-8
def int_to_roman(num):
    num = int(input("Digite um valor númerico: "))
    sub = num
    while sub != 0:
        if sub == 1:
            sub = sub - 1
            print("I", end="")
        elif sub == 4:
            sub -= 4
            print("IV", end="")
        elif sub < 5:
            sub = sub - 1
            print("v", end="")
        elif sub == 9:
            sub -= 9
            print("IX", end="")
        elif sub < 10:
            sub = sub - 5
            print("V", end="")
        elif sub == 40:
            sub = sub - 40
            print("XL", end="")
        elif sub < 50:
            sub = sub - 10
            print("X", end="")
        elif sub < 100:
            sub = sub - 50
            print("L", end="")
        elif sub < 500:
            sub = sub - 100
            print("C", end="")
        elif sub < 1000:
            sub = sub - 500
            print("D", end="")

int_to_roman(0)
        

def roman_to_int(s):
    # Implemente sua função aqui
    pass
