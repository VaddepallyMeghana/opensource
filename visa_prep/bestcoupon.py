X = float(input())
amount_after_10_percent = 0.90 * X
amount_after_flat_100 = X - 100
final_amount = min(amount_after_10_percent, amount_after_flat_100)
print(int(final_amount))
