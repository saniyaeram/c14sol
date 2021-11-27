import matplotlib.pyplot as plt

Marks = [60, 65, 70, 50, 75, 80, 95, 85, 100, 90, 80, 40, 50, 75, 75, 95, 70, 99, 50, 75]

plt.hist(Marks)

plt.xlabel('Marks')
plt.ylabel('Count')

plt.show()