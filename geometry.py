# Améliorations par Emma Burdin

# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
from math import sqrt, pi


while True:
    choice_fig = int(
        input(
            "Which figure you want to work with ? 1: equilateral triangle, 2: square, 3: rectangle, 4: circle, 5: rectangle triangle ?"))
    choice_comp = int(input("Which computation do you need ? 1: perimeter, 2: area, 3:  Pythagorean theorem ?"))
    if choice_fig == 1:
        segment_length = float(input("What is the size of one side ?"))
        if choice_comp == 1:
            print("The perimeter is", round((segment_length * 3), 2), "meters")
        elif choice_comp == 2:
            print("The area is", round((segment_length * segment_length * sqrt(3) / 4), 2), "meters²")
    elif choice_fig == 2:
        segment_length = float(input("What is the size of one side ?"))
        if choice_comp == 1:
            print("The perimeter is", round((segment_length * 4), 2), "meters")
        elif choice_comp == 2:
            print("The area is", round((segment_length * segment_length), 2), "meters²")

    elif choice_fig == 3:
        segment_length = float(input("What is the size of one side in meters ?"))
        segment_length2 = float(input("What is the size of the other side in meters?"))
        if choice_comp == 1:
            print("The perimeter is", round((segment_length + segment_length2 * 2), 2), "meters")
        elif choice_comp == 2:
            print("The area is,", round((segment_length2 * segment_length), 2), "meters²")
    elif choice_fig == 4:
        segment_length = float(input("What is the size of the radius in meters ?"))
        if choice_comp == 1:
            print("The perimeter is", round((2 * segment_length * pi), 2), "meters")
        elif choice_comp == 2:
            print("The area is,"(pi) * (segment_length ** 2))
    elif choice_fig == 5:
        segment_length = float(input("What is the size of one side in meters ?"))
        segment_length2 = float(input("What is the size of the other side in meters?"))
        if choice_comp == 1:
            print("The perimeter is",
                  segment_length + segment_length2 + round((sqrt(segment_length ** 2 + segment_length2 ** 2)), 2),
                  "meters")
        if choice_comp == 2:
            print("the area is", round((segment_length * segment_length2 / 2), 2), "meters²")
        if choice_comp == 3:
            print("The Pythagorean theorem is", round(sqrt(segment_length ** 2 + segment_length2 ** 2), 2), "meters")
    else:
        break
