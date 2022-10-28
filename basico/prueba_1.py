# for i in range(1,5):
#     print(i, "multiplied by 8 =", i*8)

# contador = 0

# for a in range(0,2):
#     contador += 1
#     for b in range(0,2):
#         contador += 1
#         for c in range(0,2):
#             contador += 1
#             for d in range(0,2):
#                 contador += 1
#                 for g in range(0,2):
#                     contador += 1
#                     for f in range(0,2):
#                         contador += 1

# print(contador)

# games = []
# while True:
#     print('hi')


# print('Toppr', end=' ')

# print('is awesome')

L = list(map(int, input('Ingrese una lista: ')))

count=0
for i in L:
	if i!=0:
		print(i, end=" ")
		count+=1
	else:
		continue
for i in range(len(L)-count):
	print(0, end=" ")

###
#La función map() recibe una función como entrada y un 
# interable y devuelve la función aplicada al iterable
###

# def addition(n):
#     return n + n

# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

