file_builder = open("logger.txt", "w+")            # create the variable called file-builder call the function open(allows you to open or create a file)
                                                   # if it finds file it will open(if not it will create)-pass in name of file
                                                   # and then the way we want to open it w+ (write to the file)
for i in range(1000):                              # for i in range and say 1000
    file_builder.write(f"I'm on line {i + 1}\n")   # inside the loop call the file builder.write(in a formatted string)
                                                   # Im on line- then i + 1 (increment by one)...carriage return \n


# file_builder.write("Hey, I'm in a file!")        # say file build and write and inside say yuou are in a file

file_builder.close()                               # now say file builder and call the close function with no arguments