import requests
from tkinter import messagebox
try:
 parameters={"amount":10,"difficulty":"easy","type":"multiple"}
 response =requests.get(url="https://opentdb.com/api.php",params=parameters)
 question_bank=response.json()["results"]
  
except Exception as z:
    messagebox.showinfo("ERROR","Connect to internet") 
    exit(0)
    