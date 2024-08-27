
class originalSql():
    
    # 静态方法
    # @staticmethod
    # def order_all_sql(scheduleDate_input, coprojlpName_input):
    #     sql_perfix = '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
    #         FJzfs AS pump, FGcdz AS location, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
    #         FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount, FCzy AS operatorName,
    #         FSgpb AS scheduleRecipeId, FPhbNo AS scheduleRecipeName, FJbsj AS scheduleMixingTime,
    #         Fwyzfs AS foreignAidFromOthersQuantity, Fwyzcs AS foreignAidFromOthersCarAmount
    #         FROM trwd
    #         WHERE FRwdh >58800'''
    #     # init query string
    #     scheduleDate_query_string = ''' '''
    #     coprojlpName_query_string = ''' '''
    #     if scheduleDate_input:
    #         scheduleDate_query_string = ''' AND FJhrq like "''' + scheduleDate_input + '''%" '''
    #     if coprojlpName_input:
    #         coprojlpName_query_string = ''' AND (FHtdw like "%''' + coprojlpName_input + '''%" OR FGcmc like "%''' + coprojlpName_input + '''%" OR FJzbw like "%''' + coprojlpName_input + '''%")'''
    #     sql_suffix = ''' ORDER BY FRwdh DESC;'''
    #     return sql_perfix + scheduleDate_query_string + coprojlpName_query_string + sql_suffix
    
    
    @staticmethod
    def order_all_sql():
        return '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FGcdz AS location, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
            FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount, FPhbNo AS scheduleRecipeName,
            Fwyzfs AS foreignAidFromOthersQuantity, Fwyzcs AS foreignAidFromOthersCarAmount
            FROM trwd
            WHERE FJhrq LIKE %s
            AND (FHtdw LIKE %s OR FGcmc LIKE %s OR FJzbw LIKE %s)
            ORDER BY FRwdh DESC;'''


    @staticmethod
    def order_get_sql():
        return '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FGcdz AS location, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
            FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount, FCzy AS operatorName,
            FSgpb AS scheduleRecipeId, FPhbNo AS scheduleRecipeName, FJbsj AS scheduleMixingTime,
            Fwyzfs AS foreignAidFromOthersQuantity, Fwyzcs AS foreignAidFromOthersCarAmount
            FROM trwd
            WHERE FRwdh = %s;'''
            
    

    




