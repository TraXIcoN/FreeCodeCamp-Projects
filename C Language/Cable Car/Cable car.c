#include <stdio.h>
#include <math.h>

int main(void)

{
float position,distance,velocity;
int tower;

	printf("Enter the value	 of position");
	scanf("%f",&position);

	if (position <= 250)
	{
		tower = 1;
		distance = position;
	}

	else if (position <= 750)
	{
		tower = 2;
		distance = position < 500 ? 500 - position : position - 500;
	}
	else
	{
		tower = 3;
		distance = 1000-position;
	
	}


	if(distance<=30)
		velocity = 2.425 +0.00175*distance*distance;
	else
		velocity = 0.625 + 0.12*distance - 0.00025*distance*distance;

	printf("Nearest Tower: %d     Velocity: %f\n",tower,velocity);




}
