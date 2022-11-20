x=input("enter word")
y='AEIOU'
c=0
x=x.upper()
l=list(x)
l=set(l)
l=list(l)
for i in range(len(l)):
    for e in range(len(y)):
        if l[i]==y[e]:
            c=c+1
if c==len(y):
    print("contains all vowels")
else:
    print("does not contains all vowels")
