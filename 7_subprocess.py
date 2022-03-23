import subprocess

# shell=True: 打開終端機再執行(e.g. dir只有終端機看得到)
# 盡量不要使用shell=True

# shell=True, 帶入字串 "ls -al&rm -rf"
# shell=False, 帶入list ["pip", "install", "jieba"]
# 除了第一個以外, 都不會被當成執行檔執行, safe
command = ["/usr/local/bin/python3.9", "6_gui.py"]
# subprocess.run(command)

command = ["/usr/local/bin/pip3.9", "install", "jieba"]
# result = subprocess.run(command)
# print(result)

# 別寫encoding, 出來什麼就怎麼存
command =  ["/usr/local/bin/python3.9", "test.py"]
with open("log.txt", "w") as f1, open("err.txt", "w") as f2:
    result = subprocess.run(command, stdout=f1, stderr=f2)
    print(result)
