import cv2 as cv
import numpy as np


def main():
    img = cv.imread("car.jpg")
    gray = cv.imread("car.jpg", 0)
    print("Please select from the option below")
    print("1. Accept/load colored img. Grayscale should be rejected.")
    print("2. Output a pixel value")
    print("3. Modify a pixel value")
    print("4. Set img dimensions")
    print("5. Set image pixel count")
    print("6. Loaded image's data type")
    print("7. Exit")

    opt = int(input("input number: "))

    if opt == 1:
        imgLen = len(img.shape)
        grayLen = len(gray.shape)
        if imgLen > grayLen:
            cv.imshow("colored", img)
            cv.waitKey(0)
            main()
        else:
            exit()

    elif opt == 2:
        x = int(input("for x axis: "))
        y = int(input("for y axis: "))
        color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
        print(img.item(x, y, color))
        main()

    elif opt == 3:
        x = int(input("for x axis: "))
        y = int(input("for y axis: "))
        print(img[x, y])
        for i in range(0, 3, 1):
            color = int(input("BGR selection: [1. BLUE] [2. GREEN] [3. RED]: "))
            pixelValue = int(input("Pixel Value: "))
            img.itemset((x, y, color), pixelValue)
        print(img[x, y])
        cv.imshow("colored", img)
        cv.waitKey(0)
        main()

    elif opt == 4:
        x = 450
        y = 150
        print(img.shape)
        print(f"""
                    total pixel in x-axis: {img.shape[0]}
                    total pixel in y-axis: {img.shape[1]}
                    compared value in x-axis: {x}
                    compared value in y-axis: {y}
                """)

        if x <= img.shape[0] and y <= img.shape[1] :
            print("Within boundaries")
            main()
        else:
            print("Out of boundaries")
            main()

    elif opt == 5:
        x = 150
        y = 150
        fixedValue = x * y
        totalPixel = img.shape[0] * img.shape[1]

        print(f"""
                  total fixed variable: {fixedValue}
                  total image pixels: {totalPixel}
                """)

        if fixedValue > totalPixel :
            print("higher")
            main()
        elif fixedValue < totalPixel :
            print("lower")
            main()
        else:
            print("equal")
            main()

    elif opt == 6:
        print(f"image data type is: {img.dtype}")
        main()

    elif opt == 7:
        exit()

    else:
        print("Wrong Input, please try again")
main()