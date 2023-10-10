import tkinter as tk
from tkinter.messagebox import showinfo
import windnd
from PIL import ImageTk, Image
import base64
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import time


def button1():  # the method of encryption button on the DES interface
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new interface
    newinterface.resizable(0, 0)
    bg = ImageTk.PhotoImage(image)  # the background picture
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    newinterface.title('DES encryption')
    bgL = tk.Label(newinterface, image=bg)
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your file in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # hint of drag txt file
    lb.place(x=95, y=50)
    lb2 = tk.Label(newinterface, text='Please enter a 8 - digit key below', bg='#87CEFA',
                   font=('Times New Roman', 14))  # hint of entering key
    lb2.place(x=110, y=100)
    entry = tk.Entry(newinterface)  # the enter box
    entry.place(x=160, y=130)
    windnd.hook_dropfiles(newinterface, func=drag)  # the drag document function
    b = tk.Button(newinterface, text='encryption', command=lambda: button3(entry.get(), newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))  # encryption button
    b.place(x=180, y=180)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    newinterface.focus_force()  # focus on the new window
    newinterface.mainloop()


def button10():  # the method of encryption button on the AES interface
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new interface
    newinterface.resizable(0, 0)
    bg = ImageTk.PhotoImage(image)  # the background picture
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    newinterface.title('AES encryption')
    bgL = tk.Label(newinterface, image=bg)
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your file in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # hint of drag txt file
    lb.place(x=95, y=50)
    lb2 = tk.Label(newinterface, text='Please enter a 16 -, 24 -, or 32 - digit key below', bg='#87CEFA',
                   font=('Times New Roman', 14))  # hint of entering key
    lb2.place(x=60, y=100)
    entry = tk.Entry(newinterface)  # the enter box
    entry.place(x=160, y=130)
    windnd.hook_dropfiles(newinterface, func=drag)  # the drag document function
    b = tk.Button(newinterface, text='encryption', command=lambda: button30(entry.get(), newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))  # encryption button
    b.place(x=180, y=180)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    newinterface.focus_force()  # focus on the new window
    newinterface.mainloop()


def button100():  # the method of encryption button on the Comparison interface
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new interface
    newinterface.resizable(0, 0)
    bg = ImageTk.PhotoImage(image)  # the background picture
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    newinterface.title('AES and DES encryption')
    bgL = tk.Label(newinterface, image=bg)
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your file in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # hint of drag txt file
    lb.place(x=100, y=50)
    lb3 = tk.Label(newinterface, text='Please enter a DES (8 - digit) key below', bg='#87CEFA',
                   font=('Times New Roman', 14))  # hint of entering key
    lb3.place(x=90, y=80)
    entry0 = tk.Entry(newinterface)  # the enter box
    entry0.place(x=160, y=110)
    lb2 = tk.Label(newinterface, text='Please enter a AES (16 -, 24 -, or 32 - digit) key below', bg='#87CEFA',
                   font=('Times New Roman', 14))  # hint of entering key
    lb2.place(x=40, y=140)
    entry = tk.Entry(newinterface)  # the enter box
    entry.place(x=160, y=170)
    windnd.hook_dropfiles(newinterface, func=drag)  # the drag document function
    b = tk.Button(newinterface, text='encryption', command=lambda: button300(entry.get(), entry0.get(),newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))  # encryption button
    b.place(x=180, y=200)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    newinterface.focus_force()  # focus on the new window
    newinterface.mainloop()

def button5():  # the method of back to main window function
    interface1.withdraw()  # destroy the top interface
    path.set('')  # clean the drag document
    interface.update()  # show the old interface
    interface.deiconify()


def button6(new):  # the method of back to AES/DES/Comparsion function
    new.destroy()  # destroy the top interface
    path.set('')  # clean the drag document
    interface1.update()  # show the old interface
    interface1.deiconify()


def drag(files):  # the method of drag document
    msg2 = '\n'.join((item.decode('gbk') for item in files))
    showinfo('your documents', msg2)  # the hint of drag successfully
    path.set(msg2)  # get the paths


