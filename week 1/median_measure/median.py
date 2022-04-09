# Write your list_stats function here.


def list_stats(arr):
    n = len(arr)
    mean = sum(arr)/n
    arr.sort()
    mid = n/2
    median = 0
    mid = int(mid)
    if(n % 2 != 0):
        median = arr[mid]
    else:
        median = (arr[mid-1] + arr[mid])/2

    return median, mean

    # You can use this to test your function.
    # Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with the first example in the question.
    m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
    print(m)

    # Run your function with the second example in the question
    m = list_stats([1.5])
    print(m)
