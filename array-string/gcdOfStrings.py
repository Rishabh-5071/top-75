#using buit in gcd funtion

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    length = gcd(len(str1), len(str2))

    return str1[:length]


#using Euclid's Algorithm

def gcdOfStrings2(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    a = len(str1)
    b = len(str2)

    while b != 0:
        a, b = b, a % b

    return str1[:a]
