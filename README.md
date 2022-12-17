# AETG by ljx & Report
 
#### there are 2 classes which the AETG method is encapsulated in here

now just run AETG.py to gen results

initialize the pairwise class and the threewise class

the result will be generated automatically
***

The AETG try to solve a cover array problem in software testing.
CA(N:K,T,V) is the solution.
K=number of parameters
T=strength
V=the scope of parameters
assume the system has K parameters, every para Ki has Li possible variables.
create a candidate set, which should include a column of Ks after calculation. 

First, the candiate is empty, select the pair in the uncovered set(ucps) whose frequence is the highest 

Second, if number of paras did not meet the strength, choose the V which has the highest frequece in ucps just like we do in first, else if the number of paras did not meet the strength, we randomly choose a para.

Third, update the ucps and cps.

that's all about the algor... 

Finally, we continue till the ucps is empty.

***
## the model of JD.com with strength 2

![image](https://user-images.githubusercontent.com/82871660/208232909-59d7813a-4c3a-462e-a065-9f716bbc640c.png)
### the calculations 
the strength of the model is 2, so the problem can be describe as CA(534;18,2,(16,4,2,5,20,15,4,5,5,14,8,8,7,18,14,5,47,5), the sum of pairs should be 17335.

there are 534 test cases generated in total, the sum of pairs in total is 17335, which is equal to our assumption. 

## the model of XC.com with strength 3

![image](https://user-images.githubusercontent.com/82871660/208233091-b3433936-2004-405b-b1c0-09a6f32ff39a.png)
### the calculations
the strength of the model is 3, so the problem can be describe as CA(503;7,3,(71,71,71,71,9,6,5), the sum of pairs should be 16201.
there are 503 test cases generated in total, the sum of pairs in total is 1851, which is equal to our assumption. 

### some adjustments
replace the return date with duration days 

figure that the maximum number of people is 9 while a adult can carry at most 2 children, so the maximum of child is 6 (with 3 adults)
also figure that the maximum number of infants is 4 since a adult can carry at most 1 infant.
