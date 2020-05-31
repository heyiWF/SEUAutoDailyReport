# SEUAutoDailyReport

这程序不是我写的，是我从网上找的。

**05-31更新：随机sleep一段时间，不然提交时间太过相近了，太容易被察觉了。**

**05-09更新autoreport_mail：每天自动提交的结果（成功还是失败）会通过邮件通知你。这是QQ邮箱的模板，其他邮箱同理。注意修改代码中有关账户的参数。** 



运行环境要求：

+ Python 3.x

+ 安装Chrome或Firefox（需要把代码里的`driver = webdriver.Firefox()`注释取消掉改成注释`driver = webdriver.Chrome()`）

+ 安装webdriver：Chrome安装chromedriver，Firefox安装geckodriver，并配置好环境变量。注意webdriver版本需要和浏览器版本对应。

+ 注意把代码里的`YourUsername`和`YourPassword`改成你自己的一卡通号和密码

+ 建议运行脚本前先把代码里的url复制到浏览器打开看看是不是正常（统一身份认证界面或者每日健康申报系统界面）



Linux配置定时任务：

1. 终端输入`crontab -e`，初次使用会让你选择一个编辑器编辑crontab文件，回车默认。

2. 在编辑界面最下面输入一行`3 0 * * * python3 __你放脚本文件的路径__ ` 即每天00:03执行一次脚本。`Ctrl + X` ，`Y` ，回车保存。

3. 重启一下cron，终端输入`/etc/init.d/cron restart` 



**注：** 

**1. 每日晨检体温默认输入36.7，可在代码里自行修改。** 

**2. 欢迎提供反馈，但开发者不对使用脚本造成的任何后果负责。** 

**3. nogui版针对没有图形界面的服务器系统进行了适配，优化了Chrome无图形界面运行配置，并提供更详细的命令行输出。** 
