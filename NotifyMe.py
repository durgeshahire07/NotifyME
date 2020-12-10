from tkinter import *
from gnewsclient import gnewsclient
from win10toast import ToastNotifier
import requests
import json
from tkinter import ttk

def Weather_Report():

    label1.grid_forget()
    label2.grid_forget()
    label3.grid_forget()
    label4.grid_forget()
    drop1.grid_forget()
    drop2.grid_forget()
    drop3.grid_forget()
    drop4.grid_forget()
    myButton.grid_forget()
    cityOptions = [
        "AGARTALA",
        "AHMEDABAD",
        "ALLAHABAD",
        "AMRITSAR",
        "ANKLESHWAR",
        "AURANGABAD",
        "ALIBAUG",
        "AJMER",
        "AMLA",
        "BADRINATH",
        "BANDIPUR",
        "BANGALORE",
        "BAREILLY",
        "BELGAUM",
        "BERHAMPUR",
        "BHARATPUR",
        "BHANDARDARA",
        "BHARUCH",
        "BHAVNAGAR",
        "BHILAI",
        "BHIMTAL",
        "BHOPAL",
        "BHUBANESHWAR",
        "BHUJ",
        "BIKANER",
        "BODHGAYA",
        "CALICUT",
        "CHANDIGARH",
        "CHENNAI",
        "CHIPLUN",
        "CHITTORGARH",
        "COIMBATORE",
        "DEHRADUN",
        "DAMAN",
        "DARJEELING",
        "DIU",
        "DWARKA",
        "DURGAPUR",
        "FARIDABAD",
        "FIROZABAD",
        "GANGTOK",
        "GANDHIDHAM",
        "GANDHINAGAR",
        "GAYA",
        "GHAZIABAD",
        "GOA",
        "GURGAON",
        "GUWAHATI",
        "GURUVAYOOR",
        "GWALIOR",
        "HAMPI",
        "HANSI",
        "HARIDWAR",
        "HASSAN",
        "HUBLI",
        "HYDERABAD",
        "IGATPURI",
        "IMPHAL",
        "INDORE",
        "JAIPUR",
        "JABALPUR",
        "JAISALMER",
        "JALGAON",
        "JALANDHAR",
        "JAMMU",
        "JAMSHEDPUR",
        "JAMNAGAR",
        "JHANSI",
        "JODHPUR",
        "KANPUR",
        "KANYAKUMARI",
        "KARGIL",
        "KARJAT",
        "KARUR",
        "KARWAR",
        "KAZIRANGA",
        "KEDARNATH",
        "KOCHIN",
        "KOLHAPUR",
        "KODAIKANAL",
        "KOLKATA",
        "KOLLAM",
        "KOTA",
        "KOTTAYAM",
        "LEH",
        "LAKSHADWEEP",
        "LONAVALA",
        "LUCKNOW",
        "LUDHIANA",
        "MADURAI",
        "MAHABALESHWAR",
        "MANALI",
        "MANGALORE",
        "MANMAD",
        "MATHURA",
        "MUMBAI",
        "MUNNAR",
        "MYSORE",
        "NAGPUR",
        "NAINITAL",
        "NASIK",
        "NEW DELHI",
        "NILGIRI",
        "NOIDA",
        "OOTY",
        "PALAMPUR",
        "PALLAKAD",
        "PANVEL",
        "PATIALA",
        "PATHANKOT",
        "PATNA",
        "PONDICHERRY",
        "PUNE",
        "RAIPUR",
        "RAJKOT",
        "RAMESHWARAM",
        "RANCHI",
        "RATNAGIRI",
        "ROURKELA",
        "SALEM",
        "SHILLONG",
        "SURAT",
        "THANE",
        "THIRUVANANTHAPURAM",
        "TIRUCHIRAPALLI",
        "TIRUPATI",
        "THRISSUR",
        "UDAIPUR",
        "UDUPI",
        "VADODARA",
        "VAPI",
        "VARANASI",
        "VELLORE",
        "VIJAYAWADA",
        "VISHAKAPATNAM",
        "WAYANAD",
        "WANKANER",
        "YAMUNOTRI",
        "YERCAUD",
    ]

    label5 = Label(master, text="Enter City:", font=('bold', 10))
    label5.grid(row=1, padx=20)
    city_entry = StringVar()
    city_entry.set(cityOptions[0])
    drop5 = ttk.Combobox(master, textvariable=city_entry, values=cityOptions)
    drop5.grid(row=1, column=1, ipady=10, padx=20, stick=W + E + N + S)

    def city_name():

        api_request = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&units=metric&appid="
            + "d87334c333a2110178e8a261a1e5d7a9")
        api = json.loads(api_request.content)
        # Temperatures
        y = api['main']
        current_temprature = y['temp']
        humidity = y['humidity']
        # Adding the received info into the screen
        lable_temp.configure(text=current_temprature)
        lable_humidity.configure(text=humidity)
    # Search Bar and Button

    city_nameButton = Button(master, text="Search", command=city_name)
    city_nameButton.grid(row=2, column=1, padx=5,pady=5, stick=W + E + N + S)
    # Country  Names and Coordinates
    # Current Temperature
    lable_temp = Label(master, text="...", width=0, bg='white', font=("Helvetica", 100), fg='black')
    lable_temp.place(x=18, y=120)
    humi = Label(master, text="Humidity: ", width=0, bg='white', font=("bold", 15))
    humi.place(x=3, y=330)
    lable_humidity = Label(master, text="...", width=0, bg='white', font=("bold", 15))
    lable_humidity.place(x=107, y=330)
    # Note
    note = Label(master, text="All temperatures in degree celsius", bg='white', font=("italic", 10))
    note.place(x=95, y=400)

