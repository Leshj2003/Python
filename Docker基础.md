## Docker基础

# 1 Docker 简介



## 1.1 Docker 是什么？

docker是一个开源的应用容器引擎。 

## 1.2 容器是什么？

容器是一种轻量级的虚拟化技术 ，它是一个由应用运行环境、容器基础镜像组成的集合。
以 Web 服务 Nginx 为例，如下图所示：Nginx 容器是由 Nginx 主程序、Nginx 运行依赖组件（gcc、pcre、openssl）、CentOS 7 基础镜像组成。（注：CentOS 7 基础镜像并非完整的操作系统镜像，只是操作系统的基础文件和库文件）
![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/814a32ebc46d48f2acb01966a264d394~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)



## 1.3 容器与虚拟机的区别

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46533aab8ca74c48a0e784a1d0f9e8f9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

1. **启动速度**：每个虚拟都机是一个完整的操作系统包括操作系统和内核，所以它是一个重量级的系统；而容器是轻量级的，因为容器只打包了操作系统的基础文件和库文件、还有应用程序及所有的依赖，他的运行速度就如同在系统中创建一个进程一样快，所以启动速度较快。
2. **运行性能**：由于虚拟机增加了虚拟化层用于虚拟化硬件，势必会增加一定的开销，所以运行性能有所损失；而容器是直接运行在物理操作系统上的，他本身与系统上其他进程并没有太大区别，所以运行性能是接近原生的。
3. **磁盘占用**：虚拟机是一个完整的操作系统，是 GB 级别的，而容器只包含了一些系统启动的必要组件和程序依赖，是 MB 级别的。
4. **数量**：运行一个操作系统的开销较大，运行一个进程的开销较小，同样的服务器资源可以运行更多的容器。
5. **隔离性**：虚拟机是一个完整的操作系统级别的隔离，要比容器好很多；容器是进程级别的隔离，隔离的不彻底，因为多个容器之间使用的是同一个宿主机的操作系统内核。
6. **封装速度**：虚拟机封装会包含操作系统，封装速度比较慢，容器只封装操作系统的基础文件和库文件、应用程序、依赖，封装速度较快。



## 1.4 Docker 和容器的关系

容器是一种虚拟化技术，docker 是实现容器的一种工具，我们称它为容器引擎；
可以驱动容器的引擎还有 podman、containerd 等，docker 是目前市面上应用范围最广的一种容器引擎。 

# 2 安装 Docker

在 CentOS 7 系统上安装 docker

```shell
shell复制代码yum install -y yum-utils device-mapper-persistent-data lvm2 && \
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo && yum makecache fast && \ 
yum -y install docker-ce && \
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://j6o4qczl.mirror.aliyuncs.com"]
}
EOF
systemctl daemon-reload
systemctl enable docker
systemctl restart docker
```



# 3 使用 Docker 启动一个容器

执行以下命令，启动一个 Nginx 容器

```shell
shell复制代码docker run -d --name nginx_test  nginx

注释：
-d					#后台运行
--name			#自定义容器名称
nginx				#容器镜像
```

使用 docker ps 可以看到有一个名为 nginx_test 的容器在运行；
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a589b28bd3b740948fa2d9d8323476c6~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

进入容器查看服务

```shell
shell复制代码docker exec -it nginx_test bash

注释：
-it		#打开终端交互（进入容器操作）
nginx_test	#容器名称
bash	#执行容器使用的 shell, bash 或 sh。
```

执行命令后，shell 端的主机名变成了随机字段串，说明进入到了容器内部；
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fff8ff63d5429c93b6b713bc592f7e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

在 Nginx 容器中可以看出 Nginx 的服务和端口都是正常的
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/968e3e67d17c4bfd96f70766c251e748~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

键入 `exit` 回到宿主机，执行 `netstat -lnt`** **查看宿主机的端口；
如下图所示，在宿主机并没有 Nginx 的端口，这是因为容器中的端口并没有映射到宿主机上，所以在宿主机无法访问到 Nginx 的服务。
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c655a2e27794c8a8eab0f59fb07b377~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp) 

## 3.1 如何访问容器服务

我们在运行容器时使用 -p 参数将容器端口映射到宿主机端口

```shell
shell复制代码docker run -d --name nginx_test -p 8080:80 nginx

注释：
-p 8080:80	# 8080 代表宿主机端口，80 代表容器端口
```

容器运行后，在宿主机执行 `netstat -lnt` 可以看到，宿主机已经监听了 8080 端口;
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/461e9a5bfc334478994a7aab756b88ff~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
查询服务器的 IP，使用 curl 命令访问 IP 地址+端口，可以返回 Nginx 服务的信息，说明可以正常访问 Nginx 服务了；
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d13a0e88e8e44c59b5808db182ba6ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

