def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
