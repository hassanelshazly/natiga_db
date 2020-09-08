from sql_scripts import drop_tables_sql, create_tables_sql
import sqlite3

# connect to the databae
conn = sqlite3.connect('../database/natiga.db')
cur = conn.cursor()

# create tables
cur.executescript(drop_tables_sql)
cur.executescript(create_tables_sql)
conn.commit()
 
fname = '../raw_data/out.txt'
fh = open(fname, "r")

# ignore the first line
# fh.readline()

x = 0
for line in fh:
    # filter the data from file
    data        = line.rstrip().split(",")
    name        = data[0]
    seat        = data[1]
    school      = data[2]
    management  = data[3]
    government  = data[4]
    sum         = data[5]
    percentage  = data[6]
    status      = data[7]
    major       = data[8]
    num_fails   = data[9]
    if len(data) == 20 or len(data) == 21:
        arabic       = data[10] 
        english      = data[11]
        foreign_lang = data[12]
        major_lang1  = data[13]
        major_lang2  = data[14]
        major_lang3  = data[15]
        major_lang4  = data[16]
        religion     = data[17]
        economy      = data[18]
        if len(data) == 20:
            watina = economy
        else :
            watina = data[19]
        
    elif len(data) == 14 or len(data) == 15 :
        arabic       = "-" 
        english      = "-"
        foreign_lang = "-"
        major_lang1  = "-"
        major_lang2  = "-"
        major_lang3  = "-"
        major_lang4  = "-"
        religion     = data[10]
        economy      = data[11]
        if len(data) == 14:
            watina = economy
        else:
            watina = data[12]
    
    # Insert into the database
    # Government
    cur.execute('''INSERT OR IGNORE INTO Government (name) 
        VALUES ( ? )''', ( government, ) )
    cur.execute('SELECT id FROM Government WHERE name = ? ', (government, ))
    government_id = cur.fetchone()[0]

    # Status
    cur.execute('''INSERT OR IGNORE INTO Status (name) 
        VALUES ( ? )''', ( status, ) )
    cur.execute('SELECT id FROM Status WHERE name = ? ', (status, ))
    status_id = cur.fetchone()[0]

    # Major
    cur.execute('''INSERT OR IGNORE INTO Major (name) 
        VALUES ( ? )''', ( major, ) )
    cur.execute('SELECT id FROM Major WHERE name = ? ', (major, ))
    major_id = cur.fetchone()[0]

    # Management
    cur.execute('''INSERT OR IGNORE INTO Management (name, government_id) 
        VALUES ( ?, ? )''', ( management, government_id ) )
    cur.execute('SELECT id FROM Management WHERE name = ? ', (management, ))
    management_id = cur.fetchone()[0]

    # School
    cur.execute('''INSERT OR IGNORE INTO School (name, management_id) 
        VALUES ( ?, ? )''', ( school, management_id ) )
    cur.execute('SELECT id FROM School WHERE name = ? ', (school, ))
    school_id = cur.fetchone()[0]

    # Student
    cur.execute('''INSERT OR REPLACE INTO Student
        (school_id, status_id, major_id, seat, name, sum, percentage, num_fails) 
        VALUES ( ?, ?, ?, ?, ?, ? , ?, ?)''', 
        (school_id, status_id, major_id, seat, name, sum, percentage, num_fails) )

    # Grades
    cur.execute('''INSERT OR REPLACE INTO Grades
        (seat, arabic, english, foreign_lang, major_lang1, 
        major_lang2, major_lang3, major_lang4, religion, watina, economy) 
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (seat, arabic, english, foreign_lang, major_lang1, \
        major_lang2, major_lang3, major_lang4, religion, watina, economy) )
    x += 1
    if x % 100 == 0 :
        conn.commit()
        print(x)
print(x) 
conn.commit()
fh.close()
cur.close()