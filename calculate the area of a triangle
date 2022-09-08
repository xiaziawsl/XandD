#include<stdio.h>
#include<math.h>
int main()
{
	printf("Enter three lengths of a triangle to calculate the area(press Enter to confirm each one or get the result).\n");
	double a,b,c,p,area;
	scanf("%lf %lf %lf",&a, &b, &c);
	if(abs(a-b)>c||abs(a-c)>b||abs(b-c)>a)
	{
		printf("not a triangle");
	}
	else
	{
	p=(a+b+c)/2;
	area=sqrt(p*(p-a)*(p-b)*(p-c));
	printf("area=%lf",area);
	}
	return 0;
}
