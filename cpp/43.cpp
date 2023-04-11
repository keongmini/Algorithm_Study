#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int a[1001], n;

int Count(int s){
    int i, cnt=1, sum=0;
    for(i=1;i<=n;i++){
        if(sum+a[i] > s){
            cnt++;
            sum = a[i];
        }else{
            sum+=a[i];
        }
    }

    return cnt;
}
int main(){
    int m, i, left=1, right=0, mid, result;
    cin>>n>>m;
    for(i=1;i<=n;i++){
        cin>>a[i];
        right+=a[i];
    }

    while(left<=right){
        mid = (left+right) / 2;
        if(Count(mid) <= m){
            result = mid;
            right = mid - 1;
        }else {
            left = mid + 1;
        }
    }
    cout<<result;
    return 0;
}