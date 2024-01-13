import functools

# dwie funkcje o nazwach: double i triple, które odpowiednio będą podwajać i potrajać przekazaną wartość 
def mul(x, y):
    return x * y

double = functools.partial(mul, y=2)
triple = functools.partial(mul, y =3)

