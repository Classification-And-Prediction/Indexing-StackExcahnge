
import MySQLdb
from xml.dom import minidom
xmldoc=minidom.parse("Votes.xml")
rowele=xmldoc.getElementsByTagName('row')
db = MySQLdb.connect("localhost","root","PASSWORD","DATABASE")
cursor = db.cursor()
for i in range(len(rowele)):
	
	try :	
		postid = str(rowele[i].attributes['PostId'].value)
	except :
		postid = 'NULL'
	try :
		voteid = str(rowele[i].attributes['VoteTypeId'].value)
	except :
		voteid = 'NULL'
	
	try :
		date = str(rowele[i].attributes['CreationDate'].value)
		date = MySQLdb.escape_string(date)
	except :
		date = 'NULL'

		
	insert_sql = "INSERT INTO `Votes` (`PostId`,`VoteTypeId`,`CreationDate`) VALUES ('%s', '%s', '%s')" %(postid,voteid,date)
	print insert_sql
	cursor.execute(insert_sql)
	db.commit()			
