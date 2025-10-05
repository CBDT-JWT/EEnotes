!!! info
    这是面向电子系学生科协学培部的教学文档，由江玮陶编写，部署于此。

## 序言

## 安装Latex
LaTeX作为学术排版的首选工具，主要有三种使用方式，适合不同需求的用户：

1. **Overleaf在线编辑**  
   无需安装任何软件，在清华自己的overleaf站点上(overleaf.tsinghua.edu.cn)注册后即可使用。平台提供各种期刊模板，支持实时协作和版本控制，适合快速入门和团队合作。编译通过点击"Recompile"按钮完成，PDF结果即时显示在右侧面板。

2. **Windows本地安装TeX Live+VSCode**  
   - 下载Texlive（https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/，约4GB），挂载后运行`install-tl-windows.bat`安装
   - VSCode安装"LaTeX Workshop"插件，在`settings.json`中添加编译链配置（需指定xelatex/pdflatex路径）

3. **WSL环境安装TeX Live+VSCode**  
   - 启用WSL后安装Ubuntu，通过`sudo apt install texlive-full`或挂载Windows本地的TeX Live ISO安装
   - VSCode安装"Remote - WSL"插件连接到wsl即可使用
   
安装时可能会遇到在这个页面卡住的现象：

![安装卡住了](assets/34a7aaa5a3148f0e12a63c22c8a397942098abc9.png){: style="display: block; margin: auto; width: 60%;" }

这里其实是程序在等待某种输入，只要多按几次`Enter`就可以了（x


WSL上的Latex编译速度比原生Windows快3-5倍，特别适合大型文档。

![Wsl还是快人一步](assets/b66fcc9ee585c92b4cd2e3692e28718d88c1371c.png){: style="display: block; margin: auto; width: 60%;" }


三种方式中，Overleaf最适合协作场景，Windows本地安装适合单机稳定使用，而WSL方案在保持Windows生态的同时获得Linux编译性能优势。

??? tip "如果你是电子系学生科协成员"
    感谢科协软件部，我们拥有自己的overleaf系统，无需使用阉割版的清华overleaf或者花钱氪金会员就可以在[科协overleaf](overleaf.eesast.com )使用协作功能。如果你需要使用这个功能，请发邮件给[我](mailto:jiangwt23@mails.tsinghua.edu.cn)，主题为“申请overleaf账户”，或者使用任何其他你确信可以联想到我的方式告知你的邮箱。申请后，你将收到一封确认邮件，进入并设置密码即可使用在线协作。
    注册账号后需要先按照指引创建一个空项目。然后即可在projects界面打开项目邀请加入协作了。

## 新建文档

## 公式和代码
### 公式
### 代码框
## 图形和表格
### 插入图形
### 使用tikz绘制图形
#### circuitikz与示意图
#### pgfplots绘制图表
### 表格