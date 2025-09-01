def Display(iRow):
    
    for i in range(1,iRow+1,1):
        print(" " * (iRow-i), end="")
        print("* "*i)
    
def main():
    print("Enter number of rows : ")
    Value1 = int(input())

    Display(Value1)