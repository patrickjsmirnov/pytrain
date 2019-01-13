import requests
import json
import psycopg2


def main():
    group_id = '-22746750'
    url = 'https://api.vk.com/method/wall.get'
    token = ''

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
    cursor.execute('TRUNCATE TABLE posts')

    for item in items:
        cursor.execute("INSERT INTO posts (id, comments, likes, reposts, text) VALUES (%s, %s, %s, %s, %s)",
                       (item['id'],
                        item['comments']['count'],
                        item['likes']['count'],
                        item['reposts']['count'],
                        item['text'])
                       )

    select_query = 'SELECT * FROM posts'
    cursor.execute(select_query)
    records = cursor.fetchall()

    for row in records:
        print(row[0])

    conn.commit()




main()
