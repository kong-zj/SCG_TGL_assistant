
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
    def product_adjustable_recipe_get_sql():
        # only include adjustable recipe
        # use productId to get orderId, startProductDateTime and machineId
        return '''SELECT adjustableT.FBz AS recipeContent
            FROM trwdphb AS adjustableT JOIN tjlb AS productT
            ON productT.FNo = %s
            AND adjustableT.FRwdh = productT.FRwdh
            AND (
	            adjustableT.FPblx = "施工"
	            OR adjustableT.FPblx = productT.FScbt
	            )
            AND adjustableT.FTzsj <= CONCAT(productT.FScrq,' ',productT.FCcsj)
            ORDER BY adjustableT.FId DESC
            LIMIT 1;'''
            
             
    @staticmethod
    def product_original_recipe_get_sql():
        # only include original recipe
        # use productId to get orderId, startProductDateTime and machineId
        return '''SELECT originalT.FYlmc AS bigMaterialName, originalT.FPzgg AS smallMaterialName, originalT.FSysl AS usageKilogram
            FROM trwdphbycl AS originalT JOIN tjlb AS productT
            ON productT.FNo = %s
            AND originalT.FRwdh = productT.FRwdh
            AND originalT.FBtId = (
	            SELECT originalT.FBtId
	            FROM trwdphbycl AS originalT JOIN tjlb AS productT
	            ON productT.FNo = %s
	            AND originalT.FRwdh = productT.FRwdh
	            AND (
		            originalT.FBtId = 0
		            OR originalT.FBtId = productT.FScbt
		            )
	            AND originalT.FPblb = 0
	            GROUP BY originalT.FBtId
	            ORDER BY originalT.FBtId DESC
	            LIMIT 1
	            )
            AND originalT.FPblb = 0;'''
    
    

    
        
    
            
