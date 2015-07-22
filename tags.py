
import MySQLdb
from xml.dom import minidom
xmldoc=minidom.parse("Tags.xml")
rowele=xmldoc.getElementsByTagName('row')
db = MySQLdb.connect("localhost","root","PASSWORD","DATABASE")
cursor = db.cursor()
for i in range(len(rowele)):
	
	try :	
		tagname = str(rowele[i].attributes['TagName'].value)
		tagname=str(filter(lambda x:ord(x)>31 and ord(x)<128,tagname))
		tagname = MySQLdb.escape_string(tagname)
	except :
		tagname = 'NULL'
	try :
		count = str(rowele[i].attributes['Count'].value)
	except :
		count = 'NULL'
	
	try :
		epostId = str(rowele[i].attributes['ExcerptPostId'].value)
		
	except :
		epostId = 'NULL'
	try :
		wpostId = str(rowele[i].attributes['WikiPostId'].value)
	except :
		wpostId = 'NULL'	
	
	
		
	insert_sql = "INSERT INTO `Tags` (`TagName`,`Count`,`ExcerptPostId`,`WikiPostId`) VALUES ('%s', '%s', '%s', '%s')" %(tagname,count,epostId,wpostId)
	print insert_sql
	cursor.execute(insert_sql)
	db.commit()			
