# Python学习资料

**07-30更新：修复保存时点击确认按钮，页面元素定位错误的问题。**

**06-30更新：清理代码；提交失败会反馈出错原因；新增通过微信推送运行结果。使用教程见下面。**

**05-31更新：随机sleep一段时间（0到5分钟），不然提交时间太过相近了，太容易被察觉了。**

**05-09更新autoreport_mail：每天自动提交的结果（成功还是失败）会通过邮件通知你。这是QQ邮箱的模板，其他邮箱同理。注意修改代码中有关账户的参数。** 



## 运行环境要求：

+ Python 3.x

+ 安装Chrome或Firefox（需要把代码里的`driver = webdriver.Firefox()`注释取消掉改成注释`driver = webdriver.Chrome()`）

+ 安装webdriver：Chrome安装chromedriver，Firefox安装geckodriver，并配置好环境变量。注意webdriver版本需要和浏览器版本对应。

+ 注意把代码里的`YourUsername`和`YourPassword`改成你自己的卡号和密码

+ 建议运行脚本前先把代码里的url复制到浏览器打开看看是不是正常



## `autoreport_wechat` 由 Server酱 提供支持

1. 用GitHub账号，登入http://sc.ftqq.com/

2. 在**微信推送**页面，扫描二维码绑定你的微信。

3. 在**发送消息**页面，你会得到你自己的SCKEY，请妥善保管。

4. 在`autoreport_wechat.py`中，把`posturl`中的`SCKEY`替换为你在上一步中获得的SCKEY。



## Linux配置定时任务：

1. 终端输入`crontab -e`，初次使用会让你选择一个编辑器编辑crontab文件，回车默认，此处以nano为例。

2. 在编辑界面最下面输入一行`3 0 * * * python3 脚本文件的路径` 即每天00:03执行一次脚本。例如`3 0 * * * python3 /home/ubuntu/autoreport.py`然后`Ctrl + X`再按`Y` ，再按回车保存。

3. 重启一下cron，终端输入`/etc/init.d/cron restart` 



## 注： 

**1. 开发者不对使用脚本造成的任何后果负责。** 

**2. nogui版针对没有图形界面的服务器系统进行了适配，优化了Chrome无图形界面运行配置，并提供更详细的命令行输出。** 

**3. 出错的log可以在 /var/mail/你的用户名 文件里看到。**
