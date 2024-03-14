

son1=int(input("Istalgan sonni kiriting: \n→ "))
son2=int(input("Ikkinchi sonni kiriting:\n→ "))
if son1 > son2:
    print(f"Birinchi son ikkinchi sondan katta. {son1}>{son2}")
elif son1 < son2:
    print(f"Ikkinchi son birinchi sondan katta. {son1}<{son2}")
else:
    print(f"Siz teng sonlar kiritdingiz. {son1}={son2}")