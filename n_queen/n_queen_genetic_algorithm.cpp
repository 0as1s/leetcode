#define TEST_TIMES 1
#define N 100
#define ITEMS 50
#define LEFT 30


#include <iostream>
#include <math.h>
#include <chrono>
#include <algorithm>		// shuffle不是在random里的
#include <random>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <fstream>
#include <string.h>
using namespace std;
int conflict(int arrange[]){
  int total = 0;
  for(int i=0;i<N-1;i++)
    for(int j=i+1;j<N;j++)
      if(arrange[i] == arrange[j] || j-i == abs(arrange[j]-arrange[i]))
	total++;
  return total;
}

int partial_conflict(int arrange[], int pos){
  int total = 0;
  for(int i=0;i<N-1;i++)
    if(arrange[i] == arrange[pos] || pos-i == abs(arrange[pos]-arrange[i]))
      total++;
  return total;
}

int * initial(){
  // 用于随机生成种群
  int * a = new int[N];
  for(int i=0;i<N;i++)
    a[i] = i;
  unsigned seed = chrono::system_clock::now().time_since_epoch().count();
  shuffle(a, a+N, default_random_engine(seed));
  // shuffle(a+N/2, a+N, default_random_engine(seed));
  return a;
}

vector<int*> hybird_and_variation(vector<int*> p){
  for(int i=LEFT;i<ITEMS;i++){
    int * a = p[rand() % LEFT];	
    int * b = p[rand() % LEFT];	// 随机选取父母
    int * new_arr = (int*)malloc(N*sizeof(int));

    int mid = rand() % N;	// 选取基因交叉点

    memcpy(new_arr, a, mid*sizeof(int));
    memcpy(new_arr+mid, b+mid, (N-mid) * sizeof(int)); // 遗传
    int pos = rand() % N;
    int before_conflict = partial_conflict(new_arr, pos);
    new_arr[pos] = rand() % N; // 变异，对随机点设置随机值
    int after_conflict = partial_conflict(new_arr,pos);
    while(before_conflict < after_conflict){
      new_arr[pos] = rand() % N;
      after_conflict = partial_conflict(new_arr,pos);
    }
    p[i] = new_arr;
  }
  return p;
}

vector<float> calcualte_survival_factor(vector<int> conflicts){
  // 根据冲突计算存活分数的函数
  // 给定冲突ｃ的排列的存活分数如下：(最大冲突数-c)/(sum(总冲突数-ci))
  // 如果使用冲突数的绝对值，那么在冲突数教高时冲突数的差异没办法产生较大的存活分数的差异
  // 使用冲突数的差值可以避免上述问题，考虑对于5000,4999,5100这三个冲突即可
  vector<float> scores = vector<float>();
  int max=-INT_MAX;
  for(int i=0;i<ITEMS;i++)
    if(conflicts[i]>max)
      max = conflicts[i];
  int total_delta = 0;

  for(int i=0;i<ITEMS;i++)
    total_delta += max - conflicts[i];

  for(int i=0;i<ITEMS;i++)
    scores.push_back((float)(max - conflicts[i]) / (float)total_delta);
  float total_score = 0;
  // 积累存活分数，用于轮盘赌算法
  for(int i=0;i<ITEMS;i++){
    total_score += scores[i];
    scores[i] = total_score;
  }
  return scores;
}

int * n_queen(){
  unsigned seed = chrono::system_clock::now().time_since_epoch().count();
  srand(seed);

  vector<int*> p = vector<int*>();
  vector<int> conflicts = vector<int>();
  // 初始化种群
  for(int i=0;i<ITEMS;i++){
    int * a = initial();
    p.push_back(a);
    conflicts.push_back(conflict(a));
  }
  int * a = p[0];
  vector<float> scores;
  ofstream out("average_conflicts.npy");
  while(true){
    scores = calcualte_survival_factor(conflicts); // 计算存活分数
    vector<int*> new_p = vector<int*>(ITEMS);
    for(int i=0;i<LEFT;i++){	// 采用轮盘赌选择
      float threshold = (float)rand() / (float) RAND_MAX;
      for(int j=0;j<ITEMS;j++){
	if(threshold<=scores[j]){
	  int * temp = (int*) malloc(N*sizeof(int));
	  memcpy(temp, p[j], N*sizeof(int));
	  new_p[i] = temp;
	  break;
	}
      }
    }
    // 释放上一代种群占用的内存
    for(int i=0;i<ITEMS;i++)
      free(p[i]);
    p = hybird_and_variation(new_p); // 杂交与变异
    int min_conflict = INT_MAX;
    int total_conflict = 0;
    for(int i=0;i<ITEMS;i++){
      int c = conflict(p[i]);
      total_conflict += c;
      if(c<min_conflict){
    	min_conflict = c;
	if(c==0)
	  return p[i];
      }
      conflicts[i] = c;
    }
    cout << (float) total_conflict / (float) ITEMS << endl;
    out << (float) total_conflict / (float) ITEMS << endl;
  }
}

int main(int argc, char *argv[])
{
  const time_t a = time(NULL);
  ofstream out("../output2.txt");
  out<< "begin" << endl;
  for(int i=0;i<TEST_TIMES;i++){
    int* result = n_queen();
    for(int j=0;j<N;j++)
      cout << result[j] << ", ";
    cout << endl << i << "---------------" << endl;
    const time_t b = time(NULL);
    cout << b-a << "/" << (i+1) << endl;
    out << b-a << "/" << (i+1) << endl;
  }
  return 0;
}
// 效率：１５皇后，约7/10 s
// 500皇后：１４３３ｓ
