import sqlite3
import datetime




	

def ins(id,name):
	try:
		con = sqlite3.connect('info1.db')
		cur = con.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS info(Id INT PRIMARY KEY, Name TEXT)')
#	
		cur.execute('insert into info values('+str(id)+', \''+name+'\');')
#			
	#		con.rollback()
		con.commit()
		return
	except sqlite3.Error,e:
		if con:
			con.rollback()
	finally:
		if con:
			con.close()
def retrieve(id):
	try:
		con2 = sqlite3.connect('info1.db')
		cur2=con2.cursor()
		cur2.execute('select name from info where id='+str(id)+';')
		n=cur2.fetchone()
		#cur2.execute('insert into info values('+str(id)+', \''+name+'\');')
#			con.rollback()
		con2.commit()
		
		return n[0]
	except sqlite3.Error,e:
		if con2:
			con2.rollback()
	finally:
		if con2:
			con2.close()
def insert(name):
	try:
		now=datetime.datetime.now()
		da=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
		t=str(now.hour)+':00:00'
		cun = sqlite3.connect('info2.db')
		con3 = sqlite3.connect('info1.db')
		cur1 = con3.cursor()
		cur = cun.cursor()

		cur.execute('CREATE TABLE IF NOT EXISTS inform(date_ DATE, time_ TEXT,  Name TEXT, ocr INT, PRIMARY KEY(date_, time_,Name))')
		
	#	cur.execute('insert into inform values(\'00-00-00\', \'00:00:00\', \'ABc\','+str(0)+');')
		cur.execute('select ocr from inform where name=\''+str(name)+'\' and time_=\''+str(t)+'\';')
		
		n=cur.fetchone()
		
		if not n:
			oc=0;
			cur.execute('insert into inform values(\''+da+'\', \''+t+'\', \''+name+'\','+str(oc)+');')
		
		else:
			oc=int(n[0])
		cur1.execute('select id from info where name=\''+str(name)+'\';')
		#n=int(cur.fetchone()[0]);
		cur.execute('update inform set ocr='+str(oc)+'+1 where name=\''+str(name)+'\' and time_=\''+str(t)+'\'')
#			con.rollback()
		cun.commit()
		return
	except sqlite3.Error,e:
		if con3:
			print e
			con3.rollback()
	
	finally:
		if con3:
			con3.close()
def show():
	try:
		cun = sqlite3.connect('info2.db')
		cur = cun.cursor()
		cur.execute('select * from inform')
		data= cur.fetchall()
		for row in data:
			print row
	except sqlite3.Error,e:
		if cun:
			cun.rollback()
	finally:
		if cun:
			cun.close()