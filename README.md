# OCR Automation Project
This automation project helps companies save costs by verifying whether their vendors are VAT-compliant. The system extracts text from invoice images to identify valid company registration numbers. These details can then be matched against a master vendor database to confirm VAT registration status.

In a South African context the goal would be to ensure that the company works with VAT-registered vendors, enabling it to claim back input VAT from SARS on qualifying purchases.
## Setup
1. Install the Sema4 extioin for VS Code.
2. Install Tesseract on your local machine....tbc
3. Install pip packages....tbc
4. Configure file paths...
### Configure Files
Configure tesseract path

## Run in VS Code
To run the project first there are two parts you need to run. 
1. First run the "Get Invoice Data" task.
2. Then run the "Generate Excel" task.
<img src="https://github.com/InnoJanu/OCR-Automation-with-Robocorp/blob/main/README%20Images/run_in_vs_code.jpg?raw=true"
     alt="Run in VS Code"
     width="70%" />
```
edit this file path
```
Optional: You can change the file path to a directory with your own images if you'd like to test it....
```
original path
```
to:
```
Your own path
```
# Potential expansion to the project
This project serves as a segment of a larger project. There is still potential to add additional automation before and afer this step. Architecture of you system may vary and this is simply a suggestion of how it could look like.

The section highligted in green shows where this project fits into the larger scope of potential expansion to the project.

Potential additions to project:
+ *Add a bot that retrieves invoices and puts them into a directory.*
+ *Add a bot that sends the sends the data back to another database.*

![image alt](https://github.com/InnoJanu/OCR-Automation-with-Robocorp/blob/main/README%20Images/project_overview.jpg?raw=true)
