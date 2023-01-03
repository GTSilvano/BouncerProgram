def main():
    print("Welcome to our club.")

    with open("age_restrictions.py") as f:
        exec(f.read())

    age = int(input("What's your age? "))

    if age >= 21:
        print("Come on in.")
    else:
        country = str(input("Where are you from? "))
        if country in globals()["age_restrictions"]:
            if age >= globals()["age_restrictions"][country]:
                print("Come on in.")
            else:
                print("Get out.")
        elif age >= 18:
            print("Come on in.")
        else:
            print("Get out.")

if __name__ == '__main__':
    main()