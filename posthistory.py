
import MySQLdb
from xml.dom import minidom
xmldoc=minidom.parse("PostHistory.xml")
rowele=xmldoc.getElementsByTagName('row')
db = MySQLdb.connect("localhost","root","PASSWORD","DATABASE")
cursor = db.cursor()
for i in range(len(rowele)):
	
	try :	
		postid = str(rowele[i].attributes['PostId'].value)
	except :
		postid = 'NULL'
	try :
		posthistorytype = str(rowele[i].attributes['PostHistoryTypeId'].value)
	except :
		posthistorytype = 'NULL'
	try :
		text = rowele[i].attributes['Text'].value
		text=str(filter(lambda x:ord(x)>31 and ord(x)<128,text))
		text = MySQLdb.escape_string(text)
	except :
		text = 'NULL'
	try :
		date = str(rowele[i].attributes['CreationDate'].value)
		date = MySQLdb.escape_string(date)
	except :
		date = 'NULL'
	try :
		uid = str(rowele[i].attributes['UserId'].value)
	except :
		uid = 'NULL'	
	
	
		
	insert_sql = "INSERT INTO `PostHistory` (`PostId`,`PostHistoryTypeId`,`Text`,`CreationDate`,`UserId`) VALUES ('%s', '%s', '%s', '%s', '%s')" %(postid,posthistorytype,text,date,uid)
	print insert_sql
	cursor.execute(insert_sql)
	db.commit()			
