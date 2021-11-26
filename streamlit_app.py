import time

import numpy as np
import pandas as pd
import streamlit as st

st.caption("Source code is here. https://github.com/IkokObi/streamlit-trial-demo")

st.header("Display and style data")


st.subheader("Use magic")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
df


st.subheader("Write a data frame")
st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)

# interactive table
dataframe = np.random.randn(15, 20)
st.dataframe(dataframe)

# table style
dataframe = pd.DataFrame(
    np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

# static table
dataframe = pd.DataFrame(
    np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)
st.table(dataframe)


st.subheader("Draw a line chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)


st.subheader("Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(map_data)


st.header("Widgets")
# slider
x = st.slider("x")
st.write(x, "squared is", x * x)

# key
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

st.subheader("Use checkboxes to show/hide data")
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    chart_data


st.subheader("Use a selectbox for options")
option = st.selectbox("Which number do you like best?", df["first column"])
"You selected: ", option


st.header("layout")
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")


st.subheader("Show progress")
"Starting a long computation..."
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"...and now we're done!"
