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


    def add_file(self , file:File):
        if file in self.files:
            print(f"{file.name}.{file.suffix} is already exist")
            return False

        if self.free_space() < file.size:
            print(f"No Space for file: {file.name}.{file.suffix}")
            return False

        self.files.append(file)
        return True



    def del_file(self , file:File):
        if file in self.files:
            self.files.remove(file)
            return True

        print(f"{file.name}.{file.suffix} doesnt exist")
        return False

    def update_file(self , file:File):
        if file not in self.files:
            print(f"{file.name}.{file.suffix} doesnt exist")
            return False
        file_index = self.files.index(file)

        #Check if there is not enough space for the new size
        if self.used_space() + self.files[file_index].size < file.size:
            print(f"No Space for updating: {file.name}.{file.suffix}")
            return False

        # All Valid - update the file size
        self.files[file_index] = file
        return True


hd1 = HardDiskFiles(200)

file1 = File("file1", "docx", 30)
file2 = File("file2", "txt", 60)
file3 = File("file3", "txt", 100)
file4 = File("file3", "txt", 100)

#hd1.files = [file1 , file2 , file3]
hd1.add_file(file1)
hd1.add_file(file2)
hd1.add_file(file3)
hd1.add_file(file4)

#print(hd1.used_space())
#print(hd1.free_space())
print(hd1)

hd1.del_file(file2)
print(hd1)

file1 = File("file1", "docx", 50)
hd1.update_file(file1)

print(hd1)