from time import time
import requests
from datetime import date, datetime 
import tkinter as tk




def bitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    current_time = datetime.now().strftime("%H:%M:%S")
    today = date.today()

    Price.config(text=str(price)+" $", bg='black', fg='gold1', font=("poppins", 25, "bold"))
    Time.config(text=current_time, bg='black', fg='#425578', font=("poppins", 25, "bold"))
    Date.config(text=today, bg='black', fg='#425578', font=("poppins", 25, "bold"))
    
    window.after(1000, bitcoin)



window = tk.Tk()
window.geometry("500x500")
window.title("Bitcoin Price")
window.config(bg="black")

header = tk.Label(window, text="LIVE BITCOIN PRICE", bg='black', fg='red', font=("poppins", 25, "bold"))
header.pack(pady=25)

Price_header = tk.Label(window, text="Bitcoin Price ",bg='black', fg='silver', font=("poppins", 25, "bold"))
Price_header.pack(pady=10)

Price = tk.Label(window,bg='black', fg='silver', font=("poppins", 25, "bold"))
Price.pack(pady=10)

Date_header = tk.Label(window, text="Date ",bg='black', fg='#7f9176', font=("poppins", 25, "bold"))
Date_header.pack(pady=10)

Date = tk.Label(window, bg='black', fg='silver', font=("poppins", 25, "bold"))
Date.pack(pady=10)

Time_header = tk.Label(window, text="Time ",bg='black', fg='#7f9176', font=("poppins", 25, "bold"))
Time_header.pack(pady=10)

Time = tk.Label(window, bg='black', fg='silver', font=("poppins", 25, "bold"))
Time.pack(pady=10)



bitcoin()


window.mainloop()