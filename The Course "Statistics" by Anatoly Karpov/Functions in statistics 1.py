def find_Dispersion(x):
    average = sum(x) / len(x)
    sm = 0
    for i in x:
        z = (i - average) ** 2
        sm += z
    return sm / (len(x) - 1)


def find_std(x):
    average = sum(x) / len(x)
    sm = 0
    for i in x:
        z = (i - average) ** 2
        sm += z
    dis = sm / (len(x) - 1)
    return dis ** 0.5


def find_Z_scores(x):
    average = sum(x) / len(x)
    z = []
    for i in x:
        z.append((i - average) / find_std(x))
    return z


def find_Se(x):
    return find_std(x) / (len(x) ** 0.5)


def find_cov(x, y):
    cardinality = len(x)
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)
    e = 0
    for i in range(len(x)):
        z = (x[i] - average_x) * (y[i] - average_y)
        e += z
    return e / (cardinality - 1)


def find_correlation_coefficient(x, y):
    return find_cov(x, y) / (find_std(x) * find_std(y))


def find_coefficient_determination(x, y):
    return find_correlation_coefficient(x, y) ** 2


def find_slope(x, y):
    return (find_std(y) / find_std(x)) * find_correlation_coefficient(x, y)


def find_intercept(x, y):
    average_y = sum(y) / len(y)
    average_x = sum(x) / len(x)
    return average_y - (find_slope(x, y) * average_x)


def main():
    a = [4, 5, 5, 3, 6]
    b = [2, 1, 5, 9, 6]
    print(find_Dispersion(a), find_Dispersion(b))
    print(find_std(a), find_std(b))
    print(find_Z_scores(a))
    print(find_Se(a))
    print(find_correlation_coefficient(a, b))
    print(find_coefficient_determination(a, b))
    print(find_slope(a, b))
    print(find_intercept(a, b))


if __name__ == '__main__':
    main()

