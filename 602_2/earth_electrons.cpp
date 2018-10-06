#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>
//Copyright 2018 SichunHao sichunh@bu.edu
using namespace std;
int main()
{
	double trans = 8.796e12;
	double Me = 5.98e24;
	double Mv = 0.065;
	double Mh = 0.001;
	double Mu = 0.285;
	double mol=6.02e23;
	double Nv = 13*mol*Me/Mv/trans; 
	double Nmin = mol*Me/Mu/trans; 
	double Nmax = 112*mol*Me/Mh/trans; 
	//printf ("%f\n",Mv);
	//printf ("%f\n",Mh);
	//printf ("%f\n",Mu);
	printf ("%e\n",Nv);
	printf ("%e\n",Nmin);
	printf ("%e\n",Nmax);

	return 0;
}