#Variable-length arguements.
def myfunction(**args):
    for i,j in args.items():
        print(i,j)

myfunction(firstname='sken',lastname='patel')