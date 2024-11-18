# -*- coding: utf-8 -*-
"""
Author: Tygors Woo
Create on: 2019-04
"""


# 简单的取余加密函数
import random


def encrypt(m: str) -> str:
    # 凯撒密码
    s = "abcdefghijklmnopqrstuvwxyz"  # noqa
    n = ""
    for i in m:
        j = (s.find(i) + 13) % 26
        n = n + s[j]
    return n


def decrypt(m: str, k: int) -> str:
    s = "abcdefghijklmnopqrstuvwxyz"
    n = ""
    for i in m:
        j = (s.find(i) + 26 - k) % 26
        n = n + s[j]
    return n


def modexp(x, n, p):
    # x^n(mod p)的递归定义
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n//2, p)
    if n % 2 != 0:
        tmp = (tmp * x) % p
    return tmp


# 利用欧几里得算法求最大公因数
def gcd(a, b):
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    return gcd(a-b, b)


# 改良后的欧几里得算法求最大公因数
def gcd_new(a, b):
    """
    尽管欧几里得算法易于理解和编程，但不够高效，在a>>b时尤其如此
    模运算可以解决这个问题
    当a-b<b时，减法结果等于a除以b的余数，因此可以去掉减法
    而仅用一个递归调用交换a和b
    """
    if b == 0:
        return a
    return gcd_new(b, a % b)


# 扩展gcd函数
def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)


# 实现RSA算法
def gen_keys(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(m, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(m, e)
    if b < 0:
        d = m + b
    else:
        d = b
    return ((e, d, n))


def encrypt_new(msg, e, n: int):
    chunk_size = n.bit_length() // 8
    all_chunks = str_to_chunks(msg, chunk_size)
    return [modexp(msg_chunk, e, n) for msg_chunk in all_chunks]


def decrypt_new(cipher_chunks, d, n):
    chunk_size = n.bit_length() // 8
    plain_chunks = [modexp(cipher_chunk, d, n) for cipher_chunk in cipher_chunks]
    return chunks_to_str(plain_chunks, chunk_size)


def str_to_chunks(msg, chunk_size):
    msg_bytes = bytes(msg, "utf-8")
    hex_str = "".join([f"{b:02x}" for b in msg_bytes])
    num_chunks = len(hex_str) // chunk_size
    chunk_list = []
    for i in range(0, num_chunks * chunk_size + 1, chunk_size):
        chunk_list.append(hex_str[i:i + chunk_size])
    chunk_list = [eval("0x" + x) for x in chunk_list if x]
    return chunk_list


def chunks_to_str(chunk_list, chunk_size):
    hex_list = []
    for chunk in chunk_list:
        hex_str = hex(chunk)[2:]
        clen = len(hex_str)
        hex_list.append("0" * ((chunk_size - clen) % 2) + hex_str)
    hstring = "".join(hex_list)
    msg_array = bytearray.fromhex(hstring)
    return msg_array.decode("utf-8")