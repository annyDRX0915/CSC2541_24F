#!/bin/bash

# 创建一个目录用于本地安装
mkdir -p $HOME/local/sqlite
cd $HOME/local/sqlite

# 下载 SQLite 源码
wget https://www.sqlite.org/2023/sqlite-autoconf-3410000.tar.gz
tar -xzvf sqlite-autoconf-3410000.tar.gz
cd sqlite-autoconf-3410000

# 编译并安装到用户目录
./configure --prefix=$HOME/local/sqlite
make
make install
