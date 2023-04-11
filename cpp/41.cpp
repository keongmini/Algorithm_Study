#include<iostream>
#include<vector>
using namespace std;

int main(){
    int a, b=1, cnt=0, tmp, i;
    cin>>a;
    tmp = a;
    a--;
    while(a>0){
        b++;
        a = a- b;
        if(a % b == 0){
            for(i=1;i<b;i++){
                cout<<(a/b) + i<<" + ";
            }
            cout<<(a/b)+i<<" = "<<tmp<<"\n";
            cnt++;
        }
    }

    cout<<cnt;

    return 0;
}

// 내 풀이
// int main(){
//     int n, i, left=1, right=1, result=0, sum=0;
//     cin>>n;
//     vector<int> nums(n+1);

//     for(i=1;i<=n;i++){
//         nums[i] = i;
//     }

//     while(left <= right){
//         if(sum == n){
//             if(left == right - 1){
//                 break;
//             }
//             for(i=left;i<right - 1;i++){
//                 cout<<nums[i]<<" + ";
//             }
//             cout<<nums[i]<<" = "<<n<<"\n";
//             result++;
//             sum -= nums[left++];
//         }
//         if(sum < n){
//             sum += nums[right++];
//         }else{
//             sum -= nums[left++];
//         }
//     }

//     cout<<result<<"\n";



//     return 0;
// }