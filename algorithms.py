

# greatest common denominator #
def gcd(a, b):
	while(b != 0):
		t= a
		a= b
		b= t%b

	return a

# power #
def power(num, pow):
	if pow == 0:
		return 1
	else:
		return num * power(num, pow-1)

# factorial #
def fact(num):
	if num == 0:
		return 1
	else:
		return num * fact(num-1)

# bubble sort #
def Bsort(args):
	for i in range(len(args)-1, 0, -1):
		for j in range(i):
			if args[j] > args[j+1]:
				temp= args[j]
				args[j]= args[j+1]
				args[j+1]= temp

# merge sort #
def Msort(args):
	if len(args) > 1:
		mid= len(args) // 2
		leftarr= args[:mid]
		rightarr= args[mid:]

		Msort(leftarr)
		Msort(rightarr)

		li=0 #left array index
		ri=0 #right array index
		si=0 #sorted array index

		while li < len(leftarr) and ri < len(rightarr):
			if leftarr[li] < rightarr[ri]:
				args[si]= leftarr[li]
				li= li+1
			else:
				args[si]= rightarr[ri]
				ri= ri+1
			si= si+1

		while li < len(leftarr):
			args[si]= leftarr[li]
			li= li+1
			si= si+1

		while ri < len(rightarr):
			args[si]= leftarr[ri]
			ri= ri+1
			si= si+1

# quick sort #
def Qsort(args, first, last):
	if first < last:
		pi= partition(args, first, last) #pivot value index
		Qsort(args, first, pi-1)
		Qsort(args, pi+1, last)

def partition(arr, first, last):
	pv= arr[first] #pivot value
	li= first+1 #lower index
	ui= last #upper index

	done= True
	while not done:
		while li <= ui and arr[li] <= pv: li= li+1
		while ui >= li and arr[ui] >= pv: ui= ui-1
		if ui < li: done= True
		else:
			temp= arr[li]
			arr[li]= arr[ui]
			arr[ui]= temp

	temp= arr[first]
	arr[first]= arr[ui]
	arr[ui]= temp

	return ui

# unordered list search #
def Usearch(item, items):
	for i in range(len(items)):
		if items[i] == item:
			return i
	return None

# ordered list search #
def Osearch(item, items):
	li= 0 #lower index
	ui= len(items)-1 #upper index

	while li <= ui:
		mid= (li+ui)//2
		if item == items[mid]: return mid
		if item > items[mid]: li= mid
		if item < items[mid]: ui= mid
	if li > ui: return None

# unique filtering #
def Ufilter(items):
	f= dict()
	for key in items:
		f[key]= 0
	return set(f.keys())

# value counting #
def valueCounter(items):
	counter= dict()
	for key in items:
		if key in counter.keys(): counter[key]+= 1
		else: counter[key]= 1
	return counter

# finfing max value #
def maxof(items):
	if len(items) == 1: return items[0]
	a= items[0]
	b= maxof(items[1:])
	if a > b: return a
	else: return b 