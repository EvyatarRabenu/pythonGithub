class File:
    # Attributes : name , suffix , size
    def __init__(self , name , suffix , size):
        if type(size) != int:
            raise TypeError('size must be int!!')
        if type(name) != str:
            raise TypeError('name must be string!!')
        if type(suffix) != str:
            raise TypeError('suffix must be string!!')
        if len(suffix)<2:
            raise ValueError('suffix too short!!')
        if size < 0:
            size = 0

        self.name = name
        self.suffix = suffix
        self.size = size

    def __str__(self):
        print("i am _str_")
        return f"{self.name} , {self.suffix} , Size: {self.size}"

    # מדפיסה גם אובייקט אחד וגם רשימה של אובייקטים
    # שמים את פונקציה זו אם יהיה לי סדרה שנרצה להדפיס
    # נשתמש בפונקציה זו רק אם רוצים להדפיס אובייקט ברשימה
    def __repr__(self):
        return f"{self.name}.{self.suffix}  Size: {self.size}"

    def __eq__(self, other):
        if self.name == other.name and self.suffix == other.suffix:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.size > other.size

if __name__ == "__main__":
    file1 = File("file1", "docx", 30)
    file2 = File("file2", "txt", 60)
    file3 = File("file3", "txt", 100)
    file4 = File("file3", "txt", 100)

    print(file1)
    print(file2)
    print(file3)

    list_files = [file1, file2, file3]
    print(list_files)

    print(file3==file4)
    print(file4 in list_files)