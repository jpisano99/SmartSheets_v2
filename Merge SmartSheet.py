__author__ = 'jpisano'

import mysql.connector
from settings import database

cnx = mysql.connector.connect(user='root', password=database['PASSWORD'], host='localhost', database='ref_db')
mycursor = cnx.cursor()

cnx1 = mysql.connector.connect(user='root', password=database['PASSWORD'], host='localhost', database='ref_db')
mycursor1 = cnx1.cursor()

path_to_import = 'c:/users/jpisano/desktop/ACI to Production Database/Todays Data/'
file_to_import = 'fy16_bookings_data.csv'
