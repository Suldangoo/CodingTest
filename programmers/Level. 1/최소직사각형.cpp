// 프로그래머스 Lv.1 최소직사각형

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    vector<int> b; // 큰 길이를 담음
    vector<int> s; // 작은 길이를 담음
    
    for(auto size : sizes) {
        sort(size.begin(), size.end());
        s.push_back(size[0]);
        b.push_back(size[1]);
    }
    
    int h_max = *max_element(b.begin(), b.end()); // 긴 길이에서의 최댓값
    int v_max = *max_element(s.begin(), s.end()); // 짧은 길이에서의 최댓값
    
    return h_max * v_max;
}