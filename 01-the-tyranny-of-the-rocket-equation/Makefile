test: build
	./part1 < test1.input
	./part2 < test2.input

part1: build
	./part1 < part1.input

part2: build
	./part2 < part2.input

build: part1.c part2.c
	gcc -g -o part1 part1.c
	gcc -g -o part2 part2.c
