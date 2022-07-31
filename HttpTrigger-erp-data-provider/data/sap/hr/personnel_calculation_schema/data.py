# See https://help.sap.com/docs/ERP_HCM_SPV/b52ef0936e7c43c7ba12ce64ee6c32db/5c9fe2539c70424de10000000a174cb4.html?version=600_HRSP_H3

data = [
    {
        "id": "1",
        "Func.": "COM",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Payroll schema: INTERNATIONAL"
    },
    {
        "id": "2",
        "Func.": "COM",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Gross wage calculation and"
    },
    {
        "id": "3",
        "Func.": "COM",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "transfer"
    },
    {
        "id": "4",
        "Func.": "COPY",
        "Par1": "XIN0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Initialization of payroll"
    },
    {
        "id": "5",
        "Func.": "COPY",
        "Par1": "XBD0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Edit basic data"
    },
    {
        "id": "6",
        "Func.": "IF",
        "Par1": None,
        "Par2": "SPRN",
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Special run?"
    },
    {
        "id": "7",
        "Func.": "RFRSH",
        "Par1": None,
        "Par2": "IT",
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Delete IT"
    },
    {
        "id": "8",
        "Func.": "ENDIF",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "to: Special run?"
    },
    {
        "id": "9",
        "Func.": "COPY",
        "Par1": "XPRO",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Import previous result for current period"
    },
    {
        "id": "10",
        "Func.": "COPY",
        "Par1": "XLR0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Import last payroll result"
    },
    {
        "id": "11",
        "Func.": "COPY",
        "Par1": "XT00",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Gross remuneration (time management)"
    },
    {
        "id": "12",
        "Func.": "COPY",
        "Par1": "XLON",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": "*",
        "Text": "Loans"
    },
    {
        "id": "13",
        "Func.": "COPY",
        "Par1": "XAP0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": "*",
        "Text": "Import further payments/deductions"
    },
    {
        "id": "14",
        "Func.": "COPY",
        "Par1": "XAP9",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Import further payments/deductions"
    },
    {
        "id": "15",
        "Func.": "COPY",
        "Par1": "XAL0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": "*",
        "Text": "Factoring and storage"
    },
    {
        "id": "16",
        "Func.": "COPY",
        "Par1": "XAL9",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Factoring and storage"
    },
    {
        "id": "17",
        "Func.": "COPY",
        "Par1": "XTBS",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Save table before iteration"
    },
    {
        "id": "18",
        "Func.": "LPBEG",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Start iteration"
    },
    {
        "id": "19",
        "Func.": "COPY",
        "Par1": "XTBL",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Reload saved tables"
    },
    {
        "id": "20",
        "Func.": "COPY",
        "Par1": "XDD9",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Processing of deductions and storage"
    },
    {
        "id": "21",
        "Func.": "COPY",
        "Par1": "XNA0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": "*",
        "Text": "Cumulation of net amount/payment amount"
    },
    {
        "id": "22",
        "Func.": "COPY",
        "Par1": "XNA9",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Cumulation of net amount/payment amount"
    },
    {
        "id": "23",
        "Func.": "COPY",
        "Par1": "XDNT",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "All deductions taken?"
    },
    {
        "id": "24",
        "Func.": "LPEND",
        "Par1": None,
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "End of iteration"
    },
    {
        "id": "25",
        "Func.": "COPY",
        "Par1": "XRR0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Retroactive accounting"
    },
    {
        "id": "26",
        "Func.": "COPY",
        "Par1": "XNN0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Net payments/deductions and transfer"
    },
    {
        "id": "27",
        "Func.": "COPY",
        "Par1": "XAC0",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": "*",
        "Text": "Month End Accruals"
    },
    {
        "id": "28",
        "Func.": "COPY",
        "Par1": "XEND",
        "Par2": None,
        "Par3": None,
        "Par4": None,
        "D": None,
        "Text": "Final processing rule"
    },
]