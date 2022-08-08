def main():
    print("Welcome to our club.")

    age = int(input("What's your age? "))


    if age >=21: 
        print("Come on in.")
    else:
        country = str(input("Where are you from? "))
        if country == "USA" and age <=21:
            print("Get out")
        else:
            if country == "Mali" and age >=15:
                print("Come on in.")
            else:
                if age >=18:
                    print("Come on in.")
                else: 
                    print("Get out.")





      
if __name__ == '__main__':
    main()
    