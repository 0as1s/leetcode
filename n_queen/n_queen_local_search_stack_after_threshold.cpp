#define TEST_TIMES 10
#define N 300
#define RANDOM_TIMES N/10
#define MAX_STACK_SIZE N
#define I_TRIES_LIMIT 3
#define J_TRIES_LIMIT 3
#define THRESHOLD 10


#include <iostream>
#include <stack>
#include <math.h>
#include <chrono>
#include <algorithm>		// shuffle不是在random里的
#include <random>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
using namespace std;
int conflict(int arrange[], int n, int cur){
  int total = 0;
  for(int i=0;i<n-1;i++)
    for(int j=i+1;j<n;j++){
      if(j-i == abs(arrange[j]-arrange[i])){
	total++;
	if(total>cur)
	  return total;
      }
    }
  return total;
}

int * n_queen(int n){
  int m_ = INT_MAX;
  int *m_a;
  vector<int*> s = vector<int*>();
  for(int t=0;t<RANDOM_TIMES;t++){
    int * arrange = new int[n];
    for(int i=0;i<n;i++)
      arrange[i] = i+1;
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    shuffle(arrange, arrange + n,default_random_engine(seed));
    int c = conflict(arrange, n, INT_MAX);
    if(c<m_){
      m_ = c;
      m_a = arrange;
    }
  }
  s.push_back(m_a);
  while(true){
    int * a;
    if(s.empty()==true){
      a = new int[n];
      unsigned seed = chrono::system_clock::now().time_since_epoch().count();
      for(int i=0;i<n;i++)
	a[i] = i+1;
      shuffle(a, a + n,default_random_engine(seed));
    }else{
      a = s.back();
      s.pop_back();
    }
    int cur_conflict = conflict(a, n, INT_MAX);
    int min_conflict = cur_conflict;
    int* min_arrange = a;
    cout << min_conflict << endl;
    int i_limit = 0;
    for(int i=0;i<n-1;i++){
      int j_limit = 0;
      for(int j=i+1;j<n;j++){
	int* temp = new int[n];
	memcpy(temp, a, n*sizeof(int)); // 注意这里以字节为单位
	swap(temp[i], temp[j]);
	int c = conflict(temp, n, cur_conflict);
	if(c==0)
	  return temp;
	if(c<cur_conflict){
	  if(c<THRESHOLD){
	    s.push_back(temp);
	    if(s.size() > MAX_STACK_SIZE){
	      free(*(s.begin()));
	      s.erase(s.begin());
	    }
	  }else
	    j_limit ++;
	  if(c<min_conflict){
	    min_conflict = c;
	    min_arrange = temp;
	  }
	  if(j_limit > J_TRIES_LIMIT)
	    break;
	}else
	  free(temp);
      }
      j_limit = 0;
      i_limit += 1;
      if(i_limit>I_TRIES_LIMIT && min_conflict>THRESHOLD)
	break;
    }
    if(min_arrange != a)
      s.push_back(min_arrange);
  }
}

int main(int argc, char *argv[])
{
  const time_t a = time(NULL);
  for(int i=0;i<TEST_TIMES;i++){
    n_queen(N);
    cout << i << "---------------" << endl;
  }
  const time_t b = time(NULL);
  cout << b-a << "/" << TEST_TIMES << endl;
  return 0;
}
