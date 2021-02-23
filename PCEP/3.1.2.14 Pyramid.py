blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)
