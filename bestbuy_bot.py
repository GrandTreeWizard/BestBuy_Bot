# december 18
from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from tkinter import Tk
from tkinter import *


# A hopefully helpful command line comment.
print('\n\t!? NEED HELP ?!\n\nEnter the email, password & cvv attached to your Best Buy account (If you don\'t have an account then make one. Optimally with all the fields fully and correctly filled out) Then copy and past your desired item\'s URL into the box.\n')

# Starts up the Best Buy site.
driver = webdriver.Firefox(executable_path="C:\\Users\\HP\\Desktop\\BestBuy_Bot\\geckodriver.exe")
driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956")

# The bot.
def best_buy_bot():

    # User input
        email = email_entry.get()
        password = Password_entry.get()
        cvv = cvv_entry.get()
        must_have = address_entry.get()

    # Error handling with loops
        # Make the humn do the things if the bot fails UwU.
        def User_needed_plz(help_with):
            root = Tk()
            root.title("Lazy bot")
            root.geometry("180x100")
            words = Label(root, text=help_with)
            words.pack()
            ignoring_words = Button(root, text="Continue", command=root.destroy)
            ignoring_words.pack()
            mainloop()

        # Loops over the product page until it's avalable.
        def buy_this(item):
            driver.get(item)
            try:
                driver.find_element_by_class_name('c-button-icon-leading').click()
                    # c-button c-button-disabled c-button-lg c-button-block add-to-cart-button
                    # c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button
                driver.get("https://www.bestbuy.com/cart")
            except NoSuchElementException:
                buy_this(item)

        # Letting things break until they don't break no more UwU
            # Should track down all the break points and give them propper handeling. Will do that latter maybe...
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
                driver.refresh()
                click_on_class(class_name)

        def login_to_bb(email, password):
            click_on_class('account-button')
                #Class: c-button-unstyled plButton account-button
            click_on_class('sign-in-btn')
                #Class: c-button c-button-secondary c-button-sm sign-in-btn
            send_keys_to_id('fld-e', email)
            send_keys_to_id('fld-p1', password)
            click_on_class('c-button-block')
                #Class: c-button c-button-secondary c-button-lg c-button-block c-button-icon c-button-icon-leading cia-form__controls__submit
            sleep(5)
            if  str(driver.current_url)[0:39] == 'https://www.bestbuy.com/identity/signin':
                User_needed_plz("Hey so... I can't seem to log in.\nCould you do it for me? Then\njust hit the continue button and\nI'll resume operations.")
            else:
                pass

    # exicuting the code
        login_to_bb(email, password)
        buy_this(must_have)
        click_on_class('btn-block')
            #Class: btn btn-lg btn-block btn-primary
        send_keys_to_id('cvv', cvv)
        click_on_class('button__fast-track')
            #Class: btn btn-lg btn-block btn-primary button__fast-track
        click_on_class('btn-primary')
            #Class: btn btn-primary

# Set up for the root window.
root = Tk()
root.title("BestBuyBot")
root.geometry("480x80")

# Creats the inputs.
email_label = Label(root, text = 'Email', font = ('calibre',10, 'bold'))
email_entry = Entry(root, font = ('calibre',10,'normal'))
Password_label = Label(root, text = 'Password', font = ('calibre',10, 'bold'))
Password_entry = Entry(root, font = ('calibre',10,'normal'))
cvv_label = Label(root, text = 'Security Code', font = ('calibre',10, 'bold'))
cvv_entry = Entry(root, font = ('calibre',10,'normal'))
address_label = Label(root, text = 'Item URL', font = ('calibre',10, 'bold'))
address_entry = Entry(root, font = ('calibre',10,'normal'))
start = Button(root,text = 'Start', command = best_buy_bot)

# Sets the layout of the gui.
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
