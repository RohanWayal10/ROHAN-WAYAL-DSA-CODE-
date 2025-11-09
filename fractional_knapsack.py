class Parcel:
    def __init__(self, profit, weight):
        self.p = profit
        self.w = weight
        self.r = profit / weight if weight != 0 else 0

def fractional_knapsack(capacity, parcels):
    parcels.sort(key=lambda x: x.r, reverse=True)
    total_profit = 0.0
    cap_left = capacity

    print("\nParcels sorted by ratio (profit/weight):")
    for p in parcels:
        print(f"Profit={p.p}, Weight={p.w}, Ratio={p.r:.2f}")

    for item in parcels:
        if cap_left == 0:
            break
        if item.w <= cap_left:
            total_profit += item.p
            cap_left -= item.w
            print(f"Taking full parcel: Profit={item.p}, Weight={item.w}")
        else:
            frac = cap_left / item.w
            total_profit += item.p * frac
            print(f"Taking {frac:.2f} fraction of parcel: Profit={item.p}, Weight={item.w}")
            cap_left = 0
    return total_profit

# --- Main Program ---
n = int(input("Enter number of parcels: "))
parcels = []
for i in range(n):
    p, w = map(float, input(f"Enter profit and weight of parcel {i+1}: ").split())
    parcels.append(Parcel(p, w))

cap = float(input("Enter truck capacity: "))
profit = fractional_knapsack(cap, parcels)
print(f"\nMaximum Profit = {profit:.2f}")
