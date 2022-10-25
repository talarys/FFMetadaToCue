import subprocess
import sys
from pathlib import Path


def msToCueTime(ms):
    ms = int(ms[6:])
    M = ms//1000//60
    S = ms//1000 % 60

    return f'{M}:{S}:{ms%100}'


def main():
    metadata = subprocess.run(
        ['ffprobe', '-show_chapters', sys.argv[1]], capture_output=True, text=True).stdout.split('\n')

    cue = []
    path = Path(sys.argv[1])
    f = open(f'{path.parent}/{path.stem}.cue', 'w')
    cue.append(f'FILE "{path.name}" {path.suffix.upper()[1:]}')

    starts = [data for data in metadata if 'start=' in data]

    for index, start in enumerate(starts):
        time = msToCueTime(start)

        if index+1 <= 9:
            cue.append(f'TRACK 0{index+1} AUDIO')
            cue.append(f'   TITLE "Chapter 0{index+1}"')
        else:
            cue.append(f'TRACK {index+1} AUDIO')
            cue.append(f'   TITLE "Chapter {index+1}"')
        cue.append(f'   INDEX 01 {time}')

    for l in cue:
        f.write(f'{l}\n')


if __name__ == "__main__":
    main()
