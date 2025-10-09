#signgame.py
import cv2
import pickle
import mediapipe as mp
import numpy as np
import time
import customtkinter as ctk
from PIL import Image, ImageTk
import random

#This is the sound file
import pygame

pygame.mixer.init()
score_up_sound = pygame.mixer.Sound('scoreupwav.wav')
music_sound = pygame.mixer.Sound('gamemusic.mp3')
music_sound.set_volume(0.45)
score_up_sound.set_volume(0.45)
music_channel = pygame.mixer.Channel(0)
effects_channel = pygame.mixer.Channel(1)

def play_music():
    if not music_channel.get_busy():
        music_channel.play(music_sound, loops=-1)
def stop_music():
    if music_channel.get_busy():
        music_channel.stop()
        

# Load model: Taking out the file pickle from the model data [the data is in a form of label of prediction for the Random Forest Model]
model_dict = pickle.load(open('model3_2.p', 'rb'))
model = model_dict['model3_2']

# Load the detection of the mediapipe to detect joint of the hands for prediction
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Create the main CustomTkinter window
game = ctk.CTk()      
game.title("ASL Game")

# Initially hide the prediction window
game.withdraw()

timeFlag = False
score = 0

# CustomTkinter widgets
prediction_label_game = ctk.CTkLabel(game, text="Prediction: ", font=("Helvetica", 20), width=50)
prediction_label_game.pack(pady=10)

timer_label = ctk.CTkLabel(game, text="Time Left: 30", font=("Helvetica", 20), width=50)
timer_label.pack()

score_label = ctk.CTkLabel(game, text=f"Score: {score}", font=("Helvetica", 20), width=50)
score_label.pack()

canvas_game = ctk.CTkCanvas(game, width=800, height=600, bg="black")
canvas_game.pack(pady=10)

#Make the score so up IF user guess right: time > 0.8s
def update_score():
    global score
    score += 1
    score_label.configure(text=f"Score: {score}")

#When the player click the start button, do start_timer func
def start_timer():
    #1st: CHECK IF PLAYER CLICK START AGAIN
    global timeFlag
    if timeFlag == True:
        game_over()
        return  
    
    timeFlag = True #Bc player start, the timeFlag is start -> True
    global time_left
    time_left = 30  # Start from 30 seconds
    
    #Check if any Label Named : GAME OVER -> DELETE IT
    for widget in game.winfo_children():
        if isinstance(widget, ctk.CTkLabel) and widget.cget("text").startswith("Game Over"):
            widget.destroy()
            
    #Make the timer start to count down from 30 -> 0
    update_timer()

def update_timer():
    global time_left, timeFlag
    #Dont update if timeFlag not on yet
    if timeFlag == False:
        return
    
    #Start to countdown
    if time_left > 0:
        time_left -= 1
        timer_label.configure(text=f"Time Left: {time_left}")
        game.after(1000, update_timer)  # Update every second
    else:
        game_over() #Timer reach 0

def game_over():
    # When over, timeFlag = Fale -> dont run timer
    # Score back to 0
    # time_left back to 60
    global score, time_left, timeFlag
    timeFlag = False
    game_over_label = ctk.CTkLabel(game, text=f"Game Over\nFinal Score: {score}", font=("Helvetica", 22))
    game_over_label.pack(pady=5)
    score = 0
    time_left = 60
    #Update GUI
    score_label.configure(text=f"Score: {score}")
    timer_label.configure(text="Time Left: 30")
    #Make the button work again
    start_button.pack(pady=10)
    
    
    
    
    
    
    
def gamestart():    
    """Start the camera"""
    # Add a start button to begin the game
    global start_button
    start_button = ctk.CTkButton(game, text="Start Game", command=start_timer, font=("Helvetica", 25), width=50)
    start_button.pack(pady=10)
    
    # Show the game window when starting the prediction, also play music
    game.deiconify()
    game.after(1500, play_music)  
      
    # Variables
    hold_start_time = None
    
    target_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Random letter to guess
    prediction_label_game.configure(text=f"Prediction: {target_letter}")

    
    # Turn on the camera, it could be different for each person
    cap = cv2.VideoCapture(0)


    # Handle window close
    def on_close():
        """Handle the close event for the ASL Prediction window."""
        cap.release()  # Release the video capture
        game.withdraw()  # Hide the game window
        game_over()
        stop_music() #Stop the music
        start_button.destroy()
        #Check if any Label Named : GAME OVER -> DELETE IT
        for widget in game.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text").startswith("Game Over"):
                widget.destroy()

    game.protocol("WM_DELETE_WINDOW", on_close)

    # Turn on hand tracking
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









                # If the current prediction is same as target letter
                if current_prediction == target_letter and timeFlag == True:
                    if hold_start_time is None:
                        hold_start_time = time.time()  # Start the timer when the correct letter is predicted
                    elif time.time() - hold_start_time >= 0.8:  # Seconds of holding the correct prediction
                        #When time over 0.8 -> Play sound, update score, new letter, and reset the timer
                        effects_channel.play(score_up_sound)
                        update_score()
                        target_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Change target letter to a new random one
                        prediction_label_game.configure(text=f"Prediction: {target_letter}")
                        hold_start_time = None
                else:
                    hold_start_time = None
            
            # Convert OpenCV frame to ImageTk format -> This part is to put frame from cv2/ your camera frame onto GUI
            # Why convert to RGB? BC we and GUI-Tinkler need RGB while openCV use BGR
            frame_rgb = cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb, (800, 600))
            
            # VERY IMPORTANT NOTE: THE MASTER IS MUST HAVE, CAUSE THE PHOTOIMAGE IF NOT HAVE -> WILL POINT TO THE DEFAULT WHICH IS ROOT
            # THIS ROOT-MASTER IS USE IN REAL_PREDICTION FILE SO SIGN GAME.PY -> MASTER = GAME, TO MAKE IT POINT TO THE CORRECT IMAGE FILE NOT THE ROOT FILE!!!
            
            # We are making the frame from OPENCV then PUT IT ON the Tinkler
            # OPENCV Frame is a NUMPY ARRAY!!!!! We need to make it into 
            img_game = Image.fromarray(frame_rgb)
            # Convert the image into Photo from an Pillow image object
            imgtk_game = ImageTk.PhotoImage(image=img_game, master = game)

            # Update the canvas with the new frame
            game.image_ref = imgtk_game
            canvas_game.create_image(0, 0, image=imgtk_game, anchor=ctk.NW)

            # Update the Tkinter window
            game.update_idletasks()
            game.update()

    cap.release()

if __name__ == "__main__":
    gamestart()
