//Copyright 2018 SichunHao sichunh@bu.edu
#include <iostream>
using namespace std;
int main(int argc,char *argv[])
{

	for(int i=1;i<argc;i=i++)
	{
		if(i>=1 && i<=4)
			{cout<<argv[i]<<endl;
			i=i+1;}
		else if (i>=5)
			{cerr<<argv[i]<<endl;
			i=i+1;}
	}

	return 0;
}