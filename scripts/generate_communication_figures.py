"""Generate the explanatory figures used by communication-and-networks.md.

The plots follow the examples and parameter choices in the course slides.  Run
this script from the repository with a Python environment that provides NumPy
and Matplotlib, for example::

    conda run -n dsp python scripts/generate_communication_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from matplotlib.patches import FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "assets"

BG = "#FAFBFC"
INK = "#243447"
MUTED = "#667085"
GRID = "#D9DEE7"
PURPLE = "#5B4B8A"
TEAL = "#2A9D8F"
CORAL = "#E76F51"
GOLD = "#E9C46A"
BLUE = "#3B6FB6"
PALE_PURPLE = "#EAE6F4"
PALE_TEAL = "#DDF1ED"
PALE_CORAL = "#F8E2DC"

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial Unicode MS", "STHeiti", "DejaVu Sans"],
        "axes.unicode_minus": False,
        "font.size": 11.5,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11.5,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "figure.facecolor": BG,
        "axes.facecolor": BG,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "mathtext.fontset": "dejavusans",
    }
)


def save(fig: plt.Figure, filename: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUT_DIR / filename,
        dpi=180,
        facecolor=BG,
        bbox_inches="tight",
        pad_inches=0.16,
    )
    plt.close(fig)


def clean_axes(ax: plt.Axes, grid: bool = True) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    if grid:
        ax.grid(True, color=GRID, linewidth=0.8, alpha=0.75)
        ax.set_axisbelow(True)


def midrise_quantize(x: np.ndarray, levels: int) -> np.ndarray:
    step = 2.0 / levels
    y = np.floor((np.clip(x, -1, 1) + 1) / step) * step - 1 + step / 2
    return np.clip(y, -1 + step / 2, 1 - step / 2)


def mu_compand(x: np.ndarray, mu: float = 255.0) -> np.ndarray:
    return np.sign(x) * np.log1p(mu * np.abs(x)) / np.log1p(mu)


def mu_expand(y: np.ndarray, mu: float = 255.0) -> np.ndarray:
    return np.sign(y) * np.expm1(np.abs(y) * np.log1p(mu)) / mu


def a_compand(x: np.ndarray, a: float = 87.6) -> np.ndarray:
    u = np.abs(x)
    y = np.empty_like(u)
    small = u < 1 / a
    y[small] = a * u[small] / (1 + np.log(a))
    y[~small] = (1 + np.log(a * u[~small])) / (1 + np.log(a))
    return np.sign(x) * y


def figure_quantization() -> None:
    x = np.linspace(-1, 1, 4001)
    levels = 8
    q_uniform = midrise_quantize(x, levels)
    compressed = mu_compand(x)
    q_nonuniform = mu_expand(midrise_quantize(compressed, levels))

    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.2), constrained_layout=True)
    panels = [
        (axes[0], q_uniform, "均匀量化", CORAL),
        (axes[1], q_nonuniform, r"$\mu$ 律压扩后的非均匀量化", TEAL),
    ]
    for ax, q, title, color in panels:
        ax.plot(x, x, color=MUTED, linestyle="--", linewidth=1.2, label="理想映射")
        ax.plot(x, q, color=color, linewidth=2.2, label=r"重建值 $Q(x)$")
        ax.set(xlim=(-1.03, 1.03), ylim=(-1.03, 1.03), xlabel=r"归一化输入 $x$", ylabel=r"输出 $Q(x)$")
        ax.set_title(title)
        ax.set_aspect("equal", adjustable="box")
        clean_axes(ax)
        ax.legend(frameon=False, loc="upper left", fontsize=9.5)

    xp = np.linspace(0, 1, 1200)
    axes[2].plot(xp, xp, color=MUTED, linestyle="--", linewidth=1.2, label=r"$g(x)=x$")
    axes[2].plot(xp, a_compand(xp), color=PURPLE, linewidth=2.2, label=r"$A=87.6$")
    axes[2].plot(xp, mu_compand(xp), color=GOLD, linewidth=2.2, label=r"$\mu=255$")
    axes[2].set(xlim=(0, 1), ylim=(0, 1.03), xlabel=r"归一化输入 $x/x_{\max}$", ylabel=r"归一化压缩输出 $g(x)/x_{\max}$")
    axes[2].set_title("A 律与 μ 律压缩曲线（正半轴）")
    clean_axes(axes[2])
    axes[2].legend(frameon=False, loc="lower right", fontsize=9.5)

    fig.suptitle("量化间隔与压扩", fontsize=16, fontweight="bold", color=INK)
    save(fig, "communication-quantization-companding.png")


def delta_reconstruct(samples: np.ndarray, delta: float) -> np.ndarray:
    reconstructed = np.zeros_like(samples)
    for n in range(1, len(samples)):
        reconstructed[n] = reconstructed[n - 1] + (
            delta if samples[n] >= reconstructed[n - 1] else -delta
        )
    return reconstructed


def figure_delta_modulation() -> None:
    ts = 0.12
    delta = 0.12

    t1 = np.arange(0, 6.0 + ts, ts)
    td1 = np.linspace(0, 6.0, 1600)
    s1 = 0.78 * np.sin(0.9 * t1)
    sd1 = 0.78 * np.sin(0.9 * td1)
    r1 = delta_reconstruct(s1, delta)

    t2 = np.arange(0, 1.45 + ts, ts)
    td2 = np.linspace(0, 1.45, 800)
    slope = 1.55
    s2 = slope * t2
    sd2 = slope * td2
    r2 = delta_reconstruct(s2, delta)

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.4), constrained_layout=True)
    for ax, td, signal, t, reconstructed in [
        (axes[0], td1, sd1, t1, r1),
        (axes[1], td2, sd2, t2, r2),
    ]:
        ax.plot(td, signal, color=PURPLE, linewidth=2.3, label=r"输入 $S(t)$")
        ax.step(t, reconstructed, where="post", color=CORAL, linewidth=2.1, label=r"重建 $\hat S(t)$")
        ax.scatter(t, reconstructed, color=CORAL, s=13, zorder=3)
        ax.set_xlabel(r"时间 $t$")
        ax.set_ylabel("幅度")
        clean_axes(ax)

    axes[0].set_title(r"正常跟踪：$\max |\mathrm{d}S/\mathrm{d}t|<\Delta/T_s$")
    axes[0].legend(frameon=False, loc="upper right")
    axes[1].set_title(r"斜率过载：$\max |\mathrm{d}S/\mathrm{d}t|>\Delta/T_s$")
    axes[1].annotate(
        "每个抽样周期最多只上升 Δ",
        xy=(0.84, r2[7]),
        xytext=(0.48, 1.85),
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=MUTED,
    )
    axes[1].legend(frameon=False, loc="upper left")
    fig.suptitle("增量调制的跟踪与斜率过载", fontsize=16, fontweight="bold")
    save(fig, "communication-delta-modulation.png")


def raised_cosine_time(t: np.ndarray, alpha: float) -> np.ndarray:
    if alpha == 0:
        return np.sinc(t)
    denominator = 1 - (2 * alpha * t) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.sinc(t) * np.cos(np.pi * alpha * t) / denominator
    singular = np.isclose(np.abs(t), 1 / (2 * alpha), atol=1e-9)
    result[singular] = (np.pi / 4) * np.sinc(1 / (2 * alpha))
    return result


def raised_cosine_frequency(f: np.ndarray, alpha: float) -> np.ndarray:
    af = np.abs(f)
    if alpha == 0:
        return (af <= 0.5).astype(float)
    low = (1 - alpha) / 2
    high = (1 + alpha) / 2
    response = np.zeros_like(f)
    response[af < low] = 1
    transition = (af >= low) & (af <= high)
    response[transition] = 0.5 * (
        1 + np.cos(np.pi / alpha * (af[transition] - low))
    )
    return response


def figure_eye_diagram() -> None:
    rng = np.random.default_rng(20260714)
    sps = 64
    span = 7
    symbols = rng.choice([-1.0, 1.0], size=260)
    impulses = np.zeros(len(symbols) * sps)
    impulses[::sps] = symbols
    pulse_t = np.arange(-span * sps, span * sps + 1) / sps
    pulse = raised_cosine_time(pulse_t, 0.5)
    waveform = np.convolve(impulses, pulse, mode="same")
    waveform += 0.018 * rng.standard_normal(waveform.size)

    # A one-symbol echo makes the sample at the current symbol depend strongly
    # on the previous symbol, so the eye visibly closes at the decision time.
    delay = sps
    channel = np.zeros(delay + 1)
    channel[0] = 1.0
    channel[-1] = 0.85
    distorted = np.convolve(waveform, channel, mode="full")[: waveform.size] / 1.35
    distorted += 0.026 * rng.standard_normal(distorted.size)

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.5), constrained_layout=True)
    eye_x = np.linspace(-1, 1, 2 * sps + 1)
    for ax, data, title, color in [
        (axes[0], waveform, "ISI 较小：眼睛张开", TEAL),
        (axes[1], distorted, "ISI 加重：眼睛闭合", CORAL),
    ]:
        for k in range(12, 132):
            center = k * sps
            segment = data[center - sps : center + sps + 1]
            if len(segment) == len(eye_x):
                ax.plot(eye_x, segment, color=color, linewidth=0.8, alpha=0.15)
        ax.axvline(0, color=PURPLE, linestyle="--", linewidth=1.2)
        ax.axhline(0, color=GRID, linewidth=0.9)
        ax.set(xlim=(-1, 1), ylim=(-1.8, 1.8), xlabel=r"相对时间 $t/T_s$", ylabel="归一化幅度")
        ax.set_title(title)
        clean_axes(ax, grid=False)
    axes[0].annotate(
        "最佳抽样时刻",
        xy=(0, -1.45),
        xytext=(-0.72, -1.67),
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=MUTED,
    )
    axes[0].annotate(
        "噪声容限",
        xy=(0, 0.46),
        xytext=(0.28, 0.08),
        arrowprops={"arrowstyle": "<->", "color": PURPLE},
        color=PURPLE,
    )
    fig.suptitle("眼图对符号间串扰的直观反映", fontsize=16, fontweight="bold")
    save(fig, "communication-eye-diagram.png")


def figure_raised_cosine() -> None:
    alphas = [0.0, 0.5, 1.0]
    colors = [PURPLE, TEAL, CORAL]
    f = np.linspace(-1.15, 1.15, 2400)
    t = np.linspace(-5, 5, 5001)

    fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.6), constrained_layout=True)
    for alpha, color in zip(alphas, colors):
        label = rf"$\alpha={alpha:g}$"
        axes[0].plot(f, raised_cosine_frequency(f, alpha), color=color, linewidth=2.2, label=label)
        axes[1].plot(t, raised_cosine_time(t.copy(), alpha), color=color, linewidth=2.0, label=label)

    axes[0].set(xlabel=r"归一化频率 $fT_s$", ylabel=r"$H_{\rm RC}(f)/T_s$", xlim=(-1.05, 1.05), ylim=(-0.04, 1.08))
    axes[0].set_title("频率响应：滚降越大，过渡带越宽")
    clean_axes(axes[0])
    axes[0].legend(frameon=False)

    integer_t = np.arange(-4, 5)
    axes[1].scatter(integer_t, np.zeros_like(integer_t), s=22, color=INK, zorder=4, label=r"$t=kT_s$ 过零")
    axes[1].scatter([0], [1], s=30, color=INK, zorder=5)
    axes[1].set(xlabel=r"归一化时间 $t/T_s$", ylabel=r"$h_{\rm RC}(t)$", xlim=(-5, 5), ylim=(-0.3, 1.08))
    axes[1].set_title("时域响应：整数倍符号周期处保持零 ISI")
    clean_axes(axes[1])
    axes[1].legend(frameon=False, ncol=2, fontsize=9.5)
    fig.suptitle("升余弦脉冲的频域与时域", fontsize=16, fontweight="bold")
    save(fig, "communication-raised-cosine.png")


def figure_matched_filter() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.7), constrained_layout=True)

    t = np.linspace(-0.15, 2.15, 1000)
    pulse = ((t >= 0) & (t <= 1)).astype(float)
    correlator = np.where((t >= 0) & (t <= 1), t, 0)
    matched = np.where(
        (t >= 0) & (t <= 1),
        t,
        np.where((t > 1) & (t <= 2), 2 - t, 0),
    )
    data = [
        (pulse, "矩形输入脉冲", PURPLE),
        (correlator, "相关器连续输出", TEAL),
        (matched, "匹配滤波器连续输出", CORAL),
    ]
    for ax, (y, title, color) in zip(axes, data):
        ax.plot(t, y, color=color, linewidth=2.5)
        ax.axvline(1, color=MUTED, linestyle="--", linewidth=1.1)
        ax.set(xlim=(-0.08, 2.08), ylim=(-0.08, 1.15), xlabel=r"时间 $t/T_s$")
        ax.set_title(title)
        ax.set_xticks([0, 1, 2], ["0", r"$T_s$", r"$2T_s$"])
        ax.set_yticks([0, 1])
        clean_axes(ax, grid=False)
    axes[1].scatter([1], [1], color=TEAL, s=35, zorder=4)
    axes[2].scatter([1], [1], color=CORAL, s=35, zorder=4)
    axes[2].annotate(
        r"峰值在 $T_s$",
        xy=(1, 1),
        xytext=(1.25, 0.82),
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=MUTED,
    )
    fig.suptitle("相关器与匹配滤波器：连续输出不同，抽样值相同", fontsize=16, fontweight="bold")
    save(fig, "communication-matched-filter.png")


def figure_mpsk_decision() -> None:
    m = 8
    angles = 2 * np.pi * np.arange(m) / m
    points = np.c_[np.cos(angles), np.sin(angles)]

    fig, ax = plt.subplots(figsize=(7.2, 6.1), constrained_layout=True)
    sector = patches.Wedge((0, 0), 1.28, -180 / m, 180 / m, facecolor=PALE_CORAL, edgecolor="none", alpha=0.8)
    ax.add_patch(sector)
    circle = patches.Circle((0, 0), 1, fill=False, color=GRID, linestyle="--", linewidth=1.3)
    ax.add_patch(circle)
    for k in range(m):
        boundary = (2 * k + 1) * np.pi / m
        ax.plot([0, 1.28 * np.cos(boundary)], [0, 1.28 * np.sin(boundary)], color=MUTED, linestyle="--", linewidth=1.0)
    ax.scatter(points[:, 0], points[:, 1], s=85, color=PURPLE, edgecolor=BG, linewidth=1.3, zorder=3)
    ax.scatter(points[[0, 1], 0], points[[0, 1], 1], s=100, color=[CORAL, TEAL], edgecolor=BG, linewidth=1.4, zorder=4)
    ax.plot(points[[0, 1], 0], points[[0, 1], 1], color=GOLD, linewidth=3.0)
    midpoint = points[[0, 1]].mean(axis=0)
    ax.annotate(
        r"$d_{\min}=2A\sin(\pi/M)$",
        xy=midpoint,
        xytext=(-0.48, 1.33),
        arrowprops={"arrowstyle": "->", "color": GOLD},
        color=INK,
        ha="center",
    )
    ax.annotate(
        "等距中垂线构成判决边界",
        xy=(1.12 * np.cos(np.pi / m), 1.12 * np.sin(np.pi / m)),
        xytext=(-1.25, -1.22),
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=MUTED,
    )
    ax.axhline(0, color=INK, linewidth=1.0)
    ax.axvline(0, color=INK, linewidth=1.0)
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.4, 1.52), xlabel="同相分量 I", ylabel="正交分量 Q")
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("8PSK 星座与最小距离判决域")
    clean_axes(ax, grid=False)
    save(fig, "communication-mpsk-decision.png")


def figure_qam_decision() -> None:
    values = np.array([-3, -1, 1, 3])
    points = np.array([(i, q) for i in values for q in values])
    corner = (np.abs(points[:, 0]) == 3) & (np.abs(points[:, 1]) == 3)
    inner = (np.abs(points[:, 0]) == 1) & (np.abs(points[:, 1]) == 1)
    edge = ~(corner | inner)

    fig, ax = plt.subplots(figsize=(7.3, 6.1), constrained_layout=True)
    ax.add_patch(patches.Rectangle((0, 0), 2, 2, facecolor=PALE_PURPLE, edgecolor="none", alpha=0.8))
    for threshold in [-2, 0, 2]:
        ax.axvline(threshold, color=MUTED, linestyle="--", linewidth=1.0)
        ax.axhline(threshold, color=MUTED, linestyle="--", linewidth=1.0)
    ax.scatter(points[corner, 0], points[corner, 1], s=90, color=CORAL, edgecolor=BG, label="角点")
    ax.scatter(points[edge, 0], points[edge, 1], s=90, color=TEAL, edgecolor=BG, label="边点")
    ax.scatter(points[inner, 0], points[inner, 1], s=90, color=PURPLE, edgecolor=BG, label="内点")
    ax.annotate("", xy=(3, -3.45), xytext=(1, -3.45), arrowprops={"arrowstyle": "<->", "color": GOLD, "linewidth": 2})
    ax.text(2, -3.72, r"最小间距 $2A$", ha="center", color=INK)
    ax.text(1, 1.52, "示例判决域", ha="center", va="center", color=PURPLE)
    ax.axhline(0, color=INK, linewidth=1.0)
    ax.axvline(0, color=INK, linewidth=1.0)
    ax.set(xlim=(-4.15, 4.15), ylim=(-4.05, 4.05), xlabel="同相分量 I / A", ylabel="正交分量 Q / A")
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("16QAM 星座、判决门限与三类星座点")
    clean_axes(ax, grid=False)
    ax.legend(frameon=False, ncol=3, loc="upper center")
    save(fig, "communication-qam-decision.png")


def rounded_box(ax: plt.Axes, xy: tuple[float, float], width: float, height: float, text: str, facecolor: str) -> patches.FancyBboxPatch:
    box = patches.FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.018,rounding_size=0.018",
        facecolor=facecolor,
        edgecolor=INK,
        linewidth=1.3,
    )
    ax.add_patch(box)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha="center", va="center", fontsize=10.5)
    return box


def arrow(ax: plt.Axes, start: tuple[float, float], end: tuple[float, float], color: str = INK, linewidth: float = 1.6) -> None:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12, linewidth=linewidth, color=color))


def figure_qam_receiver() -> None:
    fig, ax = plt.subplots(figsize=(12.2, 4.6), constrained_layout=True)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    mixer_x = 0.19
    top_y, bottom_y = 0.72, 0.28
    ax.plot([0.03, 0.09], [0.5, 0.5], color=INK, linewidth=1.8)
    ax.plot([0.09, 0.09], [bottom_y, top_y], color=INK, linewidth=1.8)
    arrow(ax, (0.09, top_y), (mixer_x - 0.035, top_y))
    arrow(ax, (0.09, bottom_y), (mixer_x - 0.035, bottom_y))
    ax.text(0.02, 0.54, r"$r(t)$", fontsize=12)

    for y in [top_y, bottom_y]:
        circle = patches.Circle((mixer_x, y), 0.036, facecolor=BG, edgecolor=PURPLE, linewidth=1.8)
        ax.add_patch(circle)
        ax.plot([mixer_x - 0.019, mixer_x + 0.019], [y - 0.019, y + 0.019], color=PURPLE, linewidth=1.4)
        ax.plot([mixer_x - 0.019, mixer_x + 0.019], [y + 0.019, y - 0.019], color=PURPLE, linewidth=1.4)

    rounded_box(ax, (0.115, 0.46), 0.15, 0.09, "本地载波", PALE_TEAL)
    arrow(ax, (0.19, 0.55), (mixer_x, top_y - 0.038), color=TEAL)
    rounded_box(ax, (0.132, 0.345), 0.116, 0.075, "90° 移相", PALE_CORAL)
    arrow(ax, (0.19, 0.46), (0.19, 0.42), color=TEAL)
    arrow(ax, (0.19, 0.345), (mixer_x, bottom_y + 0.038), color=TEAL)

    for y, channel in [(top_y, "I"), (bottom_y, "Q")]:
        arrow(ax, (mixer_x + 0.036, y), (0.32, y))
        rounded_box(ax, (0.32, y - 0.055), 0.15, 0.11, "匹配滤波器", PALE_PURPLE)
        arrow(ax, (0.47, y), (0.54, y))
        rounded_box(ax, (0.54, y - 0.055), 0.15, 0.11, f"{channel} 路电平恢复", PALE_TEAL)
        arrow(ax, (0.69, y), (0.79, y))

    rounded_box(ax, (0.79, 0.19), 0.16, 0.62, "联合符号\n估计", PALE_CORAL)
    arrow(ax, (0.95, 0.5), (0.995, 0.5), color=CORAL)
    ax.text(0.82, 0.12, r"$\hat a_i+j\hat b_i$", fontsize=12, color=CORAL)
    ax.text(0.39, 0.88, "I、Q 两路使用同一载波，正交分离后分别匹配滤波", ha="center", color=MUTED)
    ax.set_title("QAM 相干解调结构", fontsize=16, fontweight="bold", pad=6)
    save(fig, "communication-qam-receiver.png")


def figure_trellis() -> None:
    states = ["00", "01", "10", "11"]
    y_pos = {state: 3 - i for i, state in enumerate(states)}
    transitions = {
        "00": {0: ("00", "00"), 1: ("01", "11")},
        "01": {0: ("10", "10"), 1: ("11", "01")},
        "10": {0: ("00", "11"), 1: ("01", "00")},
        "11": {0: ("10", "01"), 1: ("11", "10")},
    }

    fig, ax = plt.subplots(figsize=(12.4, 5.3), constrained_layout=True)
    for k in range(4):
        for state in states:
            for bit in [0, 1]:
                next_state, _ = transitions[state][bit]
                ax.add_patch(
                    FancyArrowPatch(
                        (k + 0.035, y_pos[state]),
                        (k + 0.965, y_pos[next_state]),
                        arrowstyle="-|>",
                        mutation_scale=8,
                        linewidth=0.9,
                        color=BLUE,
                        alpha=0.38,
                    )
                )

    path_states = ["00", "01", "11", "10", "01"]
    bits = [1, 1, 0, 1]
    outputs = ["11", "01", "01", "00"]
    for k, (state, next_state, bit, output) in enumerate(zip(path_states, path_states[1:], bits, outputs)):
        ax.add_patch(
            FancyArrowPatch(
                (k + 0.035, y_pos[state]),
                (k + 0.965, y_pos[next_state]),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=3.0,
                color=CORAL,
                zorder=4,
            )
        )
        mid_y = (y_pos[state] + y_pos[next_state]) / 2
        ax.text(k + 0.5, mid_y + (0.22 if mid_y < 2.5 else -0.25), f"{bit}/{output}", ha="center", va="center", color=CORAL, fontweight="bold", bbox={"boxstyle": "round,pad=0.16", "facecolor": BG, "edgecolor": "none", "alpha": 0.88}, zorder=5)

    for k in range(5):
        for state in states:
            ax.scatter(k, y_pos[state], s=60, facecolor=BG, edgecolor=PURPLE, linewidth=1.7, zorder=6)
        ax.text(k, 3.45, rf"$k={k}$", ha="center", color=MUTED)
    for state in states:
        ax.text(-0.28, y_pos[state], state, ha="right", va="center", fontweight="bold")

    ax.text(4.2, 2.75, "输入：1 1 0 1", color=INK, fontsize=12)
    ax.text(4.2, 2.35, "输出：11 01 01 00", color=CORAL, fontsize=12, fontweight="bold")
    ax.text(4.2, 1.78, "状态映射", color=MUTED, fontweight="bold")
    ax.text(4.2, 1.42, "a=00，b=01", color=MUTED)
    ax.text(4.2, 1.08, "c=10，d=11", color=MUTED)
    ax.set(xlim=(-0.62, 5.42), ylim=(-0.45, 3.72))
    ax.set_yticks([])
    ax.set_xticks([])
    ax.axis("off")
    ax.set_title("(2,1,3) 卷积码网格图：输入 1101 的编码路径", fontsize=16, fontweight="bold")
    save(fig, "communication-convolutional-trellis.png")


def setup_resource_axis(ax: plt.Axes, title: str) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("时间")
    ax.set_ylabel("频率")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    for spine in ax.spines.values():
        spine.set_color(INK)


def figure_resource_allocation() -> None:
    colors = [PURPLE, TEAL, CORAL]
    fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.0), constrained_layout=True)

    setup_resource_axis(axes[0], "FD：沿频率划分")
    for i, color in enumerate(colors):
        y = 0.08 + i * 0.31
        axes[0].add_patch(patches.Rectangle((0.04, y), 0.92, 0.23, facecolor=color, alpha=0.78, edgecolor="none"))
        axes[0].text(0.5, y + 0.115, f"用户 {i + 1}", ha="center", va="center", color="white", fontweight="bold")
    axes[0].text(0.5, 0.35, "保护频带", ha="center", va="center", color=MUTED, fontsize=9)

    setup_resource_axis(axes[1], "TD：沿时间划分")
    for i, color in enumerate(colors):
        x = 0.04 + i * 0.31
        axes[1].add_patch(patches.Rectangle((x, 0.05), 0.27, 0.9, facecolor=color, alpha=0.78, edgecolor="none"))
        axes[1].text(x + 0.135, 0.5, f"用户 {i + 1}", ha="center", va="center", color="white", rotation=90, fontweight="bold")
    axes[1].text(0.33, 0.03, "保护时间", ha="center", va="top", color=MUTED, fontsize=9)

    setup_resource_axis(axes[2], "CD：同一时频资源，码空间区分")
    hatches = ["////", "\\\\", "xx"]
    for i, (color, hatch) in enumerate(zip(colors, hatches)):
        axes[2].add_patch(patches.Rectangle((0.08, 0.08), 0.84, 0.84, facecolor="none", edgecolor=color, linewidth=1.5, hatch=hatch, label=rf"用户 {i + 1}：码 $c_{i + 1}$"))
    axes[2].legend(frameon=True, facecolor=BG, edgecolor=GRID, loc="center", fontsize=9.5)
    fig.suptitle("频分、时分与码分的资源划分", fontsize=16, fontweight="bold")
    save(fig, "communication-resource-allocation.png")


def figure_aloha() -> None:
    g = np.linspace(0, 3.2, 1200)
    pure = g * np.exp(-2 * g)
    slotted = g * np.exp(-g)

    fig, ax = plt.subplots(figsize=(9.2, 5.0), constrained_layout=True)
    ax.plot(g, pure, color=CORAL, linewidth=2.5, label=r"纯 ALOHA：$S=Ge^{-2G}$")
    ax.plot(g, slotted, color=PURPLE, linewidth=2.5, label=r"时隙 ALOHA：$S=Ge^{-G}$")
    maxima = [(0.5, 1 / (2 * np.e), CORAL), (1.0, 1 / np.e, PURPLE)]
    for x, y, color in maxima:
        ax.scatter([x], [y], s=65, color=color, edgecolor=BG, linewidth=1.3, zorder=4)
        ax.plot([x, x], [0, y], color=color, linestyle="--", linewidth=1.1)
        ax.plot([0, x], [y, y], color=color, linestyle="--", linewidth=1.1)
    ax.annotate(r"$(0.5,\,1/2e)\approx(0.5,\,0.184)$", xy=maxima[0][:2], xytext=(0.78, 0.135), arrowprops={"arrowstyle": "->", "color": CORAL}, color=CORAL)
    ax.annotate(r"$(1,\,1/e)\approx(1,\,0.368)$", xy=maxima[1][:2], xytext=(1.34, 0.40), arrowprops={"arrowstyle": "->", "color": PURPLE}, color=PURPLE)
    ax.set(xlim=(0, 3.2), ylim=(0, 0.48), xlabel=r"网络负载 $G$", ylabel=r"归一化吞吐量 $S$")
    ax.set_title("负载继续增大时，冲突使有效吞吐量反而下降")
    clean_axes(ax)
    ax.legend(frameon=False, loc="upper right")
    save(fig, "communication-aloha-throughput.png")


def draw_crossbar(ax: plt.Axes) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("交换：分级降低开关数")
    ax.text(0.5, 0.94, r"单级 $MN\times MN$", ha="center", fontweight="bold")
    x_lines = np.linspace(0.25, 0.75, 6)
    y_lines = np.linspace(0.57, 0.83, 6)
    for x in x_lines:
        ax.plot([x, x], [0.55, 0.85], color=PURPLE, linewidth=1.0)
    for y in y_lines:
        ax.plot([0.22, 0.78], [y, y], color=TEAL, linewidth=1.0)
    xx, yy = np.meshgrid(x_lines, y_lines)
    ax.scatter(xx.ravel(), yy.ravel(), s=11, color=CORAL, zorder=3)
    ax.text(0.5, 0.5, r"开关数：$(MN)^2$", ha="center", color=MUTED)

    rounded_box(ax, (0.13, 0.16), 0.27, 0.17, "M 个\nN×N 单元", PALE_PURPLE)
    rounded_box(ax, (0.60, 0.16), 0.27, 0.17, "N 个\nM×M 单元", PALE_TEAL)
    for offset in [-0.06, 0, 0.06]:
        arrow(ax, (0.40, 0.245 + offset), (0.60, 0.245 - offset), color=BLUE, linewidth=1.0)
    ax.text(0.5, 0.08, r"两级开关数：$MN(M+N)$", ha="center", color=CORAL, fontweight="bold")


def draw_shortest_path(ax: plt.Axes) -> None:
    ax.set_xlim(-0.2, 3.5)
    ax.set_ylim(-0.1, 3.1)
    ax.axis("off")
    ax.set_title("路由：从 u 出发的最短路径树")
    pos = {
        "u": (0.1, 1.65),
        "v": (0.95, 2.55),
        "w": (0.95, 0.85),
        "x": (1.75, 1.55),
        "y": (2.35, 2.55),
        "z": (3.2, 1.95),
        "s": (1.75, 0.18),
        "t": (2.65, 0.72),
    }
    edges = {
        ("u", "v"): 3,
        ("u", "w"): 2,
        ("v", "y"): 2,
        ("v", "x"): 1,
        ("w", "x"): 1,
        ("w", "s"): 4,
        ("x", "z"): 4,
        ("x", "t"): 5,
        ("s", "t"): 3,
        ("y", "z"): 1,
    }
    tree = {("u", "v"), ("u", "w"), ("v", "y"), ("w", "x"), ("w", "s"), ("x", "t"), ("y", "z")}
    distances = {"u": 0, "v": 3, "w": 2, "x": 3, "y": 5, "z": 6, "s": 6, "t": 8}
    for (a, b), weight in edges.items():
        selected = (a, b) in tree
        color = CORAL if selected else GRID
        linewidth = 2.8 if selected else 1.5
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=color, linewidth=linewidth, zorder=1)
        midpoint = ((pos[a][0] + pos[b][0]) / 2, (pos[a][1] + pos[b][1]) / 2)
        ax.text(midpoint[0], midpoint[1] + 0.08, str(weight), ha="center", va="center", color=INK, fontsize=9.5, bbox={"facecolor": BG, "edgecolor": "none", "pad": 0.3})
    for node, (x, y) in pos.items():
        face = CORAL if node == "u" else BG
        ax.scatter([x], [y], s=330, facecolor=face, edgecolor=PURPLE, linewidth=1.8, zorder=3)
        ax.text(x, y, node, ha="center", va="center", fontweight="bold", color="white" if node == "u" else INK, zorder=4)
        ax.text(x, y - 0.31, rf"$d={distances[node]}$", ha="center", color=MUTED, fontsize=9)
    ax.text(1.65, 2.98, "彩色边为 SPF 选中的树边", ha="center", color=CORAL)


def figure_switching_routing() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.2), constrained_layout=True)
    draw_crossbar(axes[0])
    draw_shortest_path(axes[1])
    fig.suptitle("交换求快，路由谋短", fontsize=16, fontweight="bold")
    save(fig, "communication-switching-routing.png")


def figure_congestion_red() -> None:
    rounds = np.arange(0, 22)
    cwnd = np.array([1, 2, 4, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 4, 8, 12, 13, 14, 15, 16])
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), constrained_layout=True)

    ax = axes[0]
    ax.plot(rounds, cwnd, color=PURPLE, linewidth=2.7, marker="o", markersize=4.8, markerfacecolor=BG)
    ax.axhline(16, color=TEAL, linestyle="--", linewidth=1.1)
    ax.axhline(12, color=CORAL, linestyle="--", linewidth=1.1)
    ax.annotate("进入拥塞避免\nssthresh=16", xy=(4, 16), xytext=(5.2, 11.7), arrowprops={"arrowstyle": "->", "color": TEAL}, color=TEAL)
    ax.annotate("超时", xy=(12, 24), xytext=(10.8, 20.0), arrowprops={"arrowstyle": "->", "color": CORAL}, color=CORAL, fontweight="bold")
    ax.annotate(r"$cwnd\to1$", xy=(13, 1), xytext=(13.8, 5.5), arrowprops={"arrowstyle": "->", "color": CORAL}, color=CORAL)
    ax.annotate("新门限=12", xy=(17, 12), xytext=(17.4, 8.1), arrowprops={"arrowstyle": "->", "color": CORAL}, color=CORAL)
    ax.set(xlim=(0, 21.2), ylim=(0, 26), xlabel="传输轮次", ylabel="拥塞窗口 / MSS")
    ax.set_title("慢启动、拥塞避免与超时回退")
    clean_axes(ax)

    ax = axes[1]
    q_min, q_full, p_pre = 0.24, 0.88, 0.55
    ax.plot([0, q_min], [0, 0], color=TEAL, linewidth=2.7)
    ax.plot([q_min, q_full], [0, p_pre], color=GOLD, linewidth=2.7)
    ax.plot([q_full, 1.0], [p_pre, 1.0], color=CORAL, linewidth=2.7)
    ax.scatter([q_min, q_full, 1], [0, p_pre, 1], color=[TEAL, GOLD, CORAL], s=50, zorder=3)
    ax.axvline(q_min, color=MUTED, linestyle="--", linewidth=1.0)
    ax.axvline(q_full, color=MUTED, linestyle="--", linewidth=1.0)
    ax.text(q_min / 2, 0.08, "不丢包", ha="center", color=TEAL)
    ax.text((q_min + q_full) / 2, 0.3, "提前随机丢包", ha="center", color=GOLD, rotation=28)
    ax.annotate("队列满：丢包概率为 1", xy=(1, 1), xytext=(0.48, 0.88), arrowprops={"arrowstyle": "->", "color": CORAL}, color=CORAL)
    ax.set(xlim=(0, 1.04), ylim=(0, 1.08), xlabel="平均队列长度（归一化）", ylabel="丢包概率")
    ax.set_title("随机早期检测（RED）")
    clean_axes(ax)
    fig.suptitle("端到端拥塞控制与链路队列管理", fontsize=16, fontweight="bold")
    save(fig, "communication-congestion-red.png")


def main() -> None:
    figure_quantization()
    figure_delta_modulation()
    figure_eye_diagram()
    figure_raised_cosine()
    figure_matched_filter()
    figure_mpsk_decision()
    figure_qam_decision()
    figure_qam_receiver()
    figure_trellis()
    figure_resource_allocation()
    figure_aloha()
    figure_switching_routing()
    figure_congestion_red()
    print(f"Generated communication figures in {OUT_DIR}")


if __name__ == "__main__":
    main()
