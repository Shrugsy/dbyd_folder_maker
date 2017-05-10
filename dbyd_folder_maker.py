from Tkinter import Tk
import Tkinter, tkMessageBox, tkFileDialog
import sys
import os

r = Tk()
r.withdraw()
root = Tkinter.Tk()
dirName = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select Dial Before You Dig directory to create folders')
root.destroy()


confBox = tkMessageBox.askokcancel("Select column", "Please select Authorities column then confirm\n(Hint: use the 'ColumnCopy' extension in chrome for easy selection.)")
if confBox:
    result = r.selection_get(selection = "CLIPBOARD")
    print(result)
    r.destroy()
    result = result.translate(None, '/')
    resultList = result.split("\n")
    print(resultList)

else:
    sys.exit()

tmp = '\\'

for i in resultList:
    if i != 'Authority':
        foldDir = dirName+tmp+i
        print(i)
        print(foldDir)
        if not os.path.exists(foldDir):
            os.makedirs(foldDir)

