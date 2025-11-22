import numpy as np    
data_1 = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
data_4 = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
def num_letters(num_rows, num_columns):

    return num_rows + num_columns + num_rows+ num_columns -4 

assert num_letters(13, 4)== 30
assert num_letters(4,4)== 12
assert num_letters(6,4)== 16
assert num_letters(6,7)== 22
    
data_1[0,0] = 'A'        
print("Checking assertion.")
rows, columns = data_1.shape
ls =[]
words=[]
c=0
b=0
d= 1
e= 1
x=0
y=1
i=0
while c < columns:
    ls.append(str(data_1[0,c])) # Top Row
    c+=1
while b < columns:
    ls.append(str(data_1[12,b])) # Bottom Row
    b+=1
while d < rows:
    ls.append(str(data_1[d,0])) #First Column
    if d == 11: # Before getting to the first letter of last row
        d+=1
    d+=1
while e < rows:
    ls.append(str(data_1[e,3])) # Last Column
    if e == 11: # Before getting to the first letter of last row
        e+=1
    e+=1
while i < len(ls):
    words.append(ls[x]+ls[y])
    x=x+2
    y=y+2
    i+=2

r,c = data_2.shape
listing =[]
wording=[]
tr=0
br=0
fc= 1
lc= 1
o=0
p=1
q=0
while tr < c:
    listing.append(str(data_2[0,tr])) # Top Row
    tr+=1
while br < c:
    listing.append(str(data_2[3,br])) # Bottom Row
    br+=1
while fc < r:
    listing.append(str(data_2[fc,0])) #First Column
    if fc == 2: # Before getting to the first letter of last row
        fc+=1
    fc+=1
while lc < r:
    listing.append(str(data_2[lc,3])) # Last Column
    if lc == 2: # Before getting to the first letter of last row
        lc+=1
    lc+=1
while q < len(listing):
    wording.append(listing[o]+listing[p])
    o=o+2
    p=p+2
    q+=2

h,u = data_3.shape
lister =[]
worder=[]
trow=0
brow=0
fcolum= 1
lcolum= 1
ox=0
py=1
qlist=0
while trow < u:
    lister.append(str(data_3[0,trow])) # Top Row
    trow+=1
while brow < u:
    lister.append(str(data_3[5,brow])) # Bottom Row
    brow+=1
while fcolum < h:
    lister.append(str(data_3[fcolum,0])) #First Column
    if fcolum == 4: # Before getting to the first letter of last row
        fcolum+=1
    fcolum+=1
while lcolum < h:
    lister.append(str(data_3[lcolum,3])) # Last Column
    if lcolum == 4: # Before getting to the first letter of last row
        lcolum+=1
    lcolum+=1
while qlist < len(lister):
    worder.append(lister[ox]+lister[py])
    ox=ox+2
    py=py+2
    qlist+=2

z,m = data_4.shape
listering =[]
wordering=[]
trowing=0
browing=0
fcoluming= 1
lcoluming= 1
oa=0
pa=1
qlisting=0
while trowing < m:
    listering.append(str(data_4[0,trowing])) # Top Row
    trowing+=1
while browing < m:
    listering.append(str(data_4[5,browing])) # Bottom Row
    browing+=1
while fcoluming < z:
    listering.append(str(data_4[fcoluming,0])) #First Column
    if fcoluming == 4: # Before getting to the first letter of last row
        fcoluming+=1
    fcoluming+=1
while lcoluming < z:
    listering.append(str(data_4[lcoluming,6])) # Last Column
    if lcoluming == 4: # Before getting to the first letter of last row
        lcoluming+=1
    lcoluming+=1
while qlisting < len(listering):
    wordering.append(listering[oa]+listering[pa])
    oa=oa+2
    pa=pa+2
    qlisting+=2

print(words)
print(wording)
print(worder)
print(wordering)

        
    
    
    
    
    



