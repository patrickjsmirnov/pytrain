import requests
import json
import psycopg2
from time import sleep


def get_posts_api_vk(total_count_posts):
    group_id = '-22746750'
    url = 'https://api.vk.com/method/wall.get'
    token = ''

    count = 100
    offset = 0
    posts = []

    while offset < total_count_posts:

        sleep(0.5)
        r = requests.get(url, params={
            'owner_id': group_id,
            'count': count,
            'offset': offset,
            'access_token': token,
            'v': 5.52
        })

        print(r.json())
        items = r.json()['response']['items']

        for item in items:
            posts.append(item)

        offset += count

        # print(json.dumps(items, indent=4, sort_keys=True))

    return posts


def save_posts(posts):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE posts')

    for post in posts:
        cursor.execute("INSERT INTO posts (id, comments, likes, reposts, text) VALUES (%s, %s, %s, %s, %s)",
                       (post['id'],
                        post['comments']['count'],
                        post['likes']['count'],
                        post['reposts']['count'],
                        post['text'])
                       )
    conn.commit()


def get_posts():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()
    select_query = 'SELECT * FROM posts'
    cursor.execute(select_query)
    records = cursor.fetchall()
    conn.commit()
    return records


def get_post(post_id):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE id=%s", (post_id,))
    post = cursor.fetchall()
    conn.commit()

    return post


def main():
    posts = get_posts_api_vk(90000)
    print(len(posts))
    print(posts)
    print(posts)
    save_posts(posts)
    get_posts()
    post = get_post(7615550)
    print('post = ', post)


main()
