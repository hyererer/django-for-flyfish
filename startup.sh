#!/bin/bash
echo "--------------------"
echo -e "\033[34m创建必要的目录和文件\033[0m"
echo "--------------------"
if [ ! -d "histogram/logs/uwsgi" ]; then
	mkdir -pv histogram/logs/uwsgi
fi
if [ ! -d "histogram/pids/uwsgi" ]; then
        mkdir -pv histogram/pids/uwsgi
fi
if [ ! -f "histogram/logs/uwsgi/histogram.log" ]; then
        touch histogram/logs/uwsgi/histogram.log
fi
echo -e "\033[32m创建完成\033[0m"
echo "--------------------"
echo -e "\033[34m运行uWSGI\033[0m"
echo "--------------------"
source venv/bin/activate
cd histogram/
uwsgi --ini uwsgi.ini
