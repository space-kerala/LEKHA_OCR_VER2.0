import lekha_work as ocr
import cv2


img=cv2.imread("/home/space-kerala/paperwork_malayalam/lekha/line_train/d1/d1.tiff",0)
#cv2.imshow("open",img)
#cv2.waitKey(0)
text = ocr.lekha_run(img)
strtext = str(text)
print(strtext)
f = open('test.txt', 'w')
f.write(strtext)
f.close()

