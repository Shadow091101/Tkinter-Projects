import sqlite3
from tkinter import *

root=Tk()
root.geometry('400x400')

# #The follwoing line will Create a database or connect to existing one.
# conn=sqlite3.connect('address_book.db')

# #Create cursor for the specified database
# c=conn.cursor()

# #create table
# c.execute("""CREATE TABLE addresses 
#           (firstname text,
#           lastname text,
#           address text,
#           city text,
#           state text,
#           zip_code integer)""")
#sql-lite has only five datatypes:1)text,2)integer,3)real,4)null,5)blob

def edit():
    editor=Tk()
    editor.geometry('400x400')

    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    select_id=selectentry.get()
    c.execute('SELECT * FROM addresses WHERE oid=?',(select_id,))
    
    



    firstname_edit=Entry(editor,width=30)
    firstname_edit.grid(row=0,column=1)
    lastname_edit=Entry(editor,width=30)
    lastname_edit.grid(row=1,column=1)
    address_edit=Entry(editor,width=30)
    address_edit.grid(row=2,column=1)
    city_edit=Entry(editor,width=30)
    city_edit.grid(row=3,column=1)
    state_edit=Entry(editor,width=30)
    state_edit.grid(row=4,column=1)
    zipcode_edit=Entry(editor,width=30)
    zipcode_edit.grid(row=5,column=1)
    

    #Create Label for the widgets

    firstnamelabel_edit=Label(editor,text="First Name")
    firstnamelabel_edit.grid(row=0,column=0)
    lastnamelabel_edit=Label(editor,text="Last Name")
    lastnamelabel_edit.grid(row=1,column=0)
    addresslabel_edit=Label(editor,text="Address")
    addresslabel_edit.grid(row=2,column=0)
    citylabel_edit=Label(editor,text="City")
    citylabel_edit.grid(row=3,column=0)
    statelabel_edit=Label(editor,text="State")
    statelabel_edit.grid(row=4,column=0)
    zipcodelabel_edit=Label(editor,text="ZipCode")
    zipcodelabel_edit.grid(row=5,column=0)
    
    records=c.fetchall()

    for record in records:
        firstname_edit.insert(0,record[0])
        lastname_edit.insert(0,record[1])
        address_edit.insert(0,record[2])
        city_edit.insert(0,record[3])
        state_edit.insert(0,record[4])
        zipcode_edit.insert(0,record[5])

    def save():
        c=conn.cursor()
        
        c.execute("""UPDATE addresses SET 
                  firstname=:first,
                  lastname=:last,
                  address=:address,
                  city=:city,
                  state=:state,
                  zip_code=:zip_code

                  WHERE oid=:oid

                  """,
                  {
                      'first':firstname_edit.get(),
                      'last':lastname_edit.get(),
                      'address':address_edit.get(),
                      'city':city_edit.get(),
                      'state':state_edit.get(),
                      'zip_code':zipcode_edit.get(),

                      'oid':select_id
                  }
                  )


        
        
        conn.commit()
        conn.close()


        firstname_edit.delete(0,END)
        lastname_edit.delete(0,END)
        address_edit.delete(0,END)
        city_edit.delete(0,END)
        state_edit.delete(0,END)
        zipcode_edit.delete(0,END)

        editor.destroy()


        pass

    save_button=Button(editor,text="Save Changes",command=save)
    save_button.grid(row=6,column=0,columnspan=2,pady=15,padx=15,ipadx=58)

    selectentry.delete(0,END)

    # conn=sqlite3.connect('address_book.db')
    # c=conn.cursor()
    # c.execute()
    
   


def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute('DELETE from addresses WHERE oid=?',(selectentry.get(),))

    selectentry.delete(0,END)
    
    conn.commit()
    conn.close()


def submit_to_database():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute('INSERT INTO addresses VALUES(:firstname,:lastname,:address,:city,:state,:zipcode)',
           {
               'firstname':firstname.get(),
               'lastname':lastname.get(),
               'address':address.get(),
               'city':city.get(),
               'state':state.get(),
               'zipcode':zipcode.get()
           }   
              )

    conn.commit()
    conn.close()

    #Clear the Entry Widget

    firstname.delete(0,END)
    lastname.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#create a show function to show the results from the database

def show():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()

    c.execute('SELECT *,oid FROM  addresses')#Here 'oid' stands for an unique id that is prefixed to every record in the table.

    results=c.fetchall()#the fetchall function takes the records and display it in a list format.
    
    #there is also a function called 'fetchone' which fetches only one record.and 'fetchmany(howmany)' let us specify how many recors we needs to fetch.
    print(results)
    
    
    
    details=['First Name','Last Name','Address','City','State','ZipCode']
    print('\n--------------------------\n')
    print_results='\n-------------------------------\n'
    for result in results:
        listofresult=list(result)
        pop=listofresult.pop(-1)
        
        print_results+=f'ID=={pop}\n'
        print(f'ID=={pop}\n')
        for detail in details:
            popedrecord=listofresult.pop(0)
            print(f'{detail} === {popedrecord}')
            print_results+=f'{detail} === {popedrecord} \n'
        print('---------------------------------------------')
        print_results+='---------------------------------------------\n'

           
        

    query_label=Label(root,text=print_results)
    query_label.grid(row=11,column=0,columnspan=2)


    conn.commit()
    conn.close()





#Create Entry widget for our dataentry
firstname=Entry(root,width=30)
firstname.grid(row=0,column=1)
lastname=Entry(root,width=30)
lastname.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)
selectentry=Entry(root,width=30)
selectentry.grid(row=8,column=1)

#Create Label for the widgets

firstnamelabel=Label(root,text="First Name")
firstnamelabel.grid(row=0,column=0)
lastnamelabel=Label(root,text="Last Name")
lastnamelabel.grid(row=1,column=0)
addresslabel=Label(root,text="Address")
addresslabel.grid(row=2,column=0)
citylabel=Label(root,text="City")
citylabel.grid(row=3,column=0)
statelabel=Label(root,text="State")
statelabel.grid(row=4,column=0)
zipcodelabel=Label(root,text="ZipCode")
zipcodelabel.grid(row=5,column=0)
SelectLabel=Label(root,text='Select ID')
SelectLabel.grid(row=8,column=0)



#Submit button to submit our data to the database

btn=Button(root,text="Submit Changes to the database",command=submit_to_database)
btn.grid(row=6,column=0,columnspan=2,pady=15,padx=15,ipadx=100)

#create a show button to show the results
showbutton=Button(root,text="Show Results",command=show)
showbutton.grid(row=7,column=0,columnspan=2,pady=15,padx=15,ipadx=50)

deletebutton=Button(root,text="Delete Record",command=delete)
deletebutton.grid(row=9,column=0,columnspan=2,pady=15,padx=15,ipadx=50)

edit_button=Button(root,text="Edit Record",command=edit)
edit_button.grid(row=10,column=0,columnspan=2,pady=0,padx=0,ipadx=58)
# #Commit the changes in the database
# conn.commit()

# #Close the connection to the database
# conn.close()

root.mainloop()

