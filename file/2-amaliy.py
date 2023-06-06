# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:45:50 2023

@author: User
"""

ismlar = ["Abror", "Mahmud", "Hasan"]        #1-misol
#print(ismlar)
for ism in ismlar:
    print(f"Salom, {ism}! jura bugun choyxonaga boramizmi!")       #2-misol


sonlar = [7, -15, 42, -3, 10]
musbat_sonlar = []
manfiy_sonlar = []
butun_sonlar = []
onlik_sonlar = []
for son in sonlar:
    if son > 0:
        musbat_sonlar.append(son)
    elif son < 0:
        manfiy_sonlar.append(son)
    if isinstance(son, int):
        butun_sonlar.append(son)
    if isinstance(son, float):
        onlik_sonlar.append(son)
print("Musbat sonlar:", musbat_sonlar)
print("Manfiy sonlar:", manfiy_sonlar)
print("Butun sonlar:", butun_sonlar)
print("O'nlik sonlar:", onlik_sonlar)                    #3-misol


sonlar = [7, -15, 42, -3, 10, 3.14, -0.5]
musbat_sonlar = []
manfiy_sonlar = []
butun_sonlar = []
onlik_sonlar = []
for son in sonlar:
    if son > 0:
        musbat_sonlar.append(son)
    elif son < 0:
        manfiy_sonlar.append(son)
    if isinstance(son, int):
        butun_sonlar.append(son)
    if isinstance(son, float):
        onlik_sonlar.append(son)
print("Musbat sonlar:", musbat_sonlar)
print("Manfiy sonlar:", manfiy_sonlar)
print("Butun sonlar:", butun_sonlar)
print("O'nlik sonlar:", onlik_sonlar)                        #4-misol
print()

t_shaxslar = ["Muhammad Ali", "Amir Temur", "Abu Rayhon Beruniy"]
vaz_shaxslar = ["Elon Musk", "Malala Yousafzai", "Emma Watson"]
print("Tarixiy shaxslar:")
for shaxs in t_shaxslar:
    print(shaxs)
print("\nVaziyatdagi shaxslar:")
for shaxs in vaz_shaxslar:
    print(shaxs)                                       #5-misol
print()


t_shaxslar = ["Muhammad Ali", "Amir Temur", "Abu Rayhon Beruniy"]
vaz_shaxslar = ["Elon Musk", "Malala Yousafzai", "Emma Watson"]
tarixiy_shaxs = t_shaxslar.pop()
print("Men tarixiy shaxslardan", tarixiy_shaxs,"bilan")
vaziyatdagi_shaxs = vaz_shaxslar.pop()
print("Zamonaviy shaxslardan esa", vaziyatdagi_shaxs,"bilan suhbat qilishni istar edim")              #6-misol


friends = []
friends.append("Ali")
friends.append("Vali")
friends.append("Hasan")
friends.append("Husan")
friends.append("Lola")
friends.append("Sarvar")
print(friends)                                      #7-misol

friends.remove("Hasan")  # Hasan ni o'chirib tashlaymiz
friends.remove("Lola")   # Lola ni o'chirib tashlaymiz         
print(friends)                                       #8-misol

friends.append("Sarvar")   # Oxiriga "Sarvar" nomini qo'shamiz
friends.insert(0, "Aziz")  # Boshiga "Aziz" nomini qo'shamiz
friends.insert(2, "Lola")  # 2-indexga "Lola" nomini qo'shamiz
print(friends)                                #9-misol


friends = ["Ali", "Vali", "Hasan", "Husan", "Lola", "Sarvar"]
friends.remove("Hasan")  # Hasan ni o'chirib tashlaymiz
friends.remove("Lola")   # Lola ni o'chirib tashlaymiz
print(friends)



