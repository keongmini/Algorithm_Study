#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int n, m, i, p1=0, p2=0, p3=0;
    cin>>n;
    vector<int> a(n);
    for(i=0; i<n; i++){
        cin>>a[i];
    }

    sort(a.begin(), a.end());

    cin>>m;
    vector<int>b(m), c(n+m);
    for(i=0; i<m; i++){
        cin>>b[i];
    }

    sort(b.begin(), b.end());

    while(p1 < n && p2 < m){
        if(a[p1] == b[p2]){
            c[p3++] = a[p1++];
            p2++;           // 교집합 - 동시 증가
        }else if(a[p1] < b[p2]){
            p1++;
        }else{
            p2++;
        }
    }
    
    for(i=0; i<p3; i++){
        cout<<c[i]<<" ";
    }

    return 0;

}

// int main(){
//     int n, m, i, j, num, p=0;
//     cin>>n;
//     vector<int> nums1(n);

//     for(i=0;i<n;i++){
//         cin>>num;
//         nums1[i] = num;
//     }

//     cin>>m;
//     vector<int> result(n+m);

//     for(i=0;i<m;i++){
//         cin>>num;
//         for(j=0;j<n;j++){
//             if(num == nums1[j]){
//                 result[p] = num;
//                 p++;
//                 break;
//             }
//         }
//     }

//     for(i=0;i<p;i++){
//         cout<<result[i]<<" ";
//     }

//     return 0;
// }