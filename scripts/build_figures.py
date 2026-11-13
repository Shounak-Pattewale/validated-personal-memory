from pathlib import Path
import zipfile, shutil, json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'results').mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'pdf.fonttype':42})
scores=pd.read_csv(ROOT/'data/audit/scores.csv')
models=['deepseek-v4.1-flash:1017','gemma4:31b','glm-5.2']
arms=['no_memory','full_history','recent_6','rolling_summary','bm25_6','dense_6','hybrid_6','middleware_selected','middleware_visible']
a=scores.pivot(index='arm',columns='model',values='strict_accuracy').loc[arms,models].to_numpy()*100
fig,ax=plt.subplots(figsize=(6.6,4.4));ax.imshow(a,vmin=0,vmax=100,cmap='Blues',aspect='auto')
ax.set_xticks(range(3),['DeepSeek','Gemma','GLM']);ax.set_yticks(range(9),['No memory','Full history','Recent six','Rolling summary','BM25','Dense','Hybrid','Selected records','All visible records'])
for i in range(9):
 for j in range(3):ax.text(j,i,f'{a[i,j]:.1f}%',ha='center',va='center',color='white' if a[i,j]>65 else '#13283d')
ax.tick_params(length=0);fig.tight_layout();fig.savefig(ROOT/'results/accuracy.pdf');plt.close(fig)
fig,ax=plt.subplots(figsize=(7.3,3.8));ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off')
def box(x,y,w,h,t):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06',facecolor='#f0f4f7',edgecolor='#344b60',linewidth=.8));ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=8.5)
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=11,color='#344b60',linewidth=.9))
box(3.4,5,3.2,.65,'Observed message + acceptance flag')
box(.1,3.25,2.7,.85,'History / summary / retrieval\nSeven baseline contexts')
box(3.7,3.25,2.6,.85,'Model-proposed operation\nPreview and finalisation')
box(3.7,1.65,2.6,.85,'SQLite records\nSaved state and receipt')
box(7.15,2.45,2.7,1.05,'Reference-state comparison\nOffline trace audit')
box(.15,.1,2.6,.8,'Shared reader instruction\nBaseline answers')
box(3.55,.1,3,.8,'Shared reader instruction\nSelected / visible answers')
arrow((5,5),(5,4.1));arrow((3.4,5.2),(1.45,4.1));arrow((1.45,3.25),(1.45,.9));arrow((5,3.25),(5,2.5));arrow((5,1.65),(5,.9));arrow((6.3,2.15),(7.15,2.9))
fig.tight_layout(pad=.2);fig.savefig(ROOT/'results/architecture.pdf');plt.close(fig)
print('Figures generated from exported scores.')
