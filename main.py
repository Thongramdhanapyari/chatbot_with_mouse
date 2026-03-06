import pyautogui
import pyperclip
import time
import ollama
import keyboard

pyautogui.FAILSAFE = True

print("Bot is running. Slam mouse to TOP-LEFT corner to emergency stop.")

try:
    while True:
        time.sleep(2)
        pyautogui.click(1402 ,1034)
        time.sleep(1)

        pyautogui.moveTo(643,188)

        # 3. Hold SHIFT and click the END of the message
        pyautogui.dragTo(654,916,duration=1.0,button='left')
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.2)
        time.sleep(1) # wait for clipboard to update

        # text from clipboard
        received_text = pyperclip.paste()
        print(received_text)
        #.strip() will remove all leading/trailing whitespace ..."" is falsy.." "is truthy
        if received_text and "import pyautogui" not in received_text:
            print(f"Responding to: {received_text[:50]}...")
            
            #asking ollama
            response = ollama.chat(model='llama3.2:1b',messages=[
                {'role':'system','content':'You are a helpful assistent. Write a short,professional reply to this message.'},
                {'role':'user','content':received_text}
            ])
            reply = response['message']['content']
            #reply
            pyautogui.click(693,973)
            pyautogui.write(reply,interval = 0.03)
            pyautogui.press('enter')
            print("Reply sent")
            
            pyperclip.copy("") 
            print("Reply sent. Waiting for next message...")
            
except pyautogui.FailSafeException:
    print("\nFAIL-SAFE TRIGGERED: Script stopped safely.")
except KeyboardInterrupt:
    print("\nManual Ctrl+C detected. Goodbye!")