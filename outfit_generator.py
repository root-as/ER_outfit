import random
from itertools import product

from numpy import full

# TODO:
# Create 4 dictionaries: {item_name, [weight, poise]}
# input: max stamina --> calculate max / med roll weight
# output: x random outfits / max poise outfit


#  < 30: fast roll
# 30-69: med roll
# >= 70: fat roll
max_weight = float(input("Enter max equip load: "))
nof_outfits = int(input("Enter number of outfits: "))
# print(max_weight)

f_roll = max_weight / 100 * 30
m_roll = max_weight / 100 * 69


helms = {}
chest = {}
hands = {}
lower = {}
full_outfit = {}

# helms
helms["A"] = [10, 20]
helms["B"] = [3, 4]

# chest
chest["C"] = [10, 2]
chest["D"] = [3, 4]

# hands
hands["E"] = [10, 20]
hands["F"] = [30, 45]

# legs
lower["G"] = [10, 52]
lower["H"] = [3, 4]

# Output
all_combos = [
    dict(x) for x in product(helms.items(), chest.items(), hands.items(), lower.items())
]

max_poise = 0.0
max_poise_outfit = []
for i in range(len(all_combos)):
    total_weight = 0.0
    total_poise = 0.0
    outfit_list = []
    for key in all_combos[i]:
        total_weight += all_combos[i][key][0]
        total_poise += all_combos[i][key][1]
        outfit_list.append(key)
    if total_weight >= f_roll and total_weight <= m_roll:
        outfit_list.append(total_weight)
        outfit_list.append(total_poise)
        full_outfit[i] = outfit_list
        if total_poise > max_poise:
            max_poise = total_poise
            max_poise_outfit = outfit_list


for j in range(nof_outfits):
    print(random.choice(list(full_outfit.values())))
print("---Best Poise 4 items---")
print(max_poise_outfit)
