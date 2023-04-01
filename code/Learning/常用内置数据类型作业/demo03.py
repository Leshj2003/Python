# -*-  codeing = utf-8 -*-
# @Time : 2023/4/1 17:03
# @Author : LHJ青梦
# @File : demo03.py
# @Software: PyCharm

#凯撒密码
'''
import string

def caesar_cipher(plaintext):
    # 定义三个字符串，包含全部的小写字母、大写字母和数字字符
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits

    # 将每个字符向后偏移3位后替换成密文
    ciphertext = ''
    for c in plaintext:
        if c in lowers:
            ciphertext += lowers[(lowers.index(c) + 3) % 26]
        elif c in uppers:
            ciphertext += uppers[(uppers.index(c) + 3) % 26]
        elif c in digits:
            ciphertext += str((int(c) + 3) % 10)
        else:
            ciphertext += c

    return ciphertext

# 测试程序
plaintext = 'All roads lead to Rome.'
ciphertext = caesar_cipher(plaintext)
print(ciphertext) # Doo urdgv ohdg wr Urph.
'''

import string

def caesar_cipher(text):
    """接收一个字符串为参数，采用字母表和数字中后面第3个字符代替当前字符的方法
    对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    例如：2019 abc 替换为5342 def """
# 定义三个字符串，包含全部的小写字母、大写字母和数字字符
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits

    # 将每个字符向后偏移3位后替换成密文
    ciphertext = ''
    for c in plaintext:
        if c in lowers:
            ciphertext += lowers[(lowers.index(c) + 3) % 26]
        elif c in uppers:
            ciphertext += uppers[(uppers.index(c) + 3) % 26]
        elif c in digits:
            ciphertext += str((int(c) + 3) % 10)
        else:
            ciphertext += c

    return ciphertext

if __name__ == '__main__':
    plaintext = input()
    print(caesar_cipher(plaintext))
