import argparse
import sys

from PIL import Image


def generate_knitting_instructions(image):
	"""Takes a 'pillow' Image, and returns a string of knitting instructions."""
	pass


def simplify_image(image, desired_width=100, desired_height=None, desired_colors=5):
	if desired_height is None:
		desired_height = int(desired_width * (image.height / float(image.width)))
	happy = False
	while not happy:
		simple_image = image.quantize(colors=desired_colors)
		simple_image = simple_image.resize((desired_width,desired_height), Image.LANCZOS)
		simple_image.show()
		response = input('Are you happy with this simplified image?\n y/n/q\n').lower()
		if response == 'y':
			happy = True
		elif response == 'q':
			print('Quitting.')
			sys.exit(1)
		else:
			response = input('Please enter the width, height and number of colors you would like (comma separated)')
			desired_width, desired_height, desired_colors = [int(s.strip()) for s in response.split(',')]
	return simple_image


def get_parser():
	parser = argparse.ArgumentParser(description='Program to generate knitting pattern instructions for a picture.')
	parser.add_argument(
		'--image_filename',
		'-i',
		type=str,
		help='The full filename of the image you would like to make knitting instructions for'
	)
	return parser


def main():
	parser = get_parser()
	args = parser.parse_args()
	original_image = Image.open(args.image_filename)
	knittable_image = simplify_image(original_image)
	knit_instructions = generate_knitting_instructions(knittable_image)
	print(knit_instructions)

if __name__ == '__main__':
	main()
