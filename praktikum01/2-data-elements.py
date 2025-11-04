# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Percobaan Mandiri
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 2: Data Elements")
st.subheader("praktikum 01 Nama Kelompok")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan dataframe
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Hightlight Minimum Value di DataFrame")

# Highlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kelompok
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C")

# Metrics sesuai delta_color
# delta_color digunakan unruk memberi warna sesuai arah perubahan:
# 

# definisikan variasi variabel metrics
col1, col2, col3 = st.columns(3)

# Menampikan indikator data
col1.metric("Curah Hujan", "100 cm", "10cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") # netral 

# Menampilkan metrik tambahan dengan nilai koson atau nol
st.metric(label="Speed", value=None, delta=0)
st.metric ("Tress", "91456", "-1132649")

# superfunction
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))

# defining multiple arguments in write function
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))

# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nwrite is Super function")

# importing Necessary Libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])

# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])

# Defining Chart in write() function
st.write(chart)

# Magic
# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4

# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

# Magic working on Charts
import matplotlib.pyplot as plt
import numpy as np

s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

# Magic chart
"chart", chart