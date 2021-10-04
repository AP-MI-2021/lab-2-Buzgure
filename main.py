def is_prime(n):
    '''
    Determina daca un numar este prim sau nu.
    Input: 
    - n : intreg
    Output:
    - prim: bool care va fi true daca numarul este prim, respectiv 
    false daca numarul nu este prim 
    '''
    prim = True
    if n<2:
        prim = False
    for i in range (2,n):
        if n%i == 0:
            prim = False
    return prim
def get_largest_prime_below(n):
    '''
    Determina cel mai mare numar prim mai mic decat n
    - Input: 
    - n: intreg
    Output:
    - cel mai mare numar prim mai mic decat n
    '''
    
    for i in range (n,2,-1):
        check = is_prime(i)
        if check == True:
            return i
def test_get_largest_prime_below ():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(1) == None
test_get_largest_prime_below()
def main():
    while True:
        print('1.Cel mai mare numar prim mai mic decat un numar dat.')
        print('2....')
        print('x. Exit')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            nr = int(input('Dati un numar: '))
            C = get_largest_prime_below(nr)
            print(f'Cel mai mare numar prim mai mic decat {nr} este {C}')
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')
            
main()