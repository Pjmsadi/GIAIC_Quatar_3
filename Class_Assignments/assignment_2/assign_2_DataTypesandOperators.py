def display_data_types():
    print("🌟 Python Data Types 🌟")
    print("=" * 30)
    
    # Numeric Types
    print("\n1. Numeric Types:")
    print("- int: Represents integers (e.g., 1, 100, -50)")
    print("- float: Represents floating-point numbers (e.g., 3.14, -0.5)")
    print("- complex: Represents complex numbers (e.g., 3 + 4j)")
    
    # Text Type
    print("\n2. Text Type:")
    print("- str: Represents strings (e.g., 'Hello, Python!')")
    
    # Sequence Types
    print("\n3. Sequence Types:")
    print("- list: Ordered, mutable collection (e.g., [1, 2, 3])")
    print("- tuple: Ordered, immutable collection (e.g., (1, 2, 3))")
    print("- range: Represents a sequence of numbers (e.g., range(5))")
    
    # Set Types
    print("\n4. Set Types:")
    print("- set: Unordered collection of unique items (e.g., {1, 2, 3})")
    print("- frozenset: Immutable version of a set (e.g., frozenset({1, 2, 3}))")
    
    # Mapping Type
    print("\n5. Mapping Type:")
    print("- dict: Key-value pairs (e.g., {'name': 'John', 'age': 30})")
    
    # Boolean Type
    print("\n6. Boolean Type:")
    print("- bool: Represents True or False")
    
    # Binary Types
    print("\n7. Binary Types:")
    print("- bytes: Immutable sequence of bytes (e.g., b'hello')")
    print("- bytearray: Mutable sequence of bytes")
    print("- memoryview: Memory view object for handling memory buffers")
    
    # None Type
    print("\n8. None Type:")
    print("- NoneType: Represents the absence of a value (e.g., None)")

def display_operators():
    print("\n🌟 Python Operators 🌟")
    print("=" * 30)
    
    # Arithmetic Operators
    print("\n1. Arithmetic Operators:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("% : Modulus")
    print("** : Exponentiation")
    print("// : Floor Division")
    
    # Comparison Operators
    print("\n2. Comparison Operators:")
    print("== : Equal to")
    print("!= : Not equal to")
    print("> : Greater than")
    print("< : Less than")
    print(">= : Greater than or equal to")
    print("<= : Less than or equal to")
    
    # Logical Operators
    print("\n3. Logical Operators:")
    print("and : Logical AND")
    print("or : Logical OR")
    print("not : Logical NOT")
    
    # Assignment Operators
    print("\n4. Assignment Operators:")
    print("= : Assign")
    print("+= : Add and assign")
    print("-= : Subtract and assign")
    print("*= : Multiply and assign")
    print("/= : Divide and assign")
    
    # Identity Operators
    print("\n5. Identity Operators:")
    print("is : Returns True if both variables are the same object")
    print("is not : Returns True if both variables are not the same object")
    
    # Membership Operators
    print("\n6. Membership Operators:")
    print("in : Returns True if a value is found in a sequence")
    print("not in : Returns True if a value is not found in a sequence")
    
    # Bitwise Operators
    print("\n7. Bitwise Operators:")
    print("& : Bitwise AND")
    print("| : Bitwise OR")
    print("^ : Bitwise XOR")
    print("~ : Bitwise NOT")
    print("<< : Left shift")
    print(">> : Right shift")

def main():
    print("🚀 Welcome to the Python Data Types and Operators Reference Guide! 🚀")
    print("Created with gratitude to Sir Asharib Ali for their excellent teaching! 🙏\n")
    
    while True:
        print("\nWhat would you like to explore?")
        print("1. Data Types")
        print("2. Operators")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            display_data_types()
        elif choice == "2":
            display_operators()
        elif choice == "3":
            print("\nThank you for using the Python Reference Guide! Happy coding! 🚀")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()