import cv2

# color  image read
img = cv2.imread("C:/Users/Dell/Pictures/Wallpaper/images.jfif", 1)
print(img)

# gray scale image read
img = cv2.imread("C:\Users\Dell\Pictures\Wallpaper\images.jfif", 0)
print(img)
print(type(img))
print(img.shape)

img = cv2.imread("C:\Users\Dell\Pictures\Wallpaper\images.jfif", 1)
cv2.imshow("Legend", img)
cv2.waitKey(0)
cv2.destroyAllWindows()