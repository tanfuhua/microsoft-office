def calculate_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product

# 示例用法
my_array = [2, 3, 4, 5]
result = calculate_product(my_array)
print("数组乘积为:", result)