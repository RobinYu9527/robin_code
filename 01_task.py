from redis import Redis

if __name__ == '__main__':
    try:
        redis_conn = Redis(host="192.168.247.128", port=6379,db=2)
        # redis_conn.lpush('l1','a','b','c','d','e')
        # res = redis_conn.lrange('l1',0,-1)
        # print(res)

        # redis_conn.ltrim('l1',0,2)
        # res = redis_conn.lrange('l1',0,-1)
        # print(res)
        result = redis_conn.llen('l1')
        print(result)
    except Exception as e:
        print(e)