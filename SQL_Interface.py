# This module is for handling all interactions with the MYSQL data bases needed for the Home BAS system
import mysql.connector

HOME_BAS = mysql.connector.connect(host="192.168.1.68", user="python", passwd="insight", database="HOME_BAS")
print("Successfully connected to SQL Database")
cursor_remote = HOME_BAS.cursor()


def sump_pump_record(param):
    new_sql_record = "INSERT INTO sump_pump (pump_on, pump_off, run_time) VALUES (%s, %s, %s)"
    sql_values = (param.onTime, param.offTime, param.runTime)
    cursor_remote.execute(new_sql_record, sql_values)
    HOME_BAS.commit()
    print(cursor_remote.rowcount, "record inserted")
