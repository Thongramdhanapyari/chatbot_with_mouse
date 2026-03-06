#  My Local AI Chat Experiment

Hey, I built this little project to handle it for me. It’s a DIY auto-responder that "sees" my screen, copies text, and uses **Ollama (Llama 3.2)** to write back. No APIs, no fees—just local AI doing its thing.

###  What I'm using:
* **Ollama** (running the `llama3.2:1b` model)
* **Python libraries:** `pyautogui`, `pyperclip`, and `ollama`

You can grab them with:
```bash
pip install pyautogui pyperclip ollama
```

###  Getting it Working:
Since every monitor has a different resolution, my hardcoded coordinates **will not work for you**. You’ll need to map out the specific $X$ and $Y$ spots on your own screen where the chat window and input box live.

**1. Finding your coordinates:**
I’ve included a quick helper snippet. Run this in your terminal and simply hover your mouse over the areas you want the bot to click or drag:

```python
import pyautogui

#print("Move your mouse to the target area...")
while True:
    a = pyautogui.position()
    print(a)

```

**2. Update the code:**
Open the script and swap my numbers in click(), moveTo(), and dragTo() with the ones you just found. 

**3. Run the bot:**

```Bash
python main.py
```

###  How to Stop the Bot:
Automation can get a little wild if a window moves or a pop-up appears. I’ve included two ways to stop the script instantly:

* **The "Panic" Move:** Slam your mouse cursor into the **TOP-LEFT corner (0,0)** of your screen. I enabled `pyautogui.FAILSAFE`, which triggers a `FailSafeException` to kill the loop immediately.
* **Manual Kill:** Press `Ctrl+C` in your terminal. 

The code is wrapped in a `try/except` block, so it won't just crash—it'll print a clean message and exit safely.

### --Notes--
Keep the chat window visible. 
If you cover it, the bot will get confused and click the wrong thing.
This is just a fun side project I made to see how local LLMs can interact with my desktop.