beatles = []

beatles.append("John Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for b in range(1):
    var1 = input("Please enter Stu Sutcliffe. : ")
    beatles.append(var1)
    var2 = input("Please enter Pete Best. : ")
    beatles.append(var2)

print(beatles)
del beatles[-1]
print(beatles)
del beatles[-1]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)
print("The Fab", len(beatles))
