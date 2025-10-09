import os
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mediapipe as mp

# THIS IS TO PRINT OUT ALL OF THE ALPHABET INTO A FRAME!
# THIS IS TO PRINT OUT ALL OF THE ALPHABET INTO A FRAME!
# THIS IS TO PRINT OUT ALL OF THE ALPHABET INTO A FRAME!
# THIS IS TO PRINT OUT ALL OF THE ALPHABET INTO A FRAME!
# THIS IS TO PRINT OUT ALL OF THE ALPHABET INTO A FRAME!
# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.2)

# Create the Tkinter window
learn = tk.Tk()
learn.title("Learn")
learn.geometry("850x600")  # Adjust the size of the window
learn.withdraw()

# Create a canvas to make the frame scrollable
canvas = tk.Canvas(learn)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a vertical scrollbar linked to the canvas
scrollbar = tk.Scrollbar(learn, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Create a frame inside the canvas to hold the images
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.config(yscrollcommand=scrollbar.set)
    
def visualize_landmarks():
    data_dir = 'asl_dataset_test'
    learn.deiconify()
    # Variables for grid placement
    row = 0
    col = 0

    # Iterate through images in the dataset directory
    for label in sorted(os.listdir(data_dir)):
        if label == '.DS_Store':
            continue
        for img_file in os.listdir(os.path.join(data_dir, label))[:1]:  # JUST TAKE 1 IMAGE FROM THE FOLDER!
            img = cv2.imread(os.path.join(data_dir, label, img_file))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #NO is the image that done have mediapipe draw in it
            img_NO = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Process the image with Mediapipe
            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        img_rgb,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )

            # Resize image
            img_pil = Image.fromarray(img_rgb)
            img_pil2 = Image.fromarray(img_NO)
            img_resized = img_pil.resize((150, 150))
            img_resized2 = img_pil2.resize((150, 150))

            # Convert images to Tkinter compatible format
            img_tk = ImageTk.PhotoImage(img_resized, master=learn)
            img_tk2 = ImageTk.PhotoImage(img_resized2, master=learn)

            # Create label widget for the first image
            label_img = tk.Label(scrollable_frame, image=img_tk)
            label_img.image = img_tk  # Keep reference for Tkinter
            label_img.grid(row=row, column=col, padx=10, pady=10)

            # Create label widget for the second image
            label_img2 = tk.Label(scrollable_frame, image=img_tk2)
            label_img2.image = img_tk2  # Keep reference for Tkinter
            label_img2.grid(row=row, column=col + 1, padx=10, pady=10)  # Place in next column

            # Move to the next column
            col += 2
            if col >= 6:  # After 6 label, move to the next row
                col = 0
                row += 1

            # Add a title with the label name below the images
            title_label = tk.Label(scrollable_frame, text=label, font=("Helvetica", 12))
            title_label.grid(row=row, column=col, padx=10, pady=10)
            
            # Move to the next column
            col += 1
            if col >= 6:  # After 6 label, move to the next row
                col = 0
                row += 1

    # Update the scrollable frame's scroll region
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Handle window close
    def on_close():
        """Handle the close event for the ASL Prediction window."""
        learn.withdraw()
        learn.quit()

    learn.protocol("WM_DELETE_WINDOW", on_close)
    
    # Bind the mouse scroll to canvas scrolling
    def on_mouse_wheel(event):
        if event.delta > 0:  # Scroll up
            canvas.yview_scroll(-1, "units")
        else:  # Scroll down
            canvas.yview_scroll(1, "units")
    
    learn.bind_all("<MouseWheel>", on_mouse_wheel)

    # Start the Tkinter window
    learn.mainloop()

if __name__ == "__main__":
    visualize_landmarks()
