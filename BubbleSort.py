l = [3,6,1,8,13,16,5,14,17,12,9,4]
n = len(l)

for j in range(n):
    for i in range(n-1):
        if l[i]>l[i+1]:
            a = l[i]
            b = l[i+1]
            (a, b) = (b, a)
            #print(a, b)
            c = l.index(a)
            l.remove (b)
            l.insert(c, b)
            
print(l)
            
    
      
    
    