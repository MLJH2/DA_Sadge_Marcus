#Import the libraries
import requests

#Creating a Class called "Task5" for unittesting in Task 8
class TASK5:
    #Setting the target URL page
    url = 'http://192.168.253.129/algenius'
    r = requests.get(url)

    #This will get the full page
    print(r.text)

    #Getting the status code (if show *200 means Okay)
    print("Status Code:")
    print("\t*", r.status_code)

    #Displaying the Website Header
    h = requests.head(url)
    print("Header:")
    print("**********")
    #Printing the header line by line so it wont clump up
    for x in h.headers:
        print("\t", x, ":", h.headers[x])
    print("**********")

    #Modifying code for Header User-Agent to display 'Mobile'
    headers = {
        'User-Agent': 'Mobile'
    }
    #Testing it on site
    url2 = 'http://httpbin.org/headers'
    rh = requests.get(url2, headers=headers)
    print(rh.text)
