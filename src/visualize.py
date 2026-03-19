from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def save_plot(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.show()


def plot_top_cities(city_scores: pd.Series, top_n: int = 10, output_path: Path = None) -> None:
    top = city_scores.sort_values(ascending=False).head(top_n)

    plt.figure(figsize=(10, 6))
    top.sort_values().plot(kind="barh")
    plt.title(f"Top {top_n} Cities by Insecurity Score")
    plt.xlabel("Average Insecurity Score")
    plt.ylabel("City")

    if output_path:
        save_plot(output_path)
    else:
        plt.tight_layout()
        plt.show()


def plot_quarter_trend(quarter_scores: pd.Series, output_path: Path = None) -> None:
    quarter_scores = quarter_scores.sort_index()

    plt.figure(figsize=(8, 5))
    quarter_scores.plot(marker="o")
    plt.title("Insecurity Score Across 2025 Quarters")
    plt.xlabel("Quarter")
    plt.ylabel("Average Insecurity Score")

    if output_path:
        save_plot(output_path)
    else:
        plt.tight_layout()
        plt.show()


def plot_sex_comparison(sex_scores: pd.Series, output_path: Path = None) -> None:
    label_map = {1: "Men", 2: "Women"}
    plot_data = sex_scores.copy()
    plot_data.index = [label_map.get(x, str(x)) for x in plot_data.index]

    plt.figure(figsize=(6, 4))
    plot_data.plot(kind="bar")
    plt.title("Insecurity Score by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Average Insecurity Score")
    plt.xticks(rotation=0)

    if output_path:
        save_plot(output_path)
    else:
        plt.tight_layout()
        plt.show()