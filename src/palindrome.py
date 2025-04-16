import re


def is_palindrome():
    cont="y"
    palabra=input("ingrese la palabra para verificar si es palindrome")
    while cont=="y":
        if any(char.isdigit() for char in palabra):
            palabra=input("ingrese la palabra para verificar sin numeros")
        else:
            cont="n"

    palabra=palabra.lower()
    print(palabra)
    palabra_sin_signos = re.sub(r'[\s\W_]', '', palabra)
    print(palabra_sin_signos)
    return

if __name__ == "__main__":
    is_palindrome()