"""Copy missing starter materials into an explicitly selected project directory."""
import argparse
import json
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',type=Path)
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    source=Path(__file__).resolve().parents[1]
    target=args.project.expanduser().resolve()
    files=[source/'AGENTS.md']
    for name in ('context','standards','prompts','templates'):
        files.extend(p for p in (source/name).rglob('*') if p.is_file())
    created=[];skipped=[]
    for src in files:
        relative=src.relative_to(source)
        dest=target/relative
        if not dest.resolve().is_relative_to(target):
            raise SystemExit('Refusing a destination outside the selected project.')
        if dest.exists():
            skipped.append(str(relative));continue
        if not args.dry_run:
            dest.parent.mkdir(parents=True,exist_ok=True)
            try:
                with dest.open('xb') as stream:stream.write(src.read_bytes())
            except FileExistsError:
                skipped.append(str(relative));continue
        created.append(str(relative))
    print(json.dumps({'dry_run':args.dry_run,'created_or_planned':created,'existing_preserved':skipped},indent=2))

if __name__=='__main__':main()
