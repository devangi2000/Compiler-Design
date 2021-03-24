f=open(r"C:\Users\nikki\Desktop\study material\Compiler Design\Lab\ex2-LexicalAnalysis\ex2.c")
key=['int','float','string','include','stdio.h','char','break','if','else','switch','return','void'
,'while','struct','for']
iden=[]
sp={"(",")","{","}",";","&","#","$","\n",'"',","}
spec=["%d","%f","%c","%s"]
num="012345678910"
n=[]
k=[]
o=[]
l=[]
io=['scanf','printf','cin','cout']
op="+-%*=/^><"
dl=[]
F=[]
for lines in f:
 words=lines.split(" ")
 for i in range(len(words)):
    if words[i] in key:
        k.append(words[i])
    elif words[i] in io:
        l.append(words[i])
    elif words[i] in op:
        o.append(words[i])
    elif words[i] in sp:
        dl.append(words[i])
    elif words[i] in spec:
        F.append(words[i])
    elif words[i] in num:
        n.append(words[i])
    else:
        iden.append(words[i])
print("Keywords are: ")
print(set(k))
print("input/output are: ")
print(set(l))

print("Operators are: ")
print(set(o))
print("Special Symbols are: ")
print(set(dl))
print("Identifiers are: " )
print(set(iden))
print("Format Specifier are:")
print(set(F))
print("Constants are:")
print(set(n))