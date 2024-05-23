
def remove_duplicates(arr):
    j=0
    for i in range(1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]
    return arr

if __name__ == "__main__":
    print(remove_duplicates([1,2,2,3,4,5,5,5,6]))