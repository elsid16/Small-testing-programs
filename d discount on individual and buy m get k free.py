import itertools

#INPUTS{
n=int(input("Number of items: "))
m=int(input("Buy these many clothes: "))
k=int(input("To get free these many clothes: "))
d=float(input("Discount rate: "))
price=[]
for i in range(n):
    price.append(float(input("Cost of cloth", i, ": ")))
#}
'''
#tries{
n=2
m=3
k=2
d=20
price=[200,100]
#}
'''
if n<m+k:
    print(sum(price)-sum(price)*d/100)
    quit()
l=list(itertools.permutations(price))
#print(list(l))
amt=[]
'''
for i in range(len(l)):
    amt.append([l[i][0]+l[i][1]+l[i][2]-min(l[i][:3])-l[i][3]*d/100+l[i][3],l[i][0],l[i][1],l[i][2],l[i][3]])
print(sorted(amt))
'''

final=[]
r=n%(m+k)
for y in range(0,n//m+k,m+k):
    for i in range(len(l)):
        f=0
        e=m+k
        a=sum(l[i])
        amt=list(l[i])
        for j in range(n//(m+k)-y):
            least=sorted(l[i][f:e])
            #print(l[i][f:e])
            #a-=least
            z=least[:k]
            a-=sum(z)
            f+=m+k
            e+=m+k
            amt.append("Neglected: ")
            amt.append(z)
        for j in range(n-(n%(m+k)),n):
            a-=l[i][j]*d/100
            #print(l[i][j])
            amt.append("On discount: ")
            amt.append(l[i][j])
        #print(a)
        #print()
        g=[a]
        g.extend(amt)
        final.append(g)
fi=sorted(final)
for i in range(len(fi)):
    print(fi[i])
