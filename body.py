import cv2
i=0
video = cv2.VideoCapture(r"D:\VID_85980131_024725_927.mp4")
image = cv2.imread(r"D:\5d081d2a8d0ee3a49ffa08291d087355.png")
image2 = cv2.resize(image,(900,700))
while True:
    ret, frame = video.read()
    after=cv2.resize(frame,(900,700))
    cv2.waitKey(100)
    cv2.imwrite("vid"+str(i)+".jpg",after)
    i+=1
    if i == 2:
        break
    if cv2.waitKey(100)& 0xff == ord('n'):
      break


add = cv2.add(image2,after)
cv2.imshow("add",add)
cv2.waitKey(0)

divide = cv2.divide(image2,after)
cv2.imshow("divide",divide)
cv2.waitKey(0)

multiply = cv2.multiply(image2,after)
cv2.imshow("mult",multiply)
cv2.waitKey(0)

subtract = cv2.subtract(image2,after)
cv2.imshow("sub",subtract)
cv2.waitKey(0)

notimag2 =cv2.bitwise_not(image2)
cv2.imshow("not1",notimag2)
cv2.waitKey(0)

notafter= cv2.bitwise_not(after)
cv2.imshow("not2",notafter)
cv2.waitKey(0)

orb= cv2.bitwise_or(image,after)
cv2.imshow("or",orb)
cv2.waitKey(0)

andb= cv2.bitwise_and(image,after)
cv2.imshow("and",andb)
cv2.waitKey(0)

xorb= cv2.bitwise_xor(image,after)
cv2.imshow("xor",xorb)

cv2.waitKey(0)
cv2.destroyAllWindows()
