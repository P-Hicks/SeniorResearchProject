
import sys

class NullValue:
	pass


def get_args():
	params, kwargs = parse_args(sys.argv)
	return params, kwargs

def parse_args(list_args):
	kwargs = {}
	sequential_args = []

	i = 0
	while (i < len(list_args) and not list_args[i].startswith('-')):
		sequential_args.append(list_args[i])
		i = i + 1
	while (i < len(list_args)):
		arg = list_args[i]
		if (arg.startswith('--')):
			if ('=' in arg):
				key, value = arg.split('=',1)
				kwargs[key[2:]] = value
			else:
				kwargs[arg[2:]] = NullValue()
			i = i + 1
		elif (arg.startswith('-')):
			kwargs[arg[1:]] = list_args[i+1]

			i = i + 2
		else:
			print(f"Unsure how to parse arg: {arg}")
			i = i + 1
	return sequential_args, kwargs


if __name__ == '__main__':
	get_args()

