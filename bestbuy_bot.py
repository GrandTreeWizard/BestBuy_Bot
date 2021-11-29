import tkinter as tk
from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
driver = webdriver.Firefox(executable_path="C:\\Users\\HP\\Desktop\\BestBuy_Bot\\geckodriver.exe")

driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956")

def best_buy_bot():

    email = email_entry.get()
    password = Password_entry.get()
    cvv = cvv_entry.get()
    must_have = address_entry.get()

    def buy_this(item):
        try:
            driver.get(item)
            driver.find_element_by_class_name("c-button-icon-leading").click()
            driver.get("https://www.bestbuy.com/cart")
        except NoSuchElementException:
            buy_this(item)

    def send_keys_to_id(id, keys):
        try:
            driver.find_element_by_id(id).send_keys(keys)

        except NoSuchElementException:
            sleep(.5)
            send_keys_to_id(id, keys)

    def click_on_class(class_name):
        try:
            driver.find_element_by_class_name(class_name).click()
        except NoSuchElementException:
            sleep(.5)
            click_on_class(class_name)
        except ElementClickInterceptedException:
            sleep(.5)
            driver.refresh()
            click_on_class(class_name)

    driver.find_element_by_id('fld-e').send_keys(email)
    sleep(.01)
    driver.find_element_by_id('fld-p1').send_keys(password)
    sleep(.01)
    driver.find_element_by_class_name("c-button-block").click()
    sleep(.5)
    driver.get(must_have)
    buy_this(must_have)
    click_on_class('btn-block')
    send_keys_to_id("cvv", cvv)



root = tk.Tk()
root.title("BestBuyBot")
root.geometry("480x80")

Window = tk.Toplevel()
canvas = tk.Text(Window,wrap=tk.WORD)
Window.title("HELP!")
canvas.insert(tk.INSERT,'Enter the email, password & cvv attached to your Best Buy account. Then copy and past your desired item\'s URL into the box.   !THE PROGRAM CAN ONLY START FROME THE LOGIN PAGE!')
canvas.pack()

email_label = tk.Label(root, text = 'Email', font=('calibre',10, 'bold'))
email_entry = tk.Entry(root, font=('calibre',10,'normal'))

Password_label = tk.Label(root, text = 'Password', font=('calibre',10, 'bold'))
Password_entry = tk.Entry(root, font=('calibre',10,'normal'))

cvv_label = tk.Label(root, text = 'Security Code', font=('calibre',10, 'bold'))
cvv_entry = tk.Entry(root, font=('calibre',10,'normal'))

address_label = tk.Label(root, text = 'Item URL', font=('calibre',10, 'bold'))
address_entry = tk.Entry(root, font=('calibre',10,'normal'))

start=tk.Button(root,text = 'Start', command=best_buy_bot)


email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=1)
Password_label.grid(row=2,column=0)
Password_entry.grid(row=2,column=1)
cvv_label.grid(row=1,column=2)
cvv_entry.grid(row=1,column=3)
address_label.grid(row=2,column=2)
address_entry.grid(row=2,column=3)
start.grid(row=4,column=3)


root.mainloop()
