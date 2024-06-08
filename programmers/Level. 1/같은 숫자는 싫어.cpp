// 프로그래머스 Lv.1 같은 숫자는 싫어

#include <vector>
#include <set>

using namespace std;

// 원하는 인덱스부터 마지막까지 벡터를 잘라내는 Slice 함수
vector<int> vecSlice(vector<int> v, int a)
{
    return vector<int>(v.begin() + a, v.end());
}

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    answer.insert(answer.end(), arr[0]); // 가장 최상단 인덱스 추가
    
    for (auto num : vecSlice(arr, 1))
        if (answer.back() != num) // 스택의 마지막과 다른 값이라면 추가
            answer.insert(answer.end(), num);
    
    return answer;
}