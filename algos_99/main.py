url = 'https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python'

intervals =  [
   [1, 4],
   [7, 10],

]
# ) => 4


def sum_of_intervals(intervals):
    list_values = []
    if len(intervals) == 1:
        return len(range(intervals[0][0], intervals[0][-1]))

    if len(intervals) == 2:
        return len(list(range(min(intervals[0]), max(intervals[1])))) -1



    for x in intervals:
        list_values.append(list(range(x[0], x[1])))
    res = []
    if set(list_values[0]).intersection(list_values[2]):
        res.append(list(set(list_values[0]) | set(list_values[2])))

    if set(list_values[1]).intersection(list_values[2]):
        res.append(list(set(list_values[1]) | set(list_values[2])))
    if len(res) < 2:
        x = len(range(res[0][0], res[0][-1]))
        y = len(range(list_values[2][0], list_values[2][-1]))
        return x + y

print(sum_of_intervals(intervals))
