# O(n log n) time | O(n) space
def mergeOverlappingIntervals(intervals):

	sortedIntervals = sorted(intervals, key=lambda x: x[0])
	result = [sortedIntervals[0]]


    for i in range(1,len(sortedIntervals)):
		actualInterval = sortedIntervals[i]
		minActualInterval = actualInterval[0]
		maxActualInterval = actualInterval[1]
		
		if minActualInterval <= result[-1][1]:
			lastInterval = result.pop()
			lastInterval[1] = max(lastInterval[1],maxActualInterval)
			result.append(lastInterval)
		else:
			result.append(actualInterval)
	
	return result
			
    
