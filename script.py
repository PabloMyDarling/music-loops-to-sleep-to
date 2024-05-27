from pygame.mixer import *; init()
from customtkinter import *
from tkinter import Menu, PhotoImage

def newLoop(x=None):
    Channel(1).set_volume(volume.get())
    Channel(1).stop(); Channel(1).play(Sound("loops/"+song.get()+".mp3"), -1, fade_ms=2000)

root = CTk()
root.title("music loops to sleep to")
root.geometry("420x420+5+5")
root.resizable(False, False)
root.config(menu=Menu(root))

logo = PhotoImage(file="logo.png")
root.iconphoto(True, logo)

song = StringVar(root, "Villain - Eclipse")

CTkLabel(root, text="music loops to sleep to", font=("", 23)).pack()
CTkLabel(root, text="headphones recommended!").pack()

loopFrame = CTkFrame(root, 275)
loopFrame.propagate(False); loopFrame.pack(pady=50)

CTkLabel(loopFrame, text="settings", font=("", 18)).pack(pady=1)

CTkOptionMenu(loopFrame, 188, values=["Villain - Eclipse", "Cigarettes out the Window - TV Girl", "Boys a liar - PinkPantheress", "Rain - Lee"], command=newLoop, variable=song).pack(pady=10)

CTkLabel(loopFrame, text="volume").pack()
def changeVol(x=None):Channel(1).set_volume(volume.get())
volume = CTkSlider(loopFrame, width=188, height=15, command=changeVol)
volume.pack()

def rainOn(x=None):
    if rain.get() == 1:
        Channel(2).set_volume(.5)
        Channel(2).play(Sound("ambience/rain.mp3"), -1, fade_ms=1000)
    else: Channel(2).stop()
def cafeOn(x=None):
    if cafe.get() == 1:
        Channel(3).set_volume(.5)
        Channel(3).play(Sound("ambience/cafe.mp3"), -1, fade_ms=1000)
    else: Channel(3).stop()

rain = CTkSwitch(loopFrame, text="ambience (rain)", hover=False, command=rainOn); rain.pack(pady=2)
cafe = CTkSwitch(loopFrame, text="ambience (cafe)", hover=False, command=cafeOn); cafe.pack()

volume.set(0.1276595744680851)
newLoop()

root.mainloop()
