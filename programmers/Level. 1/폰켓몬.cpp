// 프로그래머스 Lv.1 폰켓몬

#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int solution(vector<int> nums)
{
    // 1. set을 만들어 nums의 모든 폰켓몬을 삽입하기
    set<int> s;
    for (auto num : nums)
        s.insert(num);
    
    // 2. N/2 마리와 중복없는 폰켓몬의 종류 중 작은 수 반환하기
    return min(s.size(), nums.size()/2);
}