def frequency(l):
dl1=set(l)
dl=list(dl1)
newl=[]
for i in dl:
newl.append(l.count(i))
mi=min(newl)
ma=max(newl)
mil=[]
mal=[]
for j in range(len(newl)):
if newl[j]==mi:

mil.append(dl[j])
if newl[j]==ma:

mal.append(dl[j])
mil.sort()
mal.sort()
return(mil,mal)

def onehop(l):

new=[]
l.sort()
for i in range(len(l)):
for j in range(len(l)):
if l[i]!=l[j]:
if l[i][1]==l[j][0]:
q=l[i][0]
w=l[j][1]
if q!=w:
t=[q,w]
t=tuple(t)
if t not in new:
new.append(tuple(t))
new.sort()
return (new)
import ast

def parse(inp):
inp = ast.literal_eval(inp)
return (inp)

fncall = input()
lparen = fncall.find(&quot;(&quot;)
rparen = fncall.rfind(&quot;)&quot;)
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == &quot;frequency&quot;:
arg = parse(farg)
print(frequency(arg))

if fname == &quot;onehop&quot;:
arg = parse(farg)
print(onehop(arg))