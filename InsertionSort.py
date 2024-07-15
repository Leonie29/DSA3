l = [3, 1, 5, 2, 17, 15, 20, 13, 19, 18 ]
n = len(l)

for i in range(1, n):
    for j in range(0, i):
        if l[j] < l[j-1]:
            a = l[j]
            b = l[j-1]
            #(a, b) = (b, a)
            l[j] = b
            l[j-1] = a
            #print(a,b)
            #c = l.index(b) (erste Version des Vertauschens)
            #l.remove (a)
            #l.insert(c, a)
            #print(l)
        else:
            continue
        
print(l)