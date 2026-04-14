import os
import re
import shutil

src_dir = r'd:/CCJ-Translation/BepInEx/Translation/en/Texture'


def get_folder(fname):
    # sactx-N-WxH-FORMAT-SCENE-hash [hashes].ext
    m = re.match(r'sactx-\d+-\d+x\d+-\w+-([a-z_]+)-', fname)
    if m:
        return m.group(1)
    if fname.startswith('matching_rank_'):
        return 'matching'
    if fname.startswith('ui_chat_'):
        return 'chat'
    if fname.startswith('ui_stage_name_'):
        return 'stage'
    return None


moved = 0
skipped = []

for fname in os.listdir(src_dir):
    fpath = os.path.join(src_dir, fname)
    if os.path.isdir(fpath):
        continue
    folder = get_folder(fname)
    if folder:
        dest_dir = os.path.join(src_dir, folder)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(fpath, os.path.join(dest_dir, fname))
        print(f'{folder}/{fname}')
        moved += 1
    else:
        skipped.append(fname)

print(f'\nMoved: {moved}')
if skipped:
    print(f'Unmatched ({len(skipped)}):')
    for f in skipped:
        print(f'  {f}')
