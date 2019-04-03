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
  
 # Keras Exercises
 
 