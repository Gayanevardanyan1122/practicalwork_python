def get_median(data):
  sum = 0
  count = 0
  for num in data:
    sum += num
    count += 1
  return sum / count
data = [1, 4, 6, 9 ]
print(get_median(data))
