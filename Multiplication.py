#Sidhant Puntambekar
#Multiplication

column = input("How mant multiples of each number? ")
column = int(column)

print ("1   2   3   4   5   6   7   8   9   10")
print ("_______________________________________")


for i in range (column):
    for z in range (1,11):
        print ((i+1)*z, end="   ")
    print()