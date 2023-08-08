## git lfs配置

### [**配置**](https://help.gitee.com/enterprise/code-manage/code-hosting/large-file-manage/git-lfs#配置)

- 第一步：在Git仓库中为仓库设置相关配置：

```shellscript
$ git lfs install
```



> Tips:

> 这个命令会自动改变Git配置文件 .gitconfig，而且是全局性质的，会自动在配置文件中增加如下配置：
>
> ```shellscript
> [filter "lfs"]
> clean = git-lfs clean -- %f
> smudge = git-lfs smudge -- %f
> process = git-lfs filter-process
> required = true
> ```

- 第二步：选择要用LFS追踪的文件：

```shellscript
$ git lfs track "*.svg"
# 或者具体到某个文件
$ git lfs track "2.png"
$ git lfs track "example.lfs"
```



> Tips:

> 这个命令会更改仓库中的 .gitattributes配置文件(如果之前不存在这个文件，则会自动新建): 查看如下： $ cat .gitattributes *.svg filter=lfs diff=lfs merge=lfs -text* .png filter=lfs diff=lfs merge=lfs -text

好奇的同学可能要问了，如果想知道自己到底追踪了哪些文件，怎么办？

好办，一条命令解决！

通过 `git lfs ls-files` 可以随时查看正在被LFS追踪的文件：

```shellscript
$ git lfs ls-files
9a3c7dae41 * 1.png
d61cf5835a * 2.png
158213f90f * 3.svg
```



> git add file 之后文件才可能被追踪，也才能查看得到

可能还会有人好奇，如果不想LFS追踪某个文件，怎么办？

好办，还是一条命令解决：

```shellscript
$ git lfs untrack "1.png"
```



解决了好奇同学的问题，我们接着前面的第二步来，选择好需要LFS管理的文件之后，最好先保存一下配置：

- 第三步：保存并提交配置：

```shellscript
$ git add .gitattributes
$ git commit -m "add .gitattributes"
```



**配置总结：**

安装Git LFS之后，只需三步，即可在仓库中配置LFS功能，即：

```shellscript
#step 1
$ git lfs install

#step 2
$ git lfs track files

# step 3
$ git add .gitattributes
```



实际上，由于第一步是全局配置，所以执行一次即可，后续有其它仓库需要使用LFS，则不需要再次执行，除非中途取消了LFS配置。

> Tips： 运行 git lfs uninstall 即可取消LFS的全局配置