def button2():  # the button of decryption button on the DES interface, very similar to the encryption button
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new window
    newinterface.resizable(0, 0)
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # get the size
    newinterface.title('DES decryption')
    bgL = tk.Label(newinterface, image=bg)  # background label
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your des txt document in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # the hint
    lb.place(x=60, y=50)
    lb2 = tk.Label(newinterface, text='Please enter a 8 - digit key below', bg='#87CEFA',
                   font=('Times New Roman', 14))
    lb2.place(x=110, y=100)
    entry = tk.Entry(newinterface)
    entry.place(x=160, y=130)
    windnd.hook_dropfiles(newinterface, func=drag)  # the decryption button
    b = tk.Button(newinterface, text='decryption', command=lambda: button4(entry.get(), newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))
    b.place(x=180, y=180)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # the back button
    back.place(x=380, y=220)
    newinterface.focus_force()
    newinterface.mainloop()


def button20():  # the button of decryption button on the AES interface, very similar to the encryption button
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new window
    newinterface.resizable(0, 0)
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # get the size
    newinterface.title('AES decryption')
    bgL = tk.Label(newinterface, image=bg)  # background label
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your aes txt document in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # the hint
    lb.place(x=60, y=50)
    lb2 = tk.Label(newinterface, text='Please enter a 16 -, 24 -, or 32 - digit key below', bg='#87CEFA',
                   font=('Times New Roman', 14))
    lb2.place(x=60, y=100)
    entry = tk.Entry(newinterface)
    entry.place(x=160, y=130)
    windnd.hook_dropfiles(newinterface, func=drag)  # the decryption button
    b = tk.Button(newinterface, text='decryption', command=lambda: button40(entry.get(), newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))
    b.place(x=180, y=180)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # the back button
    back.place(x=380, y=220)
    newinterface.focus_force()
    newinterface.mainloop()


def button200():  # the button of decryption button on the COMPARSION interface, very similar to the encryption button
    interface1.withdraw()  # hide the old window
    newinterface = tk.Toplevel()  # get a new window
    newinterface.resizable(0, 0)
    w = bg.width()
    h = bg.height()
    newinterface.geometry('%dx%d+500+300' % (w, h - 60))  # get the size
    newinterface.title('AES and DES decryption')
    bgL = tk.Label(newinterface, image=bg)  # background label
    bgL.place(x=-2, y=-60)
    lb = tk.Label(newinterface, text='Please drag your aes txt document in this interface', bg='#87CEFA',
                  font=('Times New Roman', 14))  # the hint
    lb.place(x=60, y=50)
    lb3 = tk.Label(newinterface, text='Please enter a DES (8 - digit) key below', bg='#87CEFA',
                   font=('Times New Roman', 14))
    lb3.place(x=90, y=80)
    entry2 = tk.Entry(newinterface)
    entry2.place(x=160, y=110)
    lb2 = tk.Label(newinterface, text='Please enter a AES (16 -, 24 -, or 32 - digit) key below', bg='#87CEFA',
                   font=('Times New Roman', 14))
    lb2.place(x=40, y=140)
    entry = tk.Entry(newinterface)
    entry.place(x=160, y=170)
    windnd.hook_dropfiles(newinterface, func=drag)  # the decryption button
    b = tk.Button(newinterface, text='decryption', command=lambda: button400(entry.get(),entry2.get(), newinterface), bg='#87CEFA',
                  font=('Times New Roman', 14))
    b.place(x=180, y=200)
    back = tk.Button(newinterface, text='Back', command=lambda: button6(newinterface), bg='#87CEFA',
                     font=('Times New Roman', 12))  # the back button
    back.place(x=380, y=220)
    newinterface.focus_force()
    newinterface.mainloop()


def button3(yourkey, newinterface):  # the method of encryption button on encryption interface on DES interface
    pathresult = path.get()
    Time = ''
    paths = pathresult.split('\n')  # get paths
    d = 0  # it is used to judge if the file encrypt successfully
    for p in paths:  # get each path of paths
        if len(yourkey) != 8:
                showinfo(title=None, message='Please enter a 8 - digit key')
        else:
            if p == '':  # judge if the user drag the document
                showinfo(title=None, message='Please drag your document')
                break
            else:
                file.set(p)
                binfile = open(p, 'rb')  # read the binary file, and encode it ,and covert it to string
                context = base64.b64encode(binfile.read())
                c = str(context, encoding='utf-8')
                start = time.time()
                des_encode(c,yourkey)   # encryption the file
                end = time.time()
                Time = str(end-start)
                d = 1
    if d == 1:  # when succeed, show the hint information, and destroy the top window, show the main interface
        showinfo(title=None, message='encrypt successfully (' + Time + 's)')
        newinterface.destroy()
        path.set('')
        interface1.update()
        interface1.deiconify()


