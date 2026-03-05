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

### 修改原理图大小

选中page右键，找到Properties

![alt text](assets/orcad_1772643042306_png)

选择合适大小即可

![alt text](assets/orcad_1772643065528_png)

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

### 导入自带库

自带库`C:\Cadence\Cadence_SPB_17.2\tools\capture\library`下，有多个OLB文件。一般电容在`Descrete.olb`

![alt text](assets/orcad_1772645168228_png)

??? note "库文件列表"
    | 库文件 | 器件数量 | 说明 |
    |---|---|---|
    | AMPLIFIER.OLB | 182 | 存放模拟放大器 IC，如 LM386、MAX457 等 |
    | ARITHMETIC.OLB | 182 | 存放逻辑运算 IC，如 54HC147、74HC147 等 |
    | ATOD.OLB | 618 | 存放 A/D 转换 IC，如 AD7580、ADC08031 等 |
    | BUS DRIVERTRANSCEIVER.OLB | 632 | 存放总线驱动 IC，如 74LS366、74LS440 等数字 IC |
    | CAPSYM.OLB | 35 | 存放电源、地、输入输出、标题栏等 |
    | CONNECTOR.OLB | 816 | 存放连接器，如 CON10、CONN PWR 2-P、HEADERS 等 |
    | COUNTER.OLB | 182 | 存放计数器 IC，如 54AC191、74F168 |
    | DISCRETE.OLB | 872 | 存放分立式元件，如电阻、电容、电感、开关、变压器等常用器件 |
    | DRAM.OLB | 623 | 存放动态存储器，如 TM2224、HM514256 等 |
    | ELECTRO MECHANICAL.OLB | 6 | 存放马达、断路器等电机类元件 |
    | FIFO.OLB | 177 | 存放先进先出资料暂存器，如 54LS222、67413 |
    | FILTRE.OLB | 80 | 存放滤波器类元件，如 LMF100、LTC1059 等 |
    | FPGA.OLB | - | 存放可编程逻辑器件，如 A1225A |
    | GATE.OLB | 691 | 存放逻辑门（含 CMOS 和 TTL） |
    | LATCH.OLB | 305 | 存放锁存器，如 4096、5475、54HC375 等 |
    | LINE DRIVER RECEIVER.OLB | 380 | 存放线驱动与接收器，如 74ACG241、ADM203 等 |
    | MECHANICAL.OLB | 110 | 存放机构图件，如 SIPSOC-10、ZIFSOC-8x2 等 |
    | MICROCONTROLLER.OLB | 523 | 存放单片机微处理器，如 80C51FA、AT89C52 等 |
    | MICRO PROCESSOR.OLB | 288 | 存放微处理器，如 80387、HD63C09 等 |
    | MISC.OLB | 1567 | 存放杂项图件，如电压表（METER V）、微处理器周边（Z80-PIO）等 |
    | MISCLINEAR.OLB | 365 | 存放线性杂项器件（未分类），如 14574、AD534、LM334 等 |
    | MISCMEMORY.OLB | 278 | 存放记忆体杂项器件（未分类），如 28F102、M28V101 等 |
    | MISCPOWER.OLB | 222 | 存放高功率杂项器件（未分类），如 A2919、EL7272、LT1161 等 |
    | MUXDECODER.OLB | 449 | 存放解码器，如 54F253、54HC153、74AC139 等 |
    | OPAMP.OLB | 610 | 存放运放，如 AD712、OP37、OPA660 等 |
    | PASSIVEFILTER.OLB | 14 | 存放被动式滤波器，如 271MT、NFM41、EMIFILTER 等 |
    | PLD.OLB | 355 | 存放可编程逻辑器件，如 14H4、20V8 等 |
    | PROM.OLB | 811 | 存放只读记忆体，如 24LC64、27C512 等 |
    | REGULATOR.OLB | 549 | 存放稳压 IC，如 78xxx、79xxx 等 |
    | SHIFTREGISTER.OLB | 610 | 存放移位寄存器，如 100341、4021 等 |
    | SRAM.OLB | 691 | 存放静态存储器，如 54S301、74C89 等 |
    | TRANSISTOR.OLB | 210 | 存放晶体管（含 FET、UJT、PUT 等），如 2N1070、2N1613 等 |

### 导入外部元件

在Snap EDA 或 Ultra librarian上下载文件的schematic 和 layout

#### case 1: 有 OLB 文件（一般是集成电路）
![alt text](assets/orcad_1772642640813_png)

![alt text](assets/orcad_1772642667314_png)

把文件夹复制到项目文件夹

![alt text](assets/orcad_1772642853103_png)

![alt text](assets/orcad_1772642870793_png)

#### case 2: 没有olb

1. Copy the footprint and padstack files from the zipped folder and paste them into your footprint directory. The default **footprint** directory is: `C:\Cadence\SPB_xx.x\share\pcb\pcb_lib\symbols`
1. Copy the STEP model from the zipped folder and paste it into your step directory. The default **STEP** directory is: `C:\Cadence\SPB_xx.x\share\local\pcb\step`

## 版图绘制

### 修改封装
Edit-Browser-Parts

![alt text](assets/orcad_1772709761670_png)

全选，Edit-Properties（ctrl+E）

![alt text](assets/orcad_1772709822508_png)

修改PCB Footprint

![alt text](assets/orcad_1772710036818_png)

改好一个点Copy，点列头全选整列，然后Paste

![alt text](assets/orcad_1772710078734_png)

### 新建版图


首先完成DRC检查，确保原理图没有错误。然后PCB-New Layout

![alt text](assets/orcad_1772709370882_png)

![alt text](assets/orcad_1772710928773_png)

成功进入allegro界面。

![alt text](assets/orcad_1772710965954_png)

### 放置元件

Place-Manual手动放置

![alt text](assets/orcad_1772711097876_png)

选好元件就可以放。

![alt text](assets/orcad_1772711119004_png)

第一次放可能出现`Cannot load symbol 'xxxx'`报错。需要导入元件封装库：

#### 导入封装库


顶部菜单Setup-User Preferences

![alt text](assets/orcad_1772711776641_png)

左侧菜单找Paths/Library

![alt text](assets/orcad_1772711814608_png)

添加以下目录：

1. `devpath`：`../PcbLibrary/device`
1. `padpath`：`../PcbLibrary/pads`
1. `psmpath`:`../PcbLibrary/psm`

然后ok，重新放置元件就不会报错了。

### 画边框

add-Rectangle

![alt text](assets/orcad_1772713468556_png)


选择`Board Geometry`和`Design_Outline`，画出边框。
![alt text](assets/orcad_1772713497740_png)