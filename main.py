from plyer import notification
import requests
from bs4 import BeautifulSoup
from time import sleep
def notifyMe(message,title):
    notification.notify(
        title = title,
        message = message, 
        # app_icon = "C:\\Users\\RANADEEP\\Desktop\\WEB DEVELOPMENT\\Covid_Notification_Python_Project\\icon.ico", 
        # timeout = 10
    )
    #This is function will return any Webpage data into HTML format
def getDataFromUrl(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    while(True):
        myHTMLdata = getDataFromUrl("https://www.mohfw.gov.in/")
        # print(myHTMLdata)
        # Now we are parsing the HTML data
        soup = BeautifulSoup(myHTMLdata, 'html.parser')
        # print(soup.prettify())
        mydatastr = ""
        for table in soup.find_all('table'):
            #Now we are extracting data from table
            mydatastr = ""
            mydatastr += table.get_text()
        mydatastr = mydatastr[1:]
        itemList = (mydatastr.split("\n\n"))
        
        for item in itemList[3:38]:
            items = (item.split("\n"))
        items = items[2:]
        items_str = str(items)
        print(items_str)
        notifyMe(items_str,"Cases Of Covid 19")
        sleep(7200)