def print_star_pattern(n):
    """Prints a star pattern of n rows."""
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))
10000
def main():
    n = int(input("Enter the number of rows for the star pattern: "))
    print_star_pattern(n)

if __name__ == "__main__":
    main()
