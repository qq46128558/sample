Return low-level information on a container or image

#### 按模版输出信息
	# 输出Key为Image的信息
	docker inspect -f {{.Image}} a8c
		sha256:0346349a1a640da9535acfc0f68be9d9b81e85957725ecb76f3b522f4e2f0455
	# 输出NetworkSettings下IPAddress的信息
	docker inspect -f {{.NetworkSettings.IPAddress}} a8cff0eabf3f
		172.17.0.4
		
#### 查看Docker的底层信息
    docker inspect `镜像id`
    docker inspect f1b
    
#### 查看容器IP
    docker inspect `容器id`|grep "IPAddress"
    