'''
Visualize the distribution of likes ("upvotes") on Reddit. 
I predict it's a mixture of two poissons, depending on whether the post goes viral.
'''
import pandas as pd
import matplotlib.pyplot as plt
import pymc3 as pm
import numpy as np
import seaborn as sns

# Load data.
print("plot data")
df = pd.read_csv("HN_posts_year_to_Sep_26_2016.csv")
X = df.num_comments.values
X = np.random.choice(X, 250)

# Visualize.
sns.distplot(X, kde=False)
plt.yscale("log", nonposy="clip")
plt.xlabel("# Comments")
plt.ylabel("Log(frequency)")
plt.savefig("comments_frequency.png")
#plt.show()


# Fit model.
# 2-Mixture Poisson using iterable of distributions.
with pm.Model() as model:

    # The rates of these poissons are exponentially distributed.
    lam1 = pm.Exponential('Comment Rate: Not Viral', lam=1)
    lam2 = pm.Exponential('Comment Rate: Viral ', lam=1)

    # The data come from a mixture of poissons with rates lam1, lam2.
    pois1 = pm.Poisson.dist(mu=lam1)
    pois2 = pm.Poisson.dist(mu=lam2)

    # W controls the mixture of the distributions, which is multinomial,
    # e.g. binomial for multiple variables.
    w = pm.Dirichlet('P(viral=X)', a=np.array([1, 1]))

    like = pm.Mixture('like', w=w, comp_dists = [pois1, pois2], observed=X)

    # Sample.
    trace = pm.sample(tune=1000, draws=5000)

# Plot posterior.
pm.plot_posterior(trace)
plt.savefig("posteriors.png")
