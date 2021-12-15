'''
Author: Riley Zuckert
Date: December 12-14, 2021
'''

# import libraries
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import webbrowser
import time
from datetime import datetime, date

# create the GUI for user to fill in subscription information
trial_expiration_notif = tk.Tk() # application name
trial_expiration_notif.title("Don't forget about your subscriptions!") # label
lbl = ttk.Label(trial_expiration_notif, text = 'Enter the name of your subscription service (ex: Hulu):').grid(column = 0, row = 0) # click event
lbl = ttk.Label(trial_expiration_notif, text = 'Enter your trial expiration date (ex: MM/DD/YYYY):').grid(column = 0, row = 2)
lbl = ttk.Label(trial_expiration_notif, text = "Paste in the subscription management page url.\nThis will help us direct you to your account when your trial is expiring:").grid(column = 0, row = 4)

def click():
    print("We've got you covered! You can exit out of our pop-up now.")

service = tk.StringVar()
serviceEntered = ttk.Entry(trial_expiration_notif, width = 12, textvariable = service).grid(column = 0, row = 1) # textbox widget - service
service_entry = service.get()

expiration_date = tk.StringVar()
dateEntered = ttk.Entry(trial_expiration_notif, width = 12, textvariable = expiration_date).grid(column = 0, row = 3) # textbox widget - date
expiration_date_entry = expiration_date.get()

link = tk.StringVar()
linkEntered = ttk.Entry(trial_expiration_notif, width = 12, textvariable = link).grid(column = 0, row = 5) # textbox widget - link
link_entry = link.get()

button = ttk.Button(trial_expiration_notif, text = 'Remind me!', command = click).grid(column = 1, row = 6) # button widget
trial_expiration_notif.mainloop()

# calculate how many days are between the current day / user's trial start date and the trial end date
d1 = datetime.now()
expiration_date_entry = expiration_date.get()
d2 = datetime.strptime(expiration_date_entry, "%m/%d/%Y")
d3 = abs((d2 - d1).days)

# calculate the number of seconds composing the trial period - will need for telling the code how long to sleep between sending out alerts 2 days before expiration and day ofs
sleep_time = d3 * 86400
sleep_time_1 = sleep_time - 432000
sleep_time_2 = sleep_time - 604800

# craft the messages to be displayed to the user in their alerts
service_entry = service.get()
body = "Your " + service_entry + " subscription expires in " + str(d3) + " days."
body_2 = "Your " + service_entry + " subscription expires today."

# create the GUI for the user trial alert updates, sent out based upon how many days left in the trial
if d3 > 1:
    time.sleep(sleep_time_1)
    trial_update_notif = tk.Tk() # application name
    trial_update_notif.geometry("400x70") # adjust size of box
    trial_update_notif.title("Don't forget about your subscription!") # label
    lbl = ttk.Label(trial_update_notif, text = body).grid(column = 0, row = 0) # click event

    link = link.get()
    def open_link():
        webbrowser.open_new(link)
    button = ttk.Button(trial_update_notif, text = "Manage subscription", command = open_link).grid(column = 1, row = 0)
else:
    time.sleep(sleep_time_2)
    trial_update_notif = tk.Tk() # application name
    trial_update_notif.geometry("400x70") # adjust size of box
    trial_update_notif.title("Don't forget about your subscription!") # label
    lbl = ttk.Label(trial_update_notif, text = body_2).grid(column = 0, row = 0) # click event

    link = link.get()
    def open_link():
        webbrowser.open_new(link)
    button = ttk.Button(trial_update_notif, text = "Manage subscription", command = open_link).grid(column = 1, row = 0)

trial_update_notif.mainloop()
