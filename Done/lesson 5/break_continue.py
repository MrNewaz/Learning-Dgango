items = ['One', 'Two', 'Three', 'Four', 'Five']

for item in items:

    if item == 'Two':
        # continue
        break

    print(item)

num = 0

while num <= 20:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
