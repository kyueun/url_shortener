import psycopg2


def get_connection():
    conn = psycopg2.connect(host='localhost', dbname='urlshorten', user='gyudong', password='pw', port='5432')

    return conn


# find row from real URL
def find_url(oldurl):
    conn = get_connection()
    cursor = conn.cursor()

    sql = 'select * from oldurl where url=%s;'
    cursor.execute(sql, [oldurl])
    row = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    return row[0]


# find row from index
def find_oldurl(index):
    conn = get_connection()
    cursor = conn.cursor()

    sql = 'select * from oldurl where id=%s;'
    cursor.execute(sql, [index])
    row = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    return row[0]


def insert_url(oldurl):
    try:
        # if URL exists, stop insertion
        find_url(oldurl)

        return

    except:
        pass

    conn = get_connection()
    cursor = conn.cursor()

    sql = 'insert into oldurl(url) values(%s);'
    cursor.execute(sql, [oldurl])

    conn.commit()

    cursor.close()
    conn.close()