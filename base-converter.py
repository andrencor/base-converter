def int_input(x, y = 10):
    while True:
        try:
            opt = int(input(x), y)
        except:
            print()
            continue
        else:
            print()
            return opt


def sel_base():
    while True:
        opt = int_input('1 - Binário | 2 - Octal | 3 - Decimal | 4 - Hexadecimal\nEscolha uma base: ')
        if opt == 1:
            n = int_input("Insira o número em Binário: ", 2)
            return [bin(n), n]
        elif opt == 2:
            n = int_input("Insira o número em Octal: ", 8)
            return [oct(n), n]
        elif opt == 3:
            n = int_input("Insira o número em Decimal: ", 10)
            return [int(n), n]
        elif opt == 4:
            n = int_input("Insira o número em Hexadecimal: ", 16)
            return [hex(n), n]
        else:
            continue


while True:
    n1 = sel_base()
    while True:
        opt = int_input('1 - Somar (+) | 2 - Subtrair (-) | 3 - Converter\nEscolha uma operação: ')
        if opt == 1:
            n2 = sel_base()
            n3 = n1[1] + n2[1]
            print(f'{n1[0]} + {n2[0]} --> Binário: {bin(n3)}')
            print(f'{n1[0]} + {n2[0]} --> Octal: {oct(n3)}')
            print(f'{n1[0]} + {n2[0]} --> Decimal: {int(n3)}')
            print(f'{n1[0]} + {n2[0]} --> Hexadecimal: {hex(n3)}')
            print()
            break
        elif opt == 2:
            n2 = sel_base()
            n3 = n1[1] - n2[1]
            print(f'{n1[0]} - {n2[0]} --> Binário: {bin(n3)}')
            print(f'{n1[0]} - {n2[0]} --> Octal: {oct(n3)}')
            print(f'{n1[0]} - {n2[0]} --> Decimal: {int(n3)}')
            print(f'{n1[0]} - {n2[0]} --> Hexadecimal: {hex(n3)}')
            print()
            break
        elif opt == 3:
            print(f'{n1[0]} --> Binário: {bin(n1[1])}')
            print(f'{n1[0]} --> Octal: {oct(n1[1])}')
            print(f'{n1[0]} --> Decimal: {int(n1[1])}')
            print(f'{n1[0]} --> Hexadecimal: {hex(n1[1])}')
            print()
            break
        else:
            continue
