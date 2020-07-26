#include <stdio.h>

int main() {

	float grams;
	float price = 41; //Dollars
	float weight = 1500; //Grams
	int i = 1;

	printf("HOW MANY GRAMS? \n\n");


	while (1) {
		printf("Weight: ");
		scanf_s("%f", &grams);

		float final_price = ((price / weight) * grams); //Dollars
		printf("It would take $%.2f to print it!\n\n", final_price);
		i++;
	}
	return 0;
}
