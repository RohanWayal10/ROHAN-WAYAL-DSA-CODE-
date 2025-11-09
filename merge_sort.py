def merge_sort(orders):
    if len(orders) <= 1:
        return orders
    
    mid = len(orders) // 2
    left_half = merge_sort(orders[:mid])
    right_half = merge_sort(orders[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_orders = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i]['delivery_time'] <= right[j]['delivery_time']:
            sorted_orders.append(left[i])
            i += 1
        else:
            sorted_orders.append(right[j])
            j += 1
    
    sorted_orders.extend(left[i:])
    sorted_orders.extend(right[j:])
    
    return sorted_orders

# ---- Taking input from user ----
orders = []
n = int(input("Enter number of orders: "))

for i in range(n):
    order_id = input(f"Enter Order ID for order {i+1}: ")
    delivery_time = int(input(f"Enter Delivery Time (in minutes) for {order_id}: "))
    orders.append({'order_id': order_id, 'delivery_time': delivery_time})

# ---- Sorting ----
sorted_orders = merge_sort(orders)

# ---- Displaying Result ----
print("\nOrders sorted by delivery time:")
for order in sorted_orders:
    print(f"Order ID: {order['order_id']}, Delivery Time: {order['delivery_time']} minutes")
