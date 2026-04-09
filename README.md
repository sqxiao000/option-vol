# Stochastic Volatility in Options Trading

The Black-Scholes model is famous for being the standard option pricing model, and taught in curriculums. I learned how to derive it with Ito's Lemma and differential equations. However, one characteristic of the model is that Black-Scholes assumes a constant volatility. Stochastic Volatility assumes a random walk for volatility, and an extension of the Black Scholes is the Heston Model for options pricing, which accounts for stochastic volatility.

In today's time where volatility is spiking all over different asset classes, oil and commodities would be a good example to analyze. In this project my goal is to (for an asset):

1. Create a volatility surface
2. Generate the market's future price distribution based on option prices
3. Compare pricing results from Black-Scholes vs. Heston
 
