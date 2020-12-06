from redis import Redis

if __name__ == '__main__':
    try:
        redis_conn = Redis(host="192.168.247.128", port=6379,db=2)
        result = redis_conn.set('name','itcast')
        print(result)

    except Exception as e:
        print(e)