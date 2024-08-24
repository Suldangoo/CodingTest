// 1015. 수열 정렬 (실버 4)
// 알고리즘 분류 : 정렬

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N; // 배열 A의 크기 입력

    vector<int> vec(N); // N 크기의 벡터 생성
    for (int i = 0; i < N; i++)
        cin >> vec[i];


    // 확인을 위한 출력
    cout << "num = " << N << endl;
    cout << "vec = { ";
    for (int i = 0; i < N; i++) {
        cout << vec[i] << " ";
    }
    cout << "}" << endl;

    return 0;
}