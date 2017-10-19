# developer name: Reynaldo Garcia
# instructor: Dr. Nelson Rushton - Theory of Automata

primesList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

#if c1, c2, c3 ... cn are unicode characters let f("c1, ... ,cn") = product of Pi ^ atoi(ci) fron i = 1 to n
def f(S):
    i = 0
    a = 1
    n = len(S)
    while i < n:
        a *= primesList[i]**(ord(S[i]))
        i += 1
    return a

print(f("foo"))
