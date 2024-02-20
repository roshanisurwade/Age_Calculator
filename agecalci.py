
from tkinter import *
from datetime import *

root = Tk()
root.title("Age Calculator")
root.geometry("800x600+100+100")
f=("century", 30, "bold")
root.configure(bg="aquamarine")


lab_title = Label(root, text="Age Calci", font=f, bg="aquamarine")
lab_title.pack(pady=30)

lab_day = Label(root, text="Enter Day", font=f, bg="aquamarine")
ent_day=Entry(root, font=f, bg="light grey")
lab_day.pack()
ent_day.pack()

lab_month = Label(root, text="Enter Month", font=f, bg="aquamarine")
ent_month = Entry(root, font=f, bg="light grey")
lab_month.pack()
ent_month.pack()

lab_year = Label(root, text="Enter Year", font=f, bg="aquamarine")
ent_year = Entry(root, font=f, bg="light grey")
lab_year.pack()
ent_year.pack()

def find():

	try:
		day = int(ent_day.get()) 
		if day < 1 or day > 31:
			raise Exception("days shud be between 1 to 31")

	except ValueError:
		lab_result.configure(text="incorrect day")
		return
	except Exception as e:
		lab_result.configure(text=str(e))
		return


	try:	
		month = int(ent_month.get())
		if month < 1 or month > 12:
			raise Exception("month shud be between 1 to 12")
			
	except ValueError:
		lab_result.configure(text="incorrect month")
		return
	except Exception as e:
		lab_result.configure(text=str(e))
		return
	
	try:
		year = int(ent_year.get())
		if year < 1900:
			raise Exception("incorrect year")
	except ValueError:
		lab_result.configure(text="incorrect year")
		return
	except Exception as e:
		lab_result.configure(text=str(e))
		return

	try:
		bday =  datetime(year, month, day)
	except ValueError:
		lab_result.configure(text="incorrect bday")
		return

	today = datetime.today()
	age = today - bday
	msg = "age = " + str(age.days) + "days"
	lab_result.configure(text=msg)

btn_find = Button(root, text="Find Age", font=f, bg= "light grey", command=find)
btn_find.pack(pady=20)

lab_result = Label(root, font=f, bg="aquamarine")
lab_result.pack()
root.mainloop()



	








