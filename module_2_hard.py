import random
stones = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def field():
    field1 = random.choice(stones)
    return(field1)
field1_ = field()
def get_password(n):
    field2 = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                field2.append(f'{i}{j}')
    result = ' '.join(field2) # с пробелом красивее, пары видны
    return result
n = field1_
result = get_password(n)
print(f'{n} - {result}')
