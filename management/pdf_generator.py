from fpdf import FPDF
from datetime import date
from num2words import num2words


def create_invoice(shop_name, shop_address, shop_phone_number, shop_gstno, order_detail, invoice_number, amount):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_left_margin = 10
    pdf.set_right_margin = 10


    pdf.set_font("Arial", size=25, style="B")
    pdf.set_text_color(255, 90, 0)
    pdf.write(7, "                               Bharat")
    pdf.set_text_color(0,0,0)
    pdf.write(7,"Off")
    pdf.ln(7)

    pdf.set_font("Arial", size=15)
    pdf.cell(200,10, txt="Office no.45 3rd Floor, Magneto Mall, Raipur 492001 (C.G.) India",border=0, ln=1, align="C")

    pdf.line(10, 30, 200, 30) # straight line

    pdf.set_font("Arial", size=15)
    
    pdf.cell(200,10, txt="",border=0, ln=2, align="C") # for line break

    pdf.cell(200, 10, txt="Date: "+str(date.today())+"     ",border=20, ln=1, align="R")

    pdf.cell(200, 10, txt="Invoice No: "+str(invoice_number)+"     ",border=20, ln=1, align="L")


    pdf.set_font("Arial", size=15, style="U")
    
    pdf.cell(200,10, txt="INVOICE",border=0, ln=2, align="C")

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10, txt="GSTIN - 22FIAPS9006P1ZU        ",border=0, ln=2, align="R")

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 6, txt="Bill To: "+ shop_name, border=20, ln=1, align="L")
    pdf.cell(200, 6, txt="Address: "+ shop_address, border=20, ln=1, align="L")
    pdf.cell(200, 6, txt="Contact Number: "+ shop_phone_number, border=20, ln=1, align="L")
    pdf.cell(200, 6, txt="GST Number: "+ shop_gstno, border=20, ln=1, align="L")

    pdf.ln(10)

    order_details = [
        ['Description', 'Amount'],
        [order_detail, str(round(amount*0.82, 2))]
    ]

    pdf.set_font('Arial', size=12)
    pdf.ln(0.5)
    
    th = pdf.font_size

    i = 1
    
    for row in order_details:
        for datum in row:
            if i==1:
                pdf.cell(130, 2*th, str(datum), border=1, align="C")
                i+=1
            else:
                pdf.cell(60, 2*th, str(datum), border=1, align="C")
                i-=1
        pdf.ln(2*th)

    pdf.ln(3.5)
    
    pdf.cell(200, 10, txt="Total: "+ str(round(amount*0.82, 2))+"        ", border=20, ln=1, align="R")
    pdf.cell(200, 10, txt="GST: "+ str(round(amount*0.18, 2))+"        ", border=20, ln=1, align="R")
    pdf.set_font('Arial', size=12, style="B")
    pdf.ln(1.5)
    pdf.dashed_line(140, 152, 200, 152)
    pdf.cell(200, 10, txt="Grand Total: "+ str(amount)+"        ", border=20, ln=1, align="R")
    pdf.set_font('Arial', size=12, style="I")
    pdf.cell(200, 5, txt="In words: "+ num2words(amount)+"        ", border=20, ln=1, align="R")

    pdf.image("./logo.jpg", 75, 9, 11, 10)
    pdf.image("./stamp.png", 15, 122, 50, 50)

    pdf.dashed_line(10, 175, 200, 175)

    pdf.cell(500, 5, txt="In words: ", border=20, ln=1, align="C")




    pdf.output("invoice/"+shop_name+".pdf")

if __name__ == '__main__':
    create_invoice("ABC Shop", "JP Nagar, Rewa - MP", "+91 9752315423","GSTIN1212112","199 Package", "IN20210706001" ,199)