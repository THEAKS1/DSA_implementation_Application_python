def problem(arr, query):

    # Assume array is arranged in descending order
    def condition(mid):
        if arr[mid] == query:
            return "Found"
        elif arr[mid] > query:
            return "Left"
        return "Right"

    return binary_search(0, len(arr)-1, condition)

def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == "Found":
            return mid
        elif result == "Left":
            high = mid - 1
        else:
            low = mid + 1
    return "Element not Found"
