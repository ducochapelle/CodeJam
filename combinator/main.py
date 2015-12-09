from random import randint
b = "{0}+13*{1}/{2}+{3}+12*{4}-{5}-11+{6}*{7}/{8}-10"
c = b.format(1,2,3,4,5,6,7,8,9)


def generate(list):
    a = randint(1,9)
    if len(list) == 0:
        return generate([a])
    elif len(list) < 9:
        while a in list:
            a = randint(1,9)
        return generate(list + [a])
    return list

for n in range(10000):
    d = b.format(*generate([]))
    e = eval(d)
    print d, e
    if e == 66:
        break


