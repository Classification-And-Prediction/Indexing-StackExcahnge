
import MySQLdb
from xml.dom import minidom
xmldoc=minidom.parse("Posts.xml")
rowele=xmldoc.getElementsByTagName('row')
db = MySQLdb.connect("localhost","root","PASSWORD","DATABASE")
cursor = db.cursor()
for i in range(len(rowele)):
	
	try :	
		postid = str(rowele[i].attributes['PostTypeId'].value)
	except :
		postid = 'NULL'
	try :	
		accansid = str(rowele[i].attributes['AcceptedAnswerId'].value)
	except :
		accansid = 'NULL'
	try :
		score = str(rowele[i].attributes['Score'].value)
	except :
		score = 'NULL'
	try :
		viewcount = str(rowele[i].attributes['ViewCount'].value)
	except :
		viewcount = 'NULL'
	try :
		body = rowele[i].attributes['Body'].value
		body =str(filter(lambda x:ord(x)>31 and ord(x)<128,body))
		body = MySQLdb.escape_string(body)
	except :
		body = 'NULL'
	try :
		title = rowele[i].attributes['Title'].value
		title = str(filter(lambda x:ord(x)>31 and ord(x)<128,title))
		title = MySQLdb.escape_string(title)
	except :
		title = 'NULL'
	try :
		tags = rowele[i].attributes['Tags'].value
		tags = str(filter(lambda x:ord(x)>31 and ord(x)<128,tags))
		tags = MySQLdb.escape_string(tags)
	except :
		tags = 'NULL'
	try :
		date = str(rowele[i].attributes['CreationDate'].value)
		date = MySQLdb.escape_string(date)
	except :
		date = 'NULL'
	try :
		anscount = str(rowele[i].attributes['AnswerCount'].value)
	except :
		anscount = 'NULL'
	try :
		favcount = str(rowele[i].attributes['FavoriteCount'].value)
	except :
		favcount = 'NULL'
	try :
		comcount = str(rowele[i].attributes['CommentCount'].value)
	except :
		comcount = 'NULL'
		
	
	
		
	insert_sql = "INSERT INTO `Posts` (`PostTypeId`,`AcceptedAnswerId`,`Score`,`Body`,`CreationDate`,`ViewCount`,`Title`,`Tags`,`AnswerCount`,`FavoriteCount`,`CommentCount`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(postid,accansid,score,body,date,viewcount,title,tags,anscount,favcount,comcount)
	print insert_sql
	cursor.execute(insert_sql)
	db.commit()			
