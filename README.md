# SEUAutoDailyReport

**让你不再忘记每日报平安～** 



运行环境要求：

+ Python 3.x

+ 安装Chrome或Firefox（需要把代码里的`driver = webdriver.Firefox()`注释取消掉改成注释`driver = webdriver.Chrome()`）

+ 安装对应的webdriver：Chrome安装chromedriver，Firefox安装geckodriver，并配置好环境变量

+ 注意把代码里的`YourUsername`和`YourPassword`改成你自己的一卡通号和密码

+ 建议运行脚本前先把代码里的url复制到浏览器打开看看是不是正常（统一身份认证界面或者每日健康申报系统界面）



Linux配置定时任务：

终端输入`crontab -e`，初次使用会让你选择一个编辑器编辑crontab文件，回车默认。

在编辑界面最下面输入一行`3 0 * * * python3 __你放脚本文件的路径__ ` 即每天00:03执行一次脚本。`Ctrl + X` ，`Y` ，回车保存即可。
