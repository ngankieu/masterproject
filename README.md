

## Getting Started

1. Create a Virtual Environment "Education":

```bash
python -m venv education
```

2. Activate the Virtual Environment

```bash
education\Scripts\activate
```
 
3. Install the necessary libraries mentioned in requirements below.

```bash
pip install -r requirements.txt
```

4. Install Jupyter Notebook in the Virtual Environment

```bash
pip install notebook
```

5. Add the Virtual Environment to Jupyter

```bash
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name "education"
```

6. Add the Virtual Environment to Jupyter

```bash
jupyter notebook
```
7. Run the Streamlit from the terminal

```bash
streamlit run app.py
```
8. Download Git (Windows)

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repository-name.git
git push -u origin main
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT


