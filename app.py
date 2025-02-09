import streamlit as st
import pickle

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('verctorizer.pkl', 'rb'))

st.title("SMS Spam Classification application")
st.write("This application is used to classify sms as spam or not spam")
user_input = st.text_area("Enter a message:", height=150)

if st.button("Classify"):
    if user_input:
        data = [user_input]
        vectorizer_data = cv.transform(data).toarray()
        result = model.predict(vectorizer_data)
        if result[0] == 0:
            st.write("The message is not spam")
        else:
            st.write("The messsage is spam")
    else:
        st.write("Please enter an message to classify")
        