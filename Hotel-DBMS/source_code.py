import csv
def loadmenu():
    menu = {}
    with open("menu.csv", "r", newline="\n") as menu_file:
        csvr = csv.reader(menu_file)
        for row in csvr:
            dish_name,price = row
            menu[dish_name]= float(price)
    print("Dishes price:")
    for dish_name, price in menu.items():
        print(dish_name,':','$',price)
def reservation():
    o=int(input("would you like to make \n1)Room reservation \n2)Banquet reservation \n3)Restaurant reservation\n:"))
    if o==1:
        rooms=open("rooms.csv","a",newline="\n")
        csvw=csv.writer(rooms)
        checkin=input("enter checkin date")
        checkout=input("enter checkout date")
        occ=int(input("enter occupancy"))
        name=input("enter booking name")
        days=int(checkout.split("/")[0])-int(checkin.split("/")[0])
        rec=[name,checkin,checkout,occ,days]
        csvw.writerow(rec)
        print("Booking made")
        print("Grand Total=",days*10000,"/-")
        rooms.close()
    elif o==2:
        banq=open("banquet.csv","a",newline="\n")
        csvw=csv.writer(banq)
        name=input("enter booking name")
        day=input("enter day of event")
        event=input("enter name of event")
        no=int(input("no.of days you require the hall"))
        occ=int(input("no. of guests"))
        rec=[name,event,day,no,occ]
        csvw.writerow(rec)
        print("Booking made")
        print("Grand Total=",no*50000,"/-")
        banq.close()
    else:
        rest=open("restaurant.csv","a",newline="\n")
        csvw=csv.writer(rest)
        name=input("enter booking name")
        time=input("enter time of booking:")
        occ=int(input("no. of people"))
        rec=[name,time,occ]
        csvw.writerow(rec)
        print("Booking made")
        rest.close()
def viewreservation():
    print("ROOM BOOKINGS-")
    with open("rooms.csv","r",newline="\n") as room:
        csvr=csv.reader(room)
        for rec in csvr:
            print(rec)
        print("RESTAUARANT BOOKINGS-")
        with open("restaurant.csv","r",newline="\n") as rest:
            csvr=csv.reader(rest)
            for rec in csvr:
                print(rec)
        print("BANQUET BOOKINGS-")
        with open("banquet.csv","r",newline="\n") as banq:
            csvr=csv.reader(banq)
            for rec in csvr:
                print(rec)
def editreserv():
    o=int(input("would you like to update \n1)Room reservation \n2)Banquet reservation\n3)Restaurant reservation\n:"))
    if o==1:
        c=0
        name=input("enter booking name")
        checkin=input("enter checkin date")
        checkout=input("enter checkout date")
        occ=int(input("enter occupancy"))
        days=int(checkout.split("/")[0])-int(checkin.split("/")[0])
        r=[name,checkin,checkout,occ,days]
        newrec=[]
        with open("rooms.csv","r+",newline="\n") as room:
            csvr=csv.reader(room)
            for rec in csvr:
                if rec[0]==name:
                    newrec.append(r)
                    c+=1
                else:
                    newrec.append(rec)
            room.seek(0)
            room.truncate()
            room.seek(0)
            csvw=csv.writer(room)
            csvw.writerows(newrec)
            room.close()
        if c==0:
            print("Not found")
        else:
            print("Updated")
            print("Grand Total=",days*10000,"/-")
    elif o==2:
        c=0
        name=input("enter booking name")
        day=input("enter day of event")
        event=input("enter name of event")
        no=int(input("no.of days you require the hall"))
        occ=int(input("no. of guests"))
        r=[name,event,day,no,occ]
        newrec=[]
        with open("banquet.csv","r+",newline="\n") as banq:
            csvr=csv.reader(banq)
            for rec in csvr:
                if rec[0]==name:
                    newrec.append(r)
                    c+=1
                else:
                    newrec.append(rec)
                banq.seek(0)
                banq.truncate()
                banq.seek(0)
                csvw=csv.writer(banq)
                csvw.writerows(newrec)
                banq.close()
        if c==0:
            print("Not found")
        else:
            print("Updated")
            print("Grand Total=",no*50000,"/-")
    else:
        c=0
        name=input("enter booking name")
        time=input("enter time of booking:")
        occ=int(input("no. of people"))
        r=[name,time,occ]
        newrec=[]
        with open("restaurant.csv","r+",newline="\n") as rest:
            csvr=csv.reader(rest)
            for rec in csvr:
                if rec[0]==name:
                    newrec.append(r)
                    c+=1
                else:
                    newrec.append(rec)
                rest.seek(0)
                rest.truncate()
                rest.seek(0)
                csvw=csv.writer(rest)
                csvw.writerows(newrec)
                rest.close()
        if c==0:
            print("Not found")
        else:
            print("Updated")
