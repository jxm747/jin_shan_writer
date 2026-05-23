from pynput.keyboard import Controller, Key
import time
import os
import datetime

minute_time=60
deta=[f"start in {datetime.datetime.now()}"]

def get_articles_path():
    """获取 articles 文件夹的绝对路径"""
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 articles 文件夹的绝对路径
    articles_path = os.path.join(script_dir, "articles")
    return articles_path
def write_cn(thing):
    try:
        articles_path = get_articles_path()
        file_path = os.path.join(articles_path, f"{thing}.txt")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        speed=input("打字速度(字/分):")
        print("3秒后开始，请将光标移动到对应位置")
        time.sleep(3)
        for i in lines:
            for j in i:
                time.sleep(int(minute_time) / int(speed))
                keyboard.type(j)
    except Exception as e:
        print(f"输入的数据不正确，无法开始，报错:{e}")
        deta.append(f"error:{e},{datetime.datetime.now()},commod={writed}")

keyboard = Controller()

print("欢迎使用自动打字工具1.1.0 beta版\n制作人:一架惊吓猫航空的747(小红书)\n免责申明:仅供学习，请在法律范围内合法"
      "使用\n更新和用户手册请移步官网\n官网:https://share.htmlput.com/p/n47nuugxdy?lang=zh\n输入/help获取帮助")
while True:
    writed=input("\n>>>")
    if writed=="/help":
        print("-----自动打字工具帮助-----\n中文打字指令:/write cn +文章名称的每个字的拼音首字"
              "\n英文打字指令:/write en +文章名称的每个字的拼音首字\n事例(金色花):/write jsh"
              "\n若速度不准确请调节基准数，指令:/time +一分钟基准时间(默认60，运行可能会有延迟)\n事例:/time 60"
              "\n输入\"/print\"查看数据值和日志"
              "\n版本:1.1.2 beta\n"
              "---自动打字工具帮助-完-----")
    if writed[:5]=="/time":
        minute_time=writed[5:]
        print(f"完成，基准时间为{minute_time}")
        deta.append(f"set time {minute_time},{datetime.datetime.now()}")
    if writed=="/print":
        print(deta)
    elif writed.startswith("/write "):
        try:
            command = writed[7:]  # 去除 "/write " 前缀（7个字符）
            write_cn(command)
        except Exception as e:
            print("请重试1")
            deta.append(f"error:{e},{writed},{datetime.datetime.now()}")
    else:
        print("请重试2")
        deta.append(f"error:{writed},{datetime.datetime.now()}")