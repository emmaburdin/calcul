# Améliorations par Emma Burdin

# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
from math import sqrt, pi


while True:
    choice_fig = int(
        input("Which figure you want to work with ? 1: equilateral triangle, 2: square, 3: rectangle, 4: circle ?"))
    choice_comp = int(input("Which computation do you need ? 1: perimeter, 2: area"))
    if choice_fig == 1:
        segment_length = float(input("What is the size of one side ?"))
        if choice_comp == 1:
            print("The perimeter is", segment_length * 3)
        elif choice_comp == 2:
            print("The area is", segment_length * segment_length * sqrt(3) / 4)
    elif choice_fig == 2:
        segment_length = float(input("What is the size of one side ?"))
        if choice_comp == 1:
            print("The perimeter is", segment_length * 4)
        elif choice_comp == 2:
            print("The area is", segment_length * segment_length)

    elif choice_fig == 3:
        segment_length = float(input("What is the size of one side ?"))
        segment_length2 = float(input("What is the size of the other side?"))
        if choice_comp == 1:
            print("The perimeter is", (segment_length + segment_length2) * 2)
        elif choice_comp == 2:
            print("The area is,", segment_length2 * segment_length)
    elif choice_fig == 4:
        segment_length = float(input("What is the size of the radient?"))
        if choice_comp == 1
