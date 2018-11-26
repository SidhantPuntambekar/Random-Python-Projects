#Sidhant Puntambekar
#Penny Doubling

def pow(base, exponent):
    product=base
    for n in range(exponent-1):
        product=product*base
    return product


numOfDays= input("How many days to double your penny: ")
numOfDays=int(numOfDays)
money=pow(2,numOfDays-1)/100
print("After", numOfDays,"days, you have: ", money)