def deleteroom():
    c=0
    rno=int(input("enter room no."))
    newrec=[]
    with open("roomservice.csv","r+",newline="\n") as rsc:
        csvr=csv.reader(rsc)
        for rec in csvr:
            if int(rec[0])==rno:
                del rec
                c+=1
            else:
                newrec.append(rec)
                rsc.seek(0)
                rsc.truncate()
                rsc.seek(0)
                csvw=csv.writer(rsc)
                csvw.writerows(newrec)
    if c==0:
        print("Not found")
        print()
    else:
        print("Deleted")
        print()
def addorder():
    dishes=[]
    orders=open("orders.csv","a",newline="\n")
    csvw=csv.writer(orders)
    tno=int(input("enter table no."))
    loadmenu()
    while True:
        dish=input("enter dish")
        if dish=="":
            print("Order complete")
            break
        else:
            qty=int(input("enter qty"))
            dishes.append([dish,qty])
    order=[tno,dishes,"pending"]
    csvw.writerow(order)
    orders.close()
def updateorder():
    o=int(input("1.Restuarant 2.Room Service"))
    if o==1:
        c=0
        dishes=[]
        tno=int(input("enter table no."))
        loadmenu()
        while True:
            dish=input("enter dish")
            if dish=="":
                break
            else:
                qty=int(input("enter qty"))
                dishes.append([dish,qty])
        order=[tno,dishes,"pending"]
        newrec=[]
        with open("roomservice.csv","r+",newline="\n") as rsc:
            csvr=csv.reader(rsc)
            for rec in csvr:
                if int(rec[0])==tno:
                    newrec.append(order)
                    c+=1
                else:
                    newrec.append(rec)
            rsc.seek(0)
            rsc.truncate()
            rsc.seek(0)
            csvw=csv.writer(rsc)
            csvw.writerows(newrec)
        if c==0:
            print("Not found")
        else:
            print("Updated")
def completed():
    o=int(input("1.Restuarant 2.Room Service"))
    if o==1:
        c=0
        newrec=[]
        tno=int(input("enter table no."))
        with open("orders.csv","r+",newline="\n") as orders:
            csvr=csv.reader(orders)
            for rec in csvr:
                if int(rec[0])==tno:
                    rec[-1]="completed"
                    newrec.append(rec)
                    c+=1
                else:
                            newrec.append(rec)
            orders.seek(0)
            orders.truncate()
            orders.seek(0)
            csvw=csv.writer(orders)
            csvw.writerows(newrec)
        if c==0:
            print("Not found")
        else:
            print("Updated")
    elif o==2:
        c=0
        newrec=[]
        tno=int(input("enter room no."))
        with open("roomservice.csv","r+",newline="\n") as rsc:
            csvr=csv.reader(rsc)
            for rec in csvr:
                if int(rec[0])==tno:
                    rec[-1]="completed"
                    newrec.append(rec)
                    c+=1
                else:
                    newrec.append(rec)
            rsc.seek(0)
            rsc.truncate()
            rsc.seek(0)
            csvw=csv.writer(rsc)
            csvw.writerows(newrec)
        if c==0:
            print("Not found")
        else:
            print("Updated")
def viewpending():
    print(["Table no.","dishes","orderstatus"])
    with open("orders.csv","r",newline="\n") as orders:
        csvr=csv.reader(orders)
        for rec in csvr:
            if rec[-1]=="pending":
                print(rec)
    print()
    print("Room Service:")
    print(["Room no.","dishes","orderstatus"])
    with open("roomservice.csv","r",newline="\n") as rsc:
        csvr=csv.reader(rsc)
        for rec in csvr:
            if rec[-1]=="pending":
                print(rec)
