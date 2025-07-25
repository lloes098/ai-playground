import cv2 # OpenCV 라이브러리 import 
import sys # sys 모듈 import 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands 

cap = cv2.VideoCapture(0) # 비디오 캡처 객체 생성 

if not cap.isOpened(): # 연결 확인 
    print("Camera is not opened")
    sys.exit(1) # 프로그램 종료 

hands = mp_hands.Hands() 

while True: # 무한 반복 
    res, frame = cap.read() # 카메라 데이터 읽기 

    if not res: # 프레임 읽었는지 확인 
        print("Camera error")
        break 

    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS, 
                mp_drawing_styles.get_default_hand_landmarks_style(), 
                mp_drawing_styles.get_default_hand_connections_style(), 
            )
    
    cv2.imshow("MediaPipe Hands", frame)

    key = cv2.waitKey(1) & 0xFF # 키보드 입력받기 
    if key == 27: # ESC 키 눌렀을 경우 
        break # 반복문 종료 


cv2.destroyAllWindows() #영상 창 닫기 
cap.release() #비디오 캡처 객체 해제 
