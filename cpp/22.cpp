#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n, k, i, sum=0, result;
    cin>>n>>k;
    vector<int> a(n);       // 동적 배열

    for(i=0; i<n; i++){
        cin>>a[i];
    }

    for(i=0; i<k; i++){
        sum += a[i];
    }
    result = sum;

    for(i=k; i<n; i++){
        sum = sum + (a[i] - a[i - k]);

        result = max(result, sum);
    }

    cout<<result;
    
    return 0;
}