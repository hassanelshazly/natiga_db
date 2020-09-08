#################################################################################
###########################       Create Tables       ###########################
#################################################################################

drop_tables_sql = '''

    DROP TABLE IF EXISTS Government;
    DROP TABLE IF EXISTS Management;
    DROP TABLE IF EXISTS School;
    DROP TABLE IF EXISTS Status;
    DROP TABLE IF EXISTS Major;
    DROP TABLE IF EXISTS Grades;
    DROP TABLE IF EXISTS Student;

'''

create_tables_sql = '''

CREATE TABLE Government (
    id    INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name  VARCHAR(256) UNIQUE
);

CREATE TABLE Management (
    id             INTEGER NOT NULL PRIMARY KEY UNIQUE,
    government_id  INTEGER,
    name           VARCHAR(256) UNIQUE
);

CREATE TABLE School (
    id             INTEGER NOT NULL PRIMARY KEY UNIQUE,
    management_id  INTEGER,
    name           VARCHAR(256) UNIQUE
);

CREATE TABLE Status (
    id    INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name  VARCHAR(256) UNIQUE
);

CREATE TABLE Major (
    id    INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name  VARCHAR(256) UNIQUE
);

CREATE TABLE Grades (
    seat         INTEGER NOT NULL PRIMARY KEY UNIQUE,
    arabic       VARCHAR(128),
    english      VARCHAR(128),
    foreign_lang VARCHAR(128),

    major_lang1  VARCHAR(128),
    major_lang2  VARCHAR(128),
    major_lang3  VARCHAR(128),
    major_lang4  VARCHAR(128),

    religion     VARCHAR(128),
    watina       VARCHAR(128),
    economy      VARCHAR(128)
);

CREATE TABLE Student (
    id           INTEGER NOT NULL PRIMARY KEY UNIQUE,
    school_id    INTEGER,
    status_id    INTEGER,
    major_id     INTEGER,

    seat         INTEGER NOT NULL UNIQUE,
    name         VARCHAR(256),
    sum          NUMERIC,
    percentage   NUMERIC,
    num_fails    INTEGER
    
);
'''

#################################################################################
###########################        Insert Data        ###########################
#################################################################################

# # Government
# cur.execute('''INSERT OR IGNORE INTO Government (name) 
#     VALUES ( ? )''', ( government, ) )
# cur.execute('SELECT id FROM Government WHERE name = ? ', (government, ))
# government_id = cur.fetchone()[0]

# # Status
# cur.execute('''INSERT OR IGNORE INTO Status (name) 
#     VALUES ( ? )''', ( status, ) )
# cur.execute('SELECT id FROM Status WHERE name = ? ', (status, ))
# status_id = cur.fetchone()[0]

# # Major
# cur.execute('''INSERT OR IGNORE INTO Major (name) 
#     VALUES ( ? )''', ( major, ) )
# cur.execute('SELECT id FROM Major WHERE name = ? ', (major, ))
# major_id = cur.fetchone()[0]

# # Management
# cur.execute('''INSERT OR IGNORE INTO Management (name, government_id) 
#     VALUES ( ?, ? )''', ( management, government_id ) )
# cur.execute('SELECT id FROM Management WHERE name = ? ', (management, ))
# management_id = cur.fetchone()[0]

# # School
# cur.execute('''INSERT OR IGNORE INTO School (name, management_id) 
#     VALUES ( ?, ? )''', ( school, management_id ) )
# cur.execute('SELECT id FROM School WHERE name = ? ', (school, ))
# school_id = cur.fetchone()[0]

# # Student
# cur.execute('''INSERT OR REPLACE INTO Student
#     (school_id, status_id, major_id, seat, name, sum, percentage, num_fails) 
#     VALUES ( ?, ?, ?, ?, ?, ? , ?, ?)''', 
#     (school_id, status_id, major_id, seat, name, sum, percentage, num_fails) )

# # Grades
# cur.execute('''INSERT OR REPLACE INTO Grades
#     (seat, arabic, english, foreign_lang, major_lang1, 
#      major_lang2, major_lang3, major_lang4, religion, watina, economy) 
#     VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
#     (seat, arabic, english, foreign_lang, major_lang1, \
#      major_lang2, major_lang3, major_lang4, religion, watina, economy) )


#################################################################################
###########################        Select Data        ###########################
#################################################################################


select_data_sql = '''

SELECT Student.name          AS "Name",
	   Student.seat          AS "Seat No.",
	   Student.sum           AS "Sum",
	   Major.name            AS "Major.",
	   Student.percentage    AS "Percent.",
	   Status.name           AS "Status",
       Student.num_fails     AS "Fails",
	   School.name           AS "School",
	   Management.name       AS "Management",
	   Government.name       AS "Government",
	   Grades.arabic         AS "Arabic",
	   Grades.english        AS "English",
	   Grades.foreign_lang   AS "French",
	  


       CASE WHEN Major.name = "علمي رياضة" or Major.name = "علمي علوم" 
        THEN Grades.major_lang1    ELSE "-"
	   END Physics,
	  
       CASE WHEN Major.name = "علمي رياضة" or Major.name = "علمي علوم" 
        THEN Grades.major_lang1    ELSE "-"
	   END Chemistry,
	   
	   CASE WHEN Major.name = "علمي رياضة"
        THEN Grades.major_lang3    ELSE "-"
	   END "Math 1",
	   
       CASE WHEN Major.name = "علمي رياضة" 
       THEN Grades.major_lang4     ELSE "-"
	   END "Math 2",
	   

	   CASE WHEN Major.name = "علمي علوم" 
        THEN Grades.major_lang3    ELSE "-"
	   END Biology,
	   
       CASE WHEN Major.name = "علمي علوم"
        THEN Grades.major_lang4    ELSE "-"
	   END Geology,
	   

	   CASE WHEN Major.name = "أدبي"
        THEN Grades.major_lang1    ELSE "-"
	   END Philosophy,
	  
       CASE WHEN Major.name = "أدبي"
        THEN Grades.major_lang2    ELSE "-"
	   END Psychology,
	 
       CASE WHEN Major.name = "أدبي" 
       THEN Grades.major_lang3     ELSE "-"
	   END History,
	 
       CASE WHEN Major.name = "أدبي"
        THEN Grades.major_lang4    ELSE "-"
	   END Geography,

       Grades.religion AS "Religion",
	   Grades.watina   AS "Watina",
	   Grades.economy  AS "Economy"	   
	   
	   
FROM Student JOIN School JOIN Government 
	         JOIN Major  JOIN Management 
             JOIN Status JOIN Grades 


WHERE School.id      = Student.school_id
AND   Status.id      = Student.status_id   
AND	  Major.id       = Student.major_id
AND	  Grades.seat    = Student.seat
AND	  Management.id  = School.management_id   
AND	  Government.id  = Management.government_id

AND	  School.name    = "school_name"

ORDER BY Student.seat  
-- LIMIT 20
'''