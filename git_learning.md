## git基本远程推送

git add -A

git commit -m ""

git push -u origin master 



---



## git remote



| 命令                                      | 描述                               |
| ----------------------------------------- | ---------------------------------- |
| `git remote add <name> <url>`             | 添加一个远程仓库                   |
| `git remote -v`                           | 查看当前项目的所有远程仓库         |
| `git remote rm <name>`                    | 删除一个远程仓库                   |
| `git remote rename <old-name> <new-name>` | 将一个远程仓库的别名修改为新的别名 |
| `git remote set-url <name> <new-url>`     | 修改一个远程仓库的地址             |
| `git remote show <name>`                  | 显示一个远程仓库的详细信息         |
| `git remote prune <name>`                 | 删除一个远程仓库中已经不存在的分支 |

| 指令                         | 作用                           |
| ---------------------------- | ------------------------------ |
| git init                     | 初始化一个新的Git仓库          |
| git clone [url]              | 克隆一个Git仓库到本地          |
| git add [file]               | 将文件添加到暂存区             |
| git commit -m "message"      | 提交暂存区的文件到仓库         |
| git status                   | 查看工作区、暂存区和仓库的状态 |
| git diff                     | 查看工作区和暂存区的差异       |
| git diff [commit1] [commit2] | 查看两个提交之间的差异         |
| git branch                   | 查看本地分支列表               |
| git branch [name]            | 创建一个新的分支               |
| git checkout [name]          | 切换到指定分支                 |
| git merge [name]             | 将指定分支合并到当前分支       |
| git remote add [name] [url]  | 添加一个远程仓库               |
| git push [name] [branch]     | 将本地分支推送到远程仓库       |
| git pull [name] [branch]     | 从远程仓库拉取最新代码         |
| git log                      | 查看提交历史记录               |
| git reset --hard [commit]    | 恢复到指定提交                 |
| git stash                    | 暂存当前工作区的修改           |
| git stash apply              | 恢复最近一次暂存的修改         |



---

## git rebase

Git rebase是一种将提交从一个分支移动到另一个分支的操作。它可以被用来整合两个分支的提交历史，使得提交历史更加清晰、易于理解。

在rebase过程中，Git将选定一个基准提交（base commit），然后将需要移动的提交（source commit）应用到该基准提交上。这会使得源分支的提交历史变得更加线性，而不是分叉的。

rebase有两种主要的使用场景：

1. 合并分支：将两个分支的提交历史整合成一个线性的提交历史。

2. 更新分支：将一个分支的提交历史更新到另一个分支的最新提交。

使用rebase的步骤如下：

1. 切换到需要进行rebase的目标分支。

2. 运行git rebase [source-branch]命令，将需要移动的提交应用到目标分支上。

3. 解决可能出现的代码冲突。

4. 运行git rebase --continue命令，继续应用提交。

5. 重复步骤3和4，直到所有提交都被应用完毕。

注意：在进行rebase操作之前，最好先备份一下当前分支的提交历史，以便在出现问题时可以恢复到之前的状态。



---

## 同时关联gitee和github

您可以使用以下步骤同时关联 Gitee 和 GitHub：

1. 在本地计算机上设置 Git，如果您还没有设置，请在 Gitee 和 GitHub 上分别注册并创建仓库。

2. 将 Gitee 仓库克隆到本地计算机，使用 Gitee 的 HTTPS 或 SSH 链接进行克隆。例如，

   ```bash
   $ git clone https://gitee.com/yourname/repository.git
   ```

3. 将 GitHub 仓库添加为远程源。打开终端，并使用以下命令添加远程源

   ```bash
   $ git remote add github https://github.com/yourname/repository.git
   ```

   注意：确保您已经创建了与 Gitee 仓库相同名称的 GitHub 仓库。

4. 现在，您可以将代码推送到 Gitee 和 GitHub。

   ```bash
   $ git push origin master // 推送代码至Gitee
   $ git push github master // 推送代码至GitHub
   ```

