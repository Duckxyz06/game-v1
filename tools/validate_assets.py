#!/usr/bin/env python3
import csv,json,sys
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'docs/ASSET_MANIFEST.csv').open(encoding='utf8',newline='')))
pending=[];errors=[];good=[]
for r in rows:
 p=root/r['file_path']
 if not p.is_file():pending.append(r['id']);continue
 try:
  with Image.open(p) as im:
   im.load();w,h=im.size;fw=int(r['frame_width']);fh=int(r['frame_height'])
   if im.format!='PNG' or w%fw or h%fh:errors.append(f'{p}: bad format or frames')
   if r['transparent']=='yes' and 'A' not in im.getbands():errors.append(f'{p}: alpha missing')
   if r['category']=='character' and h!=4*fh:errors.append(f'{p}: four rows required')
  good.append(r['id'])
 except Exception as ex:errors.append(f'{p}: {ex}')
print(json.dumps({'valid':good,'pending':pending,'errors':errors},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
