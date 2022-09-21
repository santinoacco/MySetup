# Hypothesis Test

**Hypothesis**::
    - (Brant): proposed values for a given set of parameters.
    - (Cowan)
    - (Frodesen)
    - (Wikipedia):
    - (Noacco): an assertion of some attribute of a random variable,
                which proposes values for a given set of parameters that characterize said attribute.

**Test**::
    - (Brant) A **Test** computes the probability that the given hypothesis is _True_ if accepted.
    - (Cowan) The goal of a statistical **Test** is to make a statement about how well the observed data stand in agreement with given predicted probabilities.
    - (Noacco) Method or protocol to state the agreement of the hypothesis to the observed data. This agreement is stablished by computing the probability of mistakenly rejecting an hypothesis.

-   The general rule is to define a **Null Hypothesis** ($h_0$) over which one preforms the test with the expectation to reject it.
Logically, the negation of $H_0$ is a valid hypothesis too,
which is the natural **Alternative Hypothesis** ($H_j$);
however, one could define a set of $\{H_j\}$ not necessary mutually exclusive.

-   To investigate the measure of agreement between the observed data and a given hypothesis,
one constructs a function of the measured variables called a _test statistic_ [$t(x)$].

-   Each of the hypotheses will imply a given $p.d.f$ for the statistic $t$,
i.e. $f(t|H_0), \dots, f(t|H_j)$


**Significance Level** [$\alpha$]::
    - (Brant): an arbitrary probability (set by the scientist before the experiment) to act as a threshold of rejection.
If the probability that the hypothesis is True is smaller than $\alpha$,
then one regards the occurrence of the hypothesis as improbable.
Important Note: the opposite is not necessary true.

    - (Cowan): the critical region is chosen such that the probability for $t$ to be observed there,
under assumption of the hypothesis $H_0$, is some value $\alpha$ (4.1).
One would not reject the hypothesis $H_0$ if the value of $t$ observed is less than $t_{cut}$,
this is $t < t_{cut}$.


**Error of the first kind**:
    the probability to reject $H_0$ if $H_0$ is true,
    in terms of the variables mention above,
    this probability is given by $\alpha$.
    
**Error of the second kind**:
    the probability to not reject $H_0$ if $H_0$ is not true (false).
    This probability is given by $\beta$ (4.2),
    which depends on the $p.d.f$ given by the $H_j$.

The **power** of the test is $1 - \beta$,
because it is the power to discriminate against the alternative hypothesis.

**Significance**
-   the equivalent significance of the $p_{value}$ is defined such that the probability of finding a normally distributed variable $Z\sigma$ (Z times standar deviations) away from it's mean,
is given by the $p_{value}:
$Z = \Phi^{-1}(1-p_{value})$

## Likelihood-ratio test:


-   Frodesen sec. 14.2.(4-5)
-   Brant sec. 8.6

## Goodness of fit test:

-   (Cowan):
    How well a given null hypothesis is compatible with the observed data without specific reference to any alternative hypothesis. The key is to construct a test statistic whose value itself reflects the level of agreement between the observed measurements an the predictions of $H_0$.

