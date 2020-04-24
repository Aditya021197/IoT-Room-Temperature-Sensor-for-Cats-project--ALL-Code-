#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep
import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",#Server Name
    user="root",#Username
    passwd="12345678",#Password
    database="temperatureRecords"#Name of database
    )#Connects to the relevant database

cursor = mydatabase.cursor()#Cursor for the database

insertquery = "INSERT INTO tempDetails(temp, message) VALUES(%s, %s)"#Reserved Insert Query
sensehat = SenseHat()#Creates an object for the sense hat

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

temptoohigh = "This room temperature is too high for cats"
temptoolow = "This room temperature is too low for cats"

def temperature():
    temper = sensehat.get_temperature()#This line of code is supposed to capture the temperature
    print(temper)#Supposed to print out the captured temperature onto the console(shell)
    sensehat.show_message(temper, text_colour =blue, back_colour=yellow)#Supposed to display the captured temperature on the sense hat
    if temper > 21: #If the captured room temperature is above the ideal temperature
        print(temptoohigh)#Prints out the message to the shell stating that the temperature is too high
        vals = (temper, temptoohigh)#values to insert into database
        cursor.execute(insertquery, vals) #Supposed to execute the insert query
        mydatabase.commit()
        print(cursor.rowcount, "Details Added to Database")
        sensehat.show_message(temptoohigh, text_colour =red, back_colour=yellow)#Supposed to display the message on the sense hat
    elif temper < 21:#If the captured room temperature is below the ideal temperature
        print(temptoolow)#Prints out the message to the shell stating that the temperature is too low
        vals = (temper, temptoolow) #values to insert into database
        cursor.execute(insertquery, vals)#Supposed to execute the insert query
        mydatabase.commit()
        print(cursor.rowcount, "Details Added to Database")
        sensehat.show_message(temptoolow, text_colour =red, back_colour=yellow)#Supposed to display the message on the sense hat
    elif temper == 21:#Ideal Room Temperature for cats is 21 degrees celsius
        print("Ideal Room Temperature for cats")#Prints out the message to the shell stating that the temperature is ideal
        vals = (temper, "Ideal Room Temperature for cats")#values to insert into database
        cursor.execute(insertquery, vals) #Supposed to execute the insert query
        mydatabase.commit()
        print(cursor.rowcount, "Details Added to Database")
        sensehat.show_message(temptoohigh, text_colour =green, back_colour=yellow)#Supposed to display the message on the sense hat
        
try:
    while True:
        temperature()#calls this method
except KeyboardInterrupt:
    print("Terminated")