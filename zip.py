s1 = {1, 2, 3}
s2 = {"a", "b", "c"}

s3 = list(zip(s1, s2))

print(s3)

l1 = [10, 20, 30, 40, 50]
l2 = [100, 200, 300, 400, 500]

for x, y in zip(l1,l2[::-1]):
    print(x,y)