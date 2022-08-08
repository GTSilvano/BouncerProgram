print("Welcome to our club.")

age = int(input("What's your age? "))
country = str(input("Where you from shawty? "))

if age >=21 and country == "USA":
    print("Enter my Yankee friend")
elif age <=21 and age >=18 and country == "USA":
    print("Sorry, this is not Europe")
elif age >= 15 and country =="Mali":
    print("Come in")
elif age <=15 and country =="Mali":
    print("Get out")    
elif age >= 18 and country != "USA":
    print("Please enter. Enjoy your evening!")
else:
    print("Get the fuck out you underage dog!")

def main():
      
    if __name__ == '__main__':
         main()