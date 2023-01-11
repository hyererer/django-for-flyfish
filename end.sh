#!/bin/bash
echo "--------------------"
echo -e "\033[34m停止uWSGI\033[0m"
echo "--------------------"
source venv/bin/activate
uwsgi --stop histogram/pids/uwsgi/histogram-master.pid
if [ $? -eq 0 ]; then
	echo -e "\033[32muWSGI关闭成功\033[0m"
else
	echo -e "\033[32muWSGI关闭失败\033[0m"
fi
