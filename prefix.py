def prefix(a, b):
    for i, n in enumerate(zip(a, b)):
        if n[0] != n[1]:
            return a[0:i]
    if len(a) > len(b):
        return b
    else:
        return a

