# Demonstrating all core Python operators

# 1. Arithmetic Operators
a, b = 10, 3
print("Arithmetic:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)         # True division
print("a // b =", a // b)       # Floor division
print("a % b =", a % b)         # Modulo
print("a ** b =", a ** b)       # Exponentiation

# Matrix multiplication (@) (since Python 3.5+
mat1 = array([[1, 2], [3, 4]])
mat2 = array([[5, 6], [7, 8]])
print("\nMatrix multiplication:")
print("mat1 @ mat2 =\n", mat1 @ mat2)

# 2. Comparison Operators
print("\nComparison:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
# Chained comparison
print("1 < a < 20:", 1 < a < 20)

# 3. Assignment Operators
print("\nAssignment:")
x = 5
print("x =", x)
x += 2; print("x += 2 ->", x)
x -= 1; print("x -= 1 ->", x)
x *= 3; print("x *= 3 ->", x)
x /= 2; print("x /= 2 ->", x)
x %= 3; print("x %= 3 ->", x)
x **= 2; print("x **= 2 ->", x)
x //= 2; print("x //= 2 ->", x)
x <<= 1; print("x <<= 1 ->", x)
x >>= 1; print("x >>= 1 ->", x)
x &= 3; print("x &= 3 ->", x)
x |= 1; print("x |= 1 ->", x)
x ^= 2; print("x ^= 2 ->", x)

# Walrus operator (Python 3.8+)
print("\nWalrus operator:")
if (n := len([1, 2, 3, 4])) > 3:
    print("List length is", n)

# 4. Logical Operators
print("\nLogical:")
x, y = True, False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 5. Identity Operators
print("\nIdentity:")
lst1 = [1, 2]
lst2 = [1, 2]
lst3 = lst1
print("lst1 is lst2:", lst1 is lst2)
print("lst1 == lst2:", lst1 == lst2)
print("lst1 is lst3:", lst1 is lst3)

# 6. Membership Operators
print("\nMembership:")
s = "hello"
print("'h' in s:", 'h' in s)
print("'z' not in s:", 'z' not in s)

# 7. Bitwise Operators
print("\nBitwise:")
p, q = 6, 3  # binary: 110 and 011
print("p & q =", p & q)   # AND
print("p | q =", p | q)   # OR
print("p ^ q =", p ^ q)   # XOR
print("~p =", ~p)         # NOT (bitwise complement)
print("p << 1 =", p << 1) # Left shift
print("p >> 1 =", p >> 1) # Right shift