l = [4, 2, 7, 1, 15, 13, 9, 16, 5, 18]
n = len(l)
erste_Hälfte = l[0:n//2]
#print(erste_Hälfte)
zweite_Hälfte = l[n//2:n]
#print(zweite_Hälfte)

def merge(l):
    if n <= 1:
        return l
    if n == 2:
        if l[0] > l[1]:
            a = l[0]
            b = l[1]
            l[0] = b
            l[1] = a
            #print (l)
    