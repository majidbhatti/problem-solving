def my_sqrt(x):
        i = 0
        j = x
        mid = 0
        if x <= 1:
            return x
        while i <= j:
            mid = (i + j)//2
            if x/mid == mid:
                return mid
            elif x/mid > mid:
                i = mid + 1
            elif x/mid < mid:
                j = mid - 1

        return j

if __name__ == '__main__':
    print(my_sqrt(8))