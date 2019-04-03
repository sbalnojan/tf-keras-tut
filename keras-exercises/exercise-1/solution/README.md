# Solution to Exercise 1

## Key Takeaways
- You can call keras layers ```layer_2 = Dense(32)(layer_1)```
- You could also call a model ````layer_2 = Dense(32)(pretrained_CNN)````
- You can call any instance of a python class if you implement 
the ```__call__(self,**)``` method
- Inputs, outputs in both .Model and .Sequential