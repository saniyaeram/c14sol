import matplotlib.pyplot as plt

Roll_No = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Marks = [60, 65, 70, 50, 75, 80, 95, 85, 100, 90]

plt.bar(Roll_No, Marks)

plt.xlabel('Roll Number')
plt.ylabel('Marks out of 100')

plt.show()