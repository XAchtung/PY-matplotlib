import matplotlib.pyplot as plt
uczen = []
srednia = []
file = open('eo.txt', 'r')
data = file.read().splitlines()
for i in data:
    broken = i.split(' ')
    uczen.append(broken[0])
    srednia.append(broken[-1])
plt.bar(uczen, srednia)
plt.xlabel('Uczen')
plt.ylabel('Srednia')
plt.show()