# real_time_prediction.py
# READ ME
# READ ME
# READ ME
# READ ME
# There is a different between ASL and VSL like the T word or many other words so it ideadly to turn it into an English reconigtion
# instead of VSL regconition cause I cant find a database for VSL!!! so i changed from Vietnamese to English
# instead of VSL regconition cause I cant find a database for VSL!!! so i changed from Vietnamese to English
# instead of VSL regconition cause I cant find a database for VSL!!! so i changed from Vietnamese to English
# instead of VSL regconition cause I cant find a database for VSL!!! so i changed from Vietnamese to English
# THIS IS A DEMO, SO IT USE ONLY OPEN CV FRAME
# THIS IS A DEMO, SO IT USE ONLY OPEN CV FRAME
# THIS IS A DEMO, SO IT USE ONLY OPEN CV FRAME
# THIS IS A DEMO, SO IT USE ONLY OPEN CV FRAME
import cv2
import pickle
import mediapipe as mp
import numpy as np
import time
from geminiAI import IntoVoice

# Load model: Taking out the file pickle from the model data [the data is in a form of label of prediction for the Random Forest Model]
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
model_dict = pickle.load(open('model3_2.p', 'rb'))
model = model_dict['model3_2']

# Load the detecton of the mediapipe to detect joint of the hands for prediction
# Then we draw it with line to each connection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the camera 0 [This is base on your devices so the camera point could be different]
# Try to change into 1,2,3,4... until it could detect your camera
def start_prediction():
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    cap = cv2.VideoCapture(0)
        
    predicted_words = []  # List to store predicted words
    last_prediction = "" # This is to store the last prediction and compare it to see is it a dupilcate or not
    hold_start_time = None # This is for the hand time that hold in the air, count into dulpicate
    no_hands_start_time = None # If no hand more than 2 second then the result would print into screen and go into AI
    has_spoken = False # To see if the AI of the model is spoken yet or not
    del_hold_start_time = None #ONLY FOR MODEL THAT HAVE DEL

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
        while cap.isOpened():
            # Set the frame of the device
            data_aux = []
            x_ = []
            y_ = []
            
            #The camera read and store the data into ret and frame
            ret, frame = cap.read()
            H, W, _ = frame.shape
            
            # This is the process of coverting into BGR - Blue Green Red Because the Model is use to detect BGR
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.flip(frame_rgb, 1)
            frame_rgb.flags.writeable = False
            results = hands.process(frame_rgb)
            frame_rgb.flags.writeable = True
            # Turn it into RGB so normal people could see it
            frame_rgb = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
            
            current_prediction = ""
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame_rgb,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(28, 255, 3), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(236, 255, 3), thickness=2, circle_radius=2)
                    )

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x)
                        data_aux.append(y)
                        x_.append(x)
                        y_.append(y)

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10
                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10
                    current_prediction = model.predict([np.array(data_aux)[0:42]])[0]
                    
                    # Get probabilities for each class and find the predicted class with its confidence
                    proba = model.predict_proba([np.array(data_aux)[0:42]])
                    current_prediction = model.classes_[np.argmax(proba)]
                    confidence = np.max(proba) * 100  # Convert to percentage

                    cv2.rectangle(frame_rgb, (x1, y1 - 10), (x2, y2), (255, 99, 173), 6)
                    # cv2.putText(frame_rgb, current_prediction, (x1, y1 - 12), cv2.FONT_HERSHEY_DUPLEX, 2.5, (255, 0, 0), 3, cv2.LINE_AA) #This is without prediction
                    cv2.putText(frame_rgb, f"{current_prediction} ({confidence:.1f}%)", (x1, y1 - 15), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                    
                
                
                
                
                
                
                
                
                
                
                # Handle "Del" prediction with a timer
                if current_prediction == "Del":
                    if del_hold_start_time is None:
                        del_hold_start_time = time.time()  # Start the timer for "Del"
                    elif (time.time() - del_hold_start_time) >= 1.5:
                        if predicted_words:
                            predicted_words.pop()  # Delete the last word
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                            print("Deleted last word.")
                        del_hold_start_time = None  # Reset "Del" timer after deletion
                else:
                    del_hold_start_time = None  # Reset if the prediction is not "Del"   
                    
                    
                # If the current prediction is different from the last one
                if current_prediction != last_prediction and current_prediction != "Del":
                    last_prediction = current_prediction
                    hold_start_time = time.time()  # Start timing the new prediction
                    has_spoken = False  # Reset the spoken flag
                elif hold_start_time is not None and current_prediction != "Del":
                    # Check if the prediction has held for 1.5 seconds before adding
                    if (time.time() - hold_start_time) >= 1.5:
                        if current_prediction == "Space":
                            predicted_words.append("-")
                        else:
                            predicted_words.append(current_prediction)
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        print(f"Added: {current_prediction}")
                        hold_start_time = None

                # Reset the no hands timer since hands are detected
                no_hands_start_time = None 

            else:
                # If no hands detected
                if no_hands_start_time is None:  # Start timing when no hands detected
                    no_hands_start_time = time.time()

                # Finalize the sentence if no hands are detected for 2 seconds
                if (time.time() - no_hands_start_time) >= 2:
                    if len(predicted_words) > 0 and not has_spoken:
                        # Check if the only word is a space
                        if all(word == "-" for word in predicted_words):
                            print("Only spaces detected, skipping voice output.")
                        else:
                            sentence = ''.join(predicted_words)  # Create a sentence from the list of words
                            print(f"Final Sentence: {sentence}")
                            IntoVoice(sentence)  # Call the text-to-speech function
                            has_spoken = True  # Set the spoken flag

                    # Resetting the predictions
                    predicted_words = []
                    last_prediction = ""
                    hold_start_time = None  # Reset the hold time since hands are not detected
                    
                    
                    
            #PRINTING WORD ONTO SCREEN
            rect_height = 38
            cv2.rectangle(frame_rgb, (0, 0), (W, rect_height), (0, 0, 0), -1)

            display_text = ''.join(predicted_words)
            font_scale = 1.0
            text_width, text_height = cv2.getTextSize(display_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 1)[0]

            max_width = W - 20
            while text_width > max_width:
                font_scale -= 0.05
                text_width, text_height = cv2.getTextSize(display_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 1)[0]
                
            cv2.putText(frame_rgb, display_text, (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('frame', frame_rgb)  
            key = cv2.waitKey(10) & 0xFF
            if key == ord('q') or key == ord('Q'):
                break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_prediction()