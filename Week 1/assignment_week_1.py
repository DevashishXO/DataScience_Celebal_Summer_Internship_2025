# Create lower triangular, upper triangular and pyramid containing the "*" character.

def lower_triangle(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def upper_triangle(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    print("Lower Triangle:")
    lower_triangle(n)
    print("\nUpper Triangle:")
    upper_triangle(n)
    print("\nPyramid:")
    pyramid(n)