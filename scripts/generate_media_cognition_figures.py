"""Generate explanatory figures for ``media-and-cognition.md``.

The figures reproduce the qualitative relationships used in the course slides.
Run this script from the repository with NumPy and Matplotlib available.
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
PURPLE = "#6654A3"
TEAL = "#238B7B"
CORAL = "#D9664A"
GOLD = "#D9A72E"
BLUE = "#3B6FB6"
PALE_PURPLE = "#EAE6F4"
PALE_TEAL = "#DDF1ED"
PALE_CORAL = "#F8E2DC"

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial Unicode MS", "STHeiti", "PingFang SC", "DejaVu Sans"],
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
    if grid:
        ax.grid(True, color=GRID, linewidth=0.8, alpha=0.75)
        ax.set_axisbelow(True)


def figure_bias_variance() -> None:
    log_lambda = np.linspace(-4.0, 4.0, 500)
    variance = 1.7 / (1 + np.exp(1.05 * (log_lambda + 0.2))) + 0.12
    bias2 = 1.55 / (1 + np.exp(-1.05 * (log_lambda - 0.25))) + 0.08
    total = bias2 + variance
    optimum = int(np.argmin(total))

    fig, ax = plt.subplots(figsize=(8.8, 5.0), constrained_layout=True)
    ax.plot(log_lambda, bias2, color=CORAL, linewidth=2.5, label=r"偏差平方 $\mathrm{Bias}^2$")
    ax.plot(log_lambda, variance, color=BLUE, linewidth=2.5, label=r"方差 $\mathrm{Var}$")
    ax.plot(log_lambda, total, color=PURPLE, linewidth=2.8, label="两者之和")
    ax.axvline(log_lambda[optimum], color=MUTED, linestyle="--", linewidth=1.3)
    ax.scatter([log_lambda[optimum]], [total[optimum]], color=PURPLE, s=45, zorder=4)
    ax.annotate(
        r"平衡点 $\lambda^*$",
        xy=(log_lambda[optimum], total[optimum]),
        xytext=(log_lambda[optimum] + 0.55, total[optimum] + 0.3),
        arrowprops={"arrowstyle": "->", "color": MUTED},
        color=MUTED,
    )
    ax.set(
        xlabel=r"正则化强度 $\log \lambda$",
        ylabel="预测误差中的可约部分",
        xlim=(-4, 4),
        ylim=(0, 2.5),
        xticks=[],
        yticks=[],
    )
    ax.set_title("岭回归中的偏差-方差权衡")
    clean_axes(ax)
    ax.legend(frameon=False, ncol=3, loc="upper center")
    save(fig, "media-cognition-bias-variance.png")


def figure_activations() -> None:
    x = np.linspace(-5, 5, 1200)
    sigmoid = 1 / (1 + np.exp(-x))
    functions = [
        ("Sigmoid", sigmoid, PURPLE),
        ("Tanh", np.tanh(x), BLUE),
        ("ReLU", np.maximum(0, x), TEAL),
        ("Leaky ReLU", np.maximum(0.1 * x, x), CORAL),
        ("SiLU / Swish", x * sigmoid, GOLD),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(12.2, 7.0), constrained_layout=True)
    for ax, (title, y, color) in zip(axes.flat, functions):
        ax.axhline(0, color=GRID, linewidth=1)
        ax.axvline(0, color=GRID, linewidth=1)
        ax.plot(x, y, color=color, linewidth=2.5)
        ax.set(xlim=(-5, 5), xlabel=r"$z$", ylabel=r"$f(z)$")
        ax.set_title(title)
        clean_axes(ax, grid=False)
    ax = axes.flat[-1]
    ax.axhline(0, color=GRID, linewidth=1)
    ax.axvline(0, color=GRID, linewidth=1)
    ax.step([-5, 0, 0, 5], [0, 0, 1, 1], where="post", color=INK, linewidth=2.5)
    ax.set(xlim=(-5, 5), ylim=(-0.2, 1.2), xlabel=r"$z$", ylabel=r"$f(z)$")
    ax.set_title("阶跃函数")
    clean_axes(ax, grid=False)
    fig.suptitle("课件中的常用激活函数", fontsize=16, fontweight="bold")
    save(fig, "media-cognition-activation-functions.png")


def _project(points: np.ndarray, direction: np.ndarray) -> np.ndarray:
    direction = direction / np.linalg.norm(direction)
    return np.outer(points @ direction, direction)


def figure_pca_lda() -> None:
    rng = np.random.default_rng(20260715)
    covariance = np.array([[2.7, 1.8], [1.8, 1.7]])
    class_a = rng.multivariate_normal([-0.9, 0.7], covariance, 80)
    class_b = rng.multivariate_normal([1.0, -0.7], covariance, 80)
    all_points = np.vstack([class_a, class_b])
    _, _, vt = np.linalg.svd(all_points - all_points.mean(axis=0), full_matrices=False)
    pca_axis = vt[0]
    within = np.cov(class_a, rowvar=False) + np.cov(class_b, rowvar=False)
    lda_axis = np.linalg.solve(within, class_a.mean(axis=0) - class_b.mean(axis=0))
    lda_axis /= np.linalg.norm(lda_axis)

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.1), constrained_layout=True)
    for ax, direction, title, subtitle in [
        (axes[0], pca_axis, "PCA", "保留整体方差最大的方向"),
        (axes[1], lda_axis, "LDA", "拉大类间距离并压小类内离散"),
    ]:
        ax.scatter(class_a[:, 0], class_a[:, 1], s=20, color=BLUE, alpha=0.52, label="类别 1")
        ax.scatter(class_b[:, 0], class_b[:, 1], s=20, color=CORAL, alpha=0.52, label="类别 2")
        span = np.array([-5.5, 5.5])
        line = np.outer(span, direction)
        ax.plot(line[:, 0], line[:, 1], color=INK, linewidth=2.4)
        for points, color in [(class_a[::8], BLUE), (class_b[::8], CORAL)]:
            projected = _project(points, direction)
            for source, target in zip(points, projected):
                ax.plot([source[0], target[0]], [source[1], target[1]], color=color, alpha=0.22, linewidth=0.8)
        ax.set(xlim=(-6, 6), ylim=(-5, 5), xlabel=r"$x_1$", ylabel=r"$x_2$", xticks=[], yticks=[])
        ax.set_title(f"{title}\n{subtitle}")
        ax.set_aspect("equal", adjustable="box")
        clean_axes(ax, grid=False)
    axes[0].legend(frameon=False, loc="upper left")
    fig.suptitle("PCA 与 LDA 的投影目标不同", fontsize=16, fontweight="bold")
    save(fig, "media-cognition-pca-lda.png")


def figure_time_frequency_tiles() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.7, 4.8), constrained_layout=True)
    ax = axes[0]
    for row in range(4):
        for col in range(8):
            ax.add_patch(patches.Rectangle((col, row), 1, 1, facecolor=PALE_PURPLE, edgecolor=PURPLE, linewidth=1.1))
    ax.set(xlim=(0, 8), ylim=(0, 4), xlabel="时间", ylabel="频率", xticks=[], yticks=[])
    ax.set_title("短时傅里叶变换：固定时频窗")

    ax = axes[1]
    bands = [(0, 1, 4), (1, 2, 8), (2, 3, 16), (3, 4, 32)]
    colors = [PALE_CORAL, PALE_TEAL, PALE_PURPLE, "#E9F0FA"]
    edges = [CORAL, TEAL, PURPLE, BLUE]
    for (low, high, count), face, edge in zip(bands, colors, edges):
        width = 8 / count
        for col in range(count):
            ax.add_patch(patches.Rectangle((col * width, low), width, high - low, facecolor=face, edgecolor=edge, linewidth=0.85))
    ax.set(xlim=(0, 8), ylim=(0, 4), xlabel="时间", ylabel="频率", xticks=[], yticks=[])
    ax.set_title("小波变换：低频宽窗、高频窄窗")
    fig.suptitle("时频平面的多分辨率分析", fontsize=16, fontweight="bold")
    save(fig, "media-cognition-time-frequency.png")


def figure_self_attention() -> None:
    tokens = [r"$t_1$", r"$t_2$", r"$t_3$", r"$t_4$", r"$t_5$", r"$t_6$"]
    scores = np.array([-2.01, 3.06, -2.26, -2.26, 3.06, -2.01])
    weights = np.exp(scores - scores.max())
    weights /= weights.sum()

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.9), constrained_layout=True)
    ax = axes[0]
    positions = np.arange(len(tokens))
    for index, token in enumerate(tokens):
        ax.add_patch(patches.FancyBboxPatch((index - 0.34, -0.16), 0.68, 0.32, boxstyle="round,pad=0.04", facecolor=PALE_PURPLE, edgecolor=PURPLE))
        ax.text(index, 0, token, ha="center", va="center", fontsize=13)
    query_index = 0
    for target, weight in enumerate(weights):
        if target == query_index:
            continue
        arrow = FancyArrowPatch(
            (query_index, 0.2),
            (target, 0.2),
            connectionstyle=f"arc3,rad={0.18 if target < query_index else -0.18}",
            arrowstyle="->",
            mutation_scale=10,
            linewidth=0.7 + 5.0 * weight,
            color=TEAL,
            alpha=0.35 + 0.65 * weight / weights.max(),
        )
        ax.add_patch(arrow)
    ax.text(query_index, -0.46, "当前查询", ha="center", color=MUTED)
    ax.set(xlim=(-0.65, len(tokens) - 0.35), ylim=(-0.65, 1.1), xticks=[], yticks=[])
    ax.set_title("一个查询与所有键比较")
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax = axes[1]
    image = ax.imshow(np.vstack([scores, weights]), cmap="Purples", aspect="auto")
    ax.set_xticks(np.arange(len(tokens)), tokens)
    ax.set_yticks([0, 1], [r"点积 $h_{1i}$", r"权重 $s_{1i}$"])
    ax.set_xlabel("第 $i$ 个 Key/Value")
    ax.set_title(r"$s_{1i}=\mathrm{softmax}(h_{1i})$")
    for column, value in enumerate(scores):
        ax.text(column, 0, f"{value:.2f}", ha="center", va="center", color="white" if value > 1 else INK, fontsize=9)
    for column, value in enumerate(weights):
        ax.text(column, 1, f"{value:.2f}", ha="center", va="center", color=INK, fontsize=9)
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04, label="数值")
    fig.suptitle("缩放点积自注意力", fontsize=16, fontweight="bold")
    save(fig, "media-cognition-self-attention.png")


def figure_volume_rendering() -> None:
    fig, ax = plt.subplots(figsize=(11.5, 4.7), constrained_layout=True)
    camera = np.array([0.4, 0.8])
    direction = np.array([1.0, 0.22])
    direction /= np.linalg.norm(direction)
    distances = np.linspace(1.2, 8.4, 9)
    points = camera + distances[:, None] * direction
    density = np.exp(-0.5 * ((distances - 4.4) / 1.25) ** 2)
    colors = plt.cm.viridis(0.15 + 0.75 * density)

    ax.add_patch(patches.Circle(camera, 0.24, facecolor=INK, edgecolor=INK))
    ax.add_patch(patches.Polygon([[0.15, 0.15], [0.65, 0.15], [0.4, 0.55]], closed=True, facecolor=MUTED, alpha=0.65))
    ax.text(camera[0], -0.05, "相机", ha="center")
    end = camera + 9.2 * direction
    ax.add_patch(FancyArrowPatch(camera, end, arrowstyle="->", mutation_scale=13, linewidth=2.0, color=INK))

    transmittance = 1.0
    for index, (point, sigma, color) in enumerate(zip(points, density, colors), start=1):
        alpha = 1 - np.exp(-sigma * 0.75)
        weight = transmittance * alpha
        transmittance *= 1 - alpha
        ax.scatter([point[0]], [point[1]], s=50 + 380 * sigma, color=color, alpha=0.38 + 0.55 * sigma, edgecolor=INK, linewidth=0.5, zorder=3)
        ax.text(point[0], point[1] + 0.45, rf"$w_{index}={weight:.2f}$", ha="center", fontsize=9, color=MUTED)

    ax.text(4.8, 3.45, r"$\hat{C}(\mathbf{r})=\sum_i T_i\alpha_i\mathbf{c}_i$", ha="center", fontsize=15, color=PURPLE)
    ax.text(4.8, 3.03, r"$T_i=\prod_{j<i}(1-\alpha_j)$", ha="center", fontsize=13, color=PURPLE)
    ax.set(xlim=(-0.1, 9.8), ylim=(-0.4, 4.05), xticks=[], yticks=[])
    ax.set_title("NeRF 沿相机射线采样并按透射率合成颜色")
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "media-cognition-volume-rendering.png")


def main() -> None:
    figure_bias_variance()
    figure_activations()
    figure_pca_lda()
    figure_time_frequency_tiles()
    figure_self_attention()
    figure_volume_rendering()


if __name__ == "__main__":
    main()
