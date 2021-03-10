def max(n1,n2,n3):
    maxno=0
    if n1>n2:
        if n1>n3:
            maxno=n1
    elif n2>n3:
        maxno=n2
    else:
        maxno=n3
    return maxno
def main():
    n1=int(input())
    n2=int(input())
    n3=int(input())
    print (max(n1,n2,n3))
if __name__=="__main__":
    main()