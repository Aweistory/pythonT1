txt=" hello world! "
print(txt)
print(txt.title())
print(txt.upper())
print(txt.lower())
print(txt.strip())
print("\t"+txt)

listTxt = ['das','qwe','aaa']
print(listTxt[2].title());
listTxt.insert(1,'gg')
print(listTxt);
listTxt.sort()
# ~ #print(listTxt);
# ~ #listTxt.sort(reverse=True)
print(listTxt);
i=0
for txt in reversed(listTxt):
    i=i+1
    print(str(i)+":\t"+txt)

print("\n")


i=0
for txt in listTxt:
    i=i+1
    print(str(i)+":\t"+txt)

for value in range(1,21):
    print(value)

listNum = list(range(1,1000001))
# ~ for value in listNum:
    # ~ print(value)
print(sum(listNum))

for value in range(1,21,2):
    print(value)

for value in list(range(3,31,3)):
    print(value)

for value in range(1,11):
    print(value ** value)

print([value**value for value in range(1,11)])
