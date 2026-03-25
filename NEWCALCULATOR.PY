import  tkinter as tk
import math
rooot=tk.Tk()
rooot.title('CALCULATOR')
rooot.geometry('300x400')



entry=tk.Entry(rooot,font=("Arial",20),width=20,borderwidth=15,bg='green', fg='white', justify='right')

entry.grid(row=0,column=0,padx=10,pady=10,columnspan=5 ,sticky="nsew")

def button_click(number):
    # መጀመሪያ በሳጥኑ ውስጥ ያለውን ቁጥር ለጊዜው "current" በሚል ስም ያዘው
    current = entry.get()
    
    # የቆየውን ቁጥር አጥፋው (አዲስ ለመጻፍ እንዲመች)
    entry.delete(0, tk.END)
    
    # የቆየውን እና አዲሱን ቁጥር አቀጣጥለህ ጻፈው
    entry.insert(0, str(current) + str(number))

# 1. አንድ ቁጥር ብቻ ወደኋላ ለማጥፋት (Back)
def button_back():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1]) # የመጨረሻዋን አንድ ቁጥር ብቻ ይቆርጣል


# 1. መጻፊያ ሳጥኑን ሙሉ በሙሉ ለማጥፋት (CE ወይም Cancel)
def button_clear():
    entry.delete(0, tk.END)



# 3. ስኩዌር ሩት ለመስራት (Radical)
def button_sqrt():
    try:
        current = entry.get()
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# 4. ፐርሰንት ለመስራት (%)
def button_percent():
    try:
        current = entry.get()
        result = float(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_equal():
    try:
        # በሳጥኑ ውስጥ ያለውን ሂሳብ (ለምሳሌ "5+5") ያነባል
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        # ስህተት ከሰራህ (ለምሳሌ "5++5" ካልህ) Error ይላል
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
#column_0

btn=tk.Button(rooot,text='1',padx=10,pady=10,command=lambda:button_click(1))
btn.grid(row=1, column=0,sticky="nsew")

btn=tk.Button(rooot,text='2',padx=10,pady=10,command=lambda:button_click(2))
btn.grid(row=2, column=0,sticky="nsew")

btn=tk.Button(rooot,text='3',padx=10,pady=20,command=lambda:button_click(3))
btn.grid(row=3, column=0,sticky="nsew")

btn=tk.Button(rooot,text='4',padx=10,pady=10,command=lambda:button_click(4))
btn.grid(row=4, column=0,sticky="nsew")
btn=tk.Button(rooot,text='5',padx=10,pady=10,command=lambda:button_click(5))
btn.grid(row=5, column=0,sticky="nsew")

#column_1
btn=tk.Button(rooot,text='6',padx=10,pady=10,command=lambda:button_click(6))
btn.grid(row=1, column=1,sticky="nsew")
btn=tk.Button(rooot,text='7',padx=10,pady=10,command=lambda:button_click(7))
btn.grid(row=2, column=1,sticky="nsew")
btn=tk.Button(rooot,text='8',padx=10,pady=10,command=lambda:button_click(8))
btn.grid(row=3, column=1,sticky="nsew")
btn=tk.Button(rooot,text='9',padx=10,pady=10,command=lambda:button_click(9))
btn.grid(row=4, column=1,sticky="nsew")

btn=tk.Button(rooot,text='0',padx=10,pady=10,command=lambda:button_click(0))
btn.grid(row=5, column=1,sticky="nsew")
#column_2
btn=tk.Button(rooot,text='ce',padx=10,pady=10,command= button_clear)
btn.grid(row=1, column=2,sticky="nsew")
btn=tk.Button(rooot,text='+',padx=10,pady=10,command=lambda:button_click('+'))
btn.grid(row=2, column=2,sticky="nsew")
btn=tk.Button(rooot,text='-',padx=10,pady=10,command=lambda:button_click('-'))
btn.grid(row=3, column=2,sticky="nsew")
btn=tk.Button(rooot,text='/',padx=10,pady=10,command=lambda:button_click('/'))
btn.grid(row=4, column=2,sticky="nsew")
btn=tk.Button(rooot,text='*',padx=10,pady=10,command=lambda:button_click('*'))
btn.grid(row=5, column=2,sticky="nsew")
#column_3
btn=tk.Button(rooot,text='%',padx=10,pady=10,command=button_percent)
btn.grid(row=1, column=3,sticky="nsew")
btn=tk.Button(rooot,text='⌫',padx=10,pady=10,command=button_back)
btn.grid(row=2, column=3,sticky="nsew")
btn=tk.Button(rooot,text='√',padx=10,pady=10,command=button_sqrt)
btn.grid(row=3, column=3,sticky="nsew")

btn_equal = tk.Button(rooot, text='=', padx=10, pady=10, bg='lightblue',command=button_equal)
btn_equal.grid(row=4, column=3, rowspan=2, sticky="nsew")
rooot.mainloop()
