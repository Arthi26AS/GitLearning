import os

filepath = "D:\\python\\new.txt"

if os.path.exists(filepath):
    with open(filepath, "a") as f:
        f.write("Mr.H is good")
else:
    # open in write mode (creates new file)
    # write data
    with open(filepath, "w") as f:
        f.write("Mr.H is bad")

"""file handle"""
