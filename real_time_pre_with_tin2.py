import cv2
import pickle
import mediapipe as mp
import numpy as np
import time
import customtkinter as ctk
from PIL import Image, ImageTk
from geminiAI2 import IntoVoice

# THIS IS PREDICTION THAT MAKE FRAME BY USING TKINTER, OTHER IS THE DEMO
# THIS IS PREDICTION THAT MAKE FRAME BY USING TKINTER, OTHER IS THE DEMO
# THIS IS PREDICTION THAT MAKE FRAME BY USING TKINTER, OTHER IS THE DEMO
# THIS IS PREDICTION THAT MAKE FRAME BY USING TKINTER, OTHER IS THE DEMO
# Load model: Taking out the file pickle from the model data [the data is in a form of label of prediction for the Random Forest Model]
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
# CHOOSE YOUR MODEL
model_dict = pickle.load(open('model3_2.p', 'rb'))
model = model_dict['model3_2']

# Load the detection of the mediapipe to detect joint of the hands for prediction
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create the main Tkinter window
root = ctk.CTk()      
root.title("ASL Prediction")

# Initially hide the prediction window
root.withdraw()

# Create a label to display predictions
prediction_label = ctk.CTkLabel(root, text="Prediction: ", font=("Helvetica", 20), width=50)
prediction_label.pack(pady = 10)

# Create a canvas to display the video feed
canvas = ctk.CTkCanvas(root, width=800, height=600, bg="black")
canvas.pack(pady = 10)

# Initialize flags and variables
predicted_words = []
    
def speak_prediction():
    if len(predicted_words) > 0:
        sentence = ''.join(predicted_words)  # Create a sentence from the list of words
        print(f"Final Sentence: {sentence}")
        IntoVoice(sentence)  # Call the text-to-speech function
       
def clear_prediction():
    global predicted_words, last_prediction, hold_start_time
    predicted_words = []
    last_prediction = ""
    hold_start_time = None
    prediction_label.configure(text="Prediction: ")
    print("Cleared predictions.")

# Add Speak and Clear buttons
speak_button = ctk.CTkButton(root, text="Speak",font=("Helvetica", 25), command=speak_prediction, width=150)
speak_button.pack(pady=5)

clear_button = ctk.CTkButton(root, text="Clear All",font=("Helvetica", 25), command=clear_prediction, width=150)
clear_button.pack(pady=5)

def start_prediction():
    """Start the camera and handle the ASL prediction."""
    # Show the prediction window when starting the prediction
    root.deiconify()

    # Initialize video capture
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    # IF YOU DONT SEE THE FRAME, TRY SWITCH NUMBER BECAUSE YOUR CAMERA MAY DIFFERENT FROM MINE!
    cap = cv2.VideoCapture(0)

    last_prediction = ""
    hold_start_time = None
    del_hold_start_time = None

    # Handle window close
    def on_close():
        """Handle the close event for the ASL Prediction window."""
        cap.release()  # Release the video capture
        root.withdraw()  # Hide the prediction window
        clear_prediction()

    root.protocol("WM_DELETE_WINDOW", on_close)


    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
        while cap.isOpened():
            data_aux = []
            x_ = []
            y_ = []

            # Read frame from the camera
            ret, frame = cap.read()
            H, W, _ = frame.shape

            # Convert to RGB for processing
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.flip(frame_rgb, 1)
            frame_rgb.flags.writeable = False
            results = hands.process(frame_rgb)
            frame_rgb.flags.writeable = True
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

            # Displaying words on the Tkinter label
            display_text = ''.join(predicted_words)
            prediction_label.configure(text=f"Prediction: {display_text}")

            # Convert OpenCV frame to ImageTk format
            frame_rgb = cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb, (800, 600))
            img = Image.fromarray(frame_rgb)
            
            # VERY IMPORTANT NOTE: THE MASTER IS MUST HAVE CAUSE, THE PHOTOIMAGE IF NOT HAVE, WILL POINT TO THE DEFAULT WHICH IS ROOT
            # THIS MASTER WHEN IN OTHER FILE: SIGN GAME -> MASTER = GAME, TO MAKE IT POINT TO THE CORRECT IMAGE FILE NOT THE ROOT FILE!!!
            
            imgtk = ImageTk.PhotoImage(image=img, master = root)

            # Update the canvas with the new frame
            root.image_ref = imgtk
            canvas.create_image(0, 0, image=imgtk, anchor=ctk.NW)

            # Update the Tkinter window
            root.update_idletasks()
            root.update()

    cap.release()

if __name__ == "__main__":
    start_prediction()