5. 如果您想将某个已提交的版本标记为新的发布版本，在将其推送至 Gitee 和 GitHub 之前，必须在本地和远程仓库中为其添加一个标记。以下是示例代码。

   ```bash
   $ git tag v1.0.0 // 为发布版本添加标签
   $ git push origin v1.0.0 // 将标签推送到Gitee
   $ git push github v1.0.0 // 将标签推送到GitHub
   ```



---



## git中的^和~

在 Git 中，^ 和 ~ 符号可以用来引用某个 commit 的父提交。

- 符号 ^ 可以用在 commit SHA 的后面，来引用其父提交。例如，HEAD^ 就是当前提交的父提交，HEAD^^ 就是当前提交的爷爷提交，HEAD^3 就是当前提交的第三个父提交（只有 merge commit 才会有多个父提交）。
- 符号 ~ 也可以用在 commit SHA 的后面，表示沿着父提交链向上数的位置。例如，HEAD~3 表示当前提交的第三个父提交，等价于 HEAD^^^。

可以使用这些符号来引用特定的提交，进行 Git 操作，比如 git checkout、git diff 等等。

---

## HEAD

在git中，HEAD是一个指针，它指向当前所在分支的最后一次提交。也可以说，HEAD是当前工作目录所处的提交版本。

当我们在git中进行提交时，HEAD指针会随之移动到最新的提交版本。如果我们在某个分支上进行切换，HEAD指针也会移动到该分支的最新提交版本。

除了指向当前所在分支的最新提交版本，HEAD还可以指向其他提交版本，例如，我们可以使用git checkout命令将HEAD指向某个特定的提交版本。

需要注意的是，HEAD指针只能在本地仓库中使用，它不会被推送到远程仓库中。因此，当我们在不同的本地仓库中进行操作时，HEAD指针可能会指向不同的提交版本。

---

## git的撤销变更

在Git中，撤销变更的方式有以下几种：

1. git reset(本地仓库)
使用git reset命令可以撤销某个commit，并将指针移回到上一个commit。这个操作会清除提交历史，并且会丢失所有被撤销的提交所做的修改。具体操作如下：

```bash
# 撤销最后一次提交
git reset HEAD~1

# 撤销最后两次提交
git reset HEAD~2

# 撤销到特定的提交
git reset COMMIT_ID
```

2. git revert(远程仓库)
使用git revert命令可以撤销某个commit，并创建一个新的commit来记录这个撤销操作。这个操作会保留提交历史，并且不会丢失任何提交所做的修改。具体操作如下：

```bash
# 撤销最后一次提交
git revert HEAD

# 撤销指定的提交
git revert COMMIT_ID
```

3. git checkout
使用git checkout命令可以撤销工作区中的修改，恢复到上一次提交的状态。这个操作不会修改提交历史，也不会删除任何提交。具体操作如下：

```bash
# 恢复某个文件到上一次提交的状态
git checkout FILENAME
```

需要注意的是，这个操作会覆盖当前工作区中的修改，因此在执行之前需要先保存修改。如果要恢复所有文件到上一次提交的状态，可以使用以下命令：

```bash
# 恢复所有文件到上一次提交的状态
git checkout .
```

4. git stash
使用git stash命令可以将当前工作区中的修改存储到一个临时区域中，以便稍后恢复。这个操作不会修改提交历史，也不会删除任何提交。具体操作如下：

```bash
# 存储当前工作区中的修改
git stash

# 恢复最近一次存储的修改
git stash apply

# 恢复最近一次存储的修改，并从存储列表中删除
git stash pop
```

需要注意的是，如果在存储修改之后又进行了新的修改，那么恢复修改时可能会出现冲突，需要手动解决。因此在执行之前需要先保存修改。





---

* 遇到error: RPC failed; HTTP 413 curl 22 The requested URL returned error: 413

```bash
git remote set-url origin git@gitee.com:....
```