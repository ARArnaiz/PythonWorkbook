from pathlib import Path
import json
import glob

def analyze_json_scores(somedir: str | Path) -> None:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")

    for item in p.iterdir():
        if item.is_file() and item.suffix == '.json':

            with item.open() as f:
                data = json.load(f)

            print(f'File: {item}')
            d = {}
            for record in data:
                for subject, score in record.items():
                    d[subject] = d.get(subject, []) + [score]
            for subject, values in d.items():
                print(f'\t{subject}: min: {min(values)}, max: {max(values)}, avg: {sum(values)/len(values):.2f}')

analyze_json_scores('../scores')

def analyze_json_scores_c(somedir: str | Path) -> None:
    """Print min, max, and average scores per subject from all JSON files in a directory."""
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")

    for item in p.iterdir():
        if not (item.is_file() and item.suffix == '.json'):
            continue

        with item.open() as f:
            data = json.load(f)

        print(f'File: {item}')
        scores: dict[str, list] = {}
        for record in data:
            for subject, score in record.items():
                scores.setdefault(subject, []).append(score)

        for subject, values in scores.items():
            print(f'\t{subject}: min={min(values)}, max={max(values)}, avg={sum(values)/len(values):.2f}')

analyze_json_scores_c("../scores")

def print_scores(dirname):

    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject,
                                            [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) /
                             len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

print_scores('./scores')