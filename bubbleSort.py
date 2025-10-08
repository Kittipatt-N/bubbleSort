def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

# Ex.
data = [13, 29, 6, 4, 8]
print("before sort:", data)
sorted_data = bubble_sort(data)
print("after sort:", sorted_data)
