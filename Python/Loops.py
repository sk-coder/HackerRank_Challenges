if __name__ == "__main__":
    n = int(raw_input("Enter a Number (1-20): "))

    if (n >= 1 and n <= 20):
        for i in range(n):
            print (i**2)
