import re


def is_palindrome():
    cont="y"
    palabra=input("ingrese la palabra para verificar si es palindrome:")
    while cont=="y":
        if any(char.isdigit() for char in palabra):
            palabra=input("ingrese la palabra para verificar sin numeros:")
        else:
            cont="n"

    palabra=palabra.lower()
    palabra_sin_signos = re.sub(r'[\s\W_]', '', palabra)
    
    if palabra_sin_signos==palabra_sin_signos[::-1]:
        print("Es un palindrome")
    else:
        print("No es un palindrome")
    return

if __name__ == "__main__":
    is_palindrome()