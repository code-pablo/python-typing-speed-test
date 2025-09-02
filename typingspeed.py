import time
import pynput
from pynput.keyboard import Key , Listener

class Typingspeed:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_time = None
        self.total_words = 0
        self.accuracy = 0
        self.correct_words = 0
        self.incorrect_words = 0
        self.test_text = "typing speed tracker is a clean and fun project  to help you improve your typing speed and accuracy. "
        self.user_input = ""
        self.listener = None

    def start_test(self):
        print("Typing Speed Test")
        print("Type the following text as quickly and accurately as you can:")
        print(self.test_text)
        print("Press Enter when you are done.\n")
        
        self.start_time = time.time()
        
        with Listener(on_press=self.on_press) as listener:
            self.listener = listener
            listener.join()
        return None

    #this function is for special keys in keyboard
    def on_press(self, key):
        if key == Key.enter:
            self.end_test()
            return False  # Stop listener
        elif key == Key.backspace:
            self.user_input = self.user_input[:-1]
            print("\r" + self.user_input + " ", end="")
        elif hasattr(key, 'char') and key.char is not None:
            self.user_input += key.char
            print("\r" + self.user_input, end="")
        elif key == Key.space:
            self.user_input += ' '
            
#this function calculate total time and calls two functions to calculate and display
    def end_test(self):
        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        self.calculate_results()
        self.display_results()

#this function calculate total_words,compare words  find/count correct and incorrect words
    def calculate_results(self):
        user_words = self.user_input.split()
        test_words = self.test_text.split()
        
        self.total_words = len(user_words)

        #checking correct and incorrect words
        for uw, tw in zip(user_words, test_words):
            if uw == tw:
                self.correct_words += 1
            else:
                self.incorrect_words += 1
        
     #for checking accuracy
        if len(test_words) > 0:
            self.accuracy = (self.correct_words / len(test_words)) * 100

 #this function is for displaying final result
    def display_results(self):
        wpm = (self.total_words / self.total_time) * 60 if self.total_time > 0 else 0
        print("\n\nTest Completed!")
        print(f"Total Time: {self.total_time:.2f} seconds")
        print(f"Total Words Typed: {self.total_words:.2f}")
        print(f"Correct Words: {self.correct_words}")
        print(f"Incorrect Words: {self.incorrect_words:.2f}")

        print(f"Accuracy: {self.accuracy}%")
        print(f"Words Per Minute (WPM): {wpm:.2f}")


#example usage
t = Typingspeed()
t.start_test()