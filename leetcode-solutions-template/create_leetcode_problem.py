
import os
import sys
from pathlib import Path

def slugify(title):
    return title.lower().replace(" ", "-").replace(",", "").replace("'", "").replace(":", "").replace(".", "")

def create_problem(topic, number, title, language="py"):
    topic_folder = Path("problems") / topic
    topic_folder.mkdir(parents=True, exist_ok=True)

    slug_title = slugify(title)
    file_name = f"{number}-{slug_title}.{language}"
    file_path = topic_folder / file_name

    if file_path.exists():
        print(f"❗ File already exists: {file_path}")
        return

    with open(file_path, "w") as f:
        f.write(f"# {number}. {title}\n")
        f.write("# LeetCode problem solution\n\n")
        f.write("def solution():\n")
        f.write("    pass\n")

    print(f"✅ Created: {file_path}")

    # Update progress tracker
    progress_path = Path("progress.md")
    if progress_path.exists():
        with open(progress_path, "a") as p:
            p.write(f"| {number} | https://leetcode.com/problems/{slug_title}/ | {topic.capitalize()} | 🕐 In Progress |  |
")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python create_leetcode_problem.py <topic> <problem_number> <problem_title>")
    else:
        topic = sys.argv[1]
        number = sys.argv[2]
        title = " ".join(sys.argv[3:])
        create_problem(topic, number, title)
