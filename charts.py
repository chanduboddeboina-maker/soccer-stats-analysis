
from statsbombpy import sb
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import pandas as pd

def plot_shot(shots,team):
        
        team_shots=shots[shots['team']==team]

        pitch=Pitch(pitch_type='statsbomb',pitch_color='darkgreen',line_color='white')
        fig,axe=pitch.draw(figsize=(12,8))

        goals=team_shots[team_shots['shot_outcome']=='Goal']
        non_goals=team_shots[team_shots['shot_outcome']!='Goal']

        pitch.scatter(
                goals['x'],goals['y'],
                s=goals['shot_statsbomb_xg']*1000,
                c='pink',alpha=0.9,ax=axe,label='goal'      
        )

        pitch.scatter(
                non_goals['x'],non_goals['y'],
                s=non_goals['shot_statsbomb_xg']*1000,
                c='red',alpha=0.6,ax=axe,label='shot'
        )
        total_xg=shots['shot_statsbomb_xg'].sum()
        axe.set_title(f'{team} - shots Map | {total_xg} - Total Xg', fontsize=16)

        return fig



def plot_passes(passes,team_name):
        
        team_passes=passes[passes['team']==team_name]
        
        complete_passes=team_passes[team_passes['pass_outcome'].isna()]
        avg_position=complete_passes.groupby('player').agg(
                x=('x','mean'),
                y=('y','mean'),
                count=('x','count')
        ).reset_index()

        pair_count=complete_passes.groupby(['player','pass_recipient']).size().reset_index(name='pass_count')
        pair_count=pair_count[pair_count['pass_count']>=3]
        
        pitch=Pitch(pitch_type='statsbomb',pitch_color='darkgreen',line_color='white')
        fig,axe=pitch.draw(figsize=(12,8))

        for _ ,row in pair_count.iterrows():
                passer=avg_position[avg_position['player']==row['player']]
                receiver=avg_position[avg_position['player']==row['pass_recipient']]

                if passer.empty or receiver.empty:
                        continue
                
                axe.plot(
                        [passer['x'].values[0],receiver['x'].values[0]],
                        [passer['y'].values[0],receiver['y'].values[0]],
                        color='blue',alpha=0.4,
                        linewidth=row['pass_count']
                )
        pitch.scatter(
                 avg_position['x'],avg_position['y'],
                 s=avg_position['count']*20,color='grey',
                 ax=axe,zorder=3
         )

        for _ ,row in avg_position.iterrows():
               
                axe.annotate(
                        row['player'].split()[-1],
                        (row['x'], row['y']),
                        color='white', fontsize=7,
                        ha='center', va='bottom'
                )
        axe.set_title(f'{team_name}-player passes',fontsize=16)

        return fig



def plot_mostTime(touchs,player_name):
        
        player_touches=touchs[touchs['player']==player_name]
        
        pitch=Pitch(pitch_type='statsbomb',pitch_color='darkgreen')
        fig,axe=pitch.draw(figsize=(12,8))

        pitch.kdeplot(
                player_touches['x'],player_touches['y'],
                color='pink',fill=True,alpha=0.6,ax=axe
        )
        total_touches=len(player_touches)
        axe.set_title(f'{player_name} - Heatmap |  {total_touches} touches',color='white')

        return fig



         
       

   