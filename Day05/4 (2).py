class cal4:
    
    def setdata(self):
        self.n=int(input("Enter the number :"))
    
    def display(self):  
        ans = self.n**2
        return ans    


sum=cal4()
sum.setdata()
print(sum.display())