import pymysql

class MySQL(object):
    def __init__(self):
        pass

    def get_security_environments(self):
        # Open database connection
        db = pymysql.connect("localhost","root","password#1","security" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "SELECT id, name FROM environment ORDER BY id"

        environments = []
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Fetch all the rows in a list of lists.
           results = cursor.fetchall()
           for row in results:
              id = row[0]
              name = row[1]

              # Now print fetched result
              # print ("id = %d,name = %s" % (id, name))
              environments.append({ 'ID': id, 'NAME': name })
        except:
           print ("Error: unable to fetch data")

        # disconnect from server
        db.close()

        return environments
