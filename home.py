import streamlit as st
import socket
from datetime import datetime
from ports import ports_info


def get_ip(url):
    # ideia veio daqui: https://nekkantimadhusri.medium.com/how-to-get-ip-address-of-website-using-python-f03707c50499
    return socket.gethostbyname(url)


if 'cm' not in st.session_state:
    st.session_state.cm = False

if 'param' not in st.session_state:
    st.session_state.param = {}

st.title("Interface de Port Scanner")

ip_addr = ""

file_select = st.sidebar.selectbox(
    'Opções de Entrada',
    ('URL', 'Endereço IP')
)

if file_select == "URL":
    ip_addr = st.sidebar.text_input(
        "Coloque o URL Aqui! 👇"
    )

    if ip_addr:
        st.sidebar.write("Você Colocou: ", ip_addr)

        ip_addr = get_ip(ip_addr)

        st.sidebar.write("Endereço IP: ", ip_addr)

elif file_select == 'Endereço IP':

    ip_addr = st.sidebar.text_input(
        "Coloque o IP Aqui! 👇"
    )

    if ip_addr:
        st.sidebar.write("Você Colocou: ", ip_addr)

    ip_addr = get_ip(ip_addr)

    

    
# limite = st.sidebar.slider("Até qual porta?", 0, 65535, 800)
# st.sidebar.write("Você está Escaneando Até a Porta ", limite)

lf = st.sidebar.number_input("Limite Inferior: ", min_value=1, max_value=65534, value=1)
ls = st.sidebar.number_input("Limite Superior: ", min_value=2, max_value=65535, value=65535)

# Display the inputted number
st.sidebar.write("Vamos Escanear Portas entre",lf,"e", ls)

if st.button("Run Port Scanner"):

    # Origem do código: https://www.geeksforgeeks.org/port-scanner-using-python/

    st.write("-" * 50)
    st.write("Scanning Target: " + ip_addr)
    st.write("Scanning started at:" + str(datetime.now()))
    st.write("-" * 50)
    
    try:
        
        # will scan ports between 1 to 65,535
        for port in range(lf, ls+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)


            # returns an error indicator
            result = s.connect_ex((ip_addr,port))
            if result ==0:
                st.write("Port {} is open".format(port))
            else:
                st.write("Port {} is closed".format(port))

            if port in ports_info:
                d = ports_info[port]
                st.write(f"Service Name: {d["Service name"]}")
                st.write(f"Transport Protocol: {d["Transport protocol"]}")
                st.write(f"Description: {d['Description']}")
            st.write("-" * 50)
            
            s.close()
        st.write("Processo Concluído")
    except:

        st.write("Conexão Não Foi Bem Sucedida, Tente com Outro Endereço")





