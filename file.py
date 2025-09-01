fp=open("amit.txt","w")
fp.write("hello friends")
print(fp.name)
print(fp.readable())
print(fp.writable())
print(fp.closed)

fp.close()
