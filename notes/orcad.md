!!! danger "说明"
    这个OrCAD太难用了，我要在这里记录一些学到的方法，不会很成体系，以后有机会再整理一下。

## 新建项目

先把这堆文件复制过来，清空Layout和Schemetic文件夹

![alt text](assets/orcad_1772622370347_png)

![alt text](assets/orcad_1772621625093_png)

打开Capture CIS

![alt text](assets/orcad_1772621647030_png)

选择new

![alt text](assets/orcad_1772621726228_png)

在Schemetic文件夹下新建项目

![alt text](assets/orcad_1772622494241_png)

现在的文件结构：

![alt text](assets/orcad_1772622550930_png)

| 文件后缀 | 说明 |
|----------|------|
| `.DSN`   | PSpice 原理图设计文件，包含电路元件、连线和网名等信息 |
| `.DSNLCK`| 设计锁文件，用于防止同一个工程被多实例修改，通常不需要手动操作 |
| `.OPJ`   | OrCAD 项目文件，记录整个工程的原理图、仿真设置和库路径，双击即可打开整个项目 |
| 文件夹（PSpiceFiles） | 仿真生成的文件存放目录，包括输出结果、波形文件、netlist 等 |

## 导入已有库

![alt text](assets/orcad_1772621971293_png)

FILE / Open / Library，选择库文件（`.olb`），点击Open

![alt text](assets/orcad_1772622640144_png)

## 原理图绘制

### 新建原理图

点File-New-Design
![alt text](assets/orcad_1772622792391_png)

点左侧的`.dsn`文件，右键New-Schemetic
![alt text](assets/orcad_1772641466842_png)
### 绘制用的快捷键

| 快捷键 | English | 中文说明 |
|---|---|---|
| `P` | PSpice Component | 放置 PSpice 元件 |
| `W` | Wire | 绘制导线 |
| `B` | Bus | 绘制总线 |
| `J` | Junction | 添加连接点 |
| `E` | Bus Entry | 总线入口（总线与信号线连接） |
| `N` | Net Alias | 为网络命名 |
| `U` | NetGroup | 创建网络组 |
| `F` | Power | 放置电源符号 |
| `G` | Ground | 放置接地符号 |
| `X` | No Connect | 标记未连接引脚 |
| `Shift+G` | Pin | 放置引脚 |
| `Shift+J` | Pin Array | 放置引脚阵列 |
| `Shift+X` | IEEE Symbol | 放置 IEEE 标准符号 |
| `T` | Text | 插入文本 |
| `Shift+L` | Line | 绘制直线 |
| `Shift+R` | Rectangle | 绘制矩形 |
| `Shift+F` | Ellipse | 绘制椭圆 |
| `Shift+T` | Elliptical Arc | 绘制椭圆弧 |
| `Shift+Q` | Bezier Curve | 绘制贝塞尔曲线 |
| `Y` | Polyline | 绘制多段线 |