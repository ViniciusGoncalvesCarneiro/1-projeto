def func1():
    def func2(a,b):
        resultado = (a + b)
        return resultado
    func2(10,10)

    return func2(10,10)
print(func1())




