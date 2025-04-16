def is_palindrome():
    cont="y"
    palabra=input("ingrese la palabra para verificar si es palindrome")   
    while cont=="y":
        if any(char.isdigit() for char in palabra):
            palabra=input("ingrese la palabra para verificar sin numeros")
        else:
            print(palabra)
            cont="n"
    return

if __name__ == "__main__":
    is_palindrome()