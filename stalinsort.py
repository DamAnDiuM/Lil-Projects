import random
def createArr(n) -> list:
	Arr = []
	for i in range(n):
		Arr.append(random.randint(1,9))
	return Arr
def stalinSort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        if not sorted_arr or arr[i] >= sorted_arr[-1]:
            sorted_arr.append(arr[i])
    return sorted_arr

arr = createArr(1_000_000)
sorted_arr = stalinSort(arr)
print(f"The # of elements in the sorted arr is {len(sorted_arr)} and only {round(len(sorted_arr) / len(arr) * 100, 2)}% survived")
		
