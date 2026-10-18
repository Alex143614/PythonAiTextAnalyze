import function

def main():
    while True:
        print("\n")
        print("REVIEW ANALYZER (Hugging Face)")
        print("1. analyze text from input")
        print("2. analyze text from file")
        print("3. exit")
        choice = input("input 1/2/3: ")
        choice = choice.strip()
        if choice == "1":
            text = input("input review: ")
            function.analyze_single(text)
        elif choice == "2":
            reviews = function.load_reviews()
            function.analyze_list(reviews)
        elif choice == "3":
            print("Bye")
            break  
        else:
            print("Wrong input, it must be 1/2/3")
if __name__ == "__main__":
    main()