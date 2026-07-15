"""Generate the explanatory figures used by digital-signal-processing.md.

The figures use transparent backgrounds and a middle-gray structural palette so
that they remain readable with both light and dark documentation themes.  Run
the script from any working directory with an environment that provides NumPy
and Matplotlib, for example::

    conda run -n dsp python scripts/generate_dsp_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "assets"

# Mid-tone structure and saturated curves survive on both white and black
# pages.  Line styles repeat the color encoding for grayscale accessibility.
INK = "#747C87"
GRID = "#808894"
BLUE = "#2386C8"
ORANGE = "#E06B37"
TEAL = "#00968A"
PURPLE = "#8A62D3"
MAGENTA = "#C7447D"
CYAN = "#3ED8E3"

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Liberation Sans"],
        "font.size": 10.5,
        "axes.titlesize": 12,
        "axes.labelsize": 10.5,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.unicode_minus": False,
        "mathtext.fontset": "dejavusans",
    }
)


def clean_axes(ax: plt.Axes, *, grid: bool = True) -> None:
    """Apply the shared transparent, theme-neutral axis treatment."""

    ax.set_facecolor("none")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    if grid:
        ax.grid(True, color=GRID, linewidth=0.7, alpha=0.24)
        ax.set_axisbelow(True)


def save(fig: plt.Figure, filename: str) -> None:
    """Save a tightly cropped transparent PNG and close its figure."""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUT_DIR / filename,
        dpi=200,
        transparent=True,
        facecolor="none",
        edgecolor="none",
        bbox_inches="tight",
        pad_inches=0.12,
    )
    plt.close(fig)


def diagram_axes(ax: plt.Axes, title: str) -> None:
    """Prepare an axis for a transparent signal-flow diagram."""

    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.set_title(title, color=INK, pad=10)
    ax.set_axis_off()


def diagram_arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = INK,
    linewidth: float = 1.8,
) -> None:
    """Draw one directed signal path."""

    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={
            "arrowstyle": "-|>",
            "color": color,
            "linewidth": linewidth,
            "shrinkA": 0,
            "shrinkB": 0,
            "mutation_scale": 11,
        },
    )


def diagram_block(
    ax: plt.Axes,
    center: tuple[float, float],
    label: str,
    *,
    width: float = 0.16,
    height: float = 0.18,
    color: str = BLUE,
    fontsize: float = 11,
) -> None:
    """Draw a labeled processing block with a transparent fill."""

    x, y = center
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2),
        width,
        height,
        boxstyle="round,pad=0.015,rounding_size=0.018",
        facecolor="none",
        edgecolor=color,
        linewidth=1.9,
    )
    ax.add_patch(patch)
    ax.text(x, y, label, ha="center", va="center", color=color, fontsize=fontsize)


def diagram_node(
    ax: plt.Axes,
    center: tuple[float, float],
    label: str,
    *,
    color: str,
) -> None:
    """Draw a circular adder or subtractor node."""

    node = Circle(center, 0.047, facecolor="none", edgecolor=color, linewidth=1.9)
    ax.add_patch(node)
    ax.text(*center, label, ha="center", va="center", color=color, fontsize=13)


def triangular_spectrum(f: np.ndarray, center: float, bandwidth: float) -> np.ndarray:
    """Unit-height triangular spectrum centered at ``center``."""

    return np.maximum(1.0 - np.abs(f - center) / bandwidth, 0.0)


def draw_spectral_replicas(
    ax: plt.Axes,
    *,
    sampling_frequency: float,
    bandwidth: float,
    show_overlap: bool,
) -> None:
    f = np.linspace(-4.2, 4.2, 5000)
    centers = np.arange(-3, 4) * sampling_frequency
    components = np.vstack(
        [triangular_spectrum(f, center, bandwidth) for center in centers]
    )

    for center, component in zip(centers, components, strict=True):
        if np.max(component) == 0:
            continue
        central = np.isclose(center, 0.0)
        color = TEAL if central else ORANGE
        label = "baseband" if central else None
        if not central and np.isclose(center, sampling_frequency):
            label = "spectral replicas"
        ax.plot(f, component, color=color, linewidth=2.0, label=label)
        ax.fill_between(f, 0, component, color=color, alpha=0.08)

    if show_overlap:
        overlap = np.sum(components, axis=0) - np.max(components, axis=0)
        overlap = np.maximum(overlap, 0.0)
        ax.fill_between(
            f,
            0,
            overlap,
            where=overlap > 1e-4,
            color=PURPLE,
            alpha=0.38,
            label="overlap",
        )

    ax.axhline(0, color=INK, linewidth=0.8)
    ax.set(xlim=(-4.1, 4.1), ylim=(-0.03, 1.08), xlabel=r"normalized frequency $f/B$")
    ax.set_yticks([0, 0.5, 1.0])
    clean_axes(ax, grid=False)
    ax.legend(frameon=False, fontsize=8.5, loc="upper right", labelcolor=INK)


def figure_sampling_aliasing() -> None:
    t = np.linspace(-1.5, 1.5, 2400)
    fs = 3.0
    ts = np.arange(-1.5, 1.5 + 1 / fs, 1 / fs)

    def signal(time: np.ndarray) -> np.ndarray:
        return 0.72 * np.cos(2 * np.pi * 0.65 * time) + 0.25 * np.sin(
            2 * np.pi * 1.15 * time
        )

    fig, axes = plt.subplots(1, 3, figsize=(13.2, 3.7), constrained_layout=True)

    axes[0].plot(t, signal(t), color=BLUE, linewidth=2.1, label=r"$x_a(t)$")
    axes[0].vlines(ts, 0, signal(ts), color=ORANGE, linewidth=1.2, alpha=0.9)
    axes[0].scatter(
        ts,
        signal(ts),
        s=28,
        facecolor=ORANGE,
        edgecolor="none",
        zorder=3,
        label=r"$x_a(nT_s)$",
    )
    axes[0].axhline(0, color=INK, linewidth=0.8)
    axes[0].set(xlim=(-1.5, 1.5), ylim=(-1.08, 1.08), xlabel=r"time $t$", ylabel="amplitude")
    axes[0].set_title("Continuous signal and samples")
    clean_axes(axes[0])
    axes[0].legend(frameon=False, fontsize=8.5, loc="upper right", labelcolor=INK)

    draw_spectral_replicas(
        axes[1], sampling_frequency=2.55, bandwidth=1.0, show_overlap=False
    )
    axes[1].set_title(r"Separated replicas: $f_s>2B$")

    draw_spectral_replicas(
        axes[2], sampling_frequency=1.55, bandwidth=1.0, show_overlap=True
    )
    axes[2].set_title(r"Aliasing: $f_s<2B$")

    save(fig, "dsp_sampling_aliasing.png")


def figure_dirichlet_gibbs() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.0), constrained_layout=True)

    length = 21
    omega = np.linspace(-np.pi, np.pi, 16001)
    n = np.arange(length)
    response = np.exp(-1j * np.outer(omega, n)).sum(axis=1)
    magnitude = np.abs(response) / length
    x = omega / np.pi

    axes[0].plot(x, magnitude, color=BLUE, linewidth=2.0)
    axes[0].fill_between(x, 0, magnitude, color=BLUE, alpha=0.09)
    first_null = 2 / length
    for location in (-first_null, first_null):
        axes[0].axvline(location, color=ORANGE, linestyle="--", linewidth=1.2)
    axes[0].annotate(
        r"first nulls $\pm 2\pi/N$",
        xy=(first_null, 0.015),
        xytext=(0.24, 0.48),
        textcoords="axes fraction",
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[0].set(
        xlim=(-1, 1),
        ylim=(-0.02, 1.04),
        xlabel=r"$\omega/\pi$",
        ylabel=r"$|W_R(e^{j\omega})|/N$",
    )
    axes[0].set_title("Rectangular-window spectrum")
    clean_axes(axes[0])

    cutoff = 0.45 * np.pi
    half_length = 18
    impulse_index = np.arange(-half_length, half_length + 1)
    impulse_response = np.empty_like(impulse_index, dtype=float)
    impulse_response[impulse_index == 0] = cutoff / np.pi
    nonzero = impulse_index != 0
    impulse_response[nonzero] = np.sin(cutoff * impulse_index[nonzero]) / (
        np.pi * impulse_index[nonzero]
    )
    omega_positive = np.linspace(0, np.pi, 5000)
    truncated_response = np.cos(
        np.outer(omega_positive, impulse_index)
    ) @ impulse_response
    desired = (omega_positive <= cutoff).astype(float)

    axes[1].plot(
        omega_positive / np.pi,
        desired,
        color=INK,
        linestyle="--",
        linewidth=1.4,
        label="ideal response",
    )
    axes[1].plot(
        omega_positive / np.pi,
        truncated_response,
        color=ORANGE,
        linewidth=2.0,
        label="rectangular truncation",
    )
    axes[1].axvline(cutoff / np.pi, color=PURPLE, linestyle=":", linewidth=1.3)
    axes[1].annotate(
        "persistent edge ripple",
        xy=(cutoff / np.pi - 0.016, 1.085),
        xytext=(0.56, 0.82),
        textcoords="axes fraction",
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[1].set(
        xlim=(0, 1),
        ylim=(-0.14, 1.16),
        xlabel=r"$\omega/\pi$",
        ylabel="zero-phase response",
    )
    axes[1].set_title("Truncated ideal low-pass response")
    clean_axes(axes[1])
    axes[1].legend(frameon=False, fontsize=8.5, loc="lower left", labelcolor=INK)

    save(fig, "dsp_dirichlet_gibbs.png")


def normalized_window_spectrum(window: np.ndarray, fft_length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    spectrum = np.fft.rfft(window, fft_length)
    magnitude = np.abs(spectrum) / np.sum(window)
    frequency_bins = np.arange(spectrum.size) * len(window) / fft_length
    magnitude_db = 20 * np.log10(np.maximum(magnitude, 1e-6))
    return frequency_bins, magnitude, magnitude_db


def figure_window_tradeoff() -> None:
    length = 64
    fft_length = 65536
    windows = [
        ("Rectangular", np.ones(length), BLUE, "-"),
        ("Bartlett", np.bartlett(length), ORANGE, "--"),
        ("Hann", np.hanning(length), TEAL, "-."),
        ("Hamming", np.hamming(length), PURPLE, ":"),
        ("Blackman", np.blackman(length), MAGENTA, (0, (5, 1))),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.2), constrained_layout=True)
    for name, window, color, linestyle in windows:
        bins, magnitude, magnitude_db = normalized_window_spectrum(window, fft_length)
        axes[0].plot(
            bins,
            magnitude,
            color=color,
            linestyle=linestyle,
            linewidth=1.9,
            label=name,
        )
        axes[1].plot(
            bins,
            magnitude_db,
            color=color,
            linestyle=linestyle,
            linewidth=1.7,
            label=name,
        )

    axes[0].set(
        xlim=(0, 4),
        ylim=(-0.02, 1.03),
        xlabel=r"frequency offset $M\omega/(2\pi)$",
        ylabel="normalized magnitude",
    )
    axes[0].set_title("Main-lobe width")
    clean_axes(axes[0])

    axes[1].set(
        xlim=(0.4, 20),
        ylim=(-100, 3),
        xlabel=r"frequency offset $M\omega/(2\pi)$",
        ylabel="magnitude (dB)",
    )
    axes[1].set_title("Side-lobe suppression")
    clean_axes(axes[1])
    axes[1].legend(
        frameon=False,
        fontsize=8.3,
        loc="upper right",
        ncol=2,
        labelcolor=INK,
    )

    save(fig, "dsp_window_tradeoff.png")


def stft(
    signal: np.ndarray,
    *,
    sampling_frequency: float,
    frame_length: int,
    hop_length: int,
    fft_length: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    window = np.hanning(frame_length)
    starts = np.arange(0, len(signal) - frame_length + 1, hop_length)
    spectra = np.empty((len(starts), fft_length // 2 + 1), dtype=float)
    for row, start in enumerate(starts):
        frame = signal[start : start + frame_length] * window
        spectra[row] = np.abs(np.fft.rfft(frame, fft_length))
    times = (starts + frame_length / 2) / sampling_frequency
    frequencies = np.fft.rfftfreq(fft_length, 1 / sampling_frequency)
    spectra /= np.max(spectra)
    spectra_db = 20 * np.log10(np.maximum(spectra, 10 ** (-70 / 20)))
    return times, frequencies, spectra_db


def figure_stft_chirp() -> None:
    sampling_frequency = 800.0
    duration = 2.0
    start_frequency = 45.0
    end_frequency = 285.0
    chirp_rate = (end_frequency - start_frequency) / duration
    t = np.arange(int(duration * sampling_frequency)) / sampling_frequency
    phase = 2 * np.pi * (start_frequency * t + 0.5 * chirp_rate * t**2)
    signal = np.sin(phase)

    times, frequencies, spectra_db = stft(
        signal,
        sampling_frequency=sampling_frequency,
        frame_length=128,
        hop_length=16,
        fft_length=256,
    )

    fig, ax = plt.subplots(figsize=(10.8, 4.7), constrained_layout=True)
    mesh = ax.pcolormesh(
        times,
        frequencies,
        spectra_db.T,
        shading="gouraud",
        cmap="magma",
        vmin=-65,
        vmax=0,
        rasterized=True,
    )
    expected = start_frequency + chirp_rate * times
    ax.plot(
        times,
        expected,
        color=CYAN,
        linestyle="--",
        linewidth=1.6,
        label="instantaneous frequency",
    )
    ax.set(
        xlim=(times[0], times[-1]),
        ylim=(0, 360),
        xlabel="time (s)",
        ylabel="frequency (Hz)",
    )
    ax.set_title("STFT of a linear chirp")
    clean_axes(ax, grid=False)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left", labelcolor=INK)
    colorbar = fig.colorbar(mesh, ax=ax, pad=0.018, aspect=28)
    colorbar.set_label("relative magnitude (dB)", color=INK)
    colorbar.ax.tick_params(colors=INK)
    colorbar.outline.set_edgecolor(INK)

    save(fig, "dsp_stft_chirp.png")


def figure_zero_pole_response() -> None:
    zero_angle = 0.66 * np.pi
    pole_angle = 0.24 * np.pi
    zeros = np.array(
        [0.98 * np.exp(1j * zero_angle), 0.98 * np.exp(-1j * zero_angle)]
    )
    poles = np.array(
        [0.90 * np.exp(1j * pole_angle), 0.90 * np.exp(-1j * pole_angle)]
    )

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.4), constrained_layout=True)

    circle_angle = np.linspace(0, 2 * np.pi, 800)
    axes[0].plot(
        np.cos(circle_angle),
        np.sin(circle_angle),
        color=INK,
        linestyle="--",
        linewidth=1.2,
        label="unit circle",
    )
    axes[0].axhline(0, color=INK, linewidth=0.8)
    axes[0].axvline(0, color=INK, linewidth=0.8)
    axes[0].scatter(
        zeros.real,
        zeros.imag,
        s=100,
        facecolor="none",
        edgecolor=TEAL,
        linewidth=2.2,
        label="zeros",
        zorder=3,
    )
    axes[0].scatter(
        poles.real,
        poles.imag,
        s=100,
        marker="x",
        color=ORANGE,
        linewidth=2.2,
        label="poles",
        zorder=3,
    )
    axes[0].set(
        xlim=(-1.24, 1.24),
        ylim=(-1.24, 1.24),
        xlabel=r"$\operatorname{Re}\{z\}$",
        ylabel=r"$\operatorname{Im}\{z\}$",
    )
    axes[0].set_aspect("equal", adjustable="box")
    axes[0].set_title("Pole-zero geometry")
    clean_axes(axes[0], grid=False)
    axes[0].legend(frameon=False, fontsize=8.5, loc="upper left", labelcolor=INK)

    omega = np.linspace(0, np.pi, 5000)
    unit_circle = np.exp(1j * omega)
    numerator = np.prod(unit_circle[:, None] - zeros[None, :], axis=1)
    denominator = np.prod(unit_circle[:, None] - poles[None, :], axis=1)
    magnitude = np.abs(numerator / denominator)
    magnitude_db = 20 * np.log10(np.maximum(magnitude / np.max(magnitude), 1e-4))

    axes[1].plot(omega / np.pi, magnitude_db, color=BLUE, linewidth=2.1)
    axes[1].axvline(
        pole_angle / np.pi,
        color=ORANGE,
        linestyle="--",
        linewidth=1.2,
        label="pole angle",
    )
    axes[1].axvline(
        zero_angle / np.pi,
        color=TEAL,
        linestyle=":",
        linewidth=1.5,
        label="zero angle",
    )
    axes[1].annotate(
        "resonance",
        xy=(pole_angle / np.pi, magnitude_db[np.argmin(np.abs(omega - pole_angle))]),
        xytext=(0.31, -10),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[1].annotate(
        "deep attenuation",
        xy=(zero_angle / np.pi, magnitude_db[np.argmin(np.abs(omega - zero_angle))]),
        xytext=(0.70, -55),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[1].set(
        xlim=(0, 1),
        ylim=(-80, 3),
        xlabel=r"$\omega/\pi$",
        ylabel=r"$20\log_{10}|H(e^{j\omega})|$ (dB)",
    )
    axes[1].set_title("Response on the unit circle")
    clean_axes(axes[1])
    axes[1].legend(frameon=False, fontsize=8.5, loc="lower left", labelcolor=INK)

    save(fig, "dsp_zero_pole_response.png")


def uniform_quantize(signal: np.ndarray, bits: int) -> tuple[np.ndarray, float]:
    """Quantize a normalized signal with a mid-tread uniform quantizer."""

    step = 2.0 / 2**bits
    quantized = np.round(signal / step) * step
    return np.clip(quantized, -1.0, 1.0 - step), step


def figure_quantization_noise() -> None:
    sample_index = np.arange(0, 201)
    signal = 0.99 * np.cos(sample_index / 10)
    quantized_3, step_3 = uniform_quantize(signal, 3)
    quantized_8, step_8 = uniform_quantize(signal, 8)
    error_3 = quantized_3 - signal
    error_8 = quantized_8 - signal

    fig = plt.figure(figsize=(11.2, 6.5), constrained_layout=True)
    grid = fig.add_gridspec(2, 2, height_ratios=(1.25, 1.0))
    signal_axis = fig.add_subplot(grid[0, :])
    error_3_axis = fig.add_subplot(grid[1, 0])
    error_8_axis = fig.add_subplot(grid[1, 1])

    signal_axis.plot(
        sample_index,
        signal,
        color=BLUE,
        linewidth=2.0,
        label="original samples",
        zorder=3,
    )
    signal_axis.step(
        sample_index,
        quantized_3,
        where="post",
        color=ORANGE,
        linewidth=1.5,
        label="3-bit quantized value",
    )
    signal_axis.scatter(
        sample_index,
        quantized_3,
        s=12,
        color=ORANGE,
        edgecolor="none",
        zorder=4,
    )
    signal_axis.axhline(0, color=INK, linewidth=0.8)
    signal_axis.set(
        xlim=(0, 80),
        ylim=(-1.02, 1.02),
        xlabel=r"sample index $n$",
        ylabel="normalized amplitude",
    )
    signal_axis.set_title(r"Uniform quantization of $x[n]=0.99\cos(n/10)$")
    clean_axes(signal_axis)
    signal_axis.legend(
        frameon=False, fontsize=8.7, loc="upper right", labelcolor=INK
    )

    error_panels = [
        (error_3_axis, error_3, step_3, ORANGE, "3-bit error"),
        (error_8_axis, error_8, step_8, TEAL, "8-bit error"),
    ]
    for axis, error, step, color, title in error_panels:
        axis.plot(sample_index, error, color=color, linewidth=1.25)
        axis.scatter(
            sample_index,
            error,
            s=9,
            color=color,
            edgecolor="none",
            alpha=0.85,
        )
        axis.axhline(step / 2, color=INK, linestyle="--", linewidth=1.0)
        axis.axhline(-step / 2, color=INK, linestyle="--", linewidth=1.0)
        axis.set(
            xlim=(0, 200),
            ylim=(-0.56 * step, 0.56 * step),
            xlabel=r"sample index $n$",
            ylabel=r"error $e_q$",
        )
        axis.set_title(title + rf": $\Delta={step:.7g}$")
        clean_axes(axis)

    error_3_axis.annotate(
        r"$|e_q|\leq\Delta/2$",
        xy=(125, step_3 / 2),
        xytext=(88, 0.035),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    error_8_axis.annotate(
        r"$\Delta_{8}=\Delta_{3}/32$",
        xy=(125, step_8 / 2),
        xytext=(70, 0.0017),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )

    save(fig, "dsp_quantization_noise.png")


def wrap_to_pi(angle: np.ndarray) -> np.ndarray:
    return (angle + np.pi) % (2 * np.pi) - np.pi


def illustrative_spectrum(angle: np.ndarray) -> np.ndarray:
    """A periodic spectrum with appreciable energy beyond pi/3."""

    wrapped = wrap_to_pi(angle)
    center = 0.72 * np.exp(-0.5 * (wrapped / (0.22 * np.pi)) ** 2)
    outer = 0.54 * np.exp(
        -0.5 * ((np.abs(wrapped) - 0.56 * np.pi) / (0.105 * np.pi)) ** 2
    )
    spectrum = np.where(np.abs(wrapped) <= 0.84 * np.pi, center + outer, 0.0)
    return spectrum / 0.72


def anti_alias_spectrum(angle: np.ndarray, factor: int) -> np.ndarray:
    wrapped = wrap_to_pi(angle)
    magnitude = illustrative_spectrum(wrapped)
    pass_edge = 0.27 * np.pi
    stop_edge = np.pi / factor
    taper = np.ones_like(wrapped)
    taper[np.abs(wrapped) >= stop_edge] = 0.0
    transition = (np.abs(wrapped) > pass_edge) & (
        np.abs(wrapped) < stop_edge
    )
    taper[transition] = 0.5 * (
        1
        + np.cos(
            np.pi
            * (np.abs(wrapped[transition]) - pass_edge)
            / (stop_edge - pass_edge)
        )
    )
    return magnitude * taper


def decimation_components(
    omega: np.ndarray, factor: int, spectrum_function
) -> np.ndarray:
    return np.vstack(
        [
            spectrum_function((omega - 2 * np.pi * branch) / factor) / factor
            for branch in range(factor)
        ]
    )


def figure_multirate_spectra() -> None:
    factor = 3
    omega = np.linspace(-np.pi, np.pi, 6001)
    original = illustrative_spectrum(omega)
    direct_components = decimation_components(
        omega, factor, illustrative_spectrum
    )
    direct_output = np.sum(direct_components, axis=0)
    filtered_components = decimation_components(
        omega,
        factor,
        lambda angle: anti_alias_spectrum(angle, factor),
    )
    filtered_output = np.sum(filtered_components, axis=0)

    fig, axes = plt.subplots(
        3,
        1,
        figsize=(10.8, 7.4),
        sharex=True,
        constrained_layout=True,
    )
    x = omega / np.pi

    axes[0].plot(x, original, color=BLUE, linewidth=2.1)
    axes[0].fill_between(x, 0, original, color=BLUE, alpha=0.07)
    for cutoff in (-1 / factor, 1 / factor):
        axes[0].axvline(
            cutoff,
            color=ORANGE,
            linestyle="--",
            linewidth=1.2,
        )
    axes[0].annotate(
        r"anti-alias cutoff $\pi/M$",
        xy=(1 / factor, 0.45),
        xytext=(0.49, 0.80),
        textcoords="axes fraction",
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[0].set(ylim=(-0.02, 1.08), ylabel=r"$|X(e^{j\omega})|$")
    axes[0].set_title("Original spectrum")
    clean_axes(axes[0])

    component_colors = (BLUE, ORANGE, TEAL)
    component_styles = ("-", "--", "-.")
    for branch, (component, color, linestyle) in enumerate(
        zip(
            direct_components,
            component_colors,
            component_styles,
            strict=True,
        )
    ):
        axes[1].plot(
            x,
            component,
            color=color,
            linestyle=linestyle,
            linewidth=1.45,
            label=rf"copy $k={branch}$",
        )
        axes[1].fill_between(x, 0, component, color=color, alpha=0.045)
    axes[1].plot(
        x,
        direct_output,
        color=MAGENTA,
        linewidth=2.35,
        label="aliased sum",
        zorder=4,
    )
    axes[1].set(
        ylim=(-0.01, 1.13 * np.max(direct_output)),
        ylabel=r"$|Y(e^{j\omega})|$",
    )
    axes[1].set_title(r"Direct $\downarrow 3$: compressed copies overlap")
    clean_axes(axes[1])
    axes[1].legend(
        frameon=False,
        fontsize=8.3,
        loc="upper right",
        ncol=4,
        labelcolor=INK,
    )

    axes[2].plot(
        x,
        filtered_output,
        color=TEAL,
        linewidth=2.25,
        label="alias-free output",
    )
    axes[2].fill_between(
        x,
        0,
        filtered_output,
        color=TEAL,
        alpha=0.07,
    )
    axes[2].set(
        xlim=(-1, 1),
        ylim=(-0.01, 1.14 * np.max(filtered_output)),
        xlabel=r"normalized frequency $\omega/\pi$",
        ylabel=r"$|Y_{aa}(e^{j\omega})|$",
    )
    axes[2].set_title(
        r"Low-pass to $|\omega|\leq\pi/3$ before $\downarrow 3$: no overlap"
    )
    clean_axes(axes[2])
    axes[2].legend(
        frameon=False, fontsize=8.5, loc="upper right", labelcolor=INK
    )

    save(fig, "dsp_multirate_spectra.png")


def figure_noise_shaping() -> None:
    oversampling_ratio = 8
    cutoff = 1 / oversampling_ratio
    normalized_frequency = np.linspace(0, 1, 5000)
    white_psd = np.ones_like(normalized_frequency)
    retained_psd = np.where(normalized_frequency <= cutoff, 1.0, 0.0)

    omega = np.pi * normalized_frequency
    shaped_psd = 4 * np.sin(omega / 2) ** 2
    shaped_psd_db = 10 * np.log10(np.maximum(shaped_psd, 1e-6))

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.25), constrained_layout=True)

    axes[0].plot(
        normalized_frequency,
        white_psd,
        color=INK,
        linestyle="--",
        linewidth=1.5,
        label="white quantization-noise PSD",
    )
    axes[0].step(
        normalized_frequency,
        retained_psd,
        where="post",
        color=BLUE,
        linewidth=2.1,
        label="after ideal low-pass",
    )
    axes[0].fill_between(
        normalized_frequency,
        0,
        retained_psd,
        step="post",
        color=BLUE,
        alpha=0.10,
    )
    axes[0].axvline(cutoff, color=ORANGE, linestyle=":", linewidth=1.5)
    axes[0].annotate(
        r"retained band $0\leq\omega\leq\pi/OSR$",
        xy=(cutoff * 0.55, 0.50),
        xytext=(0.29, 0.39),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[0].set(
        xlim=(0, 1),
        ylim=(-0.04, 1.13),
        xlabel=r"$\omega/\pi$",
        ylabel="normalized PSD",
    )
    axes[0].set_title(r"Oversampling and low-pass filtering ($OSR=8$)")
    clean_axes(axes[0])
    axes[0].legend(
        frameon=False, fontsize=8.4, loc="upper right", labelcolor=INK
    )

    axes[1].axvspan(0, cutoff, color=TEAL, alpha=0.08, label="retained band")
    axes[1].plot(
        normalized_frequency,
        np.zeros_like(normalized_frequency),
        color=INK,
        linestyle="--",
        linewidth=1.5,
        label="white PSD",
    )
    axes[1].plot(
        normalized_frequency,
        shaped_psd_db,
        color=MAGENTA,
        linewidth=2.1,
        label=r"first-order $\Delta\Sigma$ PSD",
    )
    axes[1].axvline(cutoff, color=ORANGE, linestyle=":", linewidth=1.5)
    axes[1].annotate(
        r"$|NTF(e^{j\omega})|^2=|1-e^{-j\omega}|^2$",
        xy=(0.30, shaped_psd_db[np.argmin(np.abs(normalized_frequency - 0.30))]),
        xytext=(0.42, -24),
        arrowprops={"arrowstyle": "->", "color": INK, "linewidth": 0.9},
        color=INK,
    )
    axes[1].set(
        xlim=(0, 1),
        ylim=(-60, 8),
        xlabel=r"$\omega/\pi$",
        ylabel="noise PSD (dB, relative)",
    )
    axes[1].set_title("First-order high-pass noise shaping")
    clean_axes(axes[1])
    axes[1].legend(
        frameon=False, fontsize=8.3, loc="lower right", labelcolor=INK
    )

    save(fig, "dsp_noise_shaping.png")


def figure_fft_butterflies() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.2), constrained_layout=True)

    dit = axes[0]
    diagram_axes(dit, "Radix-2 DIT butterfly")
    upper_y, lower_y = 0.72, 0.28
    dit.text(0.01, upper_y, r"$E[k]$", ha="left", va="center", color=BLUE, fontsize=11)
    dit.text(0.01, lower_y, r"$O[k]$", ha="left", va="center", color=ORANGE, fontsize=11)
    diagram_arrow(dit, (0.13, upper_y), (0.67, upper_y), color=BLUE)
    diagram_arrow(dit, (0.13, upper_y), (0.67, lower_y), color=BLUE)
    diagram_arrow(dit, (0.13, lower_y), (0.22, lower_y), color=ORANGE)
    diagram_block(
        dit,
        (0.31, lower_y),
        r"$W_N^k$",
        width=0.16,
        height=0.16,
        color=ORANGE,
    )
    diagram_arrow(dit, (0.40, lower_y), (0.67, upper_y), color=ORANGE)
    diagram_arrow(dit, (0.40, lower_y), (0.67, lower_y), color=ORANGE)
    diagram_node(dit, (0.72, upper_y), "+", color=TEAL)
    diagram_node(dit, (0.72, lower_y), "-", color=PURPLE)
    diagram_arrow(dit, (0.77, upper_y), (0.95, upper_y), color=TEAL)
    diagram_arrow(dit, (0.77, lower_y), (0.95, lower_y), color=PURPLE)
    dit.text(
        0.99,
        upper_y,
        r"$X[k]$",
        ha="right",
        va="bottom",
        color=TEAL,
        fontsize=11,
    )
    dit.text(
        0.99,
        lower_y,
        r"$X[k+N/2]$",
        ha="right",
        va="bottom",
        color=PURPLE,
        fontsize=11,
    )
    dit.text(
        0.31,
        0.10,
        "twiddle before add/subtract",
        ha="center",
        color=INK,
        fontsize=9,
    )

    dif = axes[1]
    diagram_axes(dif, "Radix-2 DIF butterfly")
    dif.text(0.01, upper_y, r"$x[n]$", ha="left", va="center", color=BLUE, fontsize=10.5)
    dif.text(0.01, lower_y, r"$x[n+N/2]$", ha="left", va="center", color=ORANGE, fontsize=10.5)
    diagram_arrow(dif, (0.18, upper_y), (0.40, upper_y), color=BLUE)
    diagram_arrow(dif, (0.18, upper_y), (0.40, lower_y), color=BLUE)
    diagram_arrow(dif, (0.18, lower_y), (0.40, upper_y), color=ORANGE)
    diagram_arrow(dif, (0.18, lower_y), (0.40, lower_y), color=ORANGE)
    diagram_node(dif, (0.45, upper_y), "+", color=TEAL)
    diagram_node(dif, (0.45, lower_y), "-", color=PURPLE)
    diagram_arrow(dif, (0.50, upper_y), (0.95, upper_y), color=TEAL)
    diagram_arrow(dif, (0.50, lower_y), (0.62, lower_y), color=PURPLE)
    diagram_block(
        dif,
        (0.71, lower_y),
        r"$W_N^n$",
        width=0.16,
        height=0.16,
        color=ORANGE,
    )
    diagram_arrow(dif, (0.80, lower_y), (0.95, lower_y), color=ORANGE)
    dif.text(
        0.99,
        upper_y,
        r"$g_1[n]$",
        ha="right",
        va="bottom",
        color=TEAL,
        fontsize=11,
    )
    dif.text(
        0.99,
        lower_y,
        r"$g_2[n]$",
        ha="right",
        va="bottom",
        color=ORANGE,
        fontsize=11,
    )
    dif.text(
        0.71,
        0.10,
        "twiddle after add/subtract",
        ha="center",
        color=INK,
        fontsize=9,
    )

    save(fig, "dsp_fft_butterflies.png")


def figure_multirate_blocks() -> None:
    fig, ax = plt.subplots(figsize=(11.8, 6.4), constrained_layout=True)
    diagram_axes(ax, "Basic multirate processing chains")

    rows = (0.79, 0.50, 0.21)
    ax.text(0.02, 0.91, "Decimation", color=INK, fontsize=11, weight="bold")
    ax.text(0.02, 0.62, "Interpolation", color=INK, fontsize=11, weight="bold")
    ax.text(0.02, 0.33, "Rational rate conversion", color=INK, fontsize=11, weight="bold")

    y = rows[0]
    ax.text(0.03, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=11)
    diagram_arrow(ax, (0.10, y), (0.26, y))
    diagram_block(ax, (0.35, y), r"$H_{aa}(z)$", color=BLUE)
    diagram_arrow(ax, (0.44, y), (0.55, y))
    diagram_block(ax, (0.63, y), r"$\downarrow M$", width=0.14, color=ORANGE)
    diagram_arrow(ax, (0.71, y), (0.94, y))
    ax.text(0.97, y, r"$y[n]$", ha="right", va="center", color=INK, fontsize=11)
    ax.text(0.35, y - 0.13, "anti-alias LPF", ha="center", color=INK, fontsize=9)
    ax.text(0.17, y - 0.07, r"$f_s$", ha="center", color=INK, fontsize=9)
    ax.text(0.83, y - 0.07, r"$f_s/M$", ha="center", color=INK, fontsize=9)

    y = rows[1]
    ax.text(0.03, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=11)
    diagram_arrow(ax, (0.10, y), (0.25, y))
    diagram_block(ax, (0.33, y), r"$\uparrow L$", width=0.14, color=TEAL)
    diagram_arrow(ax, (0.41, y), (0.55, y))
    diagram_block(ax, (0.64, y), r"$H_i(z)$", color=BLUE)
    diagram_arrow(ax, (0.73, y), (0.94, y))
    ax.text(0.97, y, r"$y[n]$", ha="right", va="center", color=INK, fontsize=11)
    ax.text(0.64, y - 0.13, "anti-image LPF, gain $L$", ha="center", color=INK, fontsize=9)
    ax.text(0.17, y - 0.07, r"$f_s$", ha="center", color=INK, fontsize=9)
    ax.text(0.84, y - 0.07, r"$Lf_s$", ha="center", color=INK, fontsize=9)

    y = rows[2]
    ax.text(0.03, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=11)
    diagram_arrow(ax, (0.10, y), (0.20, y))
    diagram_block(ax, (0.28, y), r"$\uparrow L$", width=0.14, color=TEAL)
    diagram_arrow(ax, (0.36, y), (0.44, y))
    diagram_block(ax, (0.53, y), r"$H(z)$", color=BLUE)
    diagram_arrow(ax, (0.62, y), (0.70, y))
    diagram_block(ax, (0.78, y), r"$\downarrow M$", width=0.14, color=ORANGE)
    diagram_arrow(ax, (0.86, y), (0.94, y))
    ax.text(0.97, y, r"$y[n]$", ha="right", va="center", color=INK, fontsize=11)
    ax.text(
        0.53,
        y - 0.13,
        r"cutoff $\min(\pi/L,\pi/M)$",
        ha="center",
        color=INK,
        fontsize=9,
    )
    ax.text(0.15, y - 0.07, r"$f_s$", ha="center", color=INK, fontsize=9)
    ax.text(0.91, y - 0.07, r"$Lf_s/M$", ha="center", color=INK, fontsize=9)

    save(fig, "dsp_multirate_blocks.png")


def figure_noble_identities() -> None:
    fig, axes = plt.subplots(2, 1, figsize=(11.8, 5.8), constrained_layout=True)

    down = axes[0]
    diagram_axes(down, "Noble identity for decimation")
    y = 0.52
    down.text(0.01, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=10)
    diagram_arrow(down, (0.07, y), (0.11, y))
    diagram_block(down, (0.20, y), r"$H(z^M)$", color=BLUE)
    diagram_arrow(down, (0.29, y), (0.34, y))
    diagram_block(down, (0.41, y), r"$\downarrow M$", width=0.13, color=ORANGE)
    diagram_arrow(down, (0.48, y), (0.49, y))
    down.text(0.50, y, r"$\equiv$", ha="center", va="center", color=INK, fontsize=18)
    diagram_arrow(down, (0.53, y), (0.57, y))
    diagram_block(down, (0.64, y), r"$\downarrow M$", width=0.13, color=ORANGE)
    diagram_arrow(down, (0.71, y), (0.76, y))
    diagram_block(down, (0.85, y), r"$H(z)$", color=BLUE)
    diagram_arrow(down, (0.94, y), (0.99, y))
    down.text(0.25, 0.24, "filter at the high rate", ha="center", color=INK, fontsize=9)
    down.text(0.80, 0.24, "filter at the low rate", ha="center", color=INK, fontsize=9)

    up = axes[1]
    diagram_axes(up, "Noble identity for interpolation")
    up.text(0.01, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=10)
    diagram_arrow(up, (0.07, y), (0.11, y))
    diagram_block(up, (0.20, y), r"$H(z)$", color=BLUE)
    diagram_arrow(up, (0.29, y), (0.34, y))
    diagram_block(up, (0.41, y), r"$\uparrow L$", width=0.13, color=TEAL)
    diagram_arrow(up, (0.48, y), (0.49, y))
    up.text(0.50, y, r"$\equiv$", ha="center", va="center", color=INK, fontsize=18)
    diagram_arrow(up, (0.53, y), (0.57, y))
    diagram_block(up, (0.64, y), r"$\uparrow L$", width=0.13, color=TEAL)
    diagram_arrow(up, (0.71, y), (0.76, y))
    diagram_block(up, (0.85, y), r"$H(z^L)$", color=BLUE)
    diagram_arrow(up, (0.94, y), (0.99, y))
    up.text(0.25, 0.24, "filter at the low rate", ha="center", color=INK, fontsize=9)
    up.text(0.80, 0.24, "expanded filter at the high rate", ha="center", color=INK, fontsize=9)

    save(fig, "dsp_noble_identities.png")


def draw_fft_stage(
    ax: plt.Axes,
    x_start: float,
    x_end: float,
    y_positions: np.ndarray,
    pairs: list[tuple[int, int]],
    twiddles: list[str],
) -> None:
    """Draw one radix-2 DIT stage in an eight-point signal-flow graph."""

    for (upper, lower), twiddle in zip(pairs, twiddles, strict=True):
        y_upper = y_positions[upper]
        y_lower = y_positions[lower]
        ax.plot([x_start, x_end], [y_upper, y_upper], color=BLUE, linewidth=1.35)
        ax.plot([x_start, x_end], [y_upper, y_lower], color=BLUE, linewidth=1.20)
        ax.plot([x_start, x_end], [y_lower, y_upper], color=ORANGE, linewidth=1.20)
        ax.plot([x_start, x_end], [y_lower, y_lower], color=ORANGE, linewidth=1.35)
        ax.text(
            x_start + 0.035,
            y_lower - 0.020,
            twiddle,
            ha="left",
            va="top",
            color=ORANGE,
            fontsize=7.2,
        )
        ax.text(
            x_end - 0.022,
            y_lower + 0.012,
            r"$-1$",
            ha="right",
            va="bottom",
            color=PURPLE,
            fontsize=7.2,
        )


def figure_fft_8point_flow() -> None:
    fig, ax = plt.subplots(figsize=(12.2, 6.5), constrained_layout=True)
    diagram_axes(ax, "Eight-point radix-2 DIT FFT signal flow")

    y_positions = np.linspace(0.86, 0.14, 8)
    x_columns = (0.12, 0.38, 0.64, 0.90)
    input_order = (0, 4, 2, 6, 1, 5, 3, 7)

    for row, (y, index) in enumerate(zip(y_positions, input_order, strict=True)):
        ax.text(
            0.02,
            y,
            rf"$x[{index}]$",
            ha="left",
            va="center",
            color=INK,
            fontsize=9.5,
        )
        diagram_arrow(ax, (0.08, y), (x_columns[0], y), linewidth=1.15)
        diagram_arrow(ax, (x_columns[-1], y), (0.96, y), linewidth=1.15)
        ax.text(
            0.99,
            y,
            rf"$X[{row}]$",
            ha="right",
            va="center",
            color=INK,
            fontsize=9.5,
        )

    draw_fft_stage(
        ax,
        x_columns[0],
        x_columns[1],
        y_positions,
        [(0, 1), (2, 3), (4, 5), (6, 7)],
        [r"$W_2^0$"] * 4,
    )
    draw_fft_stage(
        ax,
        x_columns[1],
        x_columns[2],
        y_positions,
        [(0, 2), (1, 3), (4, 6), (5, 7)],
        [r"$W_4^0$", r"$W_4^1$", r"$W_4^0$", r"$W_4^1$"],
    )
    draw_fft_stage(
        ax,
        x_columns[2],
        x_columns[3],
        y_positions,
        [(0, 4), (1, 5), (2, 6), (3, 7)],
        [r"$W_8^0$", r"$W_8^1$", r"$W_8^2$", r"$W_8^3$"],
    )

    for x in x_columns:
        ax.scatter(
            np.full_like(y_positions, x),
            y_positions,
            s=17,
            facecolor="none",
            edgecolor=INK,
            linewidth=0.9,
            zorder=5,
        )

    ax.text(0.06, 0.96, "bit-reversed input", ha="center", color=INK, fontsize=9)
    ax.text(0.25, 0.96, r"stage 1: $W_2^0$", ha="center", color=INK, fontsize=9)
    ax.text(0.51, 0.96, r"stage 2: $W_4^{0,1}$", ha="center", color=INK, fontsize=9)
    ax.text(0.77, 0.96, r"stage 3: $W_8^{0,1,2,3}$", ha="center", color=INK, fontsize=9)
    ax.text(0.96, 0.96, "natural output", ha="center", color=INK, fontsize=9)
    ax.text(
        0.50,
        0.035,
        "blue: upper contribution   orange: twiddled lower contribution   purple: difference sign",
        ha="center",
        color=INK,
        fontsize=8.3,
    )

    save(fig, "dsp_fft_8point_flow.png")


def figure_polyphase_decimator() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.2), constrained_layout=True)

    direct = axes[0]
    diagram_axes(direct, "Direct decimator")
    y = 0.55
    direct.text(0.02, y, r"$x[n]$", ha="left", va="center", color=INK, fontsize=11)
    diagram_arrow(direct, (0.11, y), (0.23, y))
    diagram_block(direct, (0.36, y), r"$H(z)$", width=0.22, color=BLUE)
    diagram_arrow(direct, (0.48, y), (0.61, y))
    diagram_block(direct, (0.72, y), r"$\downarrow M$", width=0.18, color=ORANGE)
    diagram_arrow(direct, (0.82, y), (0.95, y))
    direct.text(0.99, y, r"$w[n]$", ha="right", va="center", color=INK, fontsize=11)
    direct.text(0.36, 0.31, "long FIR at the input rate", ha="center", color=INK, fontsize=9)

    poly = axes[1]
    diagram_axes(poly, "Polyphase decimator")
    branch_y = (0.81, 0.62, 0.38, 0.19)
    delay_labels = (r"$1$", r"$z^{-1}$", r"$\vdots$", r"$z^{-(M-1)}$")
    filter_labels = (r"$H_0(z)$", r"$H_1(z)$", r"$\vdots$", r"$H_{M-1}(z)$")

    poly.text(0.01, 0.50, r"$x[n]$", ha="left", va="center", color=INK, fontsize=10)
    diagram_arrow(poly, (0.08, 0.50), (0.14, 0.50))
    poly.plot([0.14, 0.14], [branch_y[-1], branch_y[0]], color=INK, linewidth=1.3)
    for y_branch, delay_label, filter_label in zip(
        branch_y, delay_labels, filter_labels, strict=True
    ):
        poly.plot([0.14, 0.20], [y_branch, y_branch], color=INK, linewidth=1.3)
        if delay_label == r"$\vdots$":
            poly.text(0.27, y_branch, delay_label, ha="center", va="center", color=INK, fontsize=14)
            poly.text(0.48, y_branch, r"$\vdots$", ha="center", va="center", color=INK, fontsize=14)
            poly.text(0.70, y_branch, filter_label, ha="center", va="center", color=INK, fontsize=14)
            continue
        diagram_block(
            poly,
            (0.27, y_branch),
            delay_label,
            width=0.12,
            height=0.12,
            color=PURPLE,
            fontsize=9,
        )
        diagram_arrow(poly, (0.34, y_branch), (0.41, y_branch), linewidth=1.15)
        diagram_block(
            poly,
            (0.48, y_branch),
            r"$\downarrow M$",
            width=0.12,
            height=0.12,
            color=ORANGE,
            fontsize=9,
        )
        diagram_arrow(poly, (0.55, y_branch), (0.61, y_branch), linewidth=1.15)
        diagram_block(
            poly,
            (0.70, y_branch),
            filter_label,
            width=0.15,
            height=0.12,
            color=BLUE,
            fontsize=9,
        )
        diagram_arrow(poly, (0.785, y_branch), (0.86, 0.50), linewidth=1.15)

    diagram_node(poly, (0.88, 0.50), "+", color=TEAL)
    diagram_arrow(poly, (0.93, 0.50), (0.98, 0.50), color=TEAL, linewidth=1.3)
    poly.text(0.99, 0.50, r"$w[n]$", ha="right", va="bottom", color=INK, fontsize=10)
    poly.text(
        0.61,
        0.06,
        r"$H(z)=\sum_{m=0}^{M-1}z^{-m}H_m(z^M)$; each $H_m$ runs at $f_s/M$",
        ha="center",
        color=INK,
        fontsize=8.6,
    )

    save(fig, "dsp_polyphase_decimator.png")


def main() -> None:
    figure_sampling_aliasing()
    figure_dirichlet_gibbs()
    figure_window_tradeoff()
    figure_stft_chirp()
    figure_zero_pole_response()
    figure_quantization_noise()
    figure_multirate_spectra()
    figure_noise_shaping()
    figure_fft_butterflies()
    figure_multirate_blocks()
    figure_noble_identities()
    figure_fft_8point_flow()
    figure_polyphase_decimator()


if __name__ == "__main__":
    main()
