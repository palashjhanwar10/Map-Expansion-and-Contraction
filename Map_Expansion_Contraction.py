import folium
import csv
import tkinter as tk
from tkinter import *
import webbrowser

def show_entry_fields():
    global zoomv
    global mino,maxo,mina,maxa,s
    s.set("CITY : \n")
    print("Source: %s\nDestination: %s" % (e1.get(), e2.get()))
    #Search for the longitude and latitude of the given source and destination from the csv file.    
    with open('E:\\in.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if( row['City']==e1.get() ):
                slat=float(row['Lat'])
                slong=float(row['Long'])
            if( row['City']==e2.get() ):
                dlat=float(row['Lat'])
                dlong=float(row['Long'])
    print(slat,slong,dlong,dlat)
    #Calculate the mid longitude and latitude.
    midlat=(slat+dlat)/2
    midlong=(slong+dlong)/2
    print(midlat,midlong)
    
    check=abs(slat-dlat)
    if(check<1):
        zoomv.set(8)
    if(check<0.5):
        zoomv.set(10)
    else:
        zoomv.set(5)

    mino.set(min(slong,dlong))
    maxo.set(max(slong,dlong))
    mina.set(min(slat,dlat))
    maxa.set(max(slat,dlat))
    map_osm = folium.Map(location=[midlat,midlong],zoom_start=zoomv.get())
    #Mark the source and destination on the map
    folium.Marker([slat,slong], popup=e1.get()).add_to(map_osm)
    folium.Marker([dlat,dlong], popup=e2.get()).add_to(map_osm)
    map_osm.save('E:\\mapF.html')
    url = 'file://E:/mapF.html'
    webbrowser.open(url,new=0)
def zoomin():
    global zoomv,mino,maxo,mina,maxa,s
    #Increasing the zoom value
    zoomv.set(zoomv.get()+1)
    s.set("ZOOM LEVEL : "+str(zoomv.get())+"\nCITY : \n")
    with open('E:\\in.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if( row['City']==e1.get() ):
                slat=float(row['Lat'])
                slong=float(row['Long'])
            if( row['City']==e2.get() ):
                dlat=float(row['Lat'])
                dlong=float(row['Long'])
    print(slat,slong,dlong,dlat)
    midlat=(slat+dlat)/2
    midlong=(slong+dlong)/2
    print(midlat,midlong)
    #Reducing the range of to get the citites between the soure and destination
    mino.set(mino.get()-1)
    maxo.set(maxo.get()+1)
    mina.set(mina.get()-1)
    maxa.set(maxa.get()+1)
    map_osm = folium.Map(location=[midlat,midlong],zoom_start=zoomv.get())
    with open('E:\\in.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if( float(row['Long'])>mino.get() and float(row['Long'])<maxo.get() and float(row['Lat'])>mina.get() and float(row['Lat'])<maxa.get() ):
                print(row['City'],row['Lat'],row['Long'])
                #Marking and displaying the cities between the range
                s.set(s.get()+row['City']+'\n')
                folium.Marker([row['Lat'],row['Long']], popup=row['City']).add_to(map_osm)
    folium.Marker([slat,slong], popup=e1.get()).add_to(map_osm)
    folium.Marker([dlat,dlong], popup=e2.get()).add_to(map_osm)
    s.set(s.get()+e1.get()+'\n'+e2.get())
    map_osm.save('E:\\mapF.html')
    url = 'file://E:/mapF.html'
    webbrowser.open(url,new=0)

def zoomout():
    global zoomv,mino,maxo,mina,maxam,s
    #Decreasing the zoom value
    zoomv.set(zoomv.get()-1)
    s.set("ZOOM LEVEL : "+str(zoomv.get())+"\nCITY : \n")
    with open('E:\\in.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if( row['City']==e1.get() ):
                slat=float(row['Lat'])
                slong=float(row['Long'])
            if( row['City']==e2.get() ):
                dlat=float(row['Lat'])
                dlong=float(row['Long'])
    print(slat,slong,dlong,dlat)
    midlat=(slat+dlat)/2
    midlong=(slong+dlong)/2
    print(midlat,midlong)
    #Increasing the range of to get the citites between the soure and destination
    mino.set(mino.get()+1)
    maxo.set(maxo.get()-1)
    mina.set(mina.get()+1)
    maxa.set(maxa.get()-1)
    map_osm = folium.Map(location=[midlat,midlong],zoom_start=zoomv.get())
    with open('E:\\in.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if( float(row['Long'])>mino.get() and float(row['Long'])<maxo.get() and float(row['Lat'])>mina.get() and float(row['Lat'])<maxa.get() ):
                print(row['City'],row['Lat'],row['Long'])
                #Marking and displaying the cities between the range
                s.set(s.get()+row['City']+'\n')
                folium.Marker([row['Lat'],row['Long']], popup=row['City']).add_to(map_osm)
    folium.Marker([slat,slong], popup=e1.get()).add_to(map_osm)
    folium.Marker([dlat,dlong], popup=e2.get()).add_to(map_osm)
    s.set(s.get()+e1.get()+'\n'+e2.get())
    map_osm.save('E:\\mapF.html') 
    url = 'file://E:/mapF.html'
    webbrowser.open(url,new=0)
#The Main GUI Part
master = tk.Tk()
master.geometry('300x400')
zoomv= IntVar()
mino= DoubleVar()
maxo= DoubleVar()
mina= DoubleVar()
maxa= DoubleVar()
s=StringVar()
s.set("CITY : \n")
tk.Label(master, text="Source").grid(row=0)
tk.Label(master, text="Destination").grid(row=1)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(master, text='Quit', command=master.quit).grid(row=3,column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3,column=1, sticky=tk.W, pady=4)    
tk.Button(master,text='+', command=zoomin).grid(row=4,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='-', command=zoomout).grid(row=4,column=0,sticky=tk.W,pady=4)
tk.Label(master,textvariable=s).grid(row=5,column=0,sticky=tk.W,pady=4)
tk.mainloop()

map_osm = folium.Map(location=[19.970461,79.301483],zoom_start=6)
folium.Marker([19.970461,79.301483], popup="e1.get()").add_to(map_osm)
folium.Marker([19.949788,79.302087], popup="e2.get()").add_to(map_osm)
with open('E:\\in.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        if( float(row['Long'])>71 and float(row['Long'])<85 and float(row['Lat'])>20 and float(row['Lat'])<23 ):
            folium.Marker([row['Lat'],row['Long']], popup=row['City']).add_to(map_osm)
map_osm.save('E:\\mapF.html')