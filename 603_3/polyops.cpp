#include <vector>
// Copyright 2018 SichunHao sichunh@bu.edu
using namespace std;
typedef vector<double> Poly;

Poly add_poly(const Poly &a, const Poly &b) {
Poly c;
int m, n, k;
if (b.size() > a.size()) {
        n = b.size();
        m = a.size();
	for(int i = 0; i < m; i++) {
		c.push_back(a[i] + b[i]);
	}
	for(int j = m; j < n; j++) {
		c.push_back(b[j]);
	}
}
else if(b.size() < a.size()) {
        n = a.size();
        m = b.size();
	for(int i = 0; i < m; i++) {
		c.push_back(a[i] + b[i]);
	}
	for(int j = m; j < n; j++) {
		c.push_back(a[j]);
	}
}
else {
        m = b.size();
	for(int i = 0; i < m; i++)
		c.push_back(a[i] + b[i]);
}
while(c[c.size()-1] == 0) {
	c.pop_back();
	if (c.size() == 1)
		break;
}
return c;
}

Poly multiply_poly(const Poly &a,const Poly &b) {
Poly d(a.size()+b.size()-1);
int m, n, k;
if (b.size() > a.size()) {
        n = b.size();
        m = a.size();
	for(int i = 0; i < m; i++) {
		k = i;
		for(int j = 0; j < n; j++) {
			d[k++] += a[i]*b[j];
		}
	}
}
else if(b.size() <= a.size()) {
	n=a.size();
	m=b.size();
	for(int i = 0; i < m; i++) {
		k = i;
		for(int j = 0; j < n; j++) {
			d[k++] += a[j]*b[i];
		}
	}
}
while(d[d.size()-1] == 0) {
	d.pop_back();
	if (d.size() == 1)
		break;
}
return d;
}


