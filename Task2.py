#Задача №2______________________________________________________________

import matplotlib.pyplot as plt
import random

homes = 15
def house_prices(homes):
    house_prices = []
    for _ in range(homes):
        price = random.randint(3000000, 20000000)
        house_prices.append(price)
    return house_prices
   
def area_houses(homes):
    area_houses = []
    for _ in range(homes):
        area = random.randint(100, 300)
        area_houses.append(area)
    return area_houses

def all_home(homes):
    all_home = []
    for i in range(homes):
        all_home.append(f'Дом {i+1}')
    return all_home

def square_meter_price_l(homes, house_prices,area_houses):
    square_meter_price_list = []
    for i in range(homes):
        square_meter_price = house_prices[i]//area_houses[i]
        square_meter_price_list.append(square_meter_price)
    return square_meter_price_list

def homes_50000(homes, square_meter_price_list):
    homes_50000 = []
    for i in range(homes):
        if square_meter_price_list[i] < 50000:
            homes_50000.append(f'Дом {i+1}')
    return homes_50000

def area_50000(homes, square_meter_price_list,area_houses):
    area_50000 =[]
    for i in range(homes):
        if square_meter_price_list[i] < 50000:
            area_50000.append(area_houses[i])
    return area_50000

house_pric = house_prices(homes)
area_hous = area_houses(homes)
all_h = all_home(homes)
smpl = square_meter_price_l(homes, house_pric, area_hous)
print(smpl)
h_50000 = homes_50000(homes, smpl)
a_50000 = area_50000(homes, smpl,area_hous)


ax = plt.subplot(2, 1, 1)
ax.set_title('Цена за квадратный метр каждого дома')
plt.bar(all_h, smpl)
ax = plt.subplot(2, 1, 2)
ax.set_title('Площадь домомов цена за кв.м., которых меньше 50 000')
plt.bar(h_50000, a_50000)
plt.show()

