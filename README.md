# EEnotes
![alt text](docs/assets/2image.png)

面向清华大学电子系的学习笔记，按照如下方式整理


| 组 | 具体内容 |
| --- | --- |
| 数理基础 | 线性代数(1)、线性代数(2)、大学物理（热学） |
| 物理-电磁组 | 电磁场与电磁波、量子与统计、固体物理 |
| 电路组 | 电子电路与系统基础、模拟电路原理、数字逻辑与处理器基础、微波与光波技术基础 |
| 信号组 | 信号与系统、数字信号处理、通信与网络、随机过程 |
| 计算机组 | 程设基础、数据结构与算法、媒体与认知 |
| 科研与工具 | Matlab高级编程与工程应用、高等模拟电路原理、模拟数字数据转换器、OrCAD使用笔记、Latex基础教程 |

## 在线查看
部署于 https://note.weitao-jiang.cn

## 本地部署

建议使用 Python 3.10 及以上版本，并确保本机已安装 `git`。本项目当前使用 `MkDocs Material` 主题，以及 `git-revision-date-localized`、`pymdown-extensions`、`neoteroi.timeline` 等插件/扩展。

1. 创建并激活虚拟环境

```bash
python -m venv .venv
source .venv/bin/activate
```

2. 安装 MkDocs 及所需依赖

```bash
pip install mkdocs mkdocs-material mkdocs-git-revision-date-localized-plugin pymdown-extensions neoteroi-mkdocs
```

3. 在项目根目录启动本地预览

```bash
mkdocs serve
```

默认访问地址为：

```text
http://127.0.0.1:8000
```

4. 如需生成静态站点文件，可执行

```bash
mkdocs build
```

生成结果默认位于 `site/` 目录。

### 说明

- 配置文件为项目根目录下的 `mkdocs.yml`。
- 文档源文件位于 `docs/` 目录。
- `git-revision-date-localized` 插件依赖 Git 历史记录来显示页面更新时间，因此请尽量在完整克隆仓库后再本地构建。
