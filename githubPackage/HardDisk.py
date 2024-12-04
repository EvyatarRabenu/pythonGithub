class HardDisk:
    def _init_(self , size , files_list):
        self. size = size
        self.files_list = {}

    def _str_(self):
        return f"Size: {self.size} ,Files List: {self.files_list} "


    def usedSpace(self):
        return sum(self.files_list.values())

    def freeSpace(self):
        return self.size - sum(self.files_list.values())

    def addFile(self , name , size):
        space_flag = False
        name_flag = False
        if self.freeSpace() - size > 0:
            space_flag = True
        else:
            print("No Space On Disk")
        if name is self.files_list.keys():
            print("The name is already exist")
        else:
            name_flag = True
        if name_flag and space_flag:
            self.files_list[name] = size
