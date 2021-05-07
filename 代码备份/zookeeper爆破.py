from kazoo.client import KazooClient
for ip in ['','']:
    try:
        zk = KazooClient(hosts=ip)
        zk.start()
        # 获取某个节点下所有子节点
        node = zk.get_children('/')
        # 获取某个节点对应的值
        print(node)
        # 操作完后，别忘了关闭zk连接
        zk.stop()
        print(ip)
    except:
        continue

