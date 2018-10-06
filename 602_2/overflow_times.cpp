#include <iostream>
#include <ctime>
#include <math.h>
using namespace std;
//Copyright 2018 SichunHao sichunh@bu.edu
int main()
{
	clock_t start_clock,end_clock;
	start_clock = clock();  // Timing starts here
	uint16_t m = 1;
	while ( m > 0 ) 
	{
		 m++;
	}
	end_clock = clock();    // Timing stops here
	double microseconds = 1000000*(double)(end_clock-start_clock) / CLOCKS_PER_SEC;
	//double seconds = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;
	double nanoseconds = 1000*microseconds/(pow(2,8));
	double seconds = microseconds*(pow(2,16))/1000000;
	double year = microseconds*(pow(2,48))/1000000/3600/24/365;
	std::cout << "estimated int8 time (nanoseconds): "  << nanoseconds << std::endl;
	std::cout << "measured int16 time (microseconds): " << microseconds << std::endl;
	std::cout << "estimated int32 time (seconds): " << seconds << std::endl;
	std::cout << "estimated int64 time (years): " << year << std::endl;
}