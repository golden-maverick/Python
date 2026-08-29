temp=float(input("Enter temperature: "))
if temp <=20:
    low=1
elif temp>=30:
    low=0
else:
    low=(30-temp)/10

if (temp <=20 or temp >=40):
    medium=0
elif temp<=30:
    medium=(temp-20)/10
else:
    medium=(40-temp)/10

if temp<=30:
    high=0
elif temp>=40:
    high=1
else:
    high=(temp-30)/10

slow_speed=30
medium_speed=60
high_speed=100

fan_speed= ((low*slow_speed)+(medium*medium_speed)+(high*high_speed))/(low+medium+high)

print("\nFuzzy membership values are:")
print("Low:", round(low,2))
print("Medium:", round(medium,2))
print("High:", round(high,2))
print("Fan speed is:", round(fan_speed,2))

print("\n Final fan speed is:", round(fan_speed,2),"%")


