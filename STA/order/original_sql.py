
class originalSql():
    
    # 静态方法
    @staticmethod
    def order_all_sql():
        return '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
            FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount
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
            
    

    




