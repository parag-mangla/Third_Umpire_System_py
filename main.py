import tkinter
import cv2                                              # pip install opencv-python
import PIL.Image, PIL.ImageTk                           # pip install pillow
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("videoplayback.mp4")
def play(speed):
    print(f"you clicked play. speed is {speed}")
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, height=SET_HEIGHT, width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
        
def pending(decision):
    # 1> display decision pending image
    frame = cv2.cvtColor(cv2.imread("decision_pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # wait for 1.5 second
    time.sleep(1.5)

    # 2> display sponcer image
    frame = cv2.cvtColor(cv2.imread("sponcer.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    # wait for 1.5 second
    time.sleep(1.5)

    # 3> display result image
    if decision == 'out':
        decisionImg = "OUT.jpg"
    else:
        decisionImg = "NOT_OUT.jpg"    
        
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()

    print("Player is OUT")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")

#width and height of our screen
SET_WIDTH = 500
SET_HEIGHT = 283

# tkinter GUI starts here
window = tkinter.Tk()
window.title("Third Umpire DRS REVIEW KIT")
cv_img = cv2.cvtColor(cv2.imread("IPL.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

#buttons to control play & back
btn = tkinter.Button(window, text="<< Privious (Fast)", width=70, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="< Privious (Slow)", width=70, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text=" Next (Fast) >>", width=70, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Next (Slow) >", width=70, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text=">> OUT <<", width=70, command=out)
btn.pack()

btn = tkinter.Button(window, text=">> NOT OUT <<", width=70, command=not_out)
btn.pack()


window.mainloop()












