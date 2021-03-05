<!--
 * @copyright: zwenc
 * @email: zwence@163.com
 * @Date: 2021-03-05 11:33:37
 * @FilePath: \python-init\README.md
-->
# python-init
python 通用库

## 一、tools/ArgsGet.py

### 功能
    解释输入参数

### 使用
* 代码
    ```python
    from tools.ArgsGet import ArgsGet         # 参数获取
    a = ArgsGet().get()
    print(a.param1, a.param2)
    ```

* 启动
    ```shell
    python main.py --param1 张 --param1 三
    ```

* 输出
    ```shell
    张三
    ```

## 二、tools/LoggingControl.py

### 功能
    自动把日志写入到`log`文件夹中，以程序启动时间命名。超过10个日志文件，会把最旧的自动删除掉

### 使用

* 代码
    ```python
    from tools.LoggingControl import logger   # 日志系统，日志会自动输入到log/文件夹中
    logger.info("asf")
    logger.warning("asdfa")
    logger.error("asdfasdf")
    ```
* 输出
    ```shell
    2021-03-05 12:40:27,401 - system - [main.py file line:15] - INFO - asf
    2021-03-05 12:40:27,401 - system - [main.py file line:16] - WARNING - asdfa
    2021-03-05 12:40:27,401 - system - [main.py file line:17] - ERROR - asdfasdf
    ```

## 三、tools/SystemInfo.py

    记录程序启动时间和程序名称

## 四、tools/Decorator.py

    一些工具构造器，里面目前只实现了`单例`构造器

### 使用
    ```
    @Singleton 
    def your_function_or_class():
        pass
    ```
