import os


from robocorp.tasks import task

from RPA.PDF import PDF
from RPA.JSON import JSON



@task
def generate_report():
    global pdf_path 
    pdf_path = "output/report.pdf"
    if os.path.exists(pdf_path):
        # Remove it first (to avoid PermissionError)
        os.remove(pdf_path)
    if os.path.exists("output/data.json"): 
        html_content = create_html_content()
        create_pdf(html_content)
    else: 
        print("No OCR Data Available")
    

def create_pdf(html_content):
    pd = PDF()

    pd.html_to_pdf(html_content, pdf_path)

def create_html_content():
    js = JSON()
    data = js.load_json_from_file("output/data.json")

    html_content = ""

    for item in data:
        html_content += f"""
            <h1>{item['file_name']}</h1>
            <p>Registration Number: {item['company_reg_number']}</p>
            <p>VAT Number: {item['vat_number']}</p>
        <br><br>
        """
    return html_content
    
    