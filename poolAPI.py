from tkinter import *
from urllib.request import *
import ast


response = urlopen("https://www.usxmrpool.com:8119/stats")
poolStats = response.read()
poolStats = poolStats.decode("utf-8")
poolStats = ast.literal_eval(poolStats)
print(poolStats['pool']['hashrate'])
print(poolStats['pool']['miners'])
print(poolStats['pool']['totalBlocks'])

def apiUpdate():
    response = urlopen("https://usxmrpool.com:8119/stats")
    poolStats = response.read()
    poolStats = poolStats.decode("utf-8")
    poolStats = ast.literal_eval(poolStats)
    return(poolStats['pool']['hashrate'], poolStats['pool']['miners'], poolStats['pool']['totalBlocks'])

def updateText():
    poolStatsTuple = apiUpdate()
    if poolStatsTuple[0] < 1000:
        hashrateLabel['text'] = "Hashrate: %.5s" % str(poolStatsTuple[0]+" H/s")
    elif 1000 <= poolStatsTuple[0] < 1000000:
        hashrateLabel['text'] = "Hashrate: %.5s" % str((poolStatsTuple[0]/1000))+" kH/s"
    elif 1000000 <= poolStatsTuple[0] < 1000000000:
        hashrateLabel['text'] = "Hashrate: %.5s" % str((poolStatsTuple[0]/1000000))+" mH/s"
    minersLabel['text'] = "Miners: "+str(poolStatsTuple[1])
    totalBlocksLabel['text'] = "Total Blocks: "+str(poolStatsTuple[2])
    root.after(10000, updateText)

def infoButton():
    toplevel = Toplevel()
    Toplevel.configure(bg = "black")
    poolInfo = Label(toplevel, text="Pool: www.usxmrpool.com", fg = "sky blue", bg = "black")
    poolInfo.grid()
    githubInfo = Label(toplevel, text="Github: ZachC16", fg = "sky blue", bg = "black")
    githubInfo.grid()

root = Tk()
root.geometry("400x200")
root.configure(bg = "black")
root.title("USXMRPool Stats")

titleLabel = Label(text = "US XMR Pool Stats", fg = "sky blue", bg = "black", padx = 120, pady = 25)
titleLabel.config(font = "Courier 16 bold")
titleLabel.grid()
hashrateLabel = Label(text = "", fg = "sky blue", bg = "black", padx = 120)
hashrateLabel.grid()
minersLabel = Label(text = "", fg = "sky blue", bg = "black", padx = 120)
minersLabel.grid()
totalBlocksLabel = Label(text = "", fg = "sky blue", bg = "black", padx = 120)
totalBlocksLabel.grid()


updateText()
root.mainloop()
