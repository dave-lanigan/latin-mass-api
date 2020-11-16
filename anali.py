import json
import matplotlib.pyplot as plt

with open('latin-mass-data-v0.json') as f:
    data = json.load(f)


name, year = [], []
keys = list(data["fssp"].keys())
for k in keys:
    if data["fssp"][k]["date"] != "":
        name.append(data["fssp"][k]["name"])
        year.append(int(data["fssp"][k]["date"][:4]))


year.sort()
min_, max_ = year[0], year[-1]
years_ = list(range(min_, max_))


total = []
for y in years_:
    total.append(year.count(y))


print(total)
cum_total = total.copy()
for i, t in enumerate(cum_total):
    if i > 0:
        cum_total[i] = cum_total[i]+cum_total[i-1]

print("lens")
print(len(years_))
print(len(total))
print(len(cum_total))


plt.scatter(years_, cum_total)
plt.show()
