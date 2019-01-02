import requests
import json
import psycopg2


def main():
    group_id = '-22746750'
    url = 'https://api.vk.com/method/wall.get'
    token = 'generate_your_token'

    r = requests.get(url, params={
        'owner_id': group_id,
        'count': 100,
        'offset': 0,
        'access_token': token,
        'v': 5.52
    })

    items = r.json()['response']['items']
    # print(json.dumps(items, indent=4, sort_keys=True))

    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()

    insert_query = "INSERT INTO test VALUES {}".format("(4, 'test4')")
    select_query = 'SELECT * FROM test LIMIT 10'

    cursor.execute(insert_query)

    cursor.execute(select_query)
    records = cursor.fetchall()

    for row in records:
        print(row[1])


main()
