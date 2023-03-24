
import numpy as np
import cv2
#创建一个黑色的图框，uint8是线条的类型，8连接
img=np.zeros((512,512,3),np.uint8)
img=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#在窗口展示图形
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()