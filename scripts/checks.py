import glob
import sys

import yaml


source_directories = [
    "essays",
    "dialogues",
    "meditations",
    "notes",
    "poems",
]

exit_code = 0

def print_error(filename, message):
    global exit_code
    exit_code = 1
    print(f"{filename} {message}")

files_found = {}

for sd in source_directories:
    files_found[sd] = []
    for fp in glob.iglob(f"./{sd}/*.md"):
        files_found[sd].append(fp[len(f"./{sd}/"):-len(".md")])
        lines = open(fp, "r").readlines()
        if lines[0] != "---\n":
            print(lines[0])
            print_error(fp, "YAML front matter must start on first line")
        yaml_lines = []
        for l in lines[1:]:
            if l == "---\n":
                break
            else:
                yaml_lines.append(l)
        yaml_frontmatter = "".join(yaml_lines)

        try:
            data = yaml.load(yaml_frontmatter, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            print_error(fp, f"Invalid frontmatter: {e}")
            continue

        if sd == "meditations" and "date" not in data:
            print_error(fp, "No date in frontmatter")
        if "title" not in data:
            print_error(fp, "No title in frontmatter")
        if "type" in data:
            print_error(fp, "Type specified in frontmatter")
        if "status" in data:
            print_error(fp, "Status specified in frontmatter")

        if "description" not in data:
            print_error(fp, "No description in frontmatter")
        else:
            description_len = len(data['description'])
            if description_len < 20:
                print_error(fp, f"Description shorter than 20 chars ({description_len})")
            if description_len > 350:
                print_error(fp, f"Description longer than 350 chars ({description_len})")

# check that all of the titles map out
file_index = yaml.load(open("./_data/index.yml", "r"), Loader=yaml.FullLoader)
for sd in files_found:
    expected_files = set(file_index[sd])
    actual_files = set(files_found[sd])
    missing_files = expected_files - actual_files
    if missing_files:
        print_error("", "There were missing files:")
        for f in missing_files:
            print_error("", f"  ./{sd}/{f}.md")
    extra_files = actual_files - expected_files
    if extra_files:
        print_error("", "There were extra files:")
        for f in extra_files:
            print_error("", f"  ./{sd}/{f}.md")

sys.exit(exit_code)
