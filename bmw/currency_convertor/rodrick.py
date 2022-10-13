import requests
import tkinter as tk

# gui input function
# api conversion function
# gui output function
# clear fields function

# api call functuion
def get_conversion(old, new, amount):

    url = f"https://api.apilayer.com/fixer/convert?to={new}&from={old}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "E4lxmxSexGO3smuToljWHUD2ZWN0CFuf"
    }

    try:
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        response_object = response.json()
        result = response_object['result']
        print(f"{amount} {old.upper()} is equivalent to {result} {new.upper()} ")
        error_label.config(text='')
        return result
    except:
        error_label.config(text='INVALID INPUT')
        print("Invalid input")
        return ''

# main function
def convert_currency():
    amount = amount_entry.get()
    from_curr = from_entry.get().upper()
    to_curr = to_entry.get().upper()
    converted_amount_entry.delete(0, tk.END)
    new_amount = get_conversion(from_curr, to_curr, amount)
    converted_amount_entry.insert(0, new_amount)

# function to clear input fields
def clear_fields():
    from_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    converted_amount_entry.delete(0, tk.END)

# create gui window and set window configuration
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x250")
root.resizable(height= tk.FALSE, width = tk.FALSE)

# extra space in window
padding_label = tk.Label(root, text='')
padding_label.grid(column=0, row=0)

# field for amount to convert
amount_label = tk.Label(root, text='Amount: ')
amount_label.grid(column=0, row=1)
amount_entry = tk.Entry(root)
amount_entry.grid(column=1, row=1)

# field for original currency
from_label = tk.Label(root, text='From Currency: ')
from_label.grid(column=0, row=2)
from_entry = tk.Entry(root)
from_entry.grid(column=1, row=2)

# field for new currency
to_label = tk.Label(root, text='To Currency: ')
to_label.grid(column=0, row=3)
to_entry = tk.Entry(root)
to_entry.grid(column=1, row=3)

# extra space in window
padding_label = tk.Label(root, text='')
padding_label.grid(column=0, row=4)

# convert button
button1 = tk.Button(root, text='Convert', command=convert_currency)
button1.grid(column=0 , row=5)

# extra space in window
padding_label = tk.Label(root, text='')
padding_label.grid(column=0, row=6)

# new amount field
converted_amount_label = tk.Label(root, text='Converted Amount: ')
converted_amount_label.grid(column=0, row=7)
converted_amount_entry = tk.Entry(root)
converted_amount_entry.grid(column=1, row=7)

# error field
error_label = tk.Label(root, text='')
error_label.grid(column=0, row=8)

# button to clear field inputs
button2 = tk.Button(root, text='Clear fields', command=clear_fields)
button2.grid(column=0 , row=9)

# run tkinter event loop, listening for events
root.mainloop()