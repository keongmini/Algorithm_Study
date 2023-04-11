#include<iostream>
#include<vector>
using namespace std;
// 내 풀이
// int main(){
//     int n, i, j, num, cnt, idx;
//     cin>>n;

//     vector<int> result(n);

//     for(i=1;i<=n;i++){
//         cin>>num;
//         cnt = 0;
//         idx = 0;
//         while(cnt < num){
//             if(result[idx] == 0 || result[idx] > i){
//                 cnt++;
//             }
//             idx++;
//         }
//         if(cnt == num && result[idx] > 0){
//             while(result[idx] != 0){
//                 idx++;
//             }
//         }
//         result[idx] = i;
//     }
    
//     for(i=0;i<n;i++){
//         cout<<result[i]<<" ";
//     }
//     return 0;
// }

//강의 풀이
int main(){
    int n, i, j, pos;
    cin>>n;
    vector<int> is(n+1), os(n+1);

    for(i=1;i<=n;i++){
        cin>>is[i];
    }
    for(i=n;i>=1;i--){
        pos = i;
        for(j=1;j<=is[i];j++){
            os[pos] = os[pos+1];
            pos++;
        }
        os[pos] = i;
    }

    for(i=1;i<=n;i++){
        cout<<os[i]<<" ";
    }

    return 0;
}