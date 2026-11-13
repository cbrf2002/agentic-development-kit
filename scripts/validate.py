"""Check starter structure and internal references; no scans or network access."""
import csv
import json
import re
from pathlib import Path

def validate(root):
    errors=[]
    required=['README.md','AGENTS.md','.gitignore','prompts/master.md',
              'context/README.md','context/current.md','standards/security-reporting.md',
              'templates/findings.csv','templates/test-results.csv','templates/asvs-matrix.csv',
              'templates/scope.json','scripts/bootstrap.py','docs/publication.md']
    for name in required:
        if not (root/name).is_file():errors.append('Missing '+name)
    markdown=list(root.rglob('*.md'))
    for path in markdown:
        text=path.read_text(encoding='utf-8')
        if '\ufffd' in text:errors.append('Invalid text encoding: '+str(path.relative_to(root)))
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if re.match(r'^(?:[a-z]+:|#)',link,re.I):continue
            link=link.split('#')[0].strip('<>')
            if link and not (path.parent/link).exists():
                errors.append('Broken reference in '+str(path.relative_to(root))+': '+link)
    for name,primary in [('findings.csv','finding_id'),('test-results.csv','case_id'),('asvs-matrix.csv','requirement_id')]:
        path=root/'templates'/name
        if not path.exists():continue
        with path.open(newline='',encoding='utf-8') as stream:
            reader=csv.DictReader(stream);rows=list(reader);headers=reader.fieldnames or []
        if primary not in headers or len(headers)!=len(set(headers)):
            errors.append('Invalid schema: '+name)
        ids=[r.get(primary) for r in rows]
        if len(ids)!=len(set(ids)) or any(not i for i in ids):
            errors.append('Missing/duplicate IDs: '+name)
    scope_path=root/'templates/scope.json'
    if scope_path.exists():
        scope=json.loads(scope_path.read_text(encoding='utf-8'))
        if scope.get('targets') or scope.get('allowed_actions') or scope.get('automatic_remediation'):
            errors.append('Public starter scope must have no live targets or authorized actions.')
    ignore=(root/'.gitignore').read_text(encoding='utf-8') if (root/'.gitignore').exists() else ''
    for token in ('evidence/','raw/','credentials/','keys/','.env','*.pem'):
        if token not in ignore:errors.append('Missing restricted-output ignore: '+token)
    return {'result':'FAIL' if errors else 'PASS','markdown_files':len(markdown),'csv_schemas':3,
            'scope':'Structure, local references and blank starter scope only','errors':errors}

if __name__=='__main__':
    result=validate(Path(__file__).resolve().parents[1]);print(json.dumps(result,indent=2))
    raise SystemExit(1 if result['errors'] else 0)
