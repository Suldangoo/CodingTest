// 프로그래머스 Lv.1 완주하지 못한 선수
// Hash 활용

#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    // 1. Hash Map을 만든다.
    unordered_map<string, int> map;
    
    for (auto player : participant) { // for문으로 검색
        if (map.end() == map.find(player)) // map에 해당 선수가 없다면
            map.insert(make_pair(player, 1));
        else // 해당 선수와 동명이인인 선수가 존재한다면
            map[player]++;
    }
    
    // 2. Hash Map에서 완주한 선수를 뺀다.
    for (auto player : completion)
        map[player]--;
    
    // 3. Hash Map에서 Value가 0이 아닌 선수를 찾는다.
    for (auto player : participant) {
        if (map[player] != 0)
            return player;
    }
}