'''l1=["pune\n","dhule\n","solapur\n"]
fp=open("amit.txt","a")#append
fp.writelines(l1)
fp.close()'''

fp=open("amit.txt","r")
while True:
    s1=fp.readline()
    if s1 =="":
        break
    else:
        print(s1,end="")