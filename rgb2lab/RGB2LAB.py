import cv2
i = cv2.imread('path_to_image.png')
cv2.imshow('Hello World', input)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    lab = cv2.cvtColor(input,cv2.COLOR_BGR2LAB)
    cv2.imshow("l*a*b",lab)

    L,A,B=cv2.split(lab)
    cv2.imshow("L_Channel",L) # For L Channel
    cv2.imshow("A_Channel",A) # For A Channel (Here's what You need)
    cv2.imshow("B_Channel",B) # For B Channel

    cv2.waitKey(0)
    cv2.destroyAllWindows()
