def someone(name, food='Pizza'):
    if name.lower() == 'saif':
        print(f"Hey {name}")
    print(f'Shetai  {name}  {food}')

    return name


de = someone('Saif')

print(de)


def exp(num1, num2):
    return num1 ** num2


num = exp(5, 2)

print(num)
