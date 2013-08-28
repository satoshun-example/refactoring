## before
def total(a, b, c):
    a += b
    a += c
    return a

## after
def total2(a, b, c):
    total = a
    total += b
    total += c
    return total


if __name__ == '__main__':
    b = total(1, 3, 5)
    b2 = total2(1, 3, 5)

    assert b == b2
