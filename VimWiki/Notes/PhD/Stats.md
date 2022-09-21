# Bibliography
* Frodesen (very complete)
* Cowan (good for reference)
* James
* Bohm - Zech
* Barlow (least formal, most didactical)

## ROC curve

I will save the result of the model prediction and the result of Tight,
taking Zrad as a True Value.

* context:: decision theory, classification problems.
* definition:: true positive rate ($TPR$) $vs$ false positive rate ($FPR$), for various threshold settings.
    ```latex
    \begin{equation}
    TPR = \frac{\sum_j TP}{\sum_j TP+FN}
    \end{equation}
    ``` 

In this case $TP$ happens when both the method of classification and the value of Zrad classify as signal.
The denominator is just Zrad sample.


## General Concepts
* Difference between probability and statistics.In probability given the data we compute the results, whereas in statistics given the results we infer the parameters of the problem.
* Difference between error and uncertainty. Uncertainty is related to the random nature of the process, while error is related to general mistakes
* We distinguish uncertainty into statistical and systematic.

## Terminology
* Conjunto: coleccion de elementos que pertenecen a una categoria particular
* S -> conjunto muestral
* suceso -> subconjunto de S

Interpretaion on probability:
* Frecuentist: p(A) = lim NA/N
* Bayesian: degree of credibility
La interpretacion Bayesiana de la probabilidad es como grado de confianza.


