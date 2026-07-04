# h2) First product price >= target using Binary Search

prices = [25000, 32000, 41000, 50000, 54000, 60000, 75000]
target = 50000

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1   # search left side for first occurrence
    else:
        low = mid + 1

if answer != -1:
    print("First product price >= target is:", prices[answer])
    print("Position:", answer)
else:
    print("No product found")