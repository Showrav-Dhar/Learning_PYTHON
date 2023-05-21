def add_dip(a, b):
    return (a + b)


def subtract_dip(a, b):
    c = max(a, b) - min(b, a)
    return c


def find_max(l1):
    the_mx = l1[0]
    for i in range(len(l1)):
        if (l1[i] > the_mx):
            the_mx = l1[i]

    return the_mx;
