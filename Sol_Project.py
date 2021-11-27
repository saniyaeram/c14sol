import matplotlib.pyplot as plt

Classes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
No_of_Students = [60, 65, 60, 50, 55, 40, 30, 35, 40, 40] 

plt.bar(Classes, No_of_Students, color ='maroon')
 
plt.xlabel("Grades")
plt.ylabel("No. of students enrolled")

plt.title("Students enrolled in different classes")

plt.show()