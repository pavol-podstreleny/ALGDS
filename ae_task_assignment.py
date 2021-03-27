from collections import deque

# O(n log n) time | O(n) space


def taskAssignment(k, tasks):

    taskMap = dict()

    i = 0
    for task in tasks:
        if task in taskMap:
            taskMap[task].append(i)
        else:
            taskMap[task] = deque([i])
        i += 1

    tasks.sort()

    result = []
    for i in range(len(tasks) // 2):
        task = tasks[i]
        taskLast = tasks[len(tasks)-1-i]

        smallestIndex = taskMap[task].popleft()
        largestIndex = taskMap[taskLast].pop()
        result.append([smallestIndex, largestIndex])

    return result
