# include <stdio.h>
# include <stdlib.h>
# include <math.h>

int main() {
	char *line = NULL;
	size_t size;
	int total = 0;
	while(getline(&line, &size, stdin) != -1){
		int mass = atoi(line);
		int fuel = floor(mass / 3) - 2;
		total = total + fuel;
	}
	printf("%d\n", total);
	return 0;
}

