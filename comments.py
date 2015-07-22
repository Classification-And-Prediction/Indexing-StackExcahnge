
import MySQLdb
from xml.dom import minidom
xmldoc=minidom.parse("Comments.xml")
rowele=xmldoc.getElementsByTagName('row')
db = MySQLdb.connect("localhost","root","PASSWORD","DATABASE")
cursor = db.cursor()
for i in range(len(rowele)):
	
	try :	
		postid = str(rowele[i].attributes['PostId'].value)
	except :
		postid = 'NULL'
	try :
		score = str(rowele[i].attributes['Score'].value)
	except :
		score = 'NULL'
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
	
	
		
	insert_sql = "INSERT INTO `Comments` (`PostId`,`Score`,`Text`,`CreationDate`,`UserId`) VALUES ('%s', '%s', '%s', '%s', '%s')" %(postid,score,text,date,uid)
	print insert_sql
	cursor.execute(insert_sql)
	db.commit()			
