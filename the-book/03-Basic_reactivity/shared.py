import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_freqpoly, coord_cartesian
from scipy import stats


def freqpoly(x1, x2, binwidth=0.1, xlim=(-3, 3)):
    # Combine data into a DataFrame
    df = pd.DataFrame(
        {"x": np.concatenate([x1, x2]), "g": (["x1"] * len(x1)) + (["x2"] * len(x2))}
    )

    # Create the plot
    plot = (
        ggplot(df, aes(x="x", color="g"))
        + geom_freqpoly(binwidth=binwidth, size=1)
        + coord_cartesian(xlim=xlim)
    )
    return plot


def t_test(x1, x2):
    # Perform Welch's t-test (equal_var=False matches R's default)
    res = stats.ttest_ind(x1, x2, equal_var=False)

    # Calculate confidence interval (Requires SciPy 1.11+)
    ci = res.confidence_interval()

    return f"p value: {res.pvalue:.3f}\n[{ci.low:.2f}, {ci.high:.2f}]"


# --- Example Usage ---
# x1 = np.random.normal(0, 1, 100)
# x2 = np.random.normal(0.5, 1, 100)
# print(t_test(x1, x2))
# print(freqpoly(x1, x2))
