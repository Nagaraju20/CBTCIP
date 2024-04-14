from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_payment_receipt(customer_name, amount_paid, payment_date):
 # Create a PDF document
 pdf_file_name = 'payment_receipt.pdf'
 c = canvas.Canvas(pdf_file_name, pagesize=letter)

 # Set font and size
 c.setFont("Helvetica-Bold", 16)

 # Title
 c.drawCentredString(300, 750, "Payment Receipt")

 # Customer information
 c.setFont("Helvetica", 12)
 c.drawString(50, 700, f"Customer Name: {customer_name}")
 c.drawString(50, 680, f"Amount Paid: ${amount_paid}")
 c.drawString(50, 660, f"Payment Date: {payment_date}")

 # Footer
 c.setFont("Helvetica", 10)
 c.drawCentredString(300, 50, f"Issued on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

 # Save the PDF file
 c.save()
 print(f'Payment receipt saved as {pdf_file_name}')

# Example usage
customer_name = 'John Doe'
amount_paid = 100.00
payment_date = '2024-04-05'

create_payment_receipt(customer_name, amount_paid, payment_date)
