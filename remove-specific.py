
def remove_spec(arr, val):
    j=-1
    for i in range(len(arr)):
        if arr[i]!=val:
            j+=1
            arr[j]=arr[i]
    return arr,j+1



if __name__=='__main__':
    arr, k = remove_spec([0,1,2,6,3,4,2,5],2)
    print(sorted(arr[0:k]))