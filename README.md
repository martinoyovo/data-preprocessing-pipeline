## **Data Preprocessing Program**

### **What is it about?**

This program performs the common tasks that need to be done before data analysis, namely:

* Retrieve a dataset
* Clean the data
* Reduce the data
* Perform feature engineering
* Display some summary statistics related to the data

---

### **Installation**

To install the program, simply clone the Git repository and install the dependencies:

```bash
git clone https://github.com/martinoyovo/data-preprocessing-pipeline.git
cd data-preprocessing-pipeline

# Install dependencies
pip install -r requirements.txt
```

---

### **Usage**

To use the program, simply run the following command:

```bash
python -m github_actions.workflow
```

This command will execute the GitHub Actions workflow, which performs the following tasks:

* Downloads the `data.csv` file into the `data/raw` directory

---

### **Project Structure**

The project is organized as follows:

```
.
├── data
│   ├── raw
│   │   └── dataset.csv
│   └── cleaned
│       └── dataset_cleaned.csv
├── processed
│   └── dataset_processed.csv
├── reports
│   └── stats.txt
├── requirements.txt
├── src
│   ├── process.py
│   └── train.py
└── README.md
```
