def merge_sorted_lists(arr1,m,arr2,n):
    p1=m-1
    p2=n-1
    fp=m+n-1
    del n, m
    while p2>-1 or p1>-1:
        if p1<0:
            arr1[0:p2+1] = arr2[0:p2+1]
            break
        elif p2<0:
            arr1[0:p1+1] = arr1[0:p1+1]
            break
        if arr2[p2] >= arr1[p1]:
            arr1[fp]=arr2[p2]
            fp-=1
            p2-=1
        else:
            arr1[fp]=arr1[p1]
            fp-=1
            p1-=1
arr1=[0]
merge_sorted_lists(arr1, 0, [1],1)
print(arr1)