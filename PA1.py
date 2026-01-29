# Name: Jett Marleau
# Class: CPSC 122-02
# Progamming Assignment 1
# 1 / 28 / 2026
# This program takes an input .ppm image and can make certain filtered modifications to it as an output .ppm file




import random as rn
  
y = []
z = []
q = []

input_file_name = str(input("Please input the name of the file you would like to modify (ex: ny.ppm): "))
outfile_name = "modified_" + input_file_name
line_counter = 1
infile = open(input_file_name, "r")
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
    line_counter += 1
infile.close()


def apply_modification():
    """Provides a menu for the user to select and process each 
        different image filter. Provides some simple error checking 
        and returns the selected choice"""
    
    print("Please select the image modification you would like to make \n")
    print("0: No Modification")
    print("1: Apply Vertical Flip")
    print("2: Apply Horizontal Flip")
    print("3: Remove Blue")
    print("4: Compute Negative")
    print("5: Compute High Contrast")
    print("6: Compute Random Noise")
    print("7: Compute Grayscale")
    modification = int(input("\nPlease enter a number: "))
    while modification < 0 or modification > 7:
        print("Invalid input")
        modification = int(input("\nPlease enter a number: "))
    return modification


def write_image(out_file_name: str):
    """Makes no change to the image, simply processes each character
        in the input file and writes it to a new file specified by the user"""
    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    
    for pixel_num in y:
        width += 1
        for color in pixel_num:
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            for value in color:
                outfile.write(value) 
    outfile.close()
    print("Creation Complete")


def remove_blue(out_file_name: str):
    """scans each Blue value in the RGB sequence and reduces it to 0"""

    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    blue = 0
    for pixel_num in y:
        width += 1
        for color in pixel_num:
            blue += 1
            if blue == 3:
                outfile.write(" 0")
                blue = 0
                break
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            for value in color:     
                    outfile.write(value)  
    outfile.close()
    print("Creation Complete")


def compute_negative(out_file_name: str):
    """Inverts the color of each pixel by taking its Red Blue and Green values respectively,
    and reducing the number (255 - R), (255 - B), (255 - G)
    my solution here is definetly very overcomplicated, but it uses string concatantions to 
    indiviual digit into the proper RGB values, then converts them into integers before subtracting them"""

    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    concat_num = "yes" 
    outfile.write("P3\n960 639\n255\n\n")
    for pixel_num in y:
        width += 1
        for color in pixel_num:
            if concat_num != "yes":
                integer_of_concat_num = int(concat_num)
                subtraction = 255 - integer_of_concat_num
                concat_num = str(subtraction)
                outfile.write(concat_num)
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            concat_num = "" 
            for value in color:
                concat_num += value
                
    outfile.close()
    print("Creation Complete")

def flip_horizontally(out_file_name: str):
    """Flips each line by placing the pixel into a temporary list, then using list.reverse()
        It does this for every line"""
    
    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    
    t = []
    for u in range(0,640):
        for b in range((960*u - 960),(960*u)):
            t.append(y[b])
        t.reverse()
        for list in t:
            width += 1
            for num in list:
                if width == 960:
                    width = 0
                    outfile.write("\n")
                else:
                    outfile.write(" ")
                for indiv in num:
                    outfile.write(indiv)
        t = []
    outfile.close()

def flip_vertically(out_file_name: str):
    """Vertically flips the image by placing each line of the original into a list
        this list is then repeated added as the 0th index to another list which is used
        to rewrite the image upside down"""

    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    
    t = []
    h = []
    for u in range(0,639):
        for b in range((960*u - 960),(960*u)):
            t.append(y[b])
        h.insert(0 , t)
        t = []

    for list in h:
        for num in list: 
            width += 1 
            if width == 960:
                width = 0
                outfile.write("\n")
            for indiv in num:
                if width != 960:
                    outfile.write(" ")
                for char in indiv:
                    outfile.write(char)
    outfile.close()


def compute_high_contrast(out_file_name: str):
    """Uses string concatanation to combine each character into its respective
        RGB value. Then it uses an if statement to check and set the value to 
        a corresponding min or max color value"""
    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    
    for pixel_num in y:
        width += 1
        for color in pixel_num:
            if width == 960:
                width = 0
                outfile.write("\n")
            else:
                outfile.write(" ")
            concat = ""
            for value in color:
                concat += value
                compare = int(concat)
                if compare <= 127:
                    compare = 0
                else:
                    compare = 255
                str_compare = str(compare)
                outfile.write(str_compare)
                
    outfile.close()
    print("Creation Complete")

def compute_gray_scale(out_file_name: str):
    """Uses string concatanation to combine each character into its respective
        RGB values. Then it averages all values in the pixel and writes it three times"""
    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    total = 0
    outfile.write("P3\n960 639\n255\n\n")
    for pixel_num in y:
        width += 1
        for color in pixel_num: 
            concat = ""
            for value in color:
                concat += value
            subtotal = int(concat)
            total += subtotal
        avg = total // 3
        total = 0
        str_avg = str(avg)
        outfile.write(str_avg)
        outfile.write(" ")
        outfile.write(str_avg)
        outfile.write(" ")
        outfile.write(str_avg)
        outfile.write(" ")
        if width == 960:
            width = 0
            outfile.write("\n")
            
    outfile.close()
    print("Creation Complete")


def compute_random_noise(out_file_name: str):
    """Takes each RGB value for each Pixel and adds or subtracts and random value 
    between -50 and 50. The rewrites the image"""

    outfile = open(out_file_name, "w")
    print("Creating new image...")
    width = -1
    outfile.write("P3\n960 639\n255\n\n")
    for pixel_num in y:
        width += 1
        for color in pixel_num: 
            concat = ""
            for value in color:
                concat += value
            subtotal = int(concat)
            new_total = subtotal + rn.randint(-50, 50)
            str_new_total = str(new_total)
            outfile.write(str_new_total)
            outfile.write(" ")
            if width == 960:
                width = 0
                outfile.write("\n")
            
    outfile.close()
    print("Creation Complete")

def main():
    modification = apply_modification()
    if modification == 0:
        write_image(outfile_name)
    elif modification == 1:
        flip_vertically(outfile_name)
    elif modification == 2:
        flip_horizontally(outfile_name)
    elif modification == 3:
        remove_blue(outfile_name)
    elif modification == 4:
        compute_negative(outfile_name)
    elif modification == 5:
        compute_high_contrast(outfile_name)
    elif modification == 6:
        compute_random_noise(outfile_name)
    elif modification == 7:
        compute_gray_scale(outfile_name)

    

if __name__ == "__main__":
    main()