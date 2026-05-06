from pathlib import Path
import json
import arrow

def get_file_props_c(somedir: str | Path) -> None:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    flist = [ (item.name, item.stat().st_size, item.stat().st_mtime) for item in p.iterdir() if item.is_file() ]
    with open('file_props.json', 'w') as outfile:
        json.dump(flist, outfile, indent=2)
    with open('file_props.json') as infile:
        fdata = json.load(infile)
    biggest_file = max(fdata, key=lambda x: x[1])
    smallest_file = min(fdata, key=lambda x: x[1])
    most_recent = max(fdata, key=lambda x: x[2])
    least_recent = min(fdata, key=lambda x: x[2])
    most_recent_time = arrow.Arrow.fromtimestamp(most_recent[2]).humanize()
    least_recent_time = arrow.Arrow.fromtimestamp(least_recent[2]).humanize()

    print(f"Biggest:        {biggest_file[0]:<20}  ({biggest_file[1]} bytes)")
    print(f"Smallest:       {smallest_file[0]:<20}  ({smallest_file[1]} bytes)")
    print(f"Most recent:    {most_recent[0]:<20}  (modified {most_recent_time})")
    print(f"Least recent:   {least_recent[0]:<20}  (modified {least_recent_time})")

#Claude
def collect_file_props(somedir: str | Path, output_file: str = 'file_props_c.json') -> str:
    """Collect file properties from a directory and write them to a JSON file."""
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")

    flist = []
    for item in p.iterdir():
        if item.is_file():
            stat = item.stat()
            flist.append({
                'filename': item.name,
                'size': stat.st_size,
                'mtime': stat.st_mtime,
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(flist, f, indent=2)

    return output_file


def report_file_stats(json_file: str) -> None:
    """Read a file props JSON and report biggest, smallest, most and least recently modified."""
    with open(json_file, encoding='utf-8') as f:
        fdata = json.load(f)

    biggest      = max(fdata, key=lambda x: x['size'])
    smallest     = min(fdata, key=lambda x: x['size'])
    most_recent  = max(fdata, key=lambda x: x['mtime'])
    least_recent = min(fdata, key=lambda x: x['mtime'])

    width = max(len(f['filename']) for f in fdata)

    def humanize(mtime):
        return arrow.Arrow.fromtimestamp(mtime).humanize()

    print(f"{'Biggest:':<15} {biggest['filename']:<{width}}  ({biggest['size']:>10,} bytes)")
    print(f"{'Smallest:':<15} {smallest['filename']:<{width}}  ({smallest['size']:>10,} bytes)")
    print(f"{'Most recent:':<15} {most_recent['filename']:<{width}}  ({humanize(most_recent['mtime'])})")
    print(f"{'Least recent:':<15} {least_recent['filename']:<{width}}  ({humanize(least_recent['mtime'])})")


if __name__ == '__main__':
    get_file_props_c('..')
    somedir = input("Enter directory path: ").strip()
    json_file = collect_file_props(somedir)
    report_file_stats(json_file)