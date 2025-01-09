import streamlit as st
import pandas as pd
import joblib

# Load the pretrained model
#def load_model(file_path):
#    with open(file_path, 'rb') as f:
#        return pickle.load(f)

# Main Streamlit App
def main():
    # Title
    st.title("SCORE PREDICTION USING PRE-TRAINED MODELS")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file:
        # Read the uploaded file into a DataFrame
        df = pd.read_csv(uploaded_file)
    
        # Display the DataFrame
        st.write("### Uploaded CSV File:")
        st.dataframe(df.head())

        # Select columns
        columns = st.multiselect("Select Columns for Prediction. Note that the columns should be selected in order", options=df.columns)
        if not columns:
            st.warning("Please select at least one column.")
        else:
            selected_data = df[columns]

            # loaded models
            models = {}
            model_files = ["rf_model.pkl", "xgb_model.pkl", "lgbm_model.pkl", "knn_model.pkl"]
            for model_file in model_files:
                models[model_file] = joblib.load(model_file)
            #    with open(model_file, "rb") as f:
            #        models[model_file] = pickle.load(f)

            # select model for prediction
            model_choice = st.selectbox("Choose a model: ", options=list(models.keys()))
            predictions = pd.DataFrame(index=df.index)
            if model_choice:
                selected_model = models[model_choice]
            
                # Step 5: Make Predictions
                predictions['Accuracy'] = selected_model.predict(selected_data)
                st.write("Predictions for every ID. Points >= 8 labelled 3, Points>=6.5 labelled 2, Points>=5 labelled 1")
                st.dataframe(predictions)

if __name__ == "__main__":
    main()
