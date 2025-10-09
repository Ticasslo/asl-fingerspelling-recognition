#menu.py
import customtkinter as ctk
from real_time_pre_with_tin2 import start_prediction, root  # Import root từ file dự đoán
from signgame import gamestart, game
from visualization import visualize_landmarks, learn

# Set appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASL Language Translator")
        
        self.geometry("640x480")        
        self.resizable(False, False)  # Prevent resizing
        
        # Title
        self.title_label = ctk.CTkLabel(self, text="Main Menu", font=("Arial", 24))
        self.title_label.pack(pady=25)

        # Button to go to ASL-to-Voice
        self.asl_to_voice_button = ctk.CTkButton(
            self, text="ASL to Voice", command=self.start_camera, width=200, height=50
        )
        self.asl_to_voice_button.pack(pady=15)

        # Button to go to ASL-to-Voice
        self.gameButton = ctk.CTkButton(
            self, text="ASL Sign Game!", command=self.start_game, width=200, height=50
        )
        self.gameButton.pack(pady=15)
        
        # Button to go to Visualization/Learning
        self.learnButton = ctk.CTkButton(
            self, text="Learn the ASL!", command=self.start_learn, width=200, height=50
        )
        self.learnButton.pack(pady=15)
        
        # Ensure the window closes correctly
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_camera(self):
        """Start or show the ASL prediction window."""
        if not root.winfo_ismapped():  # Check if the ASL prediction window is not currently visible
            self.withdraw()
            root.deiconify()  # Show the prediction window
            start_prediction()  # Start the prediction process
            self.deiconify()
        else:
            print("ASL Prediction is already running.")
            
    def start_game(self):
        """Start or show game window."""
        if not game.winfo_ismapped():
            self.withdraw()
            game.deiconify()  # Show the prediction window
            gamestart()  # Start the prediction process
            self.deiconify()
        else:
            print("ASL Sign Game! is already running.")

    def start_learn(self):
        """Start or show game window."""
        if not learn.winfo_ismapped():
            visualize_landmarks()
        else:
            print("Learn with ASL is already running!")
            
    def on_close(self):
        """Close the entire application."""
        learn.withdraw()
        learn.quit()
        self.quit()  # Quit the main menu window, terminating the program
        

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
