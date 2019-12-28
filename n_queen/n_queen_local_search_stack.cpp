#define TEST_TIMES 1
#define N 5000

#define RANDOM_TIMES 50
#define MAX_STACK_SIZE 20
#define I_TRIES_LIMIT 2
#define J_TRIES_LIMIT 2
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
int conflict(int arrange[], int n){
  int total = 0;
  for(int i=0;i<n-1;i++)
    for(int j=i+1;j<n;j++){
      if(j-i == abs(arrange[j]-arrange[i])){
	total++;
      }
    }
  return total;
}

int partial_conflict(int arrange[], int n, int i, int j){
  int total = 0;
  for(int k=0;k<n;k++){
    if(abs(k-i) == abs(arrange[k]-arrange[i]))
	total++;
    if(abs(k-j) == abs(arrange[k]-arrange[j]))
	total++;
  }
  return total;
}

int * n_queen(int n){
  int * arrange = new int[n];
  vector<int*> s = vector<int*>();
  for(int i=0;i<n;i++)
    arrange[i] = i+1;
  unsigned seed = chrono::system_clock::now().time_since_epoch().count();
  shuffle(arrange, arrange + n,default_random_engine(seed));
  s.push_back(arrange);
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
    int cur_conflict = conflict(a, n);
    // int min_conflict = cur_conflict;
    // int* min_arrange = a;
    cout << cur_conflict << endl;
    int i_limit = 0;
    for(int i=0;i<n-1;i++){
      int j_limit = 0;
      int flag = 0;
      for(int j=i+1;j<n;j++){
	int* temp = new int[n];
	memcpy(temp, a, n*sizeof(int)); // 注意这里以字节为单位
	int before_conflict = partial_conflict(temp, n, i,j);
	swap(temp[i], temp[j]);
	int after_conflict = partial_conflict(temp,n,i,j);
	if(after_conflict<before_conflict){
	  int c = cur_conflict + (after_conflict - before_conflict);
	  if(c==0 && conflict(temp,n)==0)
	      return temp;
	  if(c<THRESHOLD){
	    j_limit ++;
	    s.push_back(temp);
	    if(s.size() > MAX_STACK_SIZE){
	      free(*(s.begin()));
	      s.erase(s.begin());
	      if(j_limit >= J_TRIES_LIMIT){
	  	i_limit ++;
	  	break;
	      }
	    }
	  }else{
	    s.push_back(temp);
	    flag = 1;
	    break;
	  }
	}else
	  free(temp);
      }
      if(flag == 1 || i_limit>=I_TRIES_LIMIT)
	break;
    }
    // if(min_arrange != a)
    //   s.push_back(min_arrange);
  }
}

int main(int argc, char *argv[])
{
  const time_t a = time(NULL);
  for(int i=0;i<TEST_TIMES;i++){
    n_queen(N);
    cout << i << "---------------" << endl;
    const time_t b = time(NULL);
    cout << b-a << "/" << (i+1) << endl;
  }
  return 0;
}
