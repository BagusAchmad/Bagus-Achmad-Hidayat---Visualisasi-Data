# import library yang dibutuhkan 
import streamlit as st

# text element
# header, untuk membuat tulisan header
st.header("Ini header")
st.subheader("ini sub header")
st.text("ini text biasa tanpa format")
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris
""")
st.caption("ini caption")
st.title("Ini Judul")

st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 1: Text Elements")
st.subheader("praktikum 01 Nama Kelompok")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")


# Bagian 2
st.header("Displaying  LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta  ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat


# Bagian 3 menampilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

#simpan ke variabel
code = '''
def hello():
    print ("Hello. Streamlit")
'''

# st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG {
            public static void main(string arg[]) {
        System.out.printIn("Hello World");
        }
     }
""", language='java')
# fungsi st.code()bisa digunakan untuk bahasa pemograman lain seperti java, javascript, C++, HTML, DLL

st.subheader("Javascript code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest); // kesalahan ketik (addalaert)
    sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementByID("demo").innerHTML = err.message; //
    menampilkan pesan error di elemen HTML dengan id 'demo'
}
""", language='javascript')
