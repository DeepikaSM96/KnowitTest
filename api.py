import json
import urllib3
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="D9686379185d*", host="localhost", port="5432")
cur = conn.cursor()

http = urllib3.PoolManager()
url = "https://api-content.ingresso.com/v0/theaters"

try:
    response = http.request('GET', url)
    data = json.loads(response.data.decode('utf-8'))

    for i in data:
        cityName = None
        uf = None

        cityName = i['cityName']
        uf = i['uf']

        cur.execute("INSERT INTO city VALUES(%s, %s)", (cityName, uf))
        conn.commit()
    cur.close()
except IOError as io:
    print("ERROR!")