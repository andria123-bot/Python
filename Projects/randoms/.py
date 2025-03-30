inp = int(input("Enter a num: "))
product = 1

for i in range(1, inp + 1):
  product *= i

print(f'{inp}. {product}')

