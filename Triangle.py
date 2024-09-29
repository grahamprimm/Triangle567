def classifyTriangle(a, b, c):
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return 'NotATriangle'
    
    if a == b and b == c:
        return 'Equilateral'
    
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    
    if a == b or b == c or a == c:
        return 'Isoceles'
    
    return 'Scalene'
