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
To compute the training error, we use some loss function on our prediction and the real answer.
We accumulate the loss, and then divide by the size of the training set.
In order to do those calculations, we only needed the training set, and thus the answer is false.

2. False, if our data is ordered by a certain feature. For example, the first half of the images
are dolphins and the other half are horses than a 50-50 split for train-test would be meaningless.
Also, the size of the split is very important.
For example, if we have 100 images, and we split the data to 20 images for the training set, and 80 for the test set,
there is a good possibility that the generalization will not be as good, if we took 80 samples to the training set instead.

3. True, during the cross-validation stage we are training the model on the train set and validating
on the validation set. The test set is only used once in the final testing of our model.

4. True, the performance of the validation set in the cross-validation is our way to estimate
the performance of the model on unseen data, which is later tested on the test set.
```

"""

part1_q2 = r"""
**Your answer:**


```
My friend's approach isn't justified, using the test-set in order
to tune the hyper-parameters generates over-fitting on the test-set data.
This generates leakage of our test set and makes it harder to generalize on the whole data (when the model is in "operational mode",
therefore he should cross-validate on a validation set and only use the test-set once in the end.
```
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

```
From the visualization, we can sort of see the shapes of some of the digits (the most noticeable ones are 0 and 3).
Let's closely examine the picture virtualizing the "1" digit.
We can see a clear top to bottom line, right in the middle. This means that this area has (proportionally) high weight.
This makes sense, since we know that "1" has exactly this feature, that mostly differentiates it from other digits.

This also explains some of the errors. For example, we can see that there is a pretty clear "2" that was classified as
a "7". If we examine the visualization of "7", we can see that high weights are give to the top part of the "7".
Since the picture with the actual "2" has a feature that resembles this part, it can help explain why it was mislabeled. 
```

"""

part2_q3 = r"""
**Your answer:**

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


```
If we got a perfect prediction for some sample x, then the residual will be zero.
Thus, the ideal residual plot should be a straight line across the x-axis (all the residuals for all samples are zero).
We can infer from the graphs that the residuals of the training data have decreased,
and it also seems that the variance of the predictions has gotten smaller (it looks like in the first graph,
the residuals are spread across [-10,10], but in the other graph they are spread tightly between [-5,5]).
Overall, the fit of the final model is better.
```

"""

part3_q2 = r"""
**Your answer:**


```
1. Yes, it is indeed still a linear regression model.
While the function that we are fitting is non-linear, the model of the linear regression remains unchanged -
we are still taking an input matrix data X, and the main target is to find linearity between the features in that data.
The linear regression model is "blind" to the fact that some polynomial transformation was used on the data beforehand.
Simply put, the model is still linear with respect to the weights.

2. Yes.
Given a non-linear function to fit, we can use that very function on our features to get a new feature mapping.
After applying the mapping, we will have a feature that is the very same function that we are trying to fit.
Our new weights vector will have "1" at the corresponding entry for our new feature, and "0" for the rest.
Thus, having a linear correlation between that feature and the function we are mapping to.

3. It will not necessarily be a hyperplane in the original vector space.
But it will be a hyperplane in the higher dimension vector space.

If we are in some d dimension vector space, then any hyperplane in it has d-1 dimensions.
Since we ADDED a new feature, that has no linear connection with the other features,
the new classifier will be d dimensioned,
and thus it cannot be a hyperplane (unless the new feature was give a zero weight).

For example, we saw in the tutorial the feature mapping (x1,x2, x1^2 + x2^2).
We saw that the new classifier was of a circle shape, which is not a hyperplane in the old vector space.
```

"""

part3_q3 = r"""
**Your answer:**

```
1. We used np.logspace because this approach ensures that the values we are testing
in cross-validation are spread across several orders of magnitude covering small, medium and large
values for lambda.
2. In total, the model was fitted |range(lambda)| * |range(degree)| times. it is exponential in the number of
ranges of hyperparameters we are using in our model.
Since we were using the k-fold method, we also need to multiply by k.

Overall, we get |range(lambda)| * |range(degree)| * k.

Specificly, we get 20 * 3 * 3 = 180.

```

"""

# ==============

# ==============
