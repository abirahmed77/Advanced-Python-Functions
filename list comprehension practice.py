num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

e = [i for i in num if i % 2 ==0]
o = [i for i in num if i % 2 !=0]

print(e)
print(o)

f = ["banana","mango","apple","pineapple","watermelon","orange"]

capF = [f.capitalize() for f in f]
print(capF)

upperF = [f.upper() for f in f]
print(upperF)
