#able to create a logger
file_builder = open("logger.txt", "w+") #variable open allows you to open or create a file

for i in range(100):
    file_builder.write(f"Im on line {i + 1}\n") #a temporary type of logger builder
# file_builder.write("Hey I am in a file")

file_builder.close()