import tkinter as tk
from tkinter import messagebox
dic={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,
     'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,
     's':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
dicarr='abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
punctuation = [",", ".", "!", "?", ";", ":", "-", "'", "\"", "(", ")", "[", "]", "{", "}", "<", ">","\'","_"]
h_codes = '0123456789abcdef'

def in_e1(event):
    global focus
    focus = 'en1'

def in_e2(event):
    global focus
    focus = 'en2'

def in_e3(event):
    global focus
    focus = 'en3'

def c_to_b(c_num):
    code = 0
    output = ''
    while c_num>0:
        code = c_num%2
        output += str(code)
        c_num //= 2
    output = output[::-1]
    return output

def b_to_c(b_num):
    for i in b_num:
        if i != '1' and i != '0':
            return ''
    output = 0
    b_num = b_num[::-1]
    for i in range(len(b_num)):
        if b_num[i] =='0':
            pass
        else:
            output+=2 ** i 
    return output

def c_to_h(c_num):
    code = 0
    output = ''
    while c_num>0:
        code = c_num%16
        output += h_codes[code]
        c_num//=16
    output = output[::-1]
    return output

def h_to_c(h_num):
    output = 0
    h_num = h_num[::-1]
    for i in range(len(h_num)):
        digit = h_codes.index(h_num[i])
        times = 16 ** i
        output += digit * times
    return output

def instructions_for_use():
    for i in root.winfo_children():
        i.destroy()
        root.title('使用說明')
    root.geometry('335x100')
    label = tk.Label(root,text=f'{"使用說明":^15}\n{"1.全部的加密或是解密輸入格中只可輸入小寫英文或數字":<10}\n2.輸入完需加密或解密的文本好可以直接按"\"enter\" {",":<8}\n{"或圖形化介面中的" :<10}\"confirm\"{"按紐":<31}').grid(row=0,column=0)
    button = tk.Button(root,text = 'quit',width=25,command=quitt).grid(row=1,column=0)

def Affine_cipher_instructions():
    messagebox.showinfo('說明',f'{"使用說明":^15}\n{"在明文或密文欄位輸入需要轉譯的英文(僅能使用小寫)":<10}\n接著在a欄位和b欄位填入相應數值\n請注意：a數值應與26互質\n輸入完畢後放就可以按\"加密\"、\"解密\"按鈕或\"enter\"鍵')

def caesar_instructions():
    messagebox.showinfo('使用說明',f'{"使用說明":^15}\n{"在明文或密文欄位輸入需要轉譯的英文(僅能使用小寫)並在K欄位輸入位移植":<10}\n輸入完畢後放就可以按\"加密\"、\"解密\"按鈕或\"enter\"鍵')

def Vigenere_instructions():
    messagebox.showinfo('使用說明',f'{"使用說明":^15}\n{"在明文或密文欄位輸入需要轉譯的英文(僅能使用小寫)。":<10}\n金鑰的形式由一個從a~z的小寫字母組成的字串。')

def code_transfer_instructions():
    messagebox.showinfo('使用說明',f'{"使用說明":^15}\n在對應的欄位輸入對應的編碼後再按\"enter\"或是按\"confirm\"按鈕就會將結果輸出在其他兩個輸入格')

def ransposition_instructions():
    messagebox.showinfo('使用說明',f'{"使用說明：":^15}\n將字串打入輸入欄位在按下\"enter\"或是\"confirm\"就會出現轉換後的編碼')

def quitt():
    for i in root.winfo_children():
        i.destroy()
    root.title('密碼學')
    root.geometry(f'{width}x{height*3}')
    instructions = tk.Button(root,width=20,height=5,text='使用說明',command= instructions_for_use)
    instructions.pack(expand=True,fill = tk.BOTH)
    transposition_code = tk.Button(root,text='反轉換位法',width=20,height=5,command=ransposition_code)
    transposition_code.pack(expand=True,fill = tk.BOTH)
    Caesar_code = tk.Button(root,text='凱薩密碼',width=20,height=5,command=caesar)
    Caesar_code.pack(expand=True,fill = tk.BOTH)
    hybrid_code = tk.Button(root,text='維吉尼爾加密法',width=20,height=5,command=Vigenere)
    hybrid_code.pack(expand=True,fill = tk.BOTH)
    Affine_cipher_code = tk.Button(root,text='仿射密碼',width=20,height=5,command=Affine_cipher)
    Affine_cipher_code.pack(expand=True,fill = tk.BOTH)
    carry_transfer = tk.Button(root,text='進位轉換',width=20,height=5,command=code_transfer)
    carry_transfer.pack(expand=True,fill = tk.BOTH)

def caesar():
    global decrypt,encryption,knum
    for i in root.winfo_children():
        i.destroy()
    root.geometry('330x120')
    root.title('凱薩密碼')
    decrypt = tk.Entry(root,width=25)
    decrypt.grid(column=1,row=0)
    decrypt.bind('<Return>',caesar_decrypt)
    decrypt_Button = tk.Button(root,text='解密',command=lambda: caesar_decrypt(1))
    decrypt_Button.grid(column=2,row=0)
    #解密Button、Entry物件建立
    encryption = tk.Entry(root,width=25)
    encryption.grid(column=1,row=1)
    encryption.bind('<Return>',ceasar_encryption)
    encryption_Button = tk.Button(root,text='加密',command=lambda: ceasar_encryption(1))
    encryption_Button.grid(column=2,row=1)
    #加密Button、Entry物件建立
    dlabel = tk.Label(root,text='密文').grid(row=0,column=0)
    elabel = tk.Label(root,text='明文').grid(row=1,column=0)
    klabel = tk.Label(root,text='k=').grid(row=2,column=0)
    
    knum = tk.Entry(root,width=25)
    knum.grid(column=1,row=2)
    instructions = tk.Button(root,text='教學',command=caesar_instructions).grid(row=2,column=2)
    quitbutton = tk.Button(root,text='quit',command=quitt)
    quitbutton.grid(column=2,row=3)

def caesar_decrypt(event):
    dec = decrypt.get()
    k = int(knum.get())
    dec1 = []
    if bool(k) == False:
        pass
    
    for i in dec:
        if i == ' ' or i in num or i in punctuation:
            dec1.append(i)
        else :dec1.append(dicarr[(dic[i]-k)%26])
    output = ''.join(dec1)
    encryption.delete(0,len(dec))
    encryption.insert(0,output)

def ceasar_encryption(event):
    enc = encryption.get()
    k = int(knum.get())
    enc1 = []
    if bool(k) == False:
        pass
    
    for i in enc:
        if i == ' ' or i in num or i in punctuation:
            enc1.append(i)
        else :enc1.append(dicarr[(dic[i]+k)%26])
    output = ''.join(enc1)
    decrypt.delete(0,len(enc))
    decrypt.insert(0,output)

def Affine_cipher():
    global decrypt,encryption,knum,anum,bnum
    for i in root.winfo_children():
        i.destroy()
    root.geometry('310x130')
    root.title('仿射密碼')
    decrypt = tk.Entry(root,width=22)
    decrypt.place(x=30,y = 0)
    decrypt.bind('<Return>',Affine_cipher_decrypt)
    decrypt_Button = tk.Button(root,text='解密',command = lambda :Affine_cipher_decrypt(1))
    decrypt_Button.place(x=240,y=0)
    dlabel = tk.Label(root,text='密文').place(x = 0,y = 0)
    #解密Button、Entry物件建立
    encryption = tk.Entry(root,width=22)
    encryption.place(x = 30,y = 30)
    encryption.bind('<Return>',Affine_cipher_encryption)
    encryption_Button = tk.Button(root,text='加密',command=lambda : Affine_cipher_encryption(1))
    encryption_Button.place(x = 240, y =30)
    elabel = tk.Label(root,text='明文').place(x = 0,y = 30)
    #加密Button、Entry物件建立
    
    label = tk.Label(root,text='ax+b(a需與26互質)').place(x = 30, y = 60)
    instructions = tk.Button(root,text='教學',command=Affine_cipher_instructions).place(x = 240,y = 60)
    alabel = tk.Label(root,text='a=').place(x = 30, y = 90)
    anum = tk.Entry(root,width=2)
    anum.place(x = 50,y = 90 )
    klabel = tk.Label(root,text='b=')
    klabel.place(x = 80 ,y = 90)
    bnum = tk.Entry(root,width=2)
    bnum.place(x = 100,y = 90 )
    quitbutton = tk.Button(root,text='quit',command=quitt)
    quitbutton.place(x = 240 , y = 90 )

def Affine_cipher_decrypt(event):
    a = list(decrypt.get())
    b = int(anum.get())
    c = int(bnum.get())
    a1 = []
    d = 0
    if 26%b == 0:
        messagebox.showinfo('錯誤',"x前係數需與26互質，請檢查")
        return 0 
    for i in a:
        for j in range(26):
            if i == ' ' or i in num or i in punctuation:
                a1.append(i)
                break
            elif dicarr[(b*j+c)%26] == i:
                a1.append(dicarr[j])
                break
    d+=1
    output = ''.join(a1)
    encryption.delete(0,len(a))
    encryption.insert(0,output)

def Affine_cipher_encryption(event):
    a = encryption.get()
    b = int(anum.get())
    c = int(bnum.get())
    if 26%b == 0:
        messagebox.showinfo('錯誤',"x前係數需與26互質，請檢查")
        return 0 
    a1 = []
    for i in a:
        if i == ' ' or i in num or i in punctuation:
            a1.append(i)
        else:
            a1.append(dicarr[(b*dic[i]+c)%26])
    output = ''.join(a1)
    decrypt.delete(0,len(a))
    decrypt.insert(0,output)

def code_transfer():
    global entry1,entry2,entry3
    for i in root.winfo_children():
        i.destroy()
    root.title('進制轉換')
    root.geometry('325x125')
    entry1 = tk.Entry(root,width=25)
    entry1.place(x = 0,y = 0)
    entry1.bind("<FocusIn>",in_e1)
    entry1.bind("<Return>",code_transfer_enrty_1)

    entry2 = tk.Entry(root,width=25)
    entry2.place(x = 0,y = 30)
    entry2.bind("<FocusIn>",in_e2)
    entry2.bind("<Return>",code_transfer_enrty_2)

    entry3 = tk.Entry(root,width=25)
    entry3.place(x = 0,y = 60)
    entry3.bind("<FocusIn>",in_e3)
    entry3.bind("<Return>",code_transfer_enrty_3)
    
    label1 = tk.Label(root,text='二進制').place(x = 240,y =0)
    label2 = tk.Label(root,text='十進制').place(x = 240,y =30)
    label3 = tk.Label(root,text='十六進制').place(x = 240,y =60)

    button1 = tk.Button(root,text='confirm',command= code_transfer_confirm).place(x = 120,y = 90)
    instructions = tk.Button(root,text= '教學', command=code_transfer_instructions).place(x = 200,y = 90)
    button2 = tk.Button(root,text='quit',command=quitt).place(x = 260, y = 90)

def code_transfer_confirm():
    if focus == 'en1':code_transfer_enrty_1(1)
    elif focus == 'en2':code_transfer_enrty_2(1)
    elif focus == 'en3':code_transfer_enrty_3(1)

def code_transfer_enrty_1(event): 
    entry2.delete(0,len(entry2.get()))
    entry2.insert(0,str(b_to_c(str(entry1.get()))))
    entry3.delete(0,len(entry3.get()))
    entry3.insert(0,str(c_to_h(b_to_c(str(entry1.get())))))

def code_transfer_enrty_2(event):
    entry1.delete(0,len(entry1.get()))
    entry1.insert(0,str(c_to_b(int(entry2.get()))))
    entry3.delete(0,len(entry3.get()))
    entry3.insert(0,str(c_to_h(int(entry2.get()))))

def code_transfer_enrty_3(event):
    entry1.delete(0,len(entry1.get()))
    entry1.insert(0,str(c_to_b(h_to_c(entry3.get()))))
    entry2.delete(0,len(entry2.get()))
    entry2.insert(0,str(h_to_c(entry3.get()))) 

def ransposition_code():
    global entry,ranspotition_result
    for i in root.winfo_children():
        i.destroy()
    root.geometry('310x90')
    root.title('反轉加密法')
    entry = tk.Entry(root,width=24)
    entry.place(x=0,y=0)
    entry.bind('<Return>',ransposition_confirm)
    confirm_Button = tk.Button(root,text='確認',command = lambda : ransposition_confirm(1))
    confirm_Button.place(x=240,y=0)
    instructions = tk.Button(root,text='教學',command=ransposition_instructions).place(x = 240,y = 30)
    quit_Button = tk.Button(root,text='quit',command=quitt)
    quit_Button.place(x = 240, y =60)
    ranspotition_result = tk.Label(root)
    ranspotition_result.place(x = 0,y = 30)

def ransposition_confirm(event):
    a = entry.get()
    a = a[::-1]
    ranspotition_result.config(text=a)

def Vigenere():
    global decrypt,encryption,knum
    for i in root.winfo_children():
        i.destroy()
    root.geometry('300x120')
    root.title('維吉尼爾加密法')
    decrypt = tk.Entry(root)
    decrypt.grid(column=1,row=0)
    decrypt_Button = tk.Button(root,text='解密',command=Vigenere_decrypt)
    decrypt_Button.grid(column=2,row=0)
    decrylabel = tk.Label(root,text='密文')
    decrylabel.grid(column=0,row=0)
    #解密Button、Entry物件建立
    encryption = tk.Entry(root)
    encryption.grid(column=1,row=1)
    encryption_Button = tk.Button(root,text='加密',command=Vigenere_encryption)
    encryption_Button.grid(column=2,row=1)
    encrylabel = tk.Label(root,text='明文')
    encrylabel.grid(column=0,row=1)
    #加密Button、Entry物件建立
    klabel = tk.Label(root,text='金鑰:')
    klabel.grid(column=0,row=2)
    knum = tk.Entry(root)
    knum.grid(column=1,row=2)
    instructions = tk.Button(root,text='教學',command=Vigenere_instructions).grid(row=2,column=2)
    quitbutton = tk.Button(root,text='quit',command=quitt)
    quitbutton.grid(column=2,row=3)

def Vigenere_decrypt():
    code = decrypt.get()
    key = knum.get()
    k = 0
    output = []
    for i in range(len(code)):
        if code[i] ==' ' or code[i] in num or code[i] in punctuation:
            k-=1
            output.append(code[i])
        else:
            output.append(dicarr[((dic[code[i]]- dic[key[k%len(key)]])%26)])
        k+=1
    output = ''.join(output)
    encryption.delete(0,len(code))
    encryption.insert(0,output)

def Vigenere_encryption():
    code = encryption.get()
    key = knum.get()
    k = 0
    output = []
    for i in range(len(code)):
        if code[i] ==' ' or code[i] in num or code[i] in punctuation:
            k-=1
            output.append(code[i])
        elif code[i] in num:
            k-=1
            output.append(code[i])
        else:
            output.append(dicarr[((dic[code[i]]+ dic[key[k%len(key)]])%26)])
        k+=1
    output = ''.join(output)
    decrypt.delete(0,len(code))
    decrypt.insert(0,output)

root = tk.Tk()
root.title('密碼學')

#初始化
focus = None
instructions = tk.Button(root,width=20,height=5,text='使用說明',command= instructions_for_use)
instructions.pack(expand=True,fill = tk.BOTH)
transposition_code = tk.Button(root,text='反轉換位法',width=20,height=5,command=ransposition_code)
transposition_code.pack(expand=True,fill = tk.BOTH)
Caesar_code = tk.Button(root,text='凱薩密碼',width=20,height=5,command=caesar)
Caesar_code.pack(expand=True,fill = tk.BOTH)
hybrid_code = tk.Button(root,text='維吉尼爾加密法',width=20,height=5,command=Vigenere)
hybrid_code.pack(expand=True,fill = tk.BOTH)
Affine_cipher_code = tk.Button(root,text='仿射密碼',width=20,height=5,command=Affine_cipher)
Affine_cipher_code.pack(expand=True,fill = tk.BOTH)
carry_transfer = tk.Button(root,text='進位轉換',width=20,height=5,command=code_transfer)
carry_transfer.pack(expand=True,fill = tk.BOTH)

width = root.winfo_width()
height = root.winfo_height()

root.mainloop()