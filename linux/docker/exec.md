Run a command in a running container

#### 在运行的容器内执行指定命令
    docker exec `容器id` ls
	
#### 进入容器内部
	# 使用exec进入容器内部,用ctrl+d或exit命令退出容器后,容器不会停止运行
	docker exec -it `容器id` bash