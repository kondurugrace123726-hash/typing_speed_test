import time

text = "Python is easy and powerful"

print("Type this sentence exactly:")
print(text)

input("Press Enter to start...")

start = time.time()

typed = input("\nStart typing: ")

end = time.time()

time_taken = end - start

words = len(text.split())
wpm = (words / time_taken) * 60

correct_chars = 0

for i in range(min(len(text), len(typed))):
    if text[i] == typed[i]:
        correct_chars += 1

accuracy = (correct_chars / len(text)) * 100

print("\n--- Result ---")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(wpm, 2), "WPM")
print("Accuracy:", round(accuracy, 2), "%")