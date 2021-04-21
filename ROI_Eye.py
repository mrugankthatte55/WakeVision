import headers as headers
def ROI_Eye(i,gray):
    bgrl=[]
    bgrr=[]
    imgleft=[]
    imgright=[]
    left_eye=headers.left_eye_haar.detectMultiScale(gray,1.3,5)
    right_eye=headers.right_eye_haar.detectMultiScale(gray,1.3,5)  
    if len(left_eye)!=0 and len(right_eye)!=0:
        for (lx,ly,lw,lh) in left_eye:
            roi_l=gray[ly:ly+lh,lx:lx+lw]
            imgleft=headers.cv2.resize(roi_l,(224,224))
            headers.cv2.imwrite("Buffer/left_"+str(i)+".png",imgleft)
        #i+=1
        for (rx,ry,rw,rh) in right_eye:
            roi_r=gray[ry:ry+rh,rx:rx+rw]
            imgright=headers.cv2.resize(roi_r,(224,224))
            headers.cv2.imwrite("Buffer/right_"+str(i)+".png",imgright)
        #i+=1
        bgrl = headers.cv2.cvtColor(imgleft, headers.cv2.COLOR_GRAY2RGB)
        bgrr = headers.cv2.cvtColor(imgright, headers.cv2.COLOR_GRAY2RGB)
        bgrl=headers.cv2.resize(bgrl,(224,224))
        bgrr=headers.cv2.resize(bgrr,(224,224))
    return(i,imgleft,imgright)
