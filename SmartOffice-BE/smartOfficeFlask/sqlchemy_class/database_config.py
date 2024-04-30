

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# 设置 MySQL 数据库连接字符串，替换为你自己的数据库连接信息
mysql_connection_string = 'mysql+pymysql://root:root@192.168.1.171:3306/smartoffice'
# 创建 SQLAlchemy 引擎
# 指定使用的线程池 40 个线程，如果需要扩展的 给出五个额外的名额
engine = create_engine(mysql_connection_string, pool_size=40, max_overflow=5)
metadata = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)


# 返回Session 线程
def get_session():
    return Session()
