#include<iostream>
#include<vector>
using namespace std;

int main(){
    int i, n, num=0, cnt=1, result=0;
    cin>>n;
    vector<int> a(n);

    for(i=0; i<n; i++){
        cin>>a[i];
    }

    num = a[0];
    for(i=1; i<n; i++){
        if(a[i] >= num){
            cnt++;
        }else{
            result = max(result, cnt);
            cnt = 1;
        }
        num = a[i];
    }

    cout<<result;

    return 0;
}