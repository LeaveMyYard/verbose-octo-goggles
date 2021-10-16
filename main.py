nums = [1, 3, 4, 7, 6, 8, 11, 0]


def main_bad_way() -> None:
    res = []
    for num in nums:
        if num % 2 == 0:
            res.append(num)

    print(nums)
    print(res)


def main_better_way() -> None:
    res = [num for num in nums if num % 2 == 0]

    print(nums)
    print(res)


def main_another_way() -> None:
    res = list(filter(lambda num: num % 2 == 0, nums))

    print(nums)
    print(res)


if __name__ == "__main__":
    main_another_way()