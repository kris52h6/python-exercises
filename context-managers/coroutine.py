def calc_average(arr):
    total = 0
    for x in arr:
        total += x
    return total / len(arr)


def coroutine():
    print('Coroutine activated')
    nums = []
    while True:
        x = yield
        nums.append(x)
        avg = calc_average(nums)
        print(avg)


# def other_coroutine():
#     sum = 0.0
#     count = 0
#     avg = None
#     while True:
#         input = yield avg
#         sum += input
#         sum += input
#         count += 1
#         avg = sum/count


# x = coroutine()
# next(x)
# x.send(5)
# x.send(2)