def button30(yourkey, newinterface):  # the method of encryption button on encryption interface on AES interface
    pathresult = path.get()
    Time = ''
    paths = pathresult.split('\n')  # get paths
    d = 0  # it is used to judge if the file encrypt successfully
    for p in paths:  # get each path of paths
        if len(yourkey) != 16 and len(yourkey) != 24 and len(yourkey) != 32:
            showinfo(title=None, message='Please enter a 16 -, 24 -, or 32 - digit key')
        else:
            if p == '':  # judge if the user drag the document
                showinfo(title=None, message='Please drag your document')
                break
            else:
                file.set(p)
                binfile = open(p, 'rb')  # read the binary file, and encode it ,and covert it to string
                context = base64.b64encode(binfile.read())
                c = str(context, encoding='utf-8')
                start = time.time()
                aes_encode(c, yourkey)
                end = time.time()
                Time = str(end - start)
                d = 1
    if d == 1:  # when succeed, show the hint information, and destroy the top window, show the main interface
        showinfo(title=None, message='encrypt successfully (' + Time + 's)' )
        newinterface.destroy()
        path.set('')
        interface1.update()
        interface1.deiconify()


def button300(AESkey, DESkey, newinterface):  # the method of encryption button on encryption interface on Comparsion interface
    pathresult = path.get()
    Time = ''
    Time2 = ''
    paths = pathresult.split('\n')  # get paths
    d = 0  # it is used to judge if the file encrypt successfully
    for p in paths:  # get each path of paths
        if len(AESkey) != 16 and len(AESkey) != 24 and len(AESkey) != 32:
            showinfo(title=None, message='Please enter a AES  16 -, 24 -, or 32 - digit key')
        if len(DESkey) != 8:
            showinfo(title=None, message='Please enter a DES 8 - digit key')
        else:
            if p == '':  # judge if the user drag the document
                showinfo(title=None, message='Please drag your document')
                break
            else:
                file.set(p)
                binfile = open(p, 'rb')  # read the binary file, and encode it ,and covert it to string
                context = base64.b64encode(binfile.read())
                c = str(context, encoding='utf-8')
                start = time.time()
                aes_encode(c, AESkey)
                end = time.time()
                Time = str(end - start)
                start = time.time()
                des_encode(c, DESkey)
                end = time.time()
                Time2 = str(end - start)
                d = 1
    if d == 1:  # when succeed, show the hint information, and destroy the top window, show the main interface
        showinfo(title=None, message='AES time is ' + Time + '\n' + 'DES time is ' + Time2)
        newinterface.destroy()
        path.set('')
        interface1.update()
        interface1.deiconify()






def button4(yourkey, newinterface):  # the method of decryption button on decryption window on DES interface, it is similar to button3
    pathresult = path.get()
    Time = ''
    paths = pathresult.split('\n')
    d = 0  # judge if the file decrypt successfully
    for p in paths:
        name = p.split('\\')
        judge = name[len(name) - 1].split(" ")
        j = 0
        if judge[0] == 'The' and judge[1] == 'des' and judge[2] == 'text':
            # judge if the file is a encrypted txt file according to the spacial name
            j = 1
        type = name[len(name) - 1].split('.')
        if type[len(type) - 1] != 'txt':  # if  a txt
            showinfo(title=None, message='Please drag a txt document')
        else:
            if j == 1:
                if len(yourkey) != 8:
                    showinfo(title=None, message='Please enter a 8 - digit key')
                else:
                    if p == '':  # if the user drag a file
                        showinfo(title=None, message='Please drag your document')
                        break
                    else:
                        f = open(p, encoding='utf-8')
                        text = f.read()
                        file.set(p)  # decrypt the file
                        start = time.time()
                        try:
                            des_decode(text, yourkey)
                            end = time.time()
                            Time = str(end - start)
                            d = 1
                        except Exception as e:
                            showinfo(title=None, message='DESkey is wrong')
                            d = 0

            else:
                showinfo(title=None, message='Please drag a des txt document， the name is The des text of ...')
    if d == 1:  # when decryption successfully
        showinfo('congratulation!', 'decryption successfully! (' + Time + 's)')
        newinterface.destroy()
        path.set('')
        interface1.update()
        interface1.deiconify()


