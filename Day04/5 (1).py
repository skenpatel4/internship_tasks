#Variable-length arguements.
def sum(*n1):
    sum=0
    for i in n1:
        sum=sum+i

    print("answer is ", sum)


sum(10,20)
sum(10,20,30)