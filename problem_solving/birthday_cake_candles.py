def birthdayCakeCandles(candles):
    # Write your code here
    tallest = 0
    tallest_count = 0
    for i in candles:
        if i > tallest:
            tallest = i
    for i in candles:
        if i == tallest:
            tallest_count += 1
    return tallest_count

print(birthdayCakeCandles([4,4,2,1]))