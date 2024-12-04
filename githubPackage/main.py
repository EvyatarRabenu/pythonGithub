from HardDisk import *


hard_disk1 = HardDisk(1000,[])

hard_disk1.addFile("file1",150)
print(hard_disk1)
print(f"Free space is: {hard_disk1.freeSpace()}")
print(f"Used space is: {hard_disk1.usedSpace()}")

hard_disk1.delFile("file2")
print(hard_disk1)