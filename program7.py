def Display(iRow, iCol):
    
    for i in range(1,iRow+1,1):
        print("$\t"*iCol)
    
def main():
    print("Enter number of rows : ")
    Value1 = int(input())

    print("Enter number of columns : ")
    Value2 = int(input())

    Display(Value1,Value2)


main()