当然，用浏览器一样可以得到 Nginx 页面信息。
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eae29d443f1420ea6d22efe3483c8bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp) 

## 3.2 如何将容器内数据持久化存储

我们先来做个测试，测试内容是修改容器内的文件，然后删除容器、重建容器，查看文件是否会保持修改后的状态。
**第一步、修改 Nginx 容器的 index.html 查看是否生效**
我们尝试通过修改 Nginx 的 index.html 文件来更换页面信息；

```shell
shell复制代码#先进入 nginx_test 容器中；
docker exec -it nginx_test bash

#然后切换到 Nginx 的 html 目录
cd nginx/html

#vi 打开 index.html
vi index.html

#输入一段文本，并保持退出编辑
This is the demo page.
```

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dba0fc4a3d664f7b92210b7e0f11f403~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

退出容器，使用 curl 命令访问 Nginx 服务
`curl 10.1.13.130:8080`
可以返回我们更换的文本内容，index.html 修改完成。
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b82645603bd40fe9b876ec516899c3f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

**第二步、删除 Nginx 容器，然后重新创建 Nginx， 观察 index.html 内容是否保持修改后状态**

```shell
shell复制代码#删除 nginx_test 容器
docker rm -f nginx_test

#重新创建 nginx_test
docker run -d --name nginx_test -p 8080:80 nginx
```

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f73714a5ffe04873a206eb17d103b20b~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

完成重建后，使用 curl 命令访问 nginx 服务
`curl 10.1.13.130:8080`
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5578a3f1fe04343b2eee5bbfaa35e87~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
可见，curl 返回了 Nginx 默认的页面信息，并不是我们修改的内容，这是因为我们删除了容器，容器内的所有文件都一同删除了。如果想在删除容器时，保持指定文件或目录不被删除，该怎么做呢？
**将宿主机的目录映射到容器目录，我们称这个操作为：持久化存储**

在创建容器时使用 -v 参数将宿主机目录映射到容器目录

```shell
shell复制代码docker run -d --name nginx_test -p 8080:80 -v /data/nginx:/opt/nginx/html nginx

注释：
-v /data/nginx:/opt/nginx/html #/data/nginx 是宿主机目录，/opt/nginx/html 是容器目录
```

然后我们用同样的方法，在 Nginx 容器中新建一个 index.html，内容自定义，然后删除容器、重建容器；
操作步骤如下图：
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6349b6e60574a908a12861c1ca5f8bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
可以发现，index.html 文件会保持自定义的内容；
这是因为 index.html 创建到了宿主机的目录 /data/nginx 中，宿主机的目录 /data/nginx 映射到了容器中的 /opt/nginx/html 目录，即使删除容器，宿主机的文件也不会删除，再次创建容器仍然映射原目录，使得文件持久化存储。 

# 4 自己构建一个镜像

我们在创建运行容器时使用命令： `docker run -d nginx_test  nginx `
命令最后的 “nginx” 是 Docker官方仓库提供的 Nginx 镜像，我们也可以自己构建一个镜像来使用。
构建镜像需要使用 dockerfile 文件，我们以 Nginx 为例，编写一个 Nginx 镜像的 dockerfile：
`vi dockerfile`

```shell
shell复制代码FROM centos:7.9.2009

WORKDIR /opt

ADD nginx-1.24.0.tar.gz /opt


RUN yum install -y nc net-tools gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel && \
yum clean all && \
rm -rf /tmp/* rm -rf /var/cache/yum/* && \
cd /opt/nginx-1.24.0 && \
./configure --user=nobody --group=nobody --prefix=/opt/nginx --with-http_gzip_static_module --with-http_ssl_module --with-stream && \
make && make install && \
rm -rf /opt/nginx-1.24.0

CMD /opt/nginx/sbin/nginx && tail -f /dev/null
```

> 注释：
>
> FROM	#构建镜像需要一个基础镜像，centos:7.9.2009 就是一个基础镜像
>
> WORKDIR	#指定工作目录
>
> ADD		#将宿主机目录的文件拷贝到容器中并自动解压，宿主机的文件与 dockerfile 位于相同目录中
>
> RUN		#在基础镜像上要执行的命令
>
> CMD		#指定启动容器时执行的命令

**构建镜像**

```shell
shell复制代码# 在 dockerfile 同目录下执行命令
docker build -t nginx:v2 .

注释：
-t	#构建镜像的名称
. 	#表示 dockerfile 文件在当前目录下
```

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eaee8c7ff5545d0b2e1d9050142cfe7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

构建后的镜像名为 nginx:v2 ,在创建容器时可以这样使用:
`docker run -f nginx_test nginx:v2` 

