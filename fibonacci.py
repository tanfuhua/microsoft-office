def fibonacci(n):
    fib_list = [0, 1]  # 初始化斐波那契数列的前两个数
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])  # 生成下一个数并添加到列表中
    return fib_list

# 输入要生成的斐波那契数列的长度
length = int(input("请输入要生成的斐波那契数列的长度："))

# 调用函数生成斐波那契数列并打印结果
fibonacci_sequence = fibonacci(length)
print(fibonacci_sequence)