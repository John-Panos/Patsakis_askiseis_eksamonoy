from urllib.request import Request, urlopen
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
x = str(data)
y = x.index(":")
z = x.index(",")

#round
round_last = x[y+1:z]
duadiko=""
round_last = int(round_last)
round_l=round_last -99
for kati in range(round_l, round_last+1,1):
    kati_allo = str(kati)
    url = "https://drand.cloudflare.com/public/{0}".format(kati_allo)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    # πεδιο randomness
    a = x.split(":")
    a = str(a)
    a = a.split(",")
    b=a[3]
    b=b[3:-1]

    # κανει το rand binary
    def toBinary(a):
      l,m=[],[]
      for i in a:
        l.append(ord(i))
      for i in l:
        m.append(int(bin(i)[2:]))
      return m
    kapa=toBinary(b)

    for i in range(len(kapa)):
        lala=str(kapa[i])
        duadiko= duadiko +lala


ones=[]
zeros=[]
plo=0
plz=0
for mple in range(len(duadiko)):
    geia=int(duadiko[mple])
    if geia == 0:
        plz=plz+1
        if mple!=0 and plo!=0:
            ones.append(plo)
            plo=0

    elif geia == 1:
        plo=plo+1
        if mple!=0 and plz!=0:
            zeros.append(plz)
            plz=0

print("Mήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες:", max(ones) )
print("Μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά:", max(zeros))
