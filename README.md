# DjangoAutomaticDatabaseRouting
django多数据库自动化路由分配的demo

### 需要注意的地方

这里说的automatic routing不是真正意义上的自动化, 在配置路由后, 你需要手动同步每个一个数据库才可以. 

配置路由只控制数据在同步时是否写入.

具体可看第九步.

更多信息可访问[官方文档](https://docs.djangoproject.com/en/1.11/topics/db/multi-db/)

### 环境:

python3.5

Django-1.11.3

### 步骤:

1. 创建虚拟环境

   ```shell
   virtualenv --no-site-packages AutomaticMultipleDatabases
   ```

   ```shell
   Using base prefix '/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5'
   New python executable in /Users/wangyu/Github/DjangoAutomaticDatabaseRouting/AutomaticMultipleDatabases/bin/python3.5
   Also creating executable in /Users/wangyu/Github/DjangoAutomaticDatabaseRouting/AutomaticMultipleDatabases/bin/python
   Installing setuptools, pip, wheel...done.
   ```

2. 进入并加载虚拟环境

   ```shell
   ➜  DjangoAutomaticDatabaseRouting git:(master) ✗ cd AutomaticMultipleDatabases 
   ➜  AutomaticMultipleDatabases git:(master) ✗ source bin/activate 
   ```

3. 安装django

   ```shell
   (AutomaticMultipleDatabases) ➜  AutomaticMultipleDatabases git:(master) ✗ pip install django
   ```

   ```shell
   Collecting django
     Using cached Django-1.11.3-py2.py3-none-any.whl
   Collecting pytz (from django)
     Using cached pytz-2017.2-py2.py3-none-any.whl
   Installing collected packages: pytz, django
   Successfully installed django-1.11.3 pytz-2017.
   ```

4. 安装mysqlclient

   ```shell
   pip install mysqlclient
   ```

   ```shell
   Collecting mysqlclient
     Using cached mysqlclient-1.3.10.tar.gz
   Building wheels for collected packages: mysqlclient
     Running setup.py bdist_wheel for mysqlclient ... done
     Stored in directory: /Users/wangyu/Library/Caches/pip/wheels/32/50/86/c7be3383279812efb2378c7b393567569a8ab1307c75d40c5a
   Successfully built mysqlclient
   Installing collected packages: mysqlclient
   Successfully installed mysqlclient-1.3.10
   ```

5.  创建项目

   ```shell
   django-admin.py startproject AutoMultDataDemo
   ```

6. 创建APPs

   ```shell
   (AutomaticMultipleDatabases) ➜  AutomaticMultipleDatabases git:(master) ✗ cd AutoMultDataDemo 
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py startapp app 
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py startapp app1
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py startapp app2
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py startapp app3  
   ```

7. 配置多数据库([settings.py](https://github.com/WangYyyyy/DjangoAutomaticDatabaseRouting/blob/master/AutomaticMultipleDatabases/AutoMultDataDemo/AutoMultDataDemo/settings.py))

   关键代码:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       },
       'db1': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
       },
       'db2': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
       },
       'db3': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db3.sqlite3'),
       },
   }
   ```

8. 配置路由配置([settings.py](https://github.com/WangYyyyy/DjangoAutomaticDatabaseRouting/blob/master/AutomaticMultipleDatabases/AutoMultDataDemo/AutoMultDataDemo/settings.py))以及加入DatabaseAppsRouter文件([database_router.py](https://github.com/WangYyyyy/DjangoAutomaticDatabaseRouting/blob/master/AutomaticMultipleDatabases/AutoMultDataDemo/AutoMultDataDemo/database_router.py))

   关键代码:

   ```python
   DATABASE_ROUTERS = ['AutoMultDataDemo.database_router.DatabaseAppsRouter']
   DATABASE_APPS_MAPPING = {
       # example:
       # 'app_name':'database_name',
       'app':'default',
       'app1':'db1',
       'app2':'db2',
       'app3':'db3',
   }
   ```

   > 这样就把4个app分别分配到4个不同的数据库.

9. 每个APP下创建model并且同步数据库即可

   ```shell
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py migrate             
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying sessions.0001_initial... OK
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py migrate --database db1
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying sessions.0001_initial... OK
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py migrate --database db2
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying sessions.0001_initial... OK
   (AutomaticMultipleDatabases) ➜  AutoMultDataDemo git:(master) ✗ python manage.py migrate --database db3
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying sessions.0001_initial... OK
   ```

   model示例(appname/models.py):

   ```python
   class AppModel(models.Model):
   	line1 = models.CharField(max_length=50)
   	line2 = models.CharField(max_length=50)
   	line3 = models.IntegerField()
   ```

   ​