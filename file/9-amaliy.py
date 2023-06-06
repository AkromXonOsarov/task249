# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:56:15 2023

@author: User
"""

# Bo'sh lug'at yaratish
my_dict = {}
# Kalit-qiymat juftligi bilan lug'at yaratish
my_dict = {'kalit1': 'qiymat1', 'kalit2': 'qiymat2', 'kalit3': 'qiymat3'}


                     #Qiymatga murojaat qilish:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Kalit orqali qiymatni olish
name = my_dict['name']
print(name)  # Output: John
# get() metodi orqali qiymatni olish
age = my_dict.get('age')
print(age)  # Output: 25


                        #Qiymatni o'zgartirish va qo'shish:
my_dict = {'name': 'John', 'age': 25}
# Qiymatni o'zgartirish
my_dict['age'] = 30
# Qiymat qo'shish
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


                #Lug'atdan ma'lumot o'chirish:
my_dict = {'name': 'John', 'age': 25}
# Kalit orqali ma'lumotni o'chirish
del my_dict['age']
print(my_dict)  # Output: {'name': 'John'}


                       #Lug'atni qidirish:
my_dict = {'name': 'John', 'age': 25}
# Lug'atda berilgan kalitni qidirish
if 'name' in my_dict:
    print('Kalit mavjud')
# Lug'atdagi kalitlarni bo'shlig'iga tekshirish
if len(my_dict) == 0:
    print('Lug\'at bo\'sh')
    
    
    


