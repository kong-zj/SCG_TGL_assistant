# Swagger

```
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
```

# STA API

临时用于接口验证
username: admin
password: 123456

## MaterialCategory

### Category 原料分类

```
GET,POST: 
http://127.0.0.1:8000/api/material_category/category/

GET,PUT,PATCH,DELETE:
http://127.0.0.1:8000/api/material_category/category/<int:pk>
```

### OriginalMaterial 原料

```
GET:
http://127.0.0.1:8000/api/material_category/material/

GET:
http://127.0.0.1:8000/api/material_category/material/<int:pk>
```

### MaterialLinkCategory 原料与分类绑定

```
GET,POST: 
http://127.0.0.1:8000/api/material_category/material_link_category/

GET,PUT,PATCH,DELETE:
http://127.0.0.1:8000/api/material_category/material_link_category/<int:pk>
```

## Order 任务单

```
GET:
http://127.0.0.1:8000/api/order/order/
可选参数: coprojlpName (用于搜索 companyName,projectName,littleProjectName 的内容), 
    scheduleDate (格式: XXXX-XX-XX, 用于搜索数据库中 scheduleDateTime 的日期部分)

GET:
http://127.0.0.1:8000/api/order/order/<int:pk>
```

## Product 生产记录

```
GET:
http://127.0.0.1:8000/api/product/product/
可选参数: coprojlpName (用于搜索 companyName,projectName,littleProjectName 的内容), 
    productDate (格式: XXXX-XX-XX, 用于搜索数据库中 productDate 的日期部分),
    orderId (格式: 整数值, 用于搜索数据库中 orderId 的内容)

GET:
http://127.0.0.1:8000/api/product/product/<int:pk>
```

## Recipe 配比

### SystemRecipe 系统配比

```
GET:
http://127.0.0.1:8000/api/recipe/systemrecipe/
可选参数: status (1:正在使用, 2:停止使用, 3:尚未使用)

GET:
http://127.0.0.1:8000/api/recipe/systemrecipe/<int:pk>
```

### OrderRecipe 任务单配比

```
GET:
http://127.0.0.1:8000/api/recipe/orderrecipe/<int:pk>
返回值格式: dict{dateTime: dict{machineId: list[各个成分的字典] } }
    dateTime (0:和order同步生成)
    machineId (0:全部拌台)
```

### ProductRecipe 生产记录配比

```
GET:
http://127.0.0.1:8000/api/recipe/productrecipe/<int:pk>
```


