from calc_func import do_addition,do_substraction

def main():
    print("Welcome to the calculator app")
    print("""\n select a function from the given choices
          1. Add
          2. Substract
            """)
    user_input=int(input('Select a function'))
    a=int(input('Enter the value of A '))
    b=int(input('Enter the value of B '))

    if user_input==1:
        result=do_addition(a,b)
        print("The sum is {}".format(result))
    elif user_input==2:
        result=do_substraction(a,b)
        print("The substraction is {}".format(result))


if __name__=="__main__":
    main()



        