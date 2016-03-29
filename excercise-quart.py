# coding=utf-8
__author__ = 'duanxiaoyu'
"""
1.编写函数，要求输入x与y，返回x和y的平方差
"""
def squredifferenc(x, y):
    a = x ** 2
    b = y ** 2
    return a - b


def quadraticsum(x, y):
    # 2. 计算1到100的平方的和
    sum_quad = 0
    for i in range(x, y):
        sum_quad = sum_quad + i ** 2
    return sum_quad


def judge_num(x):
    # 3. 编写函数，若输入为小于100的数，返回TRUE，大于100的数，返回FALSE
    input_num = input(u"请输入一个数字：")
    if input_num > x:
        print u"大于", x
        return False
    else:
        print u"小于", x
        return True


def split_figures(four_num):
    if four_num < 1000 or four_num > 9999:
        print "Not for figures number"
        return 0, 0, 0, 0
    else:
        a = four_num % 10
        result = four_num / 10
        b = result % 10
        result /= 10
        c = result % 10
        result /= 10
        d = result % 10
        print four_num, a, b, c, d
    return a, b, c, d

def merge_figures(a, b, c, d):
    """
    :rtype : object
    """
    result = d * 1000 + c * 100 + b * 10 + a
    return result
def digit_encrypt(x):
    result = (x + 5)%10
    return result
"""
4. 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下： 
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
编写加密的函数与解密的函数。
"""
def encrypt_num(in_num):
    a,b,c,d = split_figures(in_num)
    a = digit_encrypt(a)
    b = digit_encrypt(b)
    c = digit_encrypt(c)
    d = digit_encrypt(d)
    a,d = d,a
    b,c = c,b
    result = merge_figures(a,b,c,d)
    return result
def decrypt_num(in_num):
    result = encrypt_num(in_num)
    return result
def main():
    print squredifferenc(5, 4)
    print quadraticsum(1, 100)
    print judge_num(100)
    print judge_num(100)
    a,b,c,d = split_figures(1357)
    result = merge_figures(a,b,c,d)
    print result
    original_message = 3456
    message = encrypt_num(original_message)
    result = decrypt_num(message)
    print original_message,message,result
if __name__ == '__main__':
    main()
