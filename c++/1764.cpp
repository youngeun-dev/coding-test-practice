#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n,m;
    map<string, int> list;
    vector<string> answer;
    
    cin >> n >> m;

    
    for(int i = 0; i < n+m; i++){
        string name;
        cin >> name;
        list[name]++;
        if(list.at(name) == 2){
            answer.push_back(name);
        }
    }

    sort(answer.begin(), answer.end());
    cout << answer.size() << endl;
    for(string a : answer){
        cout << a << endl;
    }

}
