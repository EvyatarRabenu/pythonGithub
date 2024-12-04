class HardDisk:
    def __init__(self , size , files_list):
        self. size = size
        self.files_list = {}

    def __str__(self):
        return f"Size: {self.size} ,Files List: {self.files_list} "


    def usedSpace(self):
        return sum(self.files_list.values())

    def freeSpace(self):
        return self.size - sum(self.files_list.values())


    def addFile(self, name, size):
        if name not in self.files_list.keys():
            if self.freeSpace() - size > 0:
                self.files_list[name] = size
                return True
            else:
                print("No Space On Disk")
                return False
        else:
            print("The name is already exist")
            return False

    def delFile(self, name):
        if name in self.files_list.keys():
            self.size -= self.files_list[name]
            del self.files_list[name]
            print("The file is deleted")
            return True
        else:
            print("The File is not found")
            return False