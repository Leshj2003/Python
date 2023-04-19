## git基本远程推送

git add -A

git commit -m ""

git push -u origin master 



| 命令                                      | 描述                               |
| ----------------------------------------- | ---------------------------------- |
| `git remote add <name> <url>`             | 添加一个远程仓库                   |
| `git remote -v`                           | 查看当前项目的所有远程仓库         |
| `git remote rm <name>`                    | 删除一个远程仓库                   |
| `git remote rename <old-name> <new-name>` | 将一个远程仓库的别名修改为新的别名 |
| `git remote set-url <name> <new-url>`     | 修改一个远程仓库的地址             |
| `git remote show <name>`                  | 显示一个远程仓库的详细信息         |
| `git remote prune <name>`                 | 删除一个远程仓库中已经不存在的分支 |