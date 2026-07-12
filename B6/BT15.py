"""Nhập một số nguyên n.

Hãy in ra:

n²
n³
n⁴

Ví dụ

Nhập: 3

n² = 9
n³ = 27
n⁴ = 81
"""
a = int(input("Nhập số nguyên : ")) #Nhập 3
b = int(input("Nhập mũ : ")) # mũ 2 3 4

t1 = a**b
print("")
print(f'{a}^{b} = {t1}')