# 5 总结 Docker 命令

**启动容器**
`docker run -d --name nginx_test -p 8080:80 -v /data/nginx:/opt/nginx/html nginx`

> 参数： -d		#后台运行
>
> -p		#端口映射，-p 8080:80， 8080 表示宿主机端口，80 表示容器端口
>
> -v		#目录映射，-v /data/nginx:/opt/nginx，/data/nginx表示宿主机目录，/opt /nginx，/opt/nginx表示容器目录
>
> --name	#设置容器名称
>
> nginx		#容器镜像

**查看正在运行的容器**
`docker ps`

> 参数： -a		#查看运行的所有容器，包括运行状态和停止状态的容器

**启动、停止、重启容器**
`docker start nginx_test`		#启动 Nginx 容器
`docker stop nginx_test`		#停止 Nginx 容器
`docker restart nginx_test`	#重启 Nginx 容器

**进入容器**
`docker exec -it nginx_test bash`

> 参数： -it		#打开终端交互（进入容器操作）

**删除运行的容器**
`docker rm -f nginx_test`

**查看容器镜像**
`docker images`

**删除容器镜像**
`docker rmi nginx:latest`
`docker rmi d6454d54b3d9 (IMAGE ID)`

**下载容器镜像**
`docker search nginx`
`docker pull nginx`

**镜像导出为文件**
`docker save nginx:latest nginx.tar`

**从文件导入镜像**
`docker load < nginx.tar`

**编译镜像**
`docker build -t nginx:v1 .` 

# 6 容器编排  docker-compose



## 6.1 docker-copose 介绍

- docker-compose 是一个容器编排工具（自动化部署、管理）;
- 它用来在单台 Linux 服务器上运行多个 Docker 容器;
- docker-compose 使用YAML文件来配置所有需要运行的 Docker 容器，该 YAML 文件的默认名称为 docker-compose.yml 

## 6.2 docker-compose 安装

```shell
shell复制代码curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose version
```



## 6.3 使用 docker-compose 启动一个容器

以下是 docker-compose.yml 的内容

```shell
shell复制代码version: '2.1'
services:
  nginx:
    image: nginx:latest
    container_name: nginx_test
    ports:
      - 8080:80
    volumes:
      - /opt/nginx:/opt/nginx/html
```

> 参数： compose		文件格式的版本，恒定为 2.1 services		标签下可以定义多个类似 nginx 这样的服务 container_name 	服务定义， nginx_test 是容器的名称 image	 	nginx容器所使用的镜像 ports			定义端口映射，本例将容器内的 80 端口映射到宿主机的 8080 端口 volumes		定义目录映射，本例将容器内的 /opt/nginx/html 目录映射到宿主机的 /opt/nginx 目录

**启动容器**
在 docker-compose 所在目录执行
`docker compose up -d`

> *参数：*
>
> *up	表示启动*
>
> *-d	表示后台运行*
>
> *-f	指定 docker-compose 文件位置 docker-compose -f /root/docker-compose/docker-compose.yml up -d*



## 6.4 Dockerdocker-compose 命令总结

在 docker-compose 所在目录执行

**启动容器**
`docker-compose up -d`

**停止容器**
`docker-compose down`

**重启容器**
`docker-compose restart`

**重载 docker-compose.yml **
`docker-compose up  --force-recreate -d`



## 6.5 docker-compose 创建多个容器

使用 docker-compose 启动 Nginx 和 Redis 两个容器：
docker-compose.yml 内容如下：

```shell
shell复制代码version: '2.1'
services:

  nginx:
    image: nginx:latest
    container_name: nginx_host1
    ports:
      - 8081:80
    volumes:
      - /opt/nginx:/opt/nginx/html
    networks:
      - host1-network

  redis:
    image: redis:latest
    container_name: redis_host1
    ports:
      - 63790:6379
    networks:
      - host1-network

networks:
  host1-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 192.168.11.0/24
          gateway: 192.168.11.254
```

> 参数：
>
> networks	定义容器网络，host1-network 为定义的网络名称，
>
> config 	网络配置，subnet 代表网段，gateway 代表网关。

执行创建命令
`docker-compose up -d`
可以看到成功创建了 Nginx 和 Redis 两个容器
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b730814610e54209857d802d373021f4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)

可以进入 nginx_host1 容器查看一下端口和 IP
![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61098b307ace44cb9ee39f1c804dc28f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
上图可见，nginx_host1 的 IP 为：192.168.11.2 ,符合 docker-compose 中定义的 192.168.11.0/24 网段；
如果访问 Redis 可以直接使用docker-compose 定义的 redis_host1 容器名访问即可。