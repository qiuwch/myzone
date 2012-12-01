import pyodbc

connection_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};dsn="./Backup_BBS_Blog/bbs.mdb";'

pyodbc.connect(connection_str)

