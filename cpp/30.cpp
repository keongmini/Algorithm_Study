#include<iostream>
using namespace std;

int main(){
    int n, lt=1, rt, cur, k=1, result=0;
    cin>>n;

    while(lt != 0){
        lt = n / (k * 10);
        rt = n % k;
        cur = (n/k) % 10;

        if(cur > 3) result += (lt+1) * k;
        else if(cur == 3) result += (lt * k) + (rt + 1);
        else result += (lt * k);

        k = k * 10;
    }

    cout<<result;

    return 0;
}