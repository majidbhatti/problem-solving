def plus_one(digits) -> list:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        num = 0
        for n in digits:
            num = num * 10 + n
        num += 1
        del digits
        l = []
        while num > 0:
            l.append(num % 10)
            num = num // 10
        l = l[::-1]
        return l

if __name__ == '__main__':
    print(plus_one([9]))