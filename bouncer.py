import ast


with open('someData.txt', 'r') as f:
    contents = f.read()
    contents = contents[contents.index('{'):]
    age_restrictions = ast.literal_eval(contents)
        
def main():
    print("Welcome to our club.")

    age = int(input("What's your age? "))

    if age >= 21:
        print("Come on in.")
    else:
        country = str(input("Where are you from? "))
        if country in age_restrictions:
            if age >= age_restrictions[country]:
                print("Come on in.")
            else:
                print("Get out.")
        elif age >= 18:
            print("Come on in.")
        else:
            print("Get out.")

if __name__ == '__main__':
    main()