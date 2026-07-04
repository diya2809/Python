# h1) Spam Detector using Linear Search

blacklist = ["A101", "B205", "X999", "M450", "P321"]

sender = input("Enter sender ID to check: ")

found = False

for i in blacklist:
    if i == sender:
        found = True
        break

if found:
    print("Spam sender found in blacklist")
else:
    print("Sender not found")
