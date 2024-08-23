// 프로그래머스 Lv.1 바탕화면 정리

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer = {0, 0, 0, 0};
    
    // 시작 x점 찾기
    for (string i : wallpaper) {
        if (i.find('#') == string::npos)
            answer[0]++;
        else
            break;
    }
    
    // 끝 x점 찾기
    for (int i = wallpaper.size() - 1; i >= 0; i--) {
        if (wallpaper[i].find('#') != string::npos) {
            answer[2] = i + 1;
            break;
        }
    }
    
    // y점 찾기
    vector<int> min_memory;
    vector<int> max_memory;
    
    for (string i : wallpaper) {
        if (i.find('#') != string::npos)
            min_memory.push_back(i.find('#'));
            max_memory.push_back(i.rfind('#') + 1);
    }
    
    if (!min_memory.empty()) {
        // 가장 작은 값을 찾아서 answer[1]에 할당
        answer[1] = *min_element(min_memory.begin(), min_memory.end());
    }
    
    if (!max_memory.empty()) {
        // 가장 큰 값을 찾아서 answer[3]에 할당
        answer[3] = *max_element(max_memory.begin(), max_memory.end());
    }
    
    return answer;
}