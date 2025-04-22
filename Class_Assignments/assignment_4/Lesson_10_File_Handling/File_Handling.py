# File Handling in Python

# File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface.
# It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

# Opening a File
# Use the open() function to open a file. Specify the mode (read, write, append, etc.).

# Modes:

# r:    Read (default)

# w:    Write (Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.)

# a:    Append (Opens the file for appending. Creates the file if it doesn't exist, or adds to it if it does.)

# x:    Exclusive creation (fails if file exists)

# b:    Binary mode (Used with the other modes (e.g., "rb", "wb") for working with binary files.)

# +:    Update mode (Can be combined with other modes (e.g., "r+", "w+") to allow both reading and writing.)

# Reading a File
# Reading a file can be achieved by file.read() which reads the entire content of the file.
# After reading the file we can close the file using file.close() which closes the file after reading it,
# which is necessary to free up system resources.

# Example: Reading a File in Read Mode (r)
# Open the file in read mode

file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a File:
# Writing to a file is done using file.write() which writes the specified string to the file. If the file exists, its content is erased.
# If it doesn’t exist, a new file is created.

# Example: Writing to a File in Write Mode (w)
file = open("geeks.txt", "w")
file.write("Hello, World!")
file.close()

# Writing to a File in Append Mode (a)
# It is done using file.write() which adds the specified string to the end of the file without erasing its existing content.

# Example: For this example, we will use the Python file created in the previous example.
# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

# Handling Exceptions When Closing a File
# It’s important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations.

#Example:
try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()


# In Python, binary mode is used when reading or writing files that are not plain text—such as images, audio files, video files, or any other non-text file formats.

# You use binary mode by adding 'b' to the file mode string. Here are some common examples:

# 'rb': Read binary — Opens a file for reading in binary mode.

# 'wb': Write binary — Opens a file for writing in binary mode. If the file already exists, it is overwritten.

# 'ab': Append binary — Opens a file for appending in binary mode.

# Example: Reading an image file in binary mode
with open('image.jpg', 'rb') as file:
    data = file.read()
    print(type(data))  # <class 'bytes'>

# Example: Writing binary data to a file
binary_data = b'\x48\x65\x6c\x6c\x6f'  # 'Hello' in bytes
with open('output.bin', 'wb') as file:
    file.write(binary_data)


# Example: Appending binary data to a file
binary_data = b'\x20\x57\x6f\x72\x6c\x64'  # ' World' in bytes
with open('output.bin', 'ab') as file:
    file.write(binary_data)

# Update mode :
# The + (plus) in Python file modes enables update mode, which means you can read and write to the same file.
# It's used in combination with 'r', 'w', or 'a'.
# Exapmle:
# r+: Read and write (no truncation)
with open('example.txt', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write("Updated!\n" + content)

# w+: Truncate and then read/write
with open('example.txt', 'w+') as file:
    file.write("New content\n")
    file.seek(0)
    content = file.read()
    print(content)  # This will be empty because the file was truncated.

# a+: Append and read
with open('example.txt', 'a+') as file:
    file.write("Appending new content\n")
    file.seek(0)
    content = file.read()
    print(content)  # This will show the previous content plus the new appended content.
# The 'a+' mode allows you to append new content to the end of the file while also allowing you to read from it.


