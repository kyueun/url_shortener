import psycopg2

id = 0

def get_connection():
    conn = psycopg2.connect(host='localhost', dbname='url', user='gyudong', password='pw', port='5432')

    return conn

def find_url(oldurl):
    conn = get_connection()
    cursor = conn.cursor()

    sql = 'select * from oldurl where url=(%s);'
    cursor.execute(sql, oldurl)
    row = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    return row

def insert_url(oldurl):
    conn = get_connection()
    cursor = conn.cursor()

    sql = 'insert into oldurl (index, url) values(%s, %s);'
    cursor.execute(sql, (id, oldurl))

    conn.commit()
    id += 1

    cursor.close()
    conn.close()

def find_oldurl(index):
    conn = get_connection()
    cursor = conn.cursor()

    sql = 'select * from oldurl where index=(%s);'
    cursor.execute(sql, index)
    row = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    return row[0]