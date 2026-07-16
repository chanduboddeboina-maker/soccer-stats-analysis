
import streamlit as st
from data import get_competition,get_clean_events,get_matches
from  charts import plot_shot,plot_passes,plot_mostTime
from css import load_css

st.set_page_config(
    page_title='Football stats analysis',
    layout='wide',
    page_icon="⚽"
)

st.markdown(load_css(), unsafe_allow_html=True)
st.title('⚽football stats analysis')
st.markdown("Powered by StatsBomb Open Data")
st.sidebar.header('select match')

competition=get_competition()
competition['label']=(
    competition['competition_name']+' - '+competition['season_name']
)

selected_label=st.sidebar.selectbox(
    'competitions and seasons',
    competition['label'].unique()
)

selected_comp = competition[competition['label'] == selected_label].iloc[0]
selected_comp_id=selected_comp['competition_id']
selected_season_id=selected_comp['season_id']

matches=get_matches(selected_comp_id,selected_season_id)
matches['label']=(
    matches['home_team']+' vs '+matches['away_team']+"("+matches['match_date']+')'
)

selected_match_label=st.sidebar.selectbox(
       "matches",
       matches['label'].unique()
)

selected_match=matches[matches['label']==selected_match_label].iloc[0]
match_id=selected_match['match_id']
home_team=selected_match['home_team']
away_team=selected_match['away_team']

@st.cache_data
def load_events(match_id):
    return get_clean_events(match_id)

try:
   shots,passes,touches=load_events(match_id)
except Exception as err:
   st.error('this match details are not found in free ,need to upgrade to subcription')
   st.stop()

select_team=st.sidebar.radio(
   'choose the team',
   [home_team,away_team]
)

team_players=touches[touches["team"]==select_team]['player'].unique()
selected_player=st.sidebar.selectbox(
   "player for Heatmap",
        team_players
   )


home_shots=shots[shots['team']==home_team]
away_shots=shots[shots['team']==away_team]

home_xg=round(home_shots['shot_statsbomb_xg'].sum(),2)
away_xg=round(away_shots["shot_statsbomb_xg"].sum(),2)

home_passes=passes[passes['team']==home_team]
away_passes=passes[passes['team']==away_team]

home_accuracy=round( len(home_passes[home_passes['pass_outcome'].isna()])/len(home_passes)*100,1) if len(home_passes)>0 else 0.0
away_accuracy=round( len(away_passes[away_passes['pass_outcome'].isna()])/len(away_passes)*100,1) if len(away_passes)>0 else 0.0

total_touches=len(touches)
home_poss=round(len(touches[touches['team']==home_team])/total_touches*100,1)
away_poss=round(len(touches[touches['team']==away_team])/total_touches*100,1)



col1,col2,col3=st.columns([2,1,2])
with col1:
   st.metric(home_team,selected_match["home_score"])
with col2:
   st.markdown('VS')
with col3:
   st.metric(away_team,selected_match["away_score"])


st.divider()
st.subheader("📊 Match Summary")
st.markdown('---')

c1,c2,c3,c4,c5=st.columns([2,1,1,1,2])
with c1:
    st.metric(home_team,len(home_shots))
with c3:
    st.markdown("**shots**")
with c5:
    st.metric(away_team,len(away_shots))

c1,c2,c3,c4,c5=st.columns([2,1,1,1,2])
with c1:
    st.metric(home_team,home_xg,help="excepted goals")
with c3:
    st.markdown("**xG**")
with c5:
    st.metric(away_team,away_xg,help="excepted goals")

c1,c2,c3,c4,c5=st.columns([2,1,1,1,2])
with c1:
    st.metric(home_team,f"{home_accuracy}%")
with c3:
    st.markdown("pass accuracy")
with c5:
    st.metric(away_team,f"{away_accuracy}%")

c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 1, 2])
with c1:
    st.metric(home_team,f"{home_poss}%")
with c3:
    st.markdown("**Possession**")
with c5:
    st.metric(away_team,f"{away_poss}%")

st.divider()



st.divider()

col_left,col_right=st.columns(2)
with col_left:
   st.subheader(f"shots map for {select_team}")
   fig_shot=plot_shot(shots,select_team)
   st.pyplot(fig_shot)
with col_right:
   st.subheader(f"passes map for {select_team}")
   fig_pass=plot_passes(passes,select_team)
   st.pyplot(fig_pass)

st.divider()


st.subheader(f"player heatmap -{selected_player}")
fig_touch=plot_mostTime(touches,selected_player)
st.pyplot(fig_touch)