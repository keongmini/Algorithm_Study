#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main(){
    int T;
    cin>>T;

    for(int t=0; t<T; t++){
        int n;
        cin >> n;

        int sx, sy;
        cin>>sx>>sy;

        vector<vector<int>> c;
        for(int i=0; i<n; i++){
            int cx, cy;
            cin>>cx>>cy;
            vector<int> tmp;
            tmp.push_back(cx);
            tmp.push_back(cy);
            c.push_back(tmp);
        }
        int visited[c.size()];

        int px, py;
        cin>>px>>py;

        queue<pair<int, int>> q;

        q.push({sx, sy});

        string result = "sad";

        while(!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            if(abs(px - x) + abs(py - y) <= 1000){
                result = "happy";
                break;
            }

            for(int i=0; i<n; i++){
                if(visited[i] == 1){
                    continue;
                }

                if(abs(c[i][0] - x) + abs(c[i][1] - y) <=1000){
                    visited[i] = 1;
                    q.push({c[i][0], c[i][1]});
                }
            }
        }

        cout<<result<<endl;

        
    }


    return 0;
}