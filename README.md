# Stochastic Volatility in Options Trading

The Black-Scholes model is famous for being the standard option pricing model, and taught in standard curriculums. I learned how to derive it with Ito's Lemma in differential equations. However, one characteristic of the model is that Black-Scholes assumes constant volatility. Stochastic Volatility is volatility modelled by a random walk, which makes a lot more intuitive sense for volatility movement. An extension of the Black Scholes Model is the Heston Model, which prices options while accounting for stochastic volatility.

In today's time where volatility is spiking all over different asset classes, commodities and tech sector stocks would be great examples to analyze. In this project my goal is, for a given asset:

1. Create a volatility surface
2. Generate the market's future price distribution based on option prices
3. Compare pricing results from the Black-Scholes vs. Heston Model
 
