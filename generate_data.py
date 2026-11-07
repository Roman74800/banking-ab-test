import numpy as np
import pandas as pd
from pathlib import Path
rng=np.random.default_rng(2026)
n=12000
user_id=np.arange(1,n+1)
variant=rng.choice(['control','treatment'],size=n)
channel=rng.choice(['organic','paid','referral'],size=n,p=[.45,.35,.2])
# Experiment design: treatment increases completion probability by 2 percentage points.
base=np.where(channel=='referral',.23,np.where(channel=='organic',.20,.17))
completed=rng.binomial(1,base+.02*(variant=='treatment'))
revenue=np.where(completed==1,rng.gamma(2,350,size=n),0).round(2)
df=pd.DataFrame({'user_id':user_id,'variant':variant,'channel':channel,'completed':completed,'revenue_rub':revenue})
out=Path(__file__).resolve().parent/'data';out.mkdir(exist_ok=True)
df.to_csv(out/'experiment.csv',index=False)
print(df.groupby('variant').agg(users=('user_id','count'),conversions=('completed','sum')))
