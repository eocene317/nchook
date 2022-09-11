import sqlite3
import plistlib
from datetime import datetime


def main():
    db = sqlite3.connect("db")
    cursor = db.cursor()
    sql = 'select * from sqlite_master where type="table" and name="notifications";'
    cursor.execute(sql)
    print(cursor.fetchall())
    sql = 'SELECT note_id, app_id, encoded_data FROM notifications'
    cursor.execute(sql)
    for row in cursor:
        plist = plistlib.loads(row[2])
        title = plist['$objects'][2]
        message = plist['$objects'][3]
        print(row[0], row[1], title, message)

if __name__ == '__main__':
    main()