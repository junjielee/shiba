# 个人博客

趁着有时间，将个人博客的项目代码托管的Github

## 环境
- Python3
- Django2.1


## 本地部署

```python
# 创建配置文件
cd shiba/conf/ && cp shiba_conf_example.py shiba_conf.py

# 然后修改 shiba_conf.py内容：包括数据库连接信息

# 创建数据库表
python manage.py migrate

# 然后启动
python manage.py runserver 127.0.0.1:9998
```


## 远程部署

```python
# 创建并且修改inventry文件
cd deploy/inventory/ && cp vps_example vps

# 然后修改 vps文件内容

# 返回到deploy目录下，执行命令部署到远端
ansible-playbook ./ansible/django.yml -i ./inventory/vps -v --ask-pass -u remote_user

```
