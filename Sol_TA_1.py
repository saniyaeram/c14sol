import matplotlib.pyplot as plt

Year=[2017,2018,2019,2020]
Population=[19.756, 19.979, 20.185, 20.411]
	  
plt.bar(Year, Population)

plt.xlabel('Year')
plt.ylabel('Population in lakhs')

plt.title('Population Graph of Mumbai')

plt.show()