#Sidhant Puntambekar
#Baggage Calculator

totalFee=0
numberofbags=input("How many bags are you traveling with: ")
numberofbags=int(numberofbags)
bagweight=input("How much do your bags weigh: ")
bagweight=int(bagweight)
international=input("Are you traveling internationally(Y/N): ")
premierstatus=input("Are you a Premier Status member(Y/N): ")



if (numberofbags=='1'):
    totalFee=totalFee+25
elif (numberofbags=='2'):
    totalFee=totalFee+35
elif (numberofbags>=3):
    totalFee= (totalFee+(60+(100*(numberofbags-2))))

if (international=='Y'):
    if (premierstatus=='Y'):
        if (numberofbags>=3):
            totalFee=totalFee-160

   
if (bagweight>70):
    totalFee=totalFee+(200*numberofbags)

if (bagweight>=51 and bagweight<=70):
    totalFee=totalFee+(100*numberofbags)

if (bagweight<=51):
    totalFee=totalFee+(0*numberofbags)
    
if (premierstatus=='Y'):
    if (numberofbags==1):
        totalFee=(totalFee-25)
    elif (numberofbags==2):
        totalFee=totalFee-35
    elif (numberofbags>=3):
        totalFee=totalFee-60

print(totalFee)



    
    
    
