import pandas as pd 


def load_data(): 
    # Specify the URL of the publicly accessible Google Sheet
    sheet1_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLTgxkwclFqHFN6qSfGfYhNgUyK4lyISq5nMyp43tLBl2ICiwbTnvPdfJyKypHe4K8fUhKLrzA7sSd/pub?gid=0&single=true&output=csv'
    sheet2_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLTgxkwclFqHFN6qSfGfYhNgUyK4lyISq5nMyp43tLBl2ICiwbTnvPdfJyKypHe4K8fUhKLrzA7sSd/pub?gid=1641625318&single=true&output=csv'
    sheet3_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLTgxkwclFqHFN6qSfGfYhNgUyK4lyISq5nMyp43tLBl2ICiwbTnvPdfJyKypHe4K8fUhKLrzA7sSd/pub?gid=1983727577&single=true&output=csv'
    sheet4_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRLTgxkwclFqHFN6qSfGfYhNgUyK4lyISq5nMyp43tLBl2ICiwbTnvPdfJyKypHe4K8fUhKLrzA7sSd/pub?gid=1973994839&single=true&output=csv'
    newDF = pd.read_csv(sheet1_url)
    oldDF = pd.read_csv(sheet2_url)
    short_listDF = pd.read_csv(sheet3_url)
    one_listDF = pd.read_csv(sheet4_url)

    return newDF, oldDF, short_listDF, one_listDF
