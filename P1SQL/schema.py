# Using python's sqlite3 module write a schema.py file that creates two database tables modeling the following:

#     * Branch: A branch has a city, a state, and a zip code

#     * Employee: An employee has a first name, a last name, an employee ID, and a salary

#     * A branch has many employees, an employee works at one branch

# Using INSERT statements in a seed.py file create two branches with four 
# employees each using the following data:


import sqlite3

DBFILENAME = 'employer.db'


def create_db(dbfilename=DBFILENAME):
    with sqlite3.connect(dbfilename) as conn:
        cur = conn.cursor()

        SQL = """ DROP TABLE IF EXISTS branch;"""
        cur.execute(SQL)

        SQL = """
        CREATE TABLE branch (
            branchpk INTEGER PRIMARY KEY AUTOINCREMENT,            
            city VARCHAR(255),
            state VARCHAR(20),
            zip VARCHAR(20)
        );
        """
        cur.execute(SQL)

        SQL = """ DROP TABLE IF EXISTS employee;"""
        cur.execute(SQL)

        SQL = """
        CREATE TABLE employee (
            employeepk INTEGER PRIMARY KEY AUTOINCREMENT,
            branchpk INTEGER,
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            employeeid INTEGER,
            salary REAL,
            FOREIGN KEY(branchpk) REFERENCES branch(branchpk)
        );
        """
        cur.execute(SQL)

        


if __name__ == "__main__":
    create_db(DBFILENAME)