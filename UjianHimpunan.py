#soal himpunan
a = set([2,4,6,8,10,12,14,16,18,20])
b = set([1,3,5,7,9,11,13,15,17,19])
c = set([-9,-8,-7,-6,-5,-4,-3,-2,-1])
d = set([2,3,5,7,11,13,17,19])
e = set([4,6,8,9,10,12,14,15,16,18])

#soal a
print(a | b | c | d | e)

#soal b

print((a & b) | (d & e))

#soal c
print((a | b) & (d | e))

#soal d
print((a | b) - (d | e))

#soal e
print((a|b|c) - (a & e))






