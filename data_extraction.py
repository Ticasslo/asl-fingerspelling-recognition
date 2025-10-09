# data_extraction.py
# READ ME
# READ ME
# READ ME
# READ ME
# if you thinking WHY NEED DATA EXTRACTION? why cant we just throw image directly to model training
# the answer is YES AND NO!
# 1. What if the model need to train many times?? with different input from n_estimate, tree_depth,...??
# 2. The process time: if it short, there no need to data extract, but what if it LONG?!? And any error happen????
# 3. You can share it with others!!
import os
import mediapipe as mp
import pandas as pd
import cv2
import pickle

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.9)

#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
#1. Select the folder data THIS IS IMPORTAINT
data_dir = 'asl_dataset_test'
data = []
labels = []

# NEW
# DS_Store is a temp folder in MAC, which will not affect for Win
total_files = sum([len(files) for r, d, files in os.walk(data_dir) if '.DS_Store' not in files])
processed_files = 0
print(f"Tổng số tệp: {total_files}")
# NEW 

for i in sorted(os.listdir(data_dir)):
    if i == '.DS_Store':
        pass
    else:
        for j in os.listdir(os.path.join(data_dir,i)): #RGB -> BGR
            data_aux = [] #42
            img = cv2.imread(os.path.join(data_dir,i,j))
            img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for z in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[z].x
                        y = hand_landmarks.landmark[z].y
                        data_aux.append(x)
                        data_aux.append(y)         
                    
                data.append(data_aux)
                labels.append(i)
        
            processed_files += 1
            percent_complete = (processed_files / total_files) * 100
            print(f"Processing: {percent_complete:.2f}% completed", end='\r')
            
            
            
# # save data
# YOU CAN USE PICKLE OR PANDAS!!!!!!!!
# YOU CAN USE PICKLE OR PANDAS!!!!!!!!
# YOU CAN USE PICKLE OR PANDAS!!!!!!!!

# f = open('datatest.pickle', 'wb')
# pickle.dump({'datatest':data,'labels':labels},f)
# f.close() 

# Save data as a pandas DataFrame
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
#2. CHOOSE THE DATA NAME OR OLD DATA GET REPLACE
df = pd.DataFrame(data)
df['label'] = labels
df.to_pickle('datatest.csv')

print("\nProcessing completed!")