
class originalSql():
    
    # 静态方法
    @staticmethod
    def original_material_all_sql():
        return 'SELECT FYclid AS materialId, FYlmc AS bigMaterialName, FPzgg AS smallMaterialName FROM tycl;'

    @staticmethod
    def original_material_get_sql(materialId):
        return 'SELECT FYclid AS materialId, FYlmc AS bigMaterialName, FPzgg AS smallMaterialName FROM tycl WHERE FYclid = ' + str(materialId) + ';'
    
    