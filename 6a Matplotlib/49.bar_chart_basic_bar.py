
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [2, 4, 6, 8, 10]
y = [4, 6, 8, 3, 9]
z = [1, 3, 5, 7, 9]

plt.bar(x, y, label='Diagram 1', color='r') # red
plt.bar(x, z, label='Diagram 2', color='c') # cyan
# plt.bar(x, y, label='Data 1', color='rgbkyr')
# plt.bar(x, y, label='Data 1', 
#     color=['r', 'g', 'b', 'k', 'y', 'r']
# )
# plt.bar(x, y, 
#     color=['r', 'g', 'b', 'y', 'k'], 
#     linewidth=5, edgecolor='black',    # edgecolor = 'rgbyk' ['r','g','b'] 
# )

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()

plt.show()