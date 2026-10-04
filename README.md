---
comments: true
---
# EEnotes
![alt text](docs/assets/2image.png)

面向清华大学电子系的学习笔记，按照“课程组 / 课程 / 章节”三级结构整理。


| 组 | 具体内容 |
| --- | --- |
| 数理基础组 | 线性代数(1)、线性代数(2)、大学物理（热学） |
| 物理-电磁组 | 电磁场与电磁波、量子与统计、固体物理 |
| 电路组 | 电子电路与系统基础、模拟电路原理、数字逻辑与处理器基础、微波与光波技术基础 |
| 信号组 | 信号与系统、数字信号处理、通信与网络、随机过程、统计信号处理 |
| 计算机组 | 程设基础、数据结构与算法、媒体与认知 |
| 科研与工具组 | Matlab高级编程与工程应用、高等模拟电路原理、模拟数字数据转换器、电源管理芯片、OrCAD使用笔记、Latex基础教程、办事指南 |

课程文档位于 `docs/`，其目录约定如下：

```text
docs/
├── xx组/
│   └── course-slug/
│       ├── 01-第一章.md
│       ├── 02-第二章.md
│       └── ...
├── assets/
└── index.md
```

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
python scripts/chatjwt_build.py
```

生成结果默认位于 `site/` 目录。

### 说明

- 配置文件为项目根目录下的 `mkdocs.yml`。
- 文档源文件位于 `docs/` 目录；新增内容时请继续使用“xx组 / 课程文件夹 / 章节 Markdown”结构。
- `git-revision-date-localized` 插件依赖 Git 历史记录来显示页面更新时间，因此请尽量在完整克隆仓库后再本地构建。

## chatJWT 小精灵

笔记页复用主页的 chatJWT 组件，DeepSeek Token、语气、自动概括和请求额度统一在主页 `/admin_chatjwt` 配置。浏览笔记时会主动概括，并可以继续提问。

每次构建后执行 `python scripts/chatjwt_build.py`，从导航中列出的已构建公开页面提取正文，生成 `site/chatjwt-index.json`，并移除旧聊天组件。部署工作流也会执行该步骤。未列入公开导航的文档不会进入索引。

部署笔记更新后，在主页 chatJWT 设置中点击“同步笔记知识”，即可更新 RAG；同步失败时保留已有索引。前端从主页加载组件，跨域接口只允许本站域名，Token 始终保留在主页后端。
