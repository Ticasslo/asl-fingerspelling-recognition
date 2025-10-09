import os
import cv2 #OpenCV

#THIS IS THE EXAMPLE ON HOW TO COLLECT DATA
#THIS IS THE EXAMPLE ON HOW TO COLLECT DATA
#THIS IS THE EXAMPLE ON HOW TO COLLECT DATA
#THIS IS THE EXAMPLE ON HOW TO COLLECT DATA
#THIS IS THE EXAMPLE ON HOW TO COLLECT DATA
DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)
#Sử dụng cam để chuyển hình ảnh thành các frame dạng danh sách lưu

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'q to collect data, b to quit', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0,255,0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(25) & 0xFF
        if key == ord('q'):  # Start collecting data
            break
        elif key == ord('b'):  # Stop everything
            print("Stopping data collection...")
            cap.release()
            cv2.destroyAllWindows()
            exit()
        

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
