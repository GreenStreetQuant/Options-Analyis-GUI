from tkinter import *

rootWindow = Tk()

rootWindow.title('Options Volatility Analysis')

canvas1 = Canvas(rootWindow, width = 500, height = 400, relief = 'raised')
canvas1.pack()

label_title = Label(rootWindow, text='Calculate the +1/-1 Standard Deviation & \n +5%/-5% Close Price')
label_title.config(font=('georgia', 14, 'bold'))
canvas1.create_window(250, 50, window=label_title)

label_close = Label(rootWindow, text='Enter the Last Close Price:')
label_close.config(font=('georgia', 10))
canvas1.create_window(90, 100, window=label_close)

entry_close = Entry(rootWindow)
canvas1.create_window(238, 100, window=entry_close)

label_vol = Label(rootWindow, text='Enter the Implied Volatility:')
label_vol.config(font=('georgia', 10))
canvas1.create_window(97, 135, window=label_vol)

entry_vol = Entry(rootWindow)
canvas1.create_window(252, 135, window=entry_vol)

label_day = Label(rootWindow, text='Enter Days Till Option Expiration:')
label_day.config(font=('georgia', 10))
canvas1.create_window(114, 170, window=label_day)

entry_day = Entry(rootWindow)
canvas1.create_window(285, 170, window=entry_day)

#function to retrieve +1/-1 Std and +5%/-5%
def getAnalysis():
    
    close = float(entry_close.get())
    vol = float(entry_vol.get())
    day = int(entry_day.get())
    year = 252 

    #calculating the Standard Deviation
    std = (close * vol) * (day/year)**0.5 

    #calculating upper band Std Price
    upper_std = round(close + std, 2)

    #calculating lower band Std Price
    lower_std = round(close - std, 2)

    #calculating +5% price
    pct_upper = round(close * 1.05, 2)

    #calculating -5% price
    pct_lower = round(close * .95, 2)

    label_output_up = Label(rootWindow, text='The +1 Standard Deviation is:', font=('georgia',10))
    canvas1.create_window(150, 210, window=label_output_up)

    label_std_upper = Label(rootWindow, text=f'${upper_std}', font=('georgia',10,'bold'))
    canvas1.create_window(150, 230, window=label_std_upper)

    label_output_down = Label(rootWindow, text='The -1 Standard Deviation is:', font=('georgia',10))
    canvas1.create_window(150, 250, window=label_output_down)

    label_std_lower = Label(rootWindow, text=f'${lower_std}', font=('georgia',10,'bold'))
    canvas1.create_window(150, 270, window=label_std_lower)

    label_output_up_pct = Label(rootWindow, text='The + 5% Close Price is:', font=('georgia',10))
    canvas1.create_window(330, 210, window=label_output_up_pct)

    label_pct_upper = Label(rootWindow, text=f'${pct_upper}', font=('georgia',10,'bold'))
    canvas1.create_window(330, 230, window=label_pct_upper)

    label_output_down_pct = Label(rootWindow, text='The - 5% Close Price is:', font=('georgia',10))
    canvas1.create_window(330, 250, window=label_output_down_pct)

    label_pct_lower = Label(rootWindow, text=f'${pct_lower}', font=('georgia',10,'bold'))
    canvas1.create_window(330, 270, window=label_pct_lower)

#adding button to fetch analysis
button = Button(text='Get Analysis', command=getAnalysis, bg='brown', fg='white', font=('georgia', 10))
canvas1.create_window(225, 325, window=button) 

rootWindow.mainloop()