# TODO make the filename an input and parameter
infile = open("ny.ppm", "r")

x = []
y = []
z = []
q = []

line_counter = 1
space_num = 0


# TODO convert this to a function and add docstring
for line in infile:
    if line_counter > 4:
        for char in line:
            if char != " " and char != "\n":
                q.append(char)
            elif char == " ":
                z.append(q)
                q = []  
            if len(z) == 3:
                y.append(z)
                z = []
            if len(y) == 3:
                x.append(y)
                
    line_counter += 1

infile.close()

# TODO add a docstring
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

# TODO Add a docstring
def write_image():
    outfile = open("modified_ny.ppm", "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    """
    for pixel_num in x: # iterating too many times?
        for color in pixel_num:
            if width == 960:
                width = 0
                outfile.write("\n")
            for value in color:
                outfile.write(" ")
                width += 1
                for num in value:
                    outfile.write(num)
    """
    for pixel_num in x[0]:
        width += 1
        for color in pixel_num:
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            for value in color:
                for num in value:
                    outfile.write(num)
                    
                    


    outfile.close()
    print("Creation Complete")


def remove_red():
    outfile = open("modified_ny.ppm", "w")
    print("Creating new image...")
    width = 0
    red = 0
    outfile.write("P3\n960 639\n255\n")
    for pixel_num in x:
        for color in pixel_num:
            if width == 960:
                width = 0
                outfile.write("\n")
            for value in color:
                outfile.write(" ")
                width += 1
                red += 1
                if red % 3 == 0:
                        outfile.write("0")
                        red = 0
                        break
                for num in value:
                    outfile.write(num)
    outfile.close()
    print("Creation Complete")

write_image()

