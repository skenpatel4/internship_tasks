class publisher:
    def Name(self,title):
        self.title=title
        print("The title is : " ,self.title)

class book(publisher):
    def data(self,pageNumber):
        self.pageNumber=int(pageNumber)
        print("the page no. is : " , self.pageNumber)

class type(publisher):
    def time(self,TIME):
        self.TIME=int(TIME)
        print("time for playing is : " , self.TIME)

a=book()
b=type()

a.Name("This is a title")
a.data(11)
b.time(1900)