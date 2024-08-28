
class originalSql():
    
    # 静态方法
    @staticmethod
    def product_all_sql(orderId):
        # orderId 为 int值 或 None
        # init None 情况
        query_orderId_string = ''
        # int值 情况
        if orderId:
            query_orderId_string = 'AND FRwdh = ' + str(orderId)
        return '''SELECT FNo AS productId, FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FScrq AS productDate, FCcsj AS startProductTime
            FROM tjlb
            WHERE FScrq LIKE %s ''' + query_orderId_string + ''' AND (FHtdw LIKE %s OR FGcmc LIKE %s OR FJzbw LIKE %s)
            ORDER BY FNo DESC;'''


    @staticmethod
    def product_get_sql():
        return '''SELECT FNo AS productId, FRwdh AS orderId, FZt AS status, FHtdw AS companyName, FGcmc AS projectName, FJzbw AS littleProjectName,
            FJzfs AS pump, FTPz AS goods, FTld AS cave, FScrq AS productDate, FCcsj AS startProductTime, FCcsjEx AS endProductTime,
            FScbt AS machineId, FShch AS licensePlateNumber, FSgpb AS originalRecipeId, FPhbNo AS originalRecipeName, FCzy AS operatorName, FCcqf AS issuerName,
            FBcps AS mixingTimesAmount, FBcfs AS inCarQuantity, FRvA AS surplusQuantity, FRvB AS realProductQuantity, FZzl AS weight,
            FLjfs AS inCarQuantityCumulativeTotal, FLjcs AS carCumulativeTotal, 
            Fdywc AS hasPrinted, Fqrscwc AS hasProduced, Fdysj AS printDateTime
            FROM tjlb
            WHERE FNo = %s;'''
            
            
            



    




