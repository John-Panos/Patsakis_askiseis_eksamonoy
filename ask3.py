import string
all_chars=string.ascii_letters +" "
with open("two_citites_ascii.txt") as f:
    data=f.read()
fil_text=""
for c in data:
    if c in all_chars:
        fil_text= fil_text + c

lekseis=fil_text.split(" ")
x=len(lekseis)
x=x-1
for y in range(0,x,2):
    w1=lekseis[y]
    z1=len(w1)
    for k in range(x ,0 ,-1):
        w2=lekseis[k]
        z2=len(w2)
        if z1+z2==20:
            lekseis[y]=" "
            lekseis[k]=" "

lekseis2=[]
for i in lekseis:
    if i !='':
        lekseis2.append(i)
lekseis3=[]
for i in lekseis2:
    if i !=' ':
        lekseis3.append(i)
lekseis=[]
for i in lekseis3:
    lekseis.append(i)

x=len(lekseis)
pl=[]
for b in range(21):
    pl.append(0)
for y in lekseis:
    w=len(y)
    for x in range(20):
        if w == x+1:
            pl[x]= pl[x]+1
    if w > 20:
        pl[20] =pl [20] +1

for m in range(20):
    print(pl[m] , "λέξεις με" ,m+1, "γράμματα")
print(pl[20], "λέξεις με 20+ γράμματα")
