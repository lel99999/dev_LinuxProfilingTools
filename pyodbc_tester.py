import pyodbc
connstr = "DRIVER={SQL Server};Server=servername;Database=dbname; \
                        User Id=uid; Password=pwd;"
conn = pyodbc.connect(connstr)
dbcur = conn.cursor()

strSQL = "SELECT col1,col2,col3 from table'
dbcur.execute(strSQL)
dict1={}
for a line in dbcur: dict1.update({line.col1:line.col2})


dbcur.close()
conn.close()
