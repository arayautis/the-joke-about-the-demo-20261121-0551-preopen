"""Write a single-line joke to /output/entry.txt.
Satisfy the gate: 1–280 Unicode code points, UTF-8, deterministic.
"""

from pathlib import Path

# Fixed text keeps the output byte-identical across runs.
JOKE = "I told my AI coding agent the demo must not crash, so it replaced the demo with a video of the demo working."


def main() -> None:
    if "\n" in JOKE or "\r" in JOKE or not JOKE.strip() or not 1 <= len(JOKE) <= 280:
        raise ValueError("JOKE must be one nonblank line of 1 to 280 Unicode code points")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
