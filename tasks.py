def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x.title < pivot.title]
        greater_than_pivot = [x for x in arr[1:] if x.title >= pivot.title]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
