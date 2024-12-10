class File:
    # Attributes : name , suffix , size
    def __init__(self , name , suffix , size):
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
        print("i am _repr_")
        return f"{self.name} , {self.suffix} , Size: {self.size}"


if __name__ == "_main_":
    file1 = File("file1", "docx", 30)
    file2 = File("file2", "txt", 60)
    file3 = File("file3", "txt", 100)

    print(file1)
    print(file2)
    print(file3)

    list_files = [file1, file2, file3]
    print(list_files)