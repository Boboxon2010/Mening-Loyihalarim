# for4
# n=float(input())
# for i in range(1,11):
#     print(i,"kg konfet",i*n,"so'm turadi")
# for 5
import numpy as np

n = float(input("1 kg konfet narxini kiriting (so'mda): "))

# 0.1 dan 1.0 gacha 0.1 qadam bilan
for i in np.arange(0.1, 1.1, 0.1):
    print(f"{i} kg konfet narxi {i*n} so'm turadi")

#for 6
for i in np.arange(1.2,2.2,0.2):
    print(f"{i} kg konfetning narxi {i*n} so'm turadi")