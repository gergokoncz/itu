#include <stdio.h>

int main(int argc, char *argv[]){
	printf("start\n\n");
	int a = isLessOrEqual(1 << 31, 1 << 31);
	printf("%d\n\n", a);
	int b = isLessOrEqual(1 << 31, 0x7FFFFFFF);
	printf("%d\n\n", b);
	int c = isLessOrEqual(0x7FFFFFFF, 1 << 31);
	printf("%d\n\n", c);

	int x = howManyBits(5);
	printf("%d\n", x);
	x = howManyBits(-5);
	printf("%d\n", x);
	x = howManyBits(0x7FFFFFFF);
	printf("%d\n", x);
	x = howManyBits(1 << 31);
	printf("%d\n", x);
}

int isLessOrEqual(int x, int y){
	int ind = !((y + ~x + 1) >> 31);
	printf("%d\n", ind);
	int xs = !(x >> 31);
	int ys = !(y >> 31);
	printf("%d\n", xs);
	printf("%d\n", ys);
	int res = (!(xs ^ ys)) & ind;
	printf("%d\n", res);
	return res | (ys & !xs);
}

int howManyBits(int x){
	int s = x >> 31;
	x = (~s & x) | (s & ~x);

	int a = 0;
	int c = 0;

	return x;
}
