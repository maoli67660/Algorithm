n = 9999 * 1000
ls = range(2, n + 1, 2)
while len(ls) != 1:
    if len(ls) > 1:
        ls = ls[1::2]
    if len(ls) > 1:
        ls = ls[-2:0:-2]
print(list(ls))
