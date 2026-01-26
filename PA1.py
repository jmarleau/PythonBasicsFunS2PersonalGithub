
infile = open("ny.ppm", "r")

x = []
y = []
z = []
q = []

line_counter = 1
space_num = 0



for line in infile:
    if line_counter > 4:
        for char in line:
            if char != " " and char != "\n":
                q.append(char)
            else:
                z.append(q)
                q = []  
            if len(z) == 3:
                y.append(z)
                z = []
            if len(y) == 3:
                x.append(y)
                
    line_counter += 1

infile.close()

def apply_modification():
    print("Please select the image modification you would like to make \n")
    print("1: Apply Vertical Flip")
    print("2: Apply Horizontal Flip")
    print("3: Remove Red")
    print("4: Compute Negative")
    print("5: Compute High Contrast")
    print("6: Compute Random Noise")
    print("7: Compute Grayscale")
    modification = int(input("\nPlease enter a number: "))
    while modification < 1 or modification > 7:
        print("Invalid input")
        modification = int(input("\nPlease enter a number: "))
    return modification


# outfile = open("modified_ny.ppm", "w")
# for pixel_num in x:
#     for color in pixel_num:
#         for value in color:
#             outfile.write(value)
            
