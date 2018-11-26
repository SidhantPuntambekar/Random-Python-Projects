#Sidhant Puntambekar
#TempConverter

#input
fahrenheitTemp = input("Please enter degrees Fahrenheit: ")
fahrenheitTemp = int(fahrenheitTemp)

#processing
celsiusTemp = (fahrenheitTemp-32) * (5/9)

#output
print(fahrenheitTemp,"degrees F is equal to", celsiusTemp, "degrees C.")
