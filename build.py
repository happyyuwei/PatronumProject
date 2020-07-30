"""
本脚本用于部署Patronum的后台服务。
构建步骤如下：
1. pull 最新的源码
2. 构建后端部分。使用命令 mvnw clean package
3. 发布到部署路径
"""


import os
import shutil
import subprocess

"""[summary]

该工程文件如下

Patronum
    |----patronum  后端工程源码
    
    |----dist 部署好的运行文件
        |----patronum.jar

    |----build.py 部署代码

    |----其他，如.gitignore



"""

# 1. 拉取最新源码

# 进入后端工程
os.chdir(os.path.join(".", "patronum"))
# pull
child = subprocess.Popen("git pull", shell=True)
child.wait()
print("Spring boot backend source code pull.")


# 2. 构建后端
# 使用mvnw构建后端
child = subprocess.Popen("mvnw clean package", shell=True)
child.wait()
print("Spring boot backend built.")
# 回到根目录
os.chdir("../")


# 3. 将该构建的jar移至dist目录
shutil.copyfile(os.path.join(".", "patronum", "target",
                             "patronum-0.0.1-SNAPSHOT.jar"), os.path.join(".", "dist", "patronum.jar"))
print("backend Jar file moved to dist")
