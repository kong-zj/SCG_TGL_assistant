# STA API

临时用于接口验证
username: admin
password: 123456

## Category 原料分类

```
GET,POST: 
http://127.0.0.1:8000/api/material_category/category/

GET,PUT,PATCH,DELETE:
http://127.0.0.1:8000/api/material_category/category/<int:pk>
```

## OriginalMaterial 原料

```
GET:
http://127.0.0.1:8000/api/material_category/material/

GET:
http://127.0.0.1:8000/api/material_category/material/<int:pk>
```

## MaterialLinkCategory 原料与分类绑定

```
GET,POST: 
http://127.0.0.1:8000/api/material_category/material_link_category/

GET,PUT,PATCH,DELETE:
http://127.0.0.1:8000/api/material_category/material_link_category/<int:pk>
```

## 

```
GET:
http://127.0.0.1:8000/api/order/order/

GET:
http://127.0.0.1:8000/api/order/order/<int:pk>
```