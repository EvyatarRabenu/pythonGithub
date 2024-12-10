from File import *

class HardDiskFiles:
    def __init__(self , size):
        self. size = size
        self.files = [] # שינינו את המילון לרשימה כי הוא צריך להיות רשימה של אובייקטים מסוג FILE


    def __str__(self):
        return f"Size: {self.size} , Used Space: {self.used_space()} , Free Space: {self.free_space()} ,\nFiles List: {self.files} "


    def used_space(self):
        """The method will return the size of the disk space"""
        sum_sizes = 0
        for file in self.files:
            sum_sizes += file.size
        return sum_sizes


    def free_space(self):
        """The method will return the free size of the disk"""
        return self.size - self.used_space()


    def add_file(self , name , size):
        if name in self.files:
            print(f"{name} is already exist")
            return False

        if self.free_space() < size:
            print(f"No Space for file: {name}")
            return False

        self.files[name] = size
        return True



    def del_file(self , name):
        if name in self.files:
            del self.files[name]
            return True

        print(f"File {name} doesnt exist")
        return False

    def update_file(self , name , new_size):
        if name not in self.files:
            print(f"File {name} doesnt exist")
            return False

        #Check if there is not enough space for the new size
        if self.free_space() + self.files[name] < new_size:
            print(f"No Space for updating file: {name}")
            return False

        # All Valid - update the file size
        self.files[name] = new_size
        return True


# class File:
#     # Attributes : name , suffix , size
#     def _init_(self , name , suffix , size):
#         self.name = name
#         self.suffix = suffix
#         self.size = size
#
#     def _str_(self):
#         print("i am _str_")
#         return f"{self.name} , {self.suffix} , Size: {self.size}"
#
#
#     # מדפיסה גם אובייקט אחד וגם רשימה של אובייקטים
#     # שמים את פונקציה זו אם יהיה לי סדרה שנרצה להדפיס
#     # נשתמש בפונקציה זו רק אם רוצים להדפיס אובייקט ברשימה
#     def _repr_(self):
#         print("i am _repr_")
#         return f"{self.name} , {self.suffix} , Size: {self.size}"


hd1 = HardDiskFiles(200)

file1 = File("file1", "docx", 30)
file2 = File("file2", "txt", 60)
file3 = File("file3", "txt", 100)

hd1.files = [file1 , file2 , file3]

print(hd1.used_space())
print(hd1.free_space())