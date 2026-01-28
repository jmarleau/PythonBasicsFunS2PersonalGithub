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
                    outfile.write(num) # remove this redundant block
    outfile.close()
    print("Creation Complete")


def remove_red():
    outfile = open("modified_ny.ppm", "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    red = 0
    for pixel_num in x[0]:
        width += 1
        for color in pixel_num:
            red += 1
            if red == 3:
                outfile.write(" 0")
                red = 0
                break
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            for value in color:     
                for num in value:
                    outfile.write(num)  # remove this redunant block
    outfile.close()
    print("Creation Complete")


def compute_negative():
    outfile = open("modified_ny.ppm", "w")
    print("Creating new image...")
    width = -1
    concat_num = "yes" 
    outfile.write("P3\n960 639\n255\n\n")
    for pixel_num in x[0]:
        width += 1
        for color in pixel_num:
            if concat_num != "yes":
                integer_of_concat_num = int(concat_num)
                subtraction = 255 - integer_of_concat_num
                concat_num = str(subtraction)
                outfile.write(concat_num)
            if width == 960:
                width = 0
                outfile.write("\n") # new-line cycling is one off
            else:
                outfile.write(" ")


            concat_num = "" 
            for value in color:
                concat_num += value
                
    outfile.close()
    print("Creation Complete")

compute_negative()

