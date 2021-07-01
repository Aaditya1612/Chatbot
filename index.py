import streamlit as st
import streamlit.components.v1 as components
import base64

hide_streamlit_style = """
            <style>
            .* {margin: 0px;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
  background-image: url("data:image/png;base64,%s");
  background-position: center;
  background-repeat: no-repeat;
  background-color: white;
  width: 410px;
  height: 620px;
  padding-top: 0rem;
  padding-left: 10rem;
  margin-top: 0px;
}
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('main4.gif')

components.html('''<html>
    <body>
        <style>
            .rw-conversation-container .rw-message-container {position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%) }
            .rw-conversation-container .rw-messages-container {background-color: rgb(255,255,255,); }
            .rw-conversation-container .rw-header {background-color: blue;box-shadow: 5px 5px 10px grey;}
            .rw-conversation-container .rw-messages-container .rw-message .rw-response {background-color: rgba(73, 255, 134, 0.719);color: black;}
        </style>
        <script>!(function () {
            let e = document.createElement("script"),
              t = document.head || document.getElementsByTagName("head")[0];
            (e.src =
              "https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.js"),
              // Replace 1.x.x with the version that you want
              (e.async = !0),
              (e.onload = () => {
                window.WebChat.default(
                  {
                    outerHeight: "1000px",
                    title: "Lara",
                    showFullScreenButton: true,
                    initPayload: "/greet",
                    customData: { language: "en" },
                    socketUrl: "https://b226ca3dda8f.ngrok.io",
                    // add other props here
                  },
                  null
                );
              }),
              t.insertBefore(e, t.firstChild);
          })();
          </script>
          
    </body>
</html>''',height=500)
