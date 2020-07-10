import sqlite3
con = sqlite3.connect('emaildb.sqlite')
cur = con.cursor()

# try:        
#     cur.execute("DROP TABLE IF EXISTS Counts")
#     cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")
#     print ('table created successfully')
# except Exception as e:
#     print ('error in operation, ', e)
#     con.rollback()
#     con.close()

# fname = './jupytorNotebooks/emailbox-short.txt'
# fh = open(fname)

# for line in fh:
#     if not line.startswith('From: '):
#         continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', 
#                         (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', 
#                         (email,))
        
#     con.commit()

# con.close()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(row[0], row[1])