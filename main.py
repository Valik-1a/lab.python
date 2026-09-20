from lib import add_numbers,multiply_numbers,greet
def main ():
    """Головна функція програми."""
    result = add_numbers(5, 7)
    print (f"Результат додавання:{result}")
    multiplication=multiply_numbers(3,4)
    print (f"Результат множення:{multiplication}")

    massage = greet ("Студент")
    print (massage)

if __name__=="__main__":
    main()