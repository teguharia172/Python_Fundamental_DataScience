
import csv

listku = [
    ['no', 'produk', 'harga'],
    [1, 'Batik', 250000],
    [2, 'Celana', 300000],
    [3, 'Drone', 10000000],
    [4, 'Kamera', 2000000],
    [5, 'Balon Udara', 25000000]
]

# writerow: write satu data
# with open('gudang.csv', 'w', newline = '') as fileku:
#     tulis = csv.writer(fileku)
#     tulis.writerow(listku[1])

# append untuk writerow: write satu data
# with open('gudang.csv', 'a', newline = '') as fileku:
#     tulis = csv.writer(fileku)
#     tulis.writerow(listku[1])

# with open('gudang.csv', 'w', newline = '') as fileku:
#     tulis = csv.writer(fileku)
#     for i in listku:
#         tulis.writerow(i)

# writerows: write semua data sekaligus
with open('gudang.csv', 'w', newline = '') as fileku:
    tulis = csv.writer(fileku)
    tulis.writerows(listku)