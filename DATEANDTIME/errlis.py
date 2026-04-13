try:
    # 1. Get the list elements
    elements = input("Enter list elements (space separated): ").split()

    # 2. Convert string list to integer list
    num_list = [int(x) for x in elements]

    # 3. Get the index
    idx = int(input("Enter index: "))

    # 4. Access and print the element
    print(num_list[idx])
except IndexError:
    print("Error: Index out of range")
except ValueError:
    print("Error: Invalid input")
