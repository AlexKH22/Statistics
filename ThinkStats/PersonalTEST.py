from hypothesis import *

# ct = CoinTest((140, 110))
# p = ct.PValue()
# print(p)
#
# live, firsts, others = first.MakeFrames()
# data = firsts.prglngth.values, others.prglngth.values
# ht = DiffMeansPermute(data)
# pvalue = ht.PValue()
#
# print(pvalue)
#
# ht.PlotCdf()
# thinkplot.Show(xlabel='test statistic',
#                ylabel='CDF')

data = [8, 9, 19, 5, 8, 11]
dt = DiceTest(data)
pvalue = dt.PValue(iters=1000)
print(pvalue)