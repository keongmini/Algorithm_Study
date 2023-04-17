#include <iostream>
#include <stack>

using namespace std;

int n;
int A[1000001];
int result[1000001];
stack<int> st;


int main(){
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>A[i];
    }

    for(int i=0; i<n; i++){
        while(!st.empty() && A[st.top()] < A[i]){
            result[st.top()] = A[i];
            st.pop();
        }
        st.push(i);
    }

    while(!st.empty()){
        result[st.top()] = -1;
        st.pop();
    }

    for(int i=0; i<n; i++){
        cout<<result[i]<<" ";
    }


    return 0;
}

// 시간 초과 
// #include <iostream>
// #include <vector>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;

//     vector<int> nums;
//     for(int i=0; i<n; i++){
//         int tmp;
//         cin>>tmp;
//         nums.push_back(tmp);
//     }

//     vector<int> result;

//     for(int i=0; i<n; i++){
//         int now = -1;
//         for(int j=i+1; j<n; j++){
//             if(nums[j] > nums[i]){
//                 now = nums[j];
//                 break;
//             }
//         }
//         result.push_back(now);
//     }

//     for(int i=0; i<result.size(); i++){
//         cout<<result[i]<<" ";
//     }


//     return 0;
// }