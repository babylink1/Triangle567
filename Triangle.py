def classifyTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 'NotATriangle'

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'NotATriangle'

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b == c:
        return 'Equilateral'
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'