def viewcompleted():
    print(["Table no.","dishes","orderstatus"])
    with open("orders.csv","r",newline="\n") as orders:
        csvr=csv.reader(orders)
        for rec in csvr:
            if rec[-1]=="completed":
                print(rec)
    print()
    print("Room Service:")
    print(["Room no.","dishes","orderstatus"])
    with open("roomservice.csv","r",newline="\n") as rsc:
        csvr=csv.reader(rsc)
        for rec in csvr:
            if rec[-1]=="completed":
                print(rec)
def vieworders():
    print(["Table no.","dishes","orderstatus"])
    with open("orders.csv","r",newline="\n") as orders:
        csvr=csv.reader(orders)
        for rec in csvr:
            print(rec)
    print()
    print("Room Service:")
    print(["Room no.","dishes","orderstatus"])
    with open("roomservice.csv","r",newline="\n") as rsc:
        csvr=csv.reader(rsc)
        for rec in csvr:
            print(rec)
def deleteorders():
    c=0
    dishes=[]
    tno=int(input("enter table no."))
    newrec=[]
    with open("orders.csv","r+",newline="\n") as orders:
        csvr=csv.reader(orders)
        for rec in csvr:
            if int(rec[0])==tno:
                del rec
                c+=1
            else:
                newrec.append(rec)
        orders.seek(0)
        orders.truncate()
        orders.seek(0)
        csvw=csv.writer(orders)
        csvw.writerows(newrec)
    if c==0:
        print("Not found")
    else:
        print("Deleted")
def search():
    c=0
    f=open("orders.csv","r")
    tno=int(input("enter tableno:"))
    csvr=csv.reader(f)
    for rec in csvr:
        if rec[0]==str(tno):
            print(rec)
            c+=1
    print()
    if c==0:
        print("record not found")
        print()
print("Welcome to Our Hotel!")
print("Your comfort is our priority.")
print()
print("The loft Hotel")
print("123 Crossword Road, Firecross City ")
print("-Free Wi-fi \n-24/7 Room Service \n-Swimming Pool \n-Fitness Center")
print()
o=int(input("Please select the below options- \n1.Staff \n2.Guest\n"))
print()
while True:
    if o==1:
        opt=input("Please select the below options- \n1.Reserve hotel/banquet/restaurant \n2.Viewreservations \n3.Edit reservation \n4.Delete a reservation \n5.Display menu \n6.Add order\n7.Update order \n8.View all orders \n9.Complete order\n10.View pending orders \n11.ViewCompleted orders \n12.Delete order \n13.Search order")
        if opt=="1":
            reservation()
        elif opt=="2":
            viewreservation()
        elif opt=="3":
            editreserv()
        elif opt=="4":
            deletereservation()
        elif opt=="5":
            loadmenu()
        elif opt=="6":
            addorder()
        elif opt=="7":
            updateorder()
        elif opt=="8":
            vieworders()
        elif opt=="9":
            completed()
        elif opt=="10":
            viewpending()
        elif opt=="11":
            viewcompleted()
        elif opt=="12":
            deleteorders()
        elif opt=="13":
            search()
        else:
            print("Thank you for visiting!")
        break
    elif o==2:
        opt=input("Please select the below options- \n1.Reserve hotel/banquet/restaurant \n2.Editreservation \n3.Delete a reservation \n4.Display menu \n5.Place an order \n6.Update order\n7.Delete Order \n8.Room service \n9.Delete Room Service order")
        if opt=="1":
            reservation()
        elif opt=="2":
            editreserv()
        elif opt=="3":
            deletereservation()
        elif opt=="4":
            loadmenu()
        elif opt=="5":
            addorder()
        elif opt=="6":
            updateorder()
        elif opt=="7":
            deleteorders()
        elif opt=="8":
            roomservice()
        elif opt=="9":
            deleteroom()
        else:
            print("Thank you for visiting!")
        break
