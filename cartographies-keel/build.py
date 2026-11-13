#!/usr/bin/env python3
"""Build the standalone native cartography tool; Python standard library only."""
from pathlib import Path
import argparse,json,zipfile

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description='Construire le HTML autonome des cartographies KEEL.')
parser.add_argument('--output-dir',type=Path,default=ROOT.parent/'dist')
args=parser.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
data=(ROOT/'data.json').read_text(encoding='utf-8');json.loads(data)
js='\n'.join((ROOT/f).read_text(encoding='utf-8') for f in ['core.js','views.js','graph.js','reinsurance.js','details.js','events.js'])
html=(ROOT/'index.template.html').read_text(encoding='utf-8').replace('__FONTS__',(ROOT/'fonts.css').read_text(encoding='utf-8')).replace('__CSS__',(ROOT/'app.css').read_text(encoding='utf-8')).replace('__DATA__',data.replace('<','\\u003c')).replace('__JS__',js.replace('</script','<\\/script'))
(out/'acheel-cartographies.html').write_text(html,encoding='utf-8')
with zipfile.ZipFile(out/'acheel-cartographies.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.writestr('acheel-cartographies.html',html)
 z.writestr('LIRE-MOI.txt',(ROOT/'GUIDE.txt').read_text(encoding='utf-8'))
 z.writestr('LICENCES-POLICES.txt',(ROOT/'LICENCES-POLICES.txt').read_text(encoding='utf-8'))
print('HTML et ZIP construits dans',out)
