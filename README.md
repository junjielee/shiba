# 个人博客

趁着有时间，将个人博客的项目代码托管的Github

## 环境
- Python3
- Django2.1


## 本地部署

```python
# 创建配置文件
cp config/localsettings.py.default config/localsettings.py

# 然后修改 localsettings.py内容：包括数据库连接信息

# 创建数据库表
python manage.py migrate

# 然后启动
python manage.py runserver 127.0.0.1:9998
```


## 远程部署

```python
```
