class cal1:
    n1=0
    n2=0
    n3=0
    
    def setdata(self, n1, n2, n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    
    def display(self):
        ans = self.n1 + self.n2 + self.n3
        print("The sum is : " , ans)

sum=cal1()
sum.setdata(10,20,30)
sum.display()