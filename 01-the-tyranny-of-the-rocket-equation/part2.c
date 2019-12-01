# include <stdio.h>
# include <stdlib.h>
# include <math.h>

int fuel_for_module(int mass, int fuel) {
	int additional_fuel =  floor(mass/3) -2;
	if (additional_fuel < 0) {
		return fuel;
	}
	return fuel_for_module(additional_fuel, fuel + additional_fuel);
}

int main() {
	char *line = NULL;
	size_t size;
	int total = 0;
	while(getline(&line, &size, stdin) != -1){
		int mass = atoi(line);
		total = fuel_for_module(mass, total);
	}
	printf("%d\n", total);
	return 0;
}

