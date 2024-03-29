# SEUAutoDailyReport

## Changelog

2022年12月15日起，停止每日健康申报。师生凭刷校园卡、测温入校。它的光荣使命在今天终于圆满完成！ **祝大家学习顺利，生活愉快，身体倍儿棒！** 

09/30/2022：预祝国庆快乐！修复了登录失败导致的程序意外中止问题；优化了代码可读性。

09/16/2022：修复页面元素定位错误问题；使用新版本的 selenium 定位元素表达式语法；使用新的定位元素方式，（一定程度上）避免了健康申报页面更新导致程序出错的问题；删除了不必要的库，精简了无用代码。

06/21/2022：使用隐身窗口打开网页，尝试修复最近频繁出现的`unknown error: net::ERR_NAME_NOT_RESOLVED`问题。或许是浏览器缓存/Cookies导致？

09/30/2021：我回来啦！修复保存时点击确认按钮，页面元素定位错误的问题。

04/24/2021：修复保存时点击确认按钮，页面元素定位错误的问题。由于新增了一个条目，未接种疫苗的同学，今天请先手动提交一次。

04/13/2021：遵循 Markdown 语法修正推送消息中的换行；新增 webdriver 版本不匹配时的异常处理。友情提醒：近期已接种疫苗的同学请注意在系统中手动填写相关信息。

02/18/2021：更新被弃用的 webdriver 参数；微信即将下线公众号模板消息，Server酱 改为使用企业微信推送通道。

02/11/2021：新春快乐！更新输出 sleep 时间，不然总是以为程序卡住了。

01/23/2021：假期愉快！更新配置 Github Actions 教程，更新脚本第一次失败后再试一次，（希望）解决由于种种原因 GitHub 服务器与学校系统连接出错而失败但手动重新运行一次又能成功的问题。

12/14/2020：初步适配 GitHub Actions（服务器到期了但是还要复习考研，只好临时做了个，教程和整理代码什么的等考完有时间再弄，看得懂 YAML 的可以自己 fork 过去配置一下也不难，本质上也就是个 Ubuntu 的 Docker 镜像……

07/30/2020：修复保存时点击确认按钮，页面元素定位错误的问题。

06/30/2020：清理代码；提交失败会反馈出错原因；新增通过微信推送运行结果。使用教程见下面。

05/31/2020：随机 sleep 一段时间（0到5分钟），不然提交时间太过相近了，太容易被察觉了。

05/09/2020：新增 autoreport_mail，每天自动提交的结果（成功还是失败）会通过邮件通知你。这是 QQ 邮箱的模板，其他邮箱同理。注意修改代码中有关账户的参数。



## 运行环境要求：

+ Python 3.x

+ 安装 Chrome 或Firefox （需要把代码里的`driver = webdriver.Firefox()`注释取消掉改成注释`driver = webdriver.Chrome()`）

+ 安装 webdriver：Chrome 安装 chromedriver， Firefox 安装 geckodriver，并配置好环境变量。注意 webdriver 版本需要和浏览器版本对应。

+ 注意把代码里的`YourUsername`和`YourPassword`改成你自己的卡号和密码

+ 建议运行脚本前先把代码里的url复制到浏览器打开看看是不是正常



## `autoreport_wechat` 由 Server酱·Turbo版 提供支持

1. 微信扫码登录 https://sct.ftqq.com/

2. 跟随**消息通道**页面的指引，注册并填写你自己企业微信账号相关信息，或使用客户端推送等其他渠道。

3. 在**SendKey**页面，你会得到你自己的 SendKey，请妥善保管。

4. 在`autoreport_wechat.py`中，把`posturl`中的`SendKey`替换为你在上一步中获得的 SendKey 即可实现消息推送。



## Linux配置定时任务：

1. 终端输入`crontab -e`，初次使用会让你选择一个编辑器编辑 crontab 文件，回车默认，此处以 nano 为例。

2. 在编辑界面最下面输入一行`3 0 * * * python3 脚本文件的路径` 即每天 00:03 执行一次脚本。例如`3 0 * * * python3 /home/ubuntu/autoreport.py`然后`Ctrl + X`再按`Y` ，再按回车保存。

3. 重启一下 cron，终端输入`/etc/init.d/cron restart` 



## Github Actions配置定时任务

1. 将本项目 fork 到你自己的仓库。

2. 进入自己 fork 的仓库，点击 Settings-> Secrets-> New Secrets 添加以下 3 个 Secrets。它们将作为应用启动时的命令行参数被传入程序。

| Secret Name | Secret Value |
| ----------- | -----------  |
| USERNAME    | 你的一卡通号  |
| PASSWORD    | 你的登录密码  |
| SCKEY       | Server酱的SCKEY     |

`SCKEY`不配置应该也可以，我没测试过。

3. 开启 Actions 并配置每日自动执行。Github Actions 默认处于关闭状态，前面都配置好后，请手动点击 Actions-> 左栏daily-report-> Run workflow-> Run workflow，执行一次工作流，验证是否可以正常工作。

如果不作任何配置， Actions 的执行策略默认是每天0点整触发运行，如果想要设置自己的运行时间，可编辑项目下 .github/workflows/main.yml 文件中第 10 行 cron 字段。

4. 如果项目有更新，可以在自己 fork 的仓库里创建一个 PR 拉取最新代码，具体教程请自行百度。


## 注： 

**1. 开发者不对使用脚本造成的任何后果负责。** 

**2. nogui版针对没有图形界面的服务器系统进行了适配，优化了Chrome无图形界面运行配置，并提供更详细的命令行输出。** 

**3. 出错的log可以在 /var/mail/你的用户名 文件里看到。**
