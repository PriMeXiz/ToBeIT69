import sys


def count_vowels(s: str) -> int:
	"""Return the number of vowels (a,e,i,o,u) in the string s, case-insensitive."""
	vowels = set('aeiou')
	return sum(1 for ch in s.lower() if ch in vowels)


def main() -> None:
	# Read a single line from standard input (keeps spaces)
	try:
		line = sys.stdin.readline()
	except Exception:
		# Fallback to input() if readline fails for some reason
		line = input()

	# Strip only the trailing newline; spaces inside the line are allowed
	if line.endswith('\n'):
		line = line[:-1]

	print(count_vowels(line))


if __name__ == '__main__':
	main()
