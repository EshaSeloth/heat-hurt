# heat-hurt
A machine learning project that predicts hair damage caused by heat styling tools. Based on a womans styling habits it predicts a damage score and gives a risk warning. 

#damage-scale 
0 - No damage, your hair is healthy 
1 - Very mild, keep an eye on your hair  
2 - mild, consider reducing heat usage 
3 - moderate, reduce heat styling frequency 
4 - high, significantly reduce heat usage 
5 - severe, stop heat styling immediately 

#tech-stack 
Python (pandas, matplotlib, scikit-learn)
MySQL 


#Sample-input
| Tool         | Temperature | Duration | Frequency | Hair Type |
|--------------|-------------|----------|-----------|-----------|
| Straightener | 230°C       | 45 mins  | Daily     | Curly     |

#Sample-output
damage score: 5, severe risk, stop heat styling immediately 

#Limitations 
-Model accuracy would improve with more real world data 


