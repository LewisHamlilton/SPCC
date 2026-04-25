#define MAX3(a,b,c)\
   if(a >= b && a >= c)\
       max = a;\
   else if(b >= a && b >= c)\
       max = b;\
   else\
       max = c;