def button40(yourkey, newinterface):  # the method of decryption button on decryption window on AES interface, it is similar to button3
    pathresult = path.get()
    Time = ''
    paths = pathresult.split('\n')
    d = 0  # judge if the file decrypt successfully
    for p in paths:
        name = p.split('\\')
        judge = name[len(name) - 1].split(" ")
        j = 0
        if judge[0] == 'The' and judge[1] == 'aes' and judge[2] == 'text':
            # judge if the file is a encrypted txt file according to the spacial name
            j = 1
        type = name[len(name) - 1].split('.')
        if type[len(type) - 1] != 'txt':  # if  a txt
            showinfo(title=None, message='Please drag a txt document')
        else:
            if j == 1:
                if len(yourkey) != 16 and len(yourkey) != 24 and len(yourkey) != 32:
                    showinfo(title=None, message='Please enter a 16 -, 24 -, or 32 - digit key')
                else:
                    if p == '':  # if the user drag a file
                        showinfo(title=None, message='Please drag your document')
                        break
                    else:
                        f = open(p, encoding='utf-8')
                        text = f.read()
                        file.set(p)  # decrypt the file
                        start = time.time()
                        try:
                            aes_decode(text, yourkey)
                            end = time.time()
                            Time = str(end - start)
                            d = 1
                        except Exception as e:
                            showinfo(title=None, message='AESkey is wrong')
                            d = 0

            else:
                showinfo(title=None, message='Please drag a des txt document， the name is The des text of ...')
    if d == 1:  # when decryption successfully
        showinfo('congratulation!', 'decryption successfully! (' + Time + 's)')
        newinterface.destroy()
        path.set('')
        interface1.update()
        interface1.deiconify()

def button400(AESkey, DESkey, newinterface):  # the method of decryption button on decryption window on Comparsion interface, it is similar to button3
    pathresult = path.get()
    Time = ''
    Time2 = ''
    paths = pathresult.split('\n')
    l = len(paths)
    if l != 2:
        showinfo('Sorry', message='Please compare an AES file with a DES file')
    else:
        d = 0  # judge if the file decrypt successfully
        for p in paths:
            name = p.split('\\')
            judge = name[len(name) - 1].split(" ")
            j = 0
            if judge[0] == 'The' and judge[1] == 'aes' and judge[2] == 'text':
                # judge if the file is a encrypted txt file according to the spacial name
                j = 1
            if judge[0] == 'The' and judge[1] == 'des' and judge[2] == 'text':
                # judge if the file is a encrypted txt file according to the spacial name
                j = 2
            type = name[len(name) - 1].split('.')
            if type[len(type) - 1] != 'txt':  # if  a txt
                showinfo(title=None, message='Please drag a txt document')
            else:
                if j == 1:
                    if len(AESkey) != 16 and len(AESkey) != 24 and len(AESkey) != 32:
                        showinfo(title=None, message='Please enter a 16 -, 24 -, or 32 - digit key')
                    else:
                        if p == '':  # if the user drag a file
                            showinfo(title=None, message='Please drag your document')
                            break
                        else:
                            f = open(p, encoding='utf-8')
                            text = f.read()
                            file.set(p)  # decrypt the file
                            start = time.time()
                            try:
                                aes_decode(text, AESkey)
                                end = time.time()
                                Time = str(end - start)
                                d = 1
                            except Exception as e:
                                showinfo(title=None, message='AESkey is wrong')
                                d = 0

                else:
                    if j == 2:
                        if len(DESkey) != 8:
                            showinfo(title=None, message='Please enter a 16 -, 24 -, or 32 - digit key')
                        else:
                            if p == '':  # if the user drag a file
                                showinfo(title=None, message='Please drag your document')
                                break
                            else:
                                f = open(p, encoding='utf-8')
                                text = f.read()
                                file.set(p)  # decrypt the file
                                start = time.time()
                                try:
                                    des_decode(text, DESkey)
                                    end = time.time()
                                    Time2 = str(end - start)
                                    d = 1
                                except Exception as e:
                                    showinfo(title=None, message='DESkey is wrong')
                                    d = 0

                    else:
                        showinfo(title=None, message='Please drag a des txt document， the name is The des text of ...')
        if d == 1:  # when decryption successfully
            if Time != '' and Time != '':
                showinfo('congratulation!', message='AES time is ' + Time + '\n' + 'DES time is ' + Time2)
                path.set('')
                newinterface.destroy()
                interface1.update()
                interface1.deiconify()
            else:
                showinfo('Sorry!', message='Please compare an AES file with a DES file')



