import pymysql,yaml
from DBUtils.PooledDB import PooledDB

class db(object):
    def __init__(self):
        yamlPath="db.yaml"
        yaml.load(yamlPath, Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        f = open(yamlPath, 'r')
        data = yaml.load(f.read())['uat']
        self.pool = PooledDB(pymysql,5,host=data['host'],user=data['user'],passwd=data['passwd'],db=data['db'],port=data['port']) 
   
    def select(self,mobile):
        sql="select content from sms_logs where id=(select max(id) from sms_logs where mobile='{0}')".format(mobile)
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