# Args:


# Uma "arg" nada mais é do que uma função que executa uma especialidade em uma seguência de termos. Por exemplo, é pode fazer com que número subsequentes se somam entre si,

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum+= i
    return sum
    

print(add(1, 2, 3, 4, 5, 6))
