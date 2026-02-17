def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]

        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged

print(merge_intervals([[1,3],[2,6],[8,10]]))


# output : [[1, 6], [8, 10]]