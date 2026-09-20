from lib import add_numbers,greet 
def main ():
    """Головна функція програми."""
    result = add_numbers(5, 7)
    print (f"Результат додавання:{result}")

    massage = greet ("Студент")
    print (massage)

if __name__=="__main__":
    main()