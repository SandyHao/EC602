#include<string>
#include<vector>
//reference 
//blog.csdn.net/langmanqishizaijia/article/details/51086700?utm_source=copy 

typedef string BigInt;
BigInt multiply_int(const BigInt &a, const BigInt &b) {
        string res = "";
        int m = a.size(), n = b.size();
        vector<long long> tmp(m + n - 1);
        for (int i = 0; i < m; i++) {
                int p = a[i] - '0';
                for (int j = 0; j < n; j++) {
                        int q = b[j] - '0';
                        tmp[i + j] += p*q;
                }
        }
        int carry = 0;
        for (int i = tmp.size() - 1; i >= 0; i--) {
                int t = tmp[i] + carry;
                tmp[i] = t % 10;
                carry = t / 10;
        }
        while (carry != 0) {
                int t = carry % 10;
                carry /= 10;
                tmp.insert(tmp.begin(), t);
        }
        for (auto a : tmp) {
                res = res + to_string(a);
        }
        if(res.size() > 0 && res[0]  == '0')
                return "0";
return res;
}



