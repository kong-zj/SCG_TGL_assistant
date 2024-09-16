
class originalSql():

    @staticmethod
    def product_consume_get_detailed_sql():
        return '''SELECT consumeT.FPanNo AS mixTimes, consumeT.FYlmc AS bigMaterialName, consumeT.FPzgg AS smallMaterialName, 
            consumeT.FPbsl AS defaultKilogram , consumeT.FSysl AS realKilogram, 
            consumeT.FHsl AS aggregateHasWaterPercent, consumeT.FGlyl AS realKilogramWithoutWater
            FROM tjlbycl AS consumeT
            WHERE consumeT.FNo = %s'''
            
    @staticmethod
    def product_consume_get_brief_sql():
        return '''SELECT consumeT.FYlmc AS bigMaterialName, consumeT.FPzgg AS smallMaterialName, 
            consumeT.FPbsl AS defaultKilogram , consumeT.FSysl AS realKilogram, 
            consumeT.FHsl AS aggregateHasWaterPercent, consumeT.FGlyl AS realKilogramWithoutWater
            FROM tjlbycl AS consumeT
            WHERE consumeT.FNo = %s
			AND consumeT.FPanNo = 0'''


    

    
        
    
            
