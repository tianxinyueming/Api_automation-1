# import sys
# sys.path.append(r"D:\Job\python\Script\Api_automation")
from Common import operate_json
# from Common.new_tool_a import New_Tool_A
from Conf import Config
import pymysql
import re


class OperateSqlAl(object):

    oj = operate_json.OperateJson()
    con = Config.Config()

    def __init__(self,envir):
        if 'ysy_test' == envir:         # 一生约测试
            self.dbhost = self.con.db_host_ysy_debug
            self.dbport = int(self.con.db_port_ysy_debug)
            self.dbname = self.con.db_name_ysy_debug
            self.db_user = self.con.db_user_ysy_debug
            self.pwd = self.con.db_pwd_ysy_debug
        elif 'ysy_relase' == envir:     # 一生约正式
            self.dbhost = self.con.db_host_ysy_release
            self.dbport = int(self.con.db_port_ysy_release)
            self.dbname = self.con.db_name_ysy_release
            self.db_user = self.con.db_user_ysy_release
            self.pwd = self.con.db_user_ysy_release
        elif 'yhz_test' == envir:       # 雨花测试环境
            self.dbhost = self.con.yhz_host
            self.dbport = int(self.con.db_port_ysy_release)
            self.dbname = self.con.db_name_ysy_release
            self.db_user = self.con.db_user_ysy_release
            self.pwd = self.con.db_user_ysy_release
        elif 'tysy_o2o' == envir:       # 小猪测试环境
            self.dbhost = self.con.db_host_ysy_debug
            self.dbport = int(self.con.db_port_ysy_debug)
            self.dbname = self.con.db_name_o2o_debug
            self.db_user = self.con.db_user_ysy_debug
            self.pwd = self.con.db_pwd_ysy_debug

    def re_sql(self,var_str):
        """
        处理str中包含了变量的sql
        :param str:可能包含了formate的字符串
        :return:不包含了formate的字符串
        """
        if 'format' in var_str:
            p1 = re.compile(r"[(](.*?)[')]", re.S)
            split_str = var_str.split('format')
            var_1 = re.findall(p1, split_str[1])
            #这里会对list中每个值进行判断
            var_1 = self.ut.circular_processing_data(var_1)
            # 注意这里只传递了第一个格式化值进来
            sql_resutl = split_str[0].format(*var_1)
            return sql_resutl
        else:
            return var_str

    def execute_sql(self, sql_str):
        try:
            db = pymysql.connect(host=self.dbhost, port=self.dbport, user=self.db_user, passwd=self.pwd, db=self.dbname,
                                 charset='utf8')
            cursor = db.cursor()  # 创建一个游标
            cursor.execute(sql_str)
            data = cursor.fetchone()
            data = self.bytes_to_str(data[0])
            return data
        except Exception:
            print("sql执行异常，请检查")
        finally:
            cursor.close()
            db.close()  # 关闭数据库

    def bytes_to_str(self,val1):
        if type(val1) == bytes:
            val1 = val1.decode(encoding='utf-8')
        return val1

    # def sql_main(self,data):
    #     '''
    #     这里的多个sql语句执行后，结果可能是一个变量或一个list并未做处理
    #     :param data:
    #     :return:
    #     '''
    #     split_data = data.split(";")
    #     for i in split_data:
    #         value = self.split_sql(i)   # 相互调用异常
    #         return value



if __name__ == "__main__":
    om = OperateSqlAl("ysy_test")
    resl = om.deal_sql('SELECT IFNULL(CONCAT(SUM(sc.product_num)),0) FROM sp_cart sc WHERE sc.id_user=(SELECT id FROM user u WHERE u.mobile={0})formate(c::tester_debug)')
    print(type(resl), resl)  # 返回结果默认为tuple
    # print(oy.read_yaml()['db']['release']['user'])
