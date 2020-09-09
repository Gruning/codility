_input = [2, 3, 1, 5]
_len = len(_input)
_lenPlusTwo = _len + 2
_sum = 0
gathered = sum(_input)
for x in range(1, _lenPlusTwo):
    _sum = _sum + x


gathered = sum(_input)
print(_sum - gathered)
