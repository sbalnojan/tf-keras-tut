# Tensorflow and Keras Tutorial/Exercises
Maybe it's just me, but I learn fastest if:
- I have actually done something (yeay exercises!)
- and get to understand the underlying principles (yeay, minimal examples)

With that in mind I try to collect a reasonable learning path for
- Tensorflow
- Keras
- Tensorflow Estimator API.

**Minimal examples** mean that I try to provide the simplest possible way of
explaining something. That means, in order to understand keras custom layers, 
I try to provide the simplest possible layer; In order to understand how 
tensorboard logging works, we work it into a simple minimize x^2 example.

That also means, that unless absolutely necessary, everything works with 
random dummy input data.
## Structure
 
 This works with Python 3.6+ and compatible tensorflow etc., see requirements.txt.
 ```bash 
 - tensorflow-exercises             # the tensorflow exercises
 -- exercise-1                      # 
 ---file1.py                        # Template code you're supposed to complete
 ---solution/file1.py               # A working solution
 ---solution/README.md              # An explanation!
 --...
 - requirements.txt                 # shared requirements currently.
 ```
 
 One exercise consists of:
 - The Exercise explanation given HERE. This contains in particular "Hints" which
 you should use.
 -  The solution/README.md which contains a solution + "Key takeaways"
 - Exercises might have subparts a-b-c, and sometimes contain a detoure in order
 to gain a deeper understanding into something not nec. related to
  Keras/Tensorflow.
  
 ## Virtual Env
 I would always recommend that you work in an virtual environment,
 and run ```make dep``` to install the requirements.
  
 # Keras Exercises
 These exercises are meant to understand keras.
 ### Exercise 1 - How Models work in keras
 In keras there is the general "model", the class keras.models.Model and there
 is a simpler one, the class keras.models.Sequential. 
 
 a) Construct a model (with 
 one layer in total) with
 - 10 inputs
 - a "dense" layer
 - 2 outputs
 
 once in the class .Sequential, then in the class .Model.
 
 b detoure) Make a python class "InputDummy" which is "callable" and simply 
 prints the called parameter (see demo code for that that means if you don't).
 
 c) Construct a longer .Sequential() model with 10 inputs, 2 hidden layers
 with 2 and 10 units and 2 output units.
 