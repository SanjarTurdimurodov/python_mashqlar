

names = []
son = int(input("Nechta yaqin do'stingiz bor?  \n >>>   "))
for n in range(son):
    names.append(input(f"{n+1} - do'tingiz  ismini kiriting: \n >>>   "))
for name in names:
    
    if name == "sanjar" :
     print("Assalomu alaykum Sanjar aka, sog'liqlaringiz yaxshimi?")
    else:
     print(f" Assalomu alaykum {name.title()}, ishlar qaley.")