def openMain(interface):  # the method of main interface
    interface.title('DES and AES encryption and decryption')
    interface.resizable(0, 0)
    bgL = tk.Label(interface, image=bg, text='DES and AES encryption', font=('Times New Roman', 25), compound='center')
    bgL.place(x=-2, y=-60)  # the background picture
    w = bg.width()
    h = bg.height()
    b1 = tk.Button(interface, text='DES', command=button0, bg='#87CEFA', font=('Times New Roman', 14))
    b1.place(x=150, y=150)  # the DES button
    b2 = tk.Button(interface, text='AES', command=button00, bg='#87CEFA', font=('Times New Roman', 14))
    b2.place(x=270, y=150)  # the AES button
    back = tk.Button(interface, text='comparison', command=button000, bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    interface.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    interface.mainloop()


def button0():  # the method of DES button on the main interface
    interface.withdraw()  # hide the old window
    interface1.title('DES encryption and decryption')
    interface1.resizable(0, 0)
    bgL = tk.Label(interface1, image=bg, text='DES encryption', font=('Times New Roman', 25), compound='center')
    bgL.place(x=-2, y=-60)  # the background picture
    w = bg.width()
    h = bg.height()
    b1 = tk.Button(interface1, text='Encryption', command=button1, bg='#87CEFA', font=('Times New Roman', 14))
    b1.place(x=100, y=150)  # the encryption button
    b2 = tk.Button(interface1, text='Decryption', command=button2, bg='#87CEFA', font=('Times New Roman', 14))
    b2.place(x=280, y=150)  # the decryption button
    back = tk.Button(interface1, text='Back', command=button5, bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    interface1.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    interface1.update()
    interface1.deiconify()
    interface1.mainloop()

def button00():  # the method of AES button on the main interface
    interface.withdraw()  # hide the old window
    interface1.title('AES encryption and decryption')
    interface1.resizable(0, 0)
    bgL = tk.Label(interface1, image=bg, text='AES encryption', font=('Times New Roman', 25), compound='center')
    bgL.place(x=-2, y=-60)  # the background picture
    w = bg.width()
    h = bg.height()
    b1 = tk.Button(interface1, text='Encryption', command=button10, bg='#87CEFA', font=('Times New Roman', 14))
    b1.place(x=100, y=150)  # the encryption button
    b2 = tk.Button(interface1, text='Decryption', command=button20, bg='#87CEFA', font=('Times New Roman', 14))
    b2.place(x=280, y=150)  # the decryption button
    back = tk.Button(interface1, text='Back', command=button5, bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    interface1.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    interface1.update()
    interface1.deiconify()
    interface1.mainloop()


def button000():  # the method of CEOMPARISON button on the main interface
    interface.withdraw()  # hide the old window
    interface1.title('AES and DES encryption and decryption')
    interface1.resizable(0, 0)
    bgL = tk.Label(interface1, image=bg, text='AES and DES encryption', font=('Times New Roman', 25), compound='center')
    bgL.place(x=-2, y=-60)  # the background picture
    w = bg.width()
    h = bg.height()
    b1 = tk.Button(interface1, text='Encryption', command=button100, bg='#87CEFA', font=('Times New Roman', 14))
    b1.place(x=100, y=150)  # the encryption button
    b2 = tk.Button(interface1, text='Decryption', command=button200, bg='#87CEFA', font=('Times New Roman', 14))
    b2.place(x=280, y=150)  # the decryption button
    back = tk.Button(interface1, text='Back', command=button5, bg='#87CEFA',
                     font=('Times New Roman', 12))  # back button
    back.place(x=380, y=220)
    interface1.geometry('%dx%d+500+300' % (w, h - 60))  # the size of the window
    interface1.update()
    interface1.deiconify()
    interface1.mainloop()


def aes_decode(data, key):
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # Initializes the encryptor
    decrypted_text = aes.decrypt(base64.decodebytes(bytes(data, encoding='utf8'))).decode("utf8")  #decrpt
    paths = file.get()  # get the name of output file, the des text of + origin name
    names = paths.split("\\")
    name = names[len(names) - 1]
    na = name.split(" ")
    name = ''
    for n in range(4, len(na) - 1):
        name = name + na[n] + " "
    last = na[len(na) - 1]  # change the type of the file to the origin type
    l = str(last).split('.')
    name = name + l[0]
    for n in range(1, len(l) - 1):
        name = name + "." + l[n]
    title = 'The origin text (AES) of ' + name
    con = bytes(decrypted_text, encoding='utf-8')
    f2 = base64.b64decode(con)
    f8 = open(title, 'wb')
    f8.write(f2)
    f8.close()







def des_decode(data, key):
    des = DES.new(str.encode(key), DES.MODE_ECB)  # Initializes the encryptor
    decrypted_text = des.decrypt(base64.decodebytes(bytes(data, encoding='utf8'))).decode("utf8")  # decrpt
    paths = file.get()  # get the name of output file, the des text of + origin name
    names = paths.split("\\")
    name = names[len(names) - 1]
    na = name.split(" ")
    name = ''
    for n in range(4, len(na) - 1):
        name = name + na[n] + " "
    last = na[len(na) - 1]  # change the type of the file to the origin type
    l = str(last).split('.')
    name = name + l[0]
    for n in range(1, len(l) - 1):
        name = name + "." + l[n]
    title = 'The origin text (DES) of ' + name
    con = bytes(decrypted_text, encoding='utf-8')
    f2 = base64.b64decode(con)
    f8 = open(title, 'wb')
    f8.write(f2)
    f8.close()

def aes_encode(data, key):
    while len(data) % 16 != 0:  # add to 16 times bits
        data += (16 - len(data) % 16) * chr(16 - len(data) % 16)
    data = str.encode(data)
    aes = AES.new(str.encode(key), AES.MODE_ECB)  # get the aes encipher
    result = str(base64.encodebytes(aes.encrypt(data)), encoding='utf8').replace('\n', '')  # encrypt
    paths = path.get()  # get the name of output file, the des text of + origin name
    names = paths.split("\\")
    name = names[len(names) - 1]
    title = 'The aes text of ' + name + '.txt'
    f = open(title, 'w', encoding='utf-8')  # write the output file
    f.write(result)
    f.close()



def des_encode(data, key):
    while len(data) % 16 != 0:  # add to 16 times bit
        data += (16 - len(data) % 16) * chr(16 - len(data) % 16)
    data = str.encode(data)
    des = DES.new(str.encode(key), DES.MODE_ECB)  #  get the des encipher
    result = str(base64.encodebytes(des.encrypt(data)), encoding='utf8').replace('\n', '')  # encrypt
    paths = path.get()  # get the name of output file, the des text of + origin name
    names = paths.split("\\")
    name = names[len(names) - 1]
    title = 'The des text of ' + name + '.txt'
    f = open(title, 'w', encoding='utf-8')  # write the output file
    f.write(result)
    f.close()

if __name__ == '__main__':
    interface = tk.Tk()  # get the main interface
    interface1 = tk.Toplevel()
    interface1.withdraw()
    path = tk.StringVar()  # store the paths
    file = tk.StringVar()
    image = Image.open(r'bg.jpg')  # get the bg image
    bg = ImageTk.PhotoImage(image)
    openMain(interface)  # open the main interface
