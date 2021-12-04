text = input("# # # #")
x = str.split(text)
j = 0
for i in x:
    x[j] = int(x[j])-1
    j = j + 1
for i in x:
    print(i, end = ' ')