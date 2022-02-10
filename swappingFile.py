def swapFileData():
    print("Swap the data of whatever two files you want... 😊😊😊")
    file1 = input("Enter the FIRST file name: ")
    file2 = input("Enter the SECOND file name: ")


    with open(file1, 'r') as a:
     data_a = a.read()

    with open(file2, 'r') as b:
     data_b = b.read()

    with open(file1, 'w') as a:
     a.write(data_b)

    with open(file2, 'w') as b:
     b.write(data_a)

swapFileData()