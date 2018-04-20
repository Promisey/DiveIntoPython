def sum67(nums):
    e = 0
    f = 0
    m = 0
    n = {}
    list6 = [a for a in range(len(nums)) if nums[a] == 6]
    list7 = [b for b in range(len(nums)) if nums[b] == 7]
    cleanlist7 = [s for s in list7 if s > list6[0]]

    for i in list6:
        n[i] = cleanlist7[m]
        m = m + 1
    print(n)

    for c in n.keys():
        for d in nums[c:n[c]+1]:
            e = e + d
    print('e=',e)

    for sum in nums:
        f = f + sum

    result = f - e
#    print(result)

    return result

if __name__ == '__main__':
    print(sum67([1, 2, 2]))
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
    print(sum67([1, 1, 6, 7, 2]))
    print(sum67([1, 2, 7, 6, 7, 6, 7, 7]))