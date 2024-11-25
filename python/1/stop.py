import subprocess
import time
def kill_vins_processes():
    try:
        # 使用 sudo 调用 pkill 命令
        result = subprocess.run(['sudo', 'pkill', '-f', 'vins'], check=True, capture_output=True, text=True)
        print("pkill 输出:", result.stdout)
        print("成功终止所有包含 'vins' 的进程")
    except subprocess.CalledProcessError as e:
        print(f"终止过程中出现错误: {e.stderr}")


    # 等待片刻，再次确认是否还有相关进程
    time.sleep(1)  # 延迟1秒
    # 确认是否还有相关进程
    check_result = subprocess.run(['pgrep', '-f', 'vins'], capture_output=True, text=True)
    if check_result.stdout:
        print("仍有以下进程未被终止:", check_result.stdout)
    else:
        print("所有包含 'vins' 的进程已成功终止")

# 调用函数
kill_vins_processes()
