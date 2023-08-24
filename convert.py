from imageio import get_writer
import imageio.v3 as iio

import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-o', type=str, required=True,
                    help='specify input files using wildcard selection (e.g. *.png)')
parser.add_argument('--output', '-o', type=str, required=False, default='./output.gif',
                    help='specify output file (default: output.gif)')
parser.add_argument('--fps', '-f', type=int, required=False, default=30, help='specify fps (default: 30)')

args = parser.parse_args()

with get_writer(args.output, mode='I', fps=args.fps) as writer:
	for filename in sorted(glob.glob(args.input)):
		image = iio.imread(filename)
		writer.append_data(image)

print('Done!')
