#import os
#import json
#from turtle import bgcolor
import requests
from tkinter import messagebox
from tkinter import Tk,ttk
from tkinter import *
import requests

def convertor_gui():
    white_color = "#FFFFFF"
    black_color = "#333333"
    red_color = "#EB5D51"
    window = Tk()
    
    
    # Setting up the window 
    window.geometry('300x320')
    window.title('CURRENCY CONVERTER')
    window.configure(bg=white_color)
    window.resizable(height=FALSE,width = FALSE)
    
    
    # A top frame
    top = Frame(window, width =300,height= 60,bg = red_color)
    top.grid(row=0,column=0)
    
    
    # A main frame
    main = Frame(window, width =300,height= 260,bg = red_color)
    main.grid(row=0,column=0)
    
    
    # App name header
    app_name = Label(top,text ="Currency converter",height=5,padx=13,pady=30,anchor=CENTER,font=('Arial'),bg=red_color)
    app_name.place(x=0,y=0)


    #A label for result
    outputvalue = Label(main,text ="",width = 16,height=2,pady=7,relief="solid",anchor=CENTER,font=('Arial'),bg=white_color)
    outputvalue.place(x=50,y=10)
    currency = ["AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BYR","BZD","CAD","CDF","CHF","CLF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR","ZMK","ZMW","ZWL",]
    
    
    # A label initial currencies
    from_label = Label(main,text ="From",width=8,height=1,padx=0,pady=0,anchor=CENTER,relief="flat",font=('Arial'),bg=white_color)
    from_label.place(x=48,y=90)
    combo1 = ttk.Combobox(main,width=8,justify=CENTER)
    combo1['values'] = (currency)
    combo1.place(x=50,y=115)


    # A label new currencies
    to_label = Label(main,text ="To",width=8,height=1,padx=0,pady=0,anchor=CENTER,relief="flat",font=('Arial'),bg=white_color)
    to_label.place(x=158,y=90)
    combo2 = ttk.Combobox(main,width=8,justify=CENTER)
    combo2['values'] = (currency)
    combo2.place(x=160,y=115)


    # A label that allows a user to enter amount
    value = Entry(main,width=22,justify=CENTER,font=('Ivy 12 bold'),relief=SOLID)
    value.place(x=50,y=155)

    def convertor():
        initial_currency = combo1.get()
        changed_currency = combo2.get()
        amount = value.get()
        url = f"https://api.apilayer.com/fixer/convert?to={changed_currency}&from={initial_currency}&amount={amount}"
        payload = {}
        headers= {
        "apikey": "E4lxmxSexGO3smuToljWHUD2ZWN0CFuf"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        if initial_currency == '':
                messagebox.showerror('Error',"Enter values")

        elif changed_currency == '':
                messagebox.showerror('Error',"Enter values")

        elif amount == '':
                messagebox.showerror('Error',"Enter values")
        else:
                try:
                    amount = int(amount)
                except ValueError:    
                    messagebox.showerror('Error',"Enter number value ")

        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        response_object = response.json()
        result = response.text
        result = response_object['result']
        out_putValue_converted_value = (f" {result} ")
        outputvalue['text'] = out_putValue_converted_value

    # if a button is clicked and the value matches all the rules a amount will be converted

    button=Button(main,text="Convert",width=19,padx=5,height=1,bg=red_color,relief=SOLID,command = convertor)
    button.place(x=50,y=210)

    window.mainloop()

convertor_gui()