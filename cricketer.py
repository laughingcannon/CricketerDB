import sqlite3
from Tkinter import *
import tkMessageBox

db = sqlite3.connect(':memory:')
db = sqlite3.connect('data/mydbms')

cursor = db.cursor()
cursor.execute("DROP TABLE batsmen")
cursor.execute('''
    CREATE TABLE batsmen(id INTEGER PRIMARY KEY, name TEXT,
                       matches INTEGER, runs INTEGER, hun INTEGER
                       )
''')
db.commit()

cursor.execute("INSERT INTO batsmen(id, name, matches, runs, hun) VALUES (101,'Tendulkar',664,34357,100)")
print('First user inserted')
cursor.execute("INSERT INTO batsmen(id, name, matches, runs, hun) VALUES (102,'Dravid',504,24064,48)")
cursor.execute("INSERT INTO batsmen(id, name, matches, runs, hun) VALUES (103,'Ganguly',421,18433,38)")	
cursor.execute("INSERT INTO batsmen(id, name, matches, runs, hun) VALUES (104,'Sehwag',363,16892,38)")
cursor.execute("INSERT INTO batsmen(id, name, matches, runs, hun) VALUES (105,'Dhoni',473,15685,15)")
print('Last user inserted')
# cursor.execute('''SELECT * FROM batsmen''')

# user1 = cursor.fetchone() #retrieve the first row
# print user1[0] #Print the first column retrieved(user's name)
# all_rows = cursor.fetchall()
# print "Om"
# for row in all_rows:
    # print row[0]
#     print("%s",row[0]) # row[0] returns the first column in the query (name), row[1] returns email column.
    #print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
    #print type(row[0])
    #print type(row[1])
titles = ["ID","Name","Matches","Runs","Hundreds"]
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

def viewDB():
	w2 = Tk()
	w2.title("View Database")
	l3 = Label(w2, text = titles)
	l3.pack()
	cursor.execute('''SELECT * FROM batsmen''')
	all_rows = cursor.fetchall()
	for row in all_rows:
		# print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
		l = Label(w2, text=row)#str(row[0])+str(row[1]))
		l.pack()
	l2 = Label(w2, text="Arrange by:")
	l2.pack(side=LEFT)

	arr_name = Button(w2, text ="Names", command = viewNames)
	arr_matches = Button(w2, text ="Matches", command = viewMatches)
	arr_runs = Button(w2, text ="Runs", command = viewRuns)
	arr_hun = Button(w2, text ="Hundreds", command = viewHundreds)

	arr_name.pack(side=LEFT, padx=10)
	arr_matches.pack(side=LEFT, padx=10)
	arr_runs.pack(side=LEFT, padx=10)
	arr_hun.pack(side=LEFT, padx=10)

	w2.mainloop()


def viewNames():
	w3 = Tk()
	w3.title("Alphabetical Order")
	l3 = Label(w3, text = titles)
	l3.pack()
	cursor.execute("SELECT * FROM batsmen ORDER BY name ASC")
	all_rows = cursor.fetchall()
	for row in all_rows:
		l = Label(w3, text=row)
		l.pack()
	w3.mainloop()

def viewMatches():
	w4 = Tk()
	w4.title("Matches")
	l3 = Label(w4, text = titles)
	l3.pack()
	cursor.execute("SELECT * FROM batsmen ORDER BY matches DESC")
	all_rows = cursor.fetchall()
	for row in all_rows:
		l = Label(w4, text=row)
		l.pack()
	w4.mainloop()


def viewRuns():
	w5 = Tk()
	w5.title("Runs")
	l3 = Label(w5, text = titles)
	l3.pack()
	cursor.execute("SELECT * FROM batsmen ORDER BY runs DESC")
	all_rows = cursor.fetchall()
	for row in all_rows:
		l = Label(w5, text=row)
		l.pack()
	w5.mainloop()

def viewHundreds():
	w6 = Tk()
	w6.title("Hundreds")
	l3 = Label(w6, text = titles)
	l3.pack()
	cursor.execute("SELECT * FROM batsmen ORDER BY hun DESC")
	all_rows = cursor.fetchall()
	for row in all_rows:
		l = Label(w6, text=row)
		l.pack()
	w6.mainloop()

"""
# def updatePlayerAdd(I,N,M,R,H):

def updatePlayerDel(I):
	cursor.execute("DELETE FROM batsmen WHERE id = ? ", (I,))
	viewDB()




def addPlayer():
	win = Tk()

	win.title("Add Player")
	# v = StringVar()
	# l = Label(win, text="Enter batsman's name")
	# l.pack(side=LEFT)
	# e = Entry(win,textvariable=v)
	# e.pack()
	# print v

	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="ID").grid(row=0, column=0, sticky=W)
        iD= StringVar()
        idee = Entry(frame1, textvariable=iD)
        idee.grid(row=1, column=1, sticky=W)
        id_no = iD.get()
        print id_no

	Label(frame1, text="Name").grid(row=1, column=0, sticky=W)
	nameVar = StringVar()
	name = Entry(frame1, textvariable=nameVar)
        name.grid(row=0, column=1, sticky=W)
        n = nameVar.get()
        print n
	
	Label(frame1, text="Matches").grid(row=2, column=0, sticky=W)
        m = StringVar()
        matches = Entry(frame1, textvariable=m)
        matches.grid(row=2, column=1, sticky=W)
        matches_no = m.get()
        print matches_no

	Label(frame1, text="Runs").grid(row=3, column=0, sticky=W)
        r = StringVar()
        runs = Entry(frame1, textvariable=r)
        runs.grid(row=3, column=1, sticky=W)
        runs_no = r.get()
        print runs_no	

	Label(frame1, text="Hundreds").grid(row=4, column=0, sticky=W)
        h = StringVar()
        hundreds = Entry(frame1, textvariable=h)
        hundreds.grid(row=4, column=1, sticky=W)
        hun_no = h.get()
        print hun_no        

	
	B = Button(win, text="Update",command=helloCallBack) #updatePlayerAdd(id_no,n,matches_no,runs_no,hun_no))
	B.pack()
	win.mainloop()

def delPlayer():
	w = Tk()
	f = Frame(w)
	def return_entry(en):
		content = entry.get()

	Label(f, text="Enter ID:").grid(row=0, column=0, sticky=W)
	#iD = StringVar()
	idee = Entry(w)#(f, textvariable=iD)
	idee.grid(row=0, column=1, sticky=W)
	#id_no = iD.get()
	#print "1",id_no, "2",type(id_no), "3",iD, "4",type(iD)
	idee.bind('<Return>', return_entry)
	B = Button(w, text="Delete",command=lambda:updatePlayerDel(idee))
	f.pack()
	B.pack()
	w.mainloop()
	#commentend
	

	# frame1 = Frame(win)
 #    frame1.pack()

 #    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
 #    nameVar = StringVar()
 #    name = Entry(frame1, textvariable=nameVar)
 #    name.grid(row=0, column=1, sticky=W)
"""



# def delPlayer():










w = Tk()
w.title("Cricketer's Database")
fr = Frame(w, width=400, height=100)
l = Label(w, text="Welcome to Cricketer's Database!")
l.pack()
view_db = Button(w, text ="View Database", command = viewDB)
#add_pl = Button(w, text ="Add Player", command = addPlayer)
# del_pl = Button(w, text ="Delete Player", command = delPlayer)

view_db.pack(side=BOTTOM)#side=LEFT, padx=10)
#add_pl.pack(side=LEFT, padx=10)
#del_pl.pack(side=LEFT, padx=10)


fr.pack()
w.mainloop()
