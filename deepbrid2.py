import requests
import json
import tkinter as tk
from tkinter import messagebox

# Define initial cookies
cookies = {",
    "cf_clearance": "",
    "crisp-client/session/ffca7959-dfd6-4915-90e2-b2feb57ae28e": "",
    "amember_nr": "",
}

# Update session cookies
session = requests.Session()
session.cookies.update(cookies)

# Define headers
headers = {
    "Host": "www.deepbrid.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.deepbrid.com/service",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.deepbrid.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

def generate_premium_link():
    # Get the user input from the text entry
    user_input = link_entry.get()
    
    if not user_input:
        messagebox.showerror("Input Error", "Please enter a valid URL.")
        return
    
    # Send POST request
    data = {
        "link": user_input,
        "pass": "",
        "boxlinklist": "0"
    }

    response = session.post('https://www.deepbrid.com/backend-dl/index.php?page=api&action=generateLink', headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        premium_link = result.get('link', 'No premium link available')
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, premium_link)
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Request Error", "Failed to generate the premium link.")

def update_cookie():
    # Get the updated cookie values from the entry fields
    cookies['PHPSESSID'] = cookie_php_entry.get()
    cookies['cf_clearance'] = cookie_cf_entry.get()
    cookies['crisp-client/session/ffca7959-dfd6-4915-90e2-b2feb57ae28e'] = cookie_crisp_entry.get()
    cookies['amember_nr'] = cookie_amember_entry.get()

    # Update the session with new cookie values
    session.cookies.update(cookies)
    messagebox.showinfo("Success", "Cookies updated successfully!")


root = tk.Tk()
root.title("Deepbrid Premium Link Generator")


tk.Label(root, text="Enter the link to make premium:").pack(padx=10, pady=5)
tk.Label(root, text="MyDopeSpot.com").pack(padx=10, pady=5)

link_entry = tk.Entry(root, width=50)
link_entry.pack(padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Premium Link", command=generate_premium_link)
generate_button.pack(padx=10, pady=10)

tk.Label(root, text="Generated Premium Link:").pack(padx=10, pady=5)

result_text = tk.Text(root, width=50, height=5, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack(padx=10, pady=5)

# Cookie management section
tk.Label(root, text="Edit Cookies:").pack(padx=10, pady=10)

cookie_php_label = tk.Label(root, text="PHPSESSID:")
cookie_php_label.pack(padx=10, pady=2)

cookie_php_entry = tk.Entry(root, width=50)
cookie_php_entry.insert(0, cookies['PHPSESSID'])  # Default value
cookie_php_entry.pack(padx=10, pady=2)

cookie_cf_label = tk.Label(root, text="cf_clearance:")
cookie_cf_label.pack(padx=10, pady=2)

cookie_cf_entry = tk.Entry(root, width=50)
cookie_cf_entry.insert(0, cookies['cf_clearance'])  # Default value
cookie_cf_entry.pack(padx=10, pady=2)

cookie_crisp_label = tk.Label(root, text="crisp-client/session:")
cookie_crisp_label.pack(padx=10, pady=2)

cookie_crisp_entry = tk.Entry(root, width=50)
cookie_crisp_entry.insert(0, cookies['crisp-client/session/ffca7959-dfd6-4915-90e2-b2feb57ae28e'])  # Default value
cookie_crisp_entry.pack(padx=10, pady=2)

cookie_amember_label = tk.Label(root, text="amember_nr:")
cookie_amember_label.pack(padx=10, pady=2)

cookie_amember_entry = tk.Entry(root, width=50)
cookie_amember_entry.insert(0, cookies['amember_nr'])  # Default value
cookie_amember_entry.pack(padx=10, pady=2)

update_cookie_button = tk.Button(root, text="Update Cookies", command=update_cookie)
update_cookie_button.pack(padx=10, pady=10)


root.mainloop()