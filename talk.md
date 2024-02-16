Intro
-----

This is a brief summary of our work in ensemble modelling of ash dispersion over the last two years

We have numerical model that can simulate the atmospheric transport, dispersion and deposition of volcanic ash and gases

Traditionally, operational forecasting relies on this kind of model to produce deterministic forecast

We are interested in going a step further and working with ensembles.

Why ensemble modelling?

* Input parameters are generally very uncertain. Especially, eruption source parameters and meteorological data. So in this way we can take into account the uncertainty of the different inputs
* We can quantify forecast errors
* We can improve forecast skill by using data assimilation. For example, using satellite observations or field measurements
* We have source term inversion techniques based on ensemble modelling

Ensemble simulations
--------------------

We use and develop the FALL3D model, a model for atmospheric transport and deposition of particles and aerosols

In order to build the ensemble we perturb different model parameters and inputs, including emission source parameters, grain size distributions, aggregation parameters, meteorological fields, and diffusion coefficients

As a result, we can produce different model outputs, such as ash/gases concentration, column mass loading, top cloud height or deposit mass loading

here, you can see an example of vertical profiles of ash emissions. Model outputs are highly sensitive to this distribution

Probability distribution of the ensembles
-----------------------------------------

We found that the gamma distribution provides a good approximation to the probability distribution of the ensemble for both airborne concentration and deposit mass loading

In the figure we represent the theoretical gamma distribution and the ensemble distribution and in most of the cases we have a good agreement

if this is true, we have, 
* when the ensemble mean is less than the ensemble spread, the mode is located at zero and we the trend shown in the upper panel
* otherwise, the mode is positive
* and in all cases the we have right-skewed distributions

Ensemble data complexity reduction
----------------------------------

In order to interpret and deal with large volumes of ensemble data, we apply a complexity reduction technique.

In this case, we simulated the 2015 eruption of Etna using an ensemble size of 120 members.

The purpose now is to find alternative output products, which provide more useful information than traditional products such as ensemble mean, ensemble spread or exceedance probability

* The complexity reduction technique removes redundancy in the ensemble data
* To this purpose, we define a metric in order to measure the distance between to ensemble members
* Ensemble members with low distances are grouped together

We can compute the probability associated with every state, as is represented is diagonal of the matrix, and it's also relevant to compute joint probabilities as two state can be highly correlated.

This matrix provides us a lot of information. For example, we can identify here three classes of qualitatively different states. For example, we have the state with the highest probability which can be compared with a low probability state with a completely different patterns of transport.

Comparison of output products
-----------------------------

Here we compare different output products that can be generated from an ensemble run.

In the upper panel we show traditional products, such as the ensemble mean and the exceedance probility. Of course, this provide valuable information, but, in general, you can cannot compare directly this with satellite image, for example. 

The ensemble mean, is a composition of very different solutions of the physical model, and the diffusion that you can see here is not a result of a physical transport, but depends on the ensemble spread.

On the other hand, below you can see, as an example, two members of the reduced ensemble.

The important point to highlight here is that these results are actual solution of the physical model. This information can be compared directly with satellite images
