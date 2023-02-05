def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False。减小判定区间，减少循环次数，提升效率"""
    # =======================================================
    number = n
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False
    # =======================================================


def reverse_prime(number):
    """接收一个正整数参数，找出并在同一行内输出所有小于number的反素数，每个数字后一个空格。
    反素数指某数i及其逆序数都是素数，但数i对应的字符串不是回文字符串。函数无返回值"""
    # ======================================================= 哈哈哈

    for i in range(10, number + 1):
        if is_prime(i):
            print(i, reversed(str(i)))

    # =======================================================


positive_int = int(input())
reverse_prime(positive_int)