# tkinter object
master = Tk()
master.title("NotifyME")
master.geometry("400x450")
master.minsize(400, 450)


#mainmenu
mainmenu = Menu(master)
mainmenu.add_command(label="Weather Report",command=Weather_Reports)
mainmenu.add_command(label="Exit", command=quit)
master.config(menu=mainmenu)


def news():
    # global label1, label2, label3, label4, drop1, drop2, drop3, drop4, myButton

    client = gnewsclient.NewsClient(language=lang.get(), location=loc.get(), topic=top.get(), max_results=5)
    news_list = client.get_news()
    toaster = ToastNotifier()
    time = t.get()
    for i in range(0, 5):
        toaster.show_toast("Breaking News", news_list[i]['title'], icon_path=None, duration=time)

    result_title.set(news_list[0]["title"] + "\n" +
                        news_list[1]["title"] + "\n" +
                        news_list[2]["title"] + "\n" +
                        news_list[3]["title"] + "\n" +
                        news_list[4]["title"] + "\n")

result_title = StringVar()
lang = StringVar()
loc = StringVar()
top = StringVar()
t = IntVar()

label1 = Label(master, text="Choose language :")
label1.grid(row=0)
label2 = Label(master, text="Choose Location :")
label2.grid(row=1)
label3 = Label(master, text="Choose Topic :")
label3.grid(row=2)
label4 = Label(master, text="Duration(Seconds):")
label4.grid(row=3)

langOptions = [
    "English",
    "Hindi",
    "Urdu",
    "Marathi",
    "Telgu",
    "Tamil",
    "Kannada",
    "Malayalam",
    "Bengali"
]

locOptions = [
    "World",
    "India"
]
topOptions = [
    "Entertainment",
    "Sports",
    "Health",
    "Science",
    "Technology",
    "Business",
]

timeOptions = [
    5,
    30,
    60,
    3600
]
lang.set(langOptions[0])
drop1 = ttk.Combobox(master, textvariable=lang, values=langOptions)
drop1.grid(row=0, column=1)

loc.set(locOptions[0])
drop2 = ttk.Combobox(master, textvariable=loc, values=locOptions)
drop2.grid(row=1, column=1)

top.set(topOptions[0])
drop3 = OptionMenu(master, top, *topOptions)
drop3.grid(row=2, column=1)

t.set(timeOptions[0])
drop4 = ttk.Combobox(master,textvariable=t, values=timeOptions)
drop4.grid(row=3, column=1)

myButton = Button(master, text="SHOW", command=news)
myButton.grid(row=4, column=1)

mainloop()
