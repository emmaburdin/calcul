# Améliorations par Emma Burdin

# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
from math import sqrt, pi  # import the square root and pi


while True:
    choice_fig = int(
        input(
            "Which figure you want to work with ? 1: equilateral triangle, 2: square, 3: rectangle, 4: circle, 5: rectangle triangle ?"))  # choice of figures
    choice_comp = int(input(
        "Which computation do you need ? 1: perimeter, 2: area, 3:  Pythagorean theorem ?"))  #choice of the formula
    if choice_fig == 1:
        segment_length = float(input("What is the size of one side ?"))  #enter the size
        if choice_comp == 1:
            print("The perimeter is", round((segment_length * 3), 2),
                  "meters")  #perimeter of the equilateral triangle in meter
        elif choice_comp == 2:
            print("The area is", round((segment_length * segment_length * sqrt(3) / 4), 2),
                  "meters²")  # area of the equilateral triangle in square meter
    elif choice_fig == 2:
        segment_length = float(input("What is the size of one side ?"))  #enter the size
        if choice_comp == 1:
            print("The perimeter is", round((segment_length * 4), 2), "meters")  #perimeter of the square in meter
        elif choice_comp == 2:
            print("The area is", round((segment_length * segment_length), 2),
                  "meters²")  #area of the quare in square meter

    elif choice_fig == 3:
        segment_length = float(input("What is the size of one side in meters ?"))  # enter the size
        segment_length2 = float(input("What is the size of the other side in meters?"))  #enter the size
        if choice_comp == 1:
            print("The perimeter is", round((segment_length + segment_length2 * 2), 2),
                  "meters")  #perimeter of the rectangle in meter
        elif choice_comp == 2:
            print("The area is,", round((segment_length2 * segment_length), 2),
                  "meters²")  #area of the rectangle in square meter
    elif choice_fig == 4:
        segment_length = float(input("What is the size of the radius in meters ?"))  #enter the size
        if choice_comp == 1:
            print("The perimeter is", round((2 * segment_length * pi), 2), "meters")  #perimeter of the circle
        elif choice_comp == 2:
            print("The area is,"(pi) * (segment_length ** 2))  #area of the circle in square meter
    elif choice_fig == 5:
        segment_length = float(input("What is the size of one side in meters ?"))
        segment_length2 = float(input("What is the size of the other side in meters?"))
        if choice_comp == 1:
            print("The perimeter is",
                  segment_length + segment_length2 + round((sqrt(segment_length ** 2 + segment_length2 ** 2)), 2),
                  "meters")  # perimeter of the rectangle triangle
        if choice_comp == 2:
            print("the area is", round((segment_length * segment_length2 / 2), 2),
                  "meters²")  # area of the rectangle triangle in square meter
        if choice_comp == 3:
            print("The Pythagorean theorem is", round(sqrt(segment_length ** 2 + segment_length2 ** 2), 2),
                  "meters")  # Pyhtagora's theorem
    else:
        break
