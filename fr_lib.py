#!/usr/bin/python3

#IMPORTING LIBRARIES
import cv2
import numpy as np
import httplib2 , urllib, base64,json,requests
import os
import webbrowser


#DEFINING HEADERS AND PARAMETERS
headers = {
	# Request headers
	'Content-Type': 'application/octet-stream',   # this should be the content type
	'Ocp-Apim-Subscription-Key': '',
}

params = {
	# Request parameters
	'returnFaceAttributes': 'emotion'
}


#GETTING CLASSIFIER
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascase = cv2.CascadeClassifier('haarcascade_eye.xml')

#INITIALIZING CAMERA
cap = cv2.VideoCapture(0)

#READING EMOJIS
happy=cv2.imread('happy.png',1)
s_happy=np.shape(happy)

sad=cv2.imread('sad.png',1)
s_sad=np.shape(sad)

angry=cv2.imread('angry.png',1)
s_angry=np.shape(angry)

crying=cv2.imread('crying.png',1)
s_crying=np.shape(crying)

vhappy=cv2.imread('vhappy.png',1)
s_vhappy=np.shape(vhappy)

surprised=cv2.imread('surprised.png',1)
s_surprised=np.shape(surprised)


#OPENING LIVE CAMERA FRAME
while True:

	#READING CAMERA AND CONVERTING TO GEAY
	ret,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#DETECTION OF FACE
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	for (x, y, w, h) in faces:    
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_color = img[y:y+h,x:x+w]
		
   
	#SAVING ACTIVE CAPTURE
	cv2.imwrite('lol.jpg',img)
	data = open('lol.jpg', 'rb').read()

	#USING API TO DETECT EMOTIONS
	face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
	response = requests.post(face_api_url, params=params, headers=headers, data=data)
	faces = response.json()

	#APPLYING THE EMOJI TO DETECTED EMOTION COMBINATION
	if np.size(faces):
		emotion=faces[0]['faceAttributes']['emotion']
		print(emotion)
		if emotion['happiness']>=emotion['sadness']:
			if emotion['happiness']>=0.4:
				
				#SETTING THE LIVE FRAME
				img[y:y+32,x+w-32:x+w,0:3] = vhappy[0:s_vhappy[0],0:s_vhappy[1],0:s_vhappy[2]]
				cv2.imshow('MOOD',img)
				#webbrowser.open_new_tab("https://www.youtube.com/watch?v=mh5J7pV1hJE")
				#break
			else:
				img[y:y+32,x+w-32:x+w,0:3] = happy[0:s_happy[0],0:s_happy[1],0:s_happy[2]]
				cv2.imshow('MOOD',img)

		elif emotion['sadness']>emotion['happiness']:
			if emotion['sadness']>=0.2:

				img[y:y+32,x+w-32:x+w,0:3] = crying[0:s_crying[0],0:s_crying[1],0:s_crying[2]]
				cv2.imshow('MOOD',img)
				#os.system("vlc /home/ashit/Downloads/tadap.mp3")
				#break
			else:
				img[y:y+32,x+w-32:x+w,0:3] = sad[0:s_sad[0],0:s_sad[1],0:s_sad[2]]
				cv2.imshow('MOOD',img)
		elif emotion['anger']>emotion['happiness'] and emotion['anger']>emotion['sadness']:
			img[y:y+32,x+w-32:x+w,0:3] = angry[0:s_angry[0],0:s_angry[1],0:s_angry[2]]
			cv2.imshow('MOOD',img)

		elif emotion['surprise']>0.05:
			img[y:y+32,x+w-32:x+w,0:3] = surprised[0:s_surprised[0],0:s_surprised[1],0:s_surprised[2]]
			cv2.imshow('MOOD',img)
	else: 	
		print("NO FACE!!")

	#TO EXIT THE LIVE FRAME
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
#RELEASE THE CAMERA AND CLOSING THE WINDOW
cap.release()
cv2.destroyAllWindows()


