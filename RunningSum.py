def runningSum(nums: list) -> list:
    """
    Дан список целых чисел. Необходимо вернуть список "бегущая" сумма.
    Бегущая сумма - это когда текущий элемент списка равен сумме всех
    предыдущих элементов первоначального списка, включая текущий элемент.
    runSum[i] = nums[0]+nums[1]+...+nums[i]
    numbers = [1, 2, 4, 6, 0, 1, 10]
    runSum =  [1, 3, 7, 13, 13, 14, 24]
    """
    runSum = nums[0]
    for idx in range(1, len(nums)):
        nums[idx] += runSum
        runSum = nums[idx]
    print(nums)

numbers = [1,2,3,4]


runningSum(numbers)