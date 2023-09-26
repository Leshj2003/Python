## Github配置ssh

配置SSH密钥对用于GitHub的步骤如下：

**第一步：检查本地是否已存在SSH密钥**

在终端（或Git Bash）中，执行以下命令检查是否已存在SSH密钥：

```bash
cd ~/.ssh
ls
```

如果您看到 `id_rsa` 和 `id_rsa.pub` 文件，说明已经存在SSH密钥，您可以跳过第二步。

**第二步：生成新的SSH密钥**

如果没有现成的SSH密钥，可以使用以下命令生成一个新的SSH密钥对，其中 `your_email@example.com` 替换为您的电子邮件地址：

```bash
ssh-keygen -t rsa -C "your_email@example.com"
```

按照提示一直按回车键，直到生成完毕。

**第三步：获取SSH公钥内容**

使用以下命令查看并复制SSH公钥的内容：

```bash
cd ~/.ssh
cat id_rsa.pub
```

将显示的公钥内容复制到剪贴板。

**第四步：将SSH公钥添加到GitHub账户**

登录到您的GitHub账户，然后按照以下步骤添加SSH公钥：

- 点击右上角的用户图标，选择 "Settings"（设置）。
- 在左侧导航栏中，选择 "SSH and GPG keys"（SSH和GPG密钥）。
- 点击 "New SSH key"（新的SSH密钥）。
- 在 "Title"（标题）字段中为密钥起一个描述性的名称（例如，"My Windows SSH Key"）。
- 在 "Key"（密钥）字段中，粘贴您之前复制的SSH公钥。
- 点击 "Add SSH key"（添加SSH密钥）。

**第五步：验证SSH连接**

在终端中，运行以下命令来验证SSH连接是否成功：

```bash
ssh -T git@github.com
```

如果一切设置正确，您应该会看到一条成功的消息，表示您已成功连接到GitHub。

配置完成后，您可以在使用Git时不再需要输入GitHub的用户名和密码，而是可以使用SSH协议来进行安全的通信。请注意，每次使用新的主机时，都需要重复这些步骤来配置SSH密钥，因为SSH密钥是与每台主机相关联的。

指定端口测试连接

```bash
ssh -p 9988 git@github.com
```

