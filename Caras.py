import cv2 as cv

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
Mongos=cv.imread("Roblox.png",cv.IMREAD_UNCHANGED)

#obtener acceso a la webcam

video_capture = cv.VideoCapture(0,cv.CAP_DSHOW)

if not video_capture.isOpened():
        print('No se pudo acceder a la camara')
else:
    while True:
        ret, frame = video_capture.read()
        frame=cv.flip(frame,1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
        faces = faceCascade.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(70, 70)
        )
        for (x, y, w, h) in faces:
            Resize=cv.resize(Mongos,(w,h))
            for i in range(Resize.shape[0]):
                for j in range(Resize.shape[1]):
                    if(Resize[i,j][3]!=0):
                        frame [y+i,x+j]=Resize[i,j]
        # Mostrar la deteccion
        frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
        cv.imshow('Video', frame)
        #se motraran las caras mientra no presionemos la tecla q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    #liberar la camara
    video_capture.release()
    #cerrar todas las ventanas
    cv.destroyAllWindows()