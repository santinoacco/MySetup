# Kernel Methods

This part of the **non-parametric methods** to estimate distributions.

## Overview (Bishop - 2.5)

We estimate the $p.d.f$ $f(X)$ as:
>   $f(X) \simeq \frac{K}{NV}$

where $V$ is the volume of the region (**R**) that contains $X$;
$N$ is the total number of observations drawn from $f(X)$;
$K$ is number of events that are **in R** is given by:
$K = \sum^N k(\frac{x - x_j}{h})$
for a given *kernel function* $k(u)$.

## Supported Vector Machine (SVM)

