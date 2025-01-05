
#arr =[1 ,2 ,3 ,4]
#N=input("Please enter Number :")
#N=int(N)
#for element in arr:
    #if element==N:
        #print(arr.index(N))
    #else:
        #print("Not found")




    #search(arr,3)

def search (arr,n):
    n=int(n)
    for element in arr:
        if element==n:
            return arr.index(n)
        else:
            print("not found")


if __name__=='__main__':
    arr=[1,2,3,4]
    print(search(arr,4))


