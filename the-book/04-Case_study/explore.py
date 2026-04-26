import polars as pl
from plotnine import *


injuries = pl.read_csv("the-book/04-Case_study/neiss/injuries.tsv.gz", separator="\t")
products = pl.read_csv("the-book/04-Case_study/neiss/products.tsv", separator="\t")
population = pl.read_csv("the-book/04-Case_study/neiss/population.tsv", separator="\t")

population.head(3)


selected = injuries.filter(pl.col("prod_code") == 649)

selected.shape

selected.head()

# weighted count by location
(
    selected.group_by("location")
    .agg(n=pl.col("weight").sum())
    .sort(by="n", descending=True)
)


# weighted count by body part

(
    selected.group_by("body_part")
    .agg(n=pl.col("weight").sum())
    .sort(by="n", descending=True)
)


# weighted count by diagnosis
(selected.group_by("diag").agg(n=pl.col("weight").sum()).sort(by="n", descending=True))


# pattern across sex and age

agg_by_age_sex = (
    selected.group_by(["age", "sex"])
    .agg(n=pl.col("weight").sum())
    .sort(by="n", descending=True)
)

(
    ggplot(agg_by_age_sex.to_pandas(), aes("age", "n", color="sex"))
    + geom_line()
    + labs(y="Estimated number of injuries")
)


agg_by_age_sex = (
    selected.group_by(["age", "sex"])
    .agg(n=pl.col("weight").sum())
    .join(population, how="left", on=["age", "sex"])
    .with_columns(rate=pl.col("n") / pl.col("population") * 1e4)
)

(
    ggplot(agg_by_age_sex.to_pandas(), aes("age", "rate", color="sex"))
    + geom_line()
    + labs(y="Injuries per 10,000 people")
)
