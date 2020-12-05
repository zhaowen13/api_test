import pymysql,yaml
from DBUtils.PooledDB import PooledDB

class db(object):
    def __init__(self):         #初始化连接，指定连接库
        yamlPath="config.yaml"
        yaml.load(yamlPath, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(yamlPath, 'r')
        data = yaml.load(f.read())['st3']
        self.pool = PooledDB(pymysql,5,host=data['db_host'],user=data['db_user'],passwd=data['db_pass'],db=data['db'],port=data['db_port']) 
   
    def select(self):
        sql="select content from sms_logs where id=(select max(id) from sms_logs where mobile='15080605720')"
        conn = self.pool.connection() 
        cur=conn.cursor()
        r=cur.execute(sql)
        r=cur.fetchall()
        cur.close()
        conn.close()
        return r
    

if __name__ == "__main__":
    mydb=db()
    contet=mydb.select()
    contet=str(contet).split('是')[1]
    print(contet.split('，有')[0])