# Solution - 1
import mysql.connector
import xlrd

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="hindalco")

cur = conn.cursor()

cur.execute("""create table hindalcop(
                serial int auto_increment not null primary key, 
                datetime varchar(20), 
                open float, 
                high float, 
                low float, 
                close float, 
                volume float, 
                instrument varchar(30));""")

l = list()

df = xlrd.open_workbook("D:\\FreeCodeCamp\\Python Projects\\Internshala_Tasks\\MusicPerk_Tasks\\HINDALCO_1D.xlsx")

sheet = df.sheet_by_index(0)

sheet.cell_value(0,0)

for i in range(1, 1216):
    l.append(tuple(sheet.row_values(i)))

query = "insert into hindalcop(datetime, open, high, low, close, volume, instrument) values(%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(query,l)
conn.commit()
conn.close()
