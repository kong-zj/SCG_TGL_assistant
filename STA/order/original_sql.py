
class originalSql():
    
    # 静态方法
    @staticmethod
    def order_all_sql():
        return '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FGcdz AS location, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
            FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount, FCzy AS operatorName,
            FSgpb AS scheduleRecipeId, FPhbNo AS scheduleRecipeName, FJbsj AS scheduleMixingTime,
            Fwyzfs AS foreignAidFromOthersQuantity, Fwyzcs AS foreignAidFromOthersCarAmount
            FROM trwd;'''

    @staticmethod
    def order_get_sql(orderId):
        return '''SELECT FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FGcdz AS location, FJhrq AS scheduleDateTime, FTPz AS goods, FTld AS cave, 
            FJhsl AS scheduleQuantity, FWcsl AS finishQuantity, FLjcs AS carAmount, FCzy AS operatorName,
            FSgpb AS scheduleRecipeId, FPhbNo AS scheduleRecipeName, FJbsj AS scheduleMixingTime,
            Fwyzfs AS foreignAidFromOthersQuantity, Fwyzcs AS foreignAidFromOthersCarAmount
            FROM trwd
            WHERE FRwdh = ''' + str(orderId) + ''';'''
            
        # return 'SELECT FYclid AS materialId, FYlmc AS bigMaterialName, FPzgg AS smallMaterialName FROM tycl WHERE FYclid = ' + str(materialId) + ';'
    

    




