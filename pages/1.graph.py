import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
from utility import *
from matplotlib.cm import get_cmap
import json
import random

page1 = "3시간별 데이터"
st.set_page_config(page_title=page1)
make_graph()