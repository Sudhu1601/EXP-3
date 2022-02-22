import itertools    

def get_v(word,substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve2(equation):
    left,right = equation.lower().replace(' ', '').split('=')
    print(left,right)
    left = left.split('+')
    print(left)
    letters = set(right)
    print(letters)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    print(letters)
    
    digits = range(15)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sum(get_v(word,sol) for word in left) == get_v(right, sol):
            print(' + '.join(str(get_v(word,sol)) for word in left )+ " = {} (mapping {})".format(get_v(right, sol),sol))
            
equation = input("Enter the equation:")
solve2(equation)
