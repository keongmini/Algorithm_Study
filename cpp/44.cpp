#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int n;

int Count(int len, int x[]){
    int i, cnt=1, pos=x[1];
    for(i=2;i<=n;i++){
        if(x[i] - pos >= len){
            cnt++;
            pos=x[i];
        }
    }
    return cnt;
}

int main(){
    int c, i, left=0, right, mid, result;
    cin>>n>>c;
    int *location = new int[n+1];  // 제약조건이 클 때, 동적으로 배열 설정

    for(i=1;i<=n;i++){
        cin>>location[i];
    }

    sort(location+1, location+n+1);   // vector가 아닌 배열 정렬
    right = location[n];

    while(left<=right){
        mid = (left + right) / 2;
        if(Count(mid, location) >= c){
            result = mid;
            left = mid + 1;
        }
        else right = mid - 1;
    }
    cout<<result;
    delete[] location;

    return 0;
}