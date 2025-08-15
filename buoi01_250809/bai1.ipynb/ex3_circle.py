import math

# Nhập bán kính từ người dùng
r = float(input("Moi ban nhap ban kinh r: "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r**2

# In kết quả
print(f"Chu vi hinh tron: {cv}")
print(f"Dien tich hinh tron: {dt}")
