# Next Prime number
Var = 2
for i in range(Var, 9999):
    for u in range(2,Var):
        if i%u==0:
            break
    else:
        Var=i
        if Var==2:
            print("The first Prime number is : ", Var)
        else:
            print("The Next Prime Number is :", Var)
        z = str(input("If you want to exit, Press [E] \n If you want to see the next prime number then press enter \n"))
    if z=="E" or z=="e":
        break

print("Program Terminated")
print("Bye!")
input()
