import random
from itertools import product
from timeit import default_timer as timer
import helms
import chest
import hands
import legs


#  < 30: fast roll
# 30-69: med roll
# >= 70: fat roll
max_weight = float(input("Enter max equip load: "))
equipment_weight = float(input("Enter equipment weight: "))
nof_outfits = int(input("Enter number of outfits: "))

f_roll = (max_weight / 100 * 30) - equipment_weight
m_roll = (max_weight / 100 * 69) - equipment_weight

full_outfit = {}

# Generate combinations
all_combos = [
    dict(x)
    for x in product(
        helms.helms.items(), chest.chest.items(), hands.hands.items(), legs.legs.items()
    )
]

# save outfits in dictionary
start = timer()
max_poise = 0.02
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
        outfit_list.append(round(total_weight + equipment_weight, 1))
        outfit_list.append(round(total_poise, 1))
        full_outfit[i] = outfit_list
        if total_poise > max_poise:
            max_poise = total_poise
            max_poise_outfit = outfit_list

stop = timer()

# print random outfit / max poise outfit
print(
    "\nCreated",
    nof_outfits,
    "out of",
    len(all_combos),
    "possible combinations in",
    round(stop - start, 2),
    "s:",
)
for j in range(nof_outfits):
    print(random.choice(list(full_outfit.values())))

print("\n---Best Poise---")
print(max_poise_outfit)
