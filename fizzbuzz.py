num=input().split(" ")
X=int(num[0])
Y=int(num[1])
end=int(num[2])
for i in range(1, end+1):
    if(i%X==0 and i%Y==0):
        print("FizzBuzz")
    elif(i%X==0):
        print("Fizz")
    elif(i%Y==0):
        print("Buzz")
    else:
        print(i)
