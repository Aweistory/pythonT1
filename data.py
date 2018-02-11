menu = ("F1","F2","F3","F5","F4")
print(menu)
# ~ menu[3]="F4"
# ~ menu[4]="F5"
# ~ print(menu[3])
menu = ("F1","F2","F3","F4","F5")
print(menu)

menu = ["F1","F2","F3","F5","F4"]
uMenu = ["F1","F12","F5"]
for mItem in uMenu:
    if mItem in menu:
        print(mItem + ",gogogo")
    else:
        print(mItem + ",no")

menu = []
if len(menu) > 0:
    print("menu is not empty")
else:
    print("menu is empty")

if menu:
    print("menu is not empty")
else:
    print("menu is empty")

people = {'name':'laji','age':10}
msg = "name is " + people['name'] + ",age is "+ str(people['age'])
print(msg.title())


people = {'name':'laji','name1':'laji','age':'10'}
for value in set(people.values()):
    print(value.title())

