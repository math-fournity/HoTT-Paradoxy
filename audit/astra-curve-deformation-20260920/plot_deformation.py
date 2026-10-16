#!/usr/bin/env python3
"""Sample the explicit Lean formula for illustration; this plot is not proof evidence."""
from pathlib import Path
import hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
u=np.unique(np.r_[np.linspace(1e-5,1-1e-5,4001),np.geomspace(1e-8,.05,400),1-np.geomspace(1e-8,.05,400)])
def curve(t,u):
 v=2*u-1;rho=v/(1-np.abs(v))
 r=(1+t*t)/2*(rho/(1+(1-t)**2*np.abs(rho)))+(1-t)/2
 d=1+(t*r)**2;x=r/d;y=t*r*r/d
 return np.column_stack(((1-t)*x+2*t*y-t,-2*t*x+(1-t)*y))
times=[0,.25,.5,.75,1]
frames=[curve(t,u) for t in times]
allp=np.concatenate(frames)
lo=allp.min(axis=0)-.18;hi=allp.max(axis=0)+.18
fig,axes=plt.subplots(1,5,figsize=(15,4.3),layout='constrained')
for ax,t,p in zip(axes,times,frames):
 seg=np.stack((p[:-1],p[1:]),axis=1)
 lc=LineCollection(seg,cmap='viridis',norm=plt.Normalize(0,1),linewidth=2.5)
 lc.set_array((u[:-1]+u[1:])/2);ax.add_collection(lc)
 marked=curve(t,np.array([.1,.3,.5,.7,.9]))
 ax.scatter(marked[:,0],marked[:,1],c=[.1,.3,.5,.7,.9],cmap='viridis',vmin=0,vmax=1,s=24,zorder=4,edgecolor='white',linewidth=.5)
 ax.set(xlim=(lo[0],hi[0]),ylim=(lo[1],hi[1]),aspect='equal',title=f't = {t:g}')
 ax.axhline(0,color='#dddddd',lw=.6,zorder=0);ax.axvline(0,color='#dddddd',lw=.6,zorder=0)
 ax.spines[['top','right']].set_visible(False)
 if t==0:ax.text(.5,.14,'N = (0,1)',ha='center',fontsize=10)
 if t==1:
  ax.scatter([1],[0],s=55,facecolor='white',edgecolor='#c93c3c',lw=1.5,zorder=6)
  ax.annotate('removed p',(1,0),xytext=(.16,1.28),arrowprops={'arrowstyle':'->','color':'#c93c3c'},color='#a12525',fontsize=9)
fig.suptitle('Continuous curve embeddings from the open segment to the punctured circle',fontsize=15)
fig.supxlabel('Colors track the same curve parameter u. Finite samples illustrate the formula; the universal statements are proved in Lean.',fontsize=10)
fig.savefig(OUT/'deformation.png',dpi=180)
fig.savefig(OUT/'deformation.svg')
(OUT/'PLOT.json').write_text(json.dumps({'status':'ILLUSTRATION_ONLY_NOT_PROOF','times':times,'interior_samples_per_time':len(u),'source':'HoTT/formal/astra-real-geometry/DeformationCircle.lean','source_sha256':hashlib.sha256((ROOT/'HoTT/formal/astra-real-geometry/DeformationCircle.lean').read_bytes()).hexdigest()},indent=2)+'\n')
print('Illustration generated:',len(u),'interior parameters per frame')
