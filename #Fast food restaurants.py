#Fast food restaurants
import numpy as np
#city,country,latitude,longitude,name,postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(1,2,4,5,6,7), unpack=True, dtype=('U66','U66',float,float,'U132',int), skip_header=1,invalid_raise=False )
city,country,latitude,longitude,name,postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(1,2,4,5,6,7), unpack=True, dtype=None, skip_header=1,invalid_raise=False )

print(city)
print(country)
print(latitude)
print(longitude)
print(name)
print(postalCode)


#Statistics_operation_on_fast_food_restaurant
print("Fast food restaurant latitude mean: " ,np.mean(latitude))
print("Fast food restaurant latitude average: " , np.average(latitude))
print("Fast food restaurant latitude std: " , np.std(latitude))
print("Fast food restaurant latitudemod: " , np.median(latitude))
print("Fast food restaurant latitude percentile - 25: " , np.percentile(latitude,25))
print("Fast food restaurant latitudepercentile  - 75: " , np.percentile(latitude,75))
print("Fast food restaurant latitude percentile  - 3: " , np.percentile(latitude,3))
print("Fast food restaurant latitude min : " , np.min(latitude))
print("Fast food restaurant latitude max : " , np.max(latitude))

# fast food restaurant math operations
print("fast food restaurant latitude square",np.square(latitude))
print("fast food restaurant latitude sqrt",np.sqrt(latitude))
print("fast food restaurant latitude pow",np.power(latitude,latitude))
print("fast food restaurant latitude abs",np.abs(latitude))
# Perform basic arithmetic operations
addition=latitude+longitude
substraction=latitude-longitude
multiplication = latitude* longitude
