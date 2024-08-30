
class originalSql():

    @staticmethod
    def system_brief_recipe_all_sql():
        # FZt is one of 正在使用, 停止使用, 尚未使用
        return '''SELECT briefT.FPhbh AS recipeId, briefT.FPhbNo AS recipeName, briefT.FTpz AS goods, briefT.FSnpz AS cement, briefT.FTld AS cave, briefT.FSzgg AS stone,
            briefT.FTbj AS mark, briefT.FYt AS normalUsage, briefT.FBz AS remark, briefT.FZt AS status
            FROM tphb AS briefT
            WHERE briefT.FZt LIKE %s;'''


    @staticmethod
    def system_brief_recipe_get_sql():
        return '''SELECT briefT.FPhbh AS recipeId, briefT.FPhbNo AS recipeName, briefT.FTpz AS goods, briefT.FSnpz AS cement, briefT.FTld AS cave, briefT.FSzgg AS stone,
            briefT.FTbj AS mark, briefT.FYt AS normalUsage, briefT.FBz AS remark, briefT.FZt AS status
            FROM tphb AS briefT
            WHERE briefT.FPhbh = %s;'''
            
            
    @staticmethod
    def system_detailed_recipe_get_sql():
        return '''SELECT detailedT.FYlmc AS bigMaterialName, detailedT.FPzgg AS smallMaterialName, detailedT.FSysl AS usageKilogram
            FROM tphbycl AS detailedT
            WHERE detailedT.FPhbh = %s;'''
        
    
    @staticmethod
    def order_original_recipe_all_sql():
        # 只纳入施工配比，忽略砂浆配比
        # 各machineId通用配比排在前，专用配比排在后
        return '''SELECT originalT.FYlmc AS bigMaterialName, originalT.FPzgg AS smallMaterialName, originalT.FSysl AS usageKilogram, originalT.FBtId AS machineId
            FROM trwdphbycl AS originalT
            WHERE originalT.FRwdh = %s
            AND originalT.FPblb = 0
            ORDER BY originalT.FBtId ASC;'''

   
    @staticmethod
    def order_adjustable_recipe_all_sql():
        # 这里有些查询出的数据未被使用
        # 只纳入施工配比，忽略砂浆配比
        # 按调整时间，由小到大排序
        return '''SELECT adjustableT.FTzsj AS adjustDateTime, adjustableT.FPblx AS machineId, adjustableT.FPbh2 AS nowRecipeId,
            adjustableT.FCzy AS operatorName, adjustableT.FBz AS recipeContent
            FROM trwdphb AS adjustableT
            WHERE adjustableT.FRwdh = %s
            AND adjustableT.FPblx != "砂浆"
            ORDER BY adjustableT.FTzsj ASC;'''
    
    
    @staticmethod
    def product_recipe_get_sql():
        # include original amd adjustable recipe
        # not use productId, use orderId and startProductDateTime
        pass
    
    

    
        
    
            
