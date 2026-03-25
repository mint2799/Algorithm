s = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """
n = int(input())
lines = s.split('\n')
for l in lines:
    print(' '.join([l] * n))