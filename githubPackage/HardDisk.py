class HardDisk:
    def __init__(self , size , files_list):
        self. size = size
        self.files_list = {}


    def __str__(self):
        return f"Size: {self.size} , Used Space: {self.used_space()} , Free Space: {self.free_space()} ,\nFiles List: {self.files_list} "


    def used_space(self):
        """The method will return the size of the disk space"""
        self.space_in_disk = sum(self.files_list.values())
        return self.space_in_disk


    def free_space(self):
        """The method will return the free size of the disk"""
        return self.size - self.used_space()


    def add_file(self , name , size):
        if name in self.files_list:
            print(f"{name} is already exist")
            return False

        if self.free_space() < size:
            print(f"No Space for file: {name}")
            return False

        self.files_list[name] = size
        return True



    def del_file(self , name):
        if name in self.files_list:
            del self.files_list[name]
            return True

        print(f"File {name} doesnt exist")
        return False

    def update_file(self , name , new_size):
        if name not in self.files_list:
            print(f"File {name} doesnt exist")
            return False

        #Check if there is not enough space for the new size
        if self.free_space() + self.files_list[name] < new_size:
            print(f"No Space for updating file: {name}")
            return False

        # All Valid - update the file size
        self.files_list[name] = new_size
        return True