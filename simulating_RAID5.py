#!/Users/yz/github/myenv/bin/python

#RAID 5 works by distributing data and parity information across multiple disks. 
#If one disk fails, the missing data can be reconstructed using the parity information stored on the other disks. 
#Below is a simplified example to illustrate how RAID 5 works, including the distribution of data and parity across three disks.

import numpy as np

# Sample data to be stored in the RAID array
data_blocks = ['data1', 'data2', 'data3', 'data5', 'data6', 'data7', 'data8', 'data9']

disk1 = []
disk2 = []
disk3 = []

# Function to calculate parity (XOR of data blocks)
def calculate_parity(blocks):
    parity = 0
    for block in blocks:
        parity ^= int.from_bytes(block.encode(), 'little')
    return parity.to_bytes((parity.bit_length() + 7) // 8, 'little').decode(errors='ignore')

# Distribute data and parity across disks
for i in range(0, len(data_blocks), 2):
    # For each pair of data blocks, calculate parity and distribute
    if i // 2 % 3 == 0:
        disk1.append(data_blocks[i])
        disk2.append(data_blocks[i + 1])
        disk3.append(calculate_parity([data_blocks[i], data_blocks[i + 1]]))
    elif i // 2 % 3 == 1:
        disk1.append(calculate_parity([data_blocks[i], data_blocks[i + 1]]))
        disk2.append(data_blocks[i])
        disk3.append(data_blocks[i + 1])
    else:
        disk1.append(data_blocks[i + 1])
        disk2.append(calculate_parity([data_blocks[i], data_blocks[i + 1]]))
        disk3.append(data_blocks[i])

# Print the content of each disk
print("Disk 1:", disk1)
print("Disk 2:", disk2)
print("Disk 3:", disk3)

# Simulate a disk failure (e.g., Disk 2 fails)
failed_disk_index = 1

# Recover data from the failed disk
recovered_data = []
for i in range(len(disk1)):
    if failed_disk_index == 0:
        recovered_data.append(calculate_parity([disk2[i], disk3[i]]))
    elif failed_disk_index == 1:
        recovered_data.append(calculate_parity([disk1[i], disk3[i]]))
    else:
        recovered_data.append(calculate_parity([disk1[i], disk2[i]]))

print("\nRecovered data for Disk 2:", recovered_data)
