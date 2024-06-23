r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**
```
1. False, in order to evaluate the in-sample (training) error we need only the training set.
```
```
2. False, if our data is ordered by a certain feature. For example, the first half of the images
are dolphins and the other half are horses than a 50-50 split for train-test would be meaningless.
```
```
3. True, during the cross-validation stage we are learning the suitable hyper-parameters for the model, and the
test set is only used once in the final validation of our model.
```
```
4. True, the performance of the validation set in the cross-validation is our way to estimate
the performance of the model on unseen data, which is later tested on the test set.
```
```

"""

part1_q2 = r"""
**Your answer:**


```python
```
My friend's approach isn't justified, using the test-set in order
to tune the hyper-parameters generates over-fitting on the test-set data.
This generates leakage of our test set and makes it harder to generalize on the whole data,
therefore he should cross-validate on a validation set and only use the test-set once in the end.
"""
# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**

``` The selection of ``` $\Delta > 0$ ``` is arbitrary for the SVM loss because as we saw in-depth in Intro to ML,
our primary goal is to ensure that the correct class score is higher than any other class, the optimization problem
will grant us a different (normalized) weights matrix for different Delta values but the margin will remain the same.
For example, for a large value of Delta we will expect the weights to be scaled proportionally downwards by the size of ``` $\Delta$.



"""

part2_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```
1. The learning rate is good. We've tried multiple values and found that the
values higher than what we've picked (higher than 0.01) had a very spikey training and validation loss graph
and for values lower than 0.01 the loss didn't converge fast enough to the optimal possible loss.
2. Based on the training set graph accuracy and the training set accuracy we
can infer that the model is slightly overfitted to the training set. Because
the training set accuracy has about 5 percent higher accuracy than the test set
accuracy.
```

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
