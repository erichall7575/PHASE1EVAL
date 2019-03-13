import sqlite3

DBFILENAME = 'employer.db'



with sqlite3.connect(DBFILENAME) as conn:
    cur = conn.cursor()

    SQL=""" DELETE FROM employee"""
    cur.execute(SQL)

    SQL=""" DELETE FROM branch"""
    cur.execute(SQL)


    SQL="""INSERT INTO branch (city,state,zip) 
    VALUES ('Flushing','NY','11368')
    """   

    cur.execute(SQL)

    SQL="""INSERT INTO branch (city,state,zip) 
    VALUES ('Houston','TX','77002')
    """   

    cur.execute(SQL)

  
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Lockett','Walker','S000000001','45000','1')
    """     
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Coleman', 'Casey', 'S000000002','70000','1')
    """     
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Kilome', 'Franklyn', 'S000000003','67000','1')
    """  
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Santiago', 'Hecton', 'S000000004','100000','1')
    """  
    cur.execute(SQL)

   

    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Valdez', 'Framber','S000000005','39000','2')
    """     
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Peacock', 'Brad', 'S000000006', '51000','2')
    """     
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Guduan', 'Reymin', 'S000000007', '67000','2')
    """  
    cur.execute(SQL)
    SQL="""INSERT INTO employee (lastname,firstname,employeeid,salary,branchpk) 
    VALUES ('Cole', 'Gerrit', 'S000000008', '55000','2')
    """  
    cur.execute(SQL)

    

    