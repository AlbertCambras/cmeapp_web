from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import CMYKColor
from datetime import date

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/procesar', methods=['POST'])
def process():
    
    try:
        # Obtén los datos de la solicitud POST
        data = request.json
        dni = data.get('dni')
        name = data.get('name')
        date = data.get('date')

        # Genera el archivo PDF en memoria
        pdf_content = CME(name, dni)

        # Devuelve el PDF como una respuesta HTTP
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=certificado.pdf'  # Esta línea indica la descarga


        return response
    
    except Exception as e:
        return jsonify({'error': str(e)})




def CME(name, nif):
    name_fitx = name.replace(" ", "").lower()
    cme  = canvas.Canvas(name_fitx +'.pdf', pagesize=A4)
    width, height = A4 # keep for later

    ##########################################
    title = cme.beginText()
    title.setTextOrigin(inch, 10.5*inch)
    title.setFont("Helvetica", 14)

    sub = cme.beginText()
    sub.setTextOrigin(inch, 10.5*inch)
    sub.setFont("Helvetica", 10)

    sub2 = cme.beginText()
    sub2.setTextOrigin(inch, 10.5*inch)
    sub2.setFont("Helvetica", 12)

    sub3 = cme.beginText()
    sub3.setFont("Helvetica", 10)

    sub4 = cme.beginText()
    sub4.setFont("Helvetica", 12)




    ##########################################

    ##  TITLE
    title.setXPos(1.75*inch)
    title.textLines("CERTIFICAT MÈDIC ESPORTIU")
    cme.drawText(title)

    sub.textLines("")
    sub.textLines("")

    ## SUB
    
    cme.drawImage("GEN_CAT.jpg", inch,9.9*inch ,width=inch/4,height=inch/4,preserveAspectRatio=True)

    sub.setXPos(inch/3)
    sub.textLines("Generalitat de Catalunya")
    sub.textLines("Departament de Salut")
    cme.drawText(sub)

    sub2.textLines("")
    sub2.textLines("")
    sub2.textLines("")
    sub2.textLines("")
    sub2.textLines("")
    sub2.textLines("")

    # SUB2
    sub2.textLines("Certificat Mèdic Esportiu (CME)")
    (x,y)=sub2.getCursor()
    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)

    sub2.textLines("")
    sub2.textLines("")


    ## DADES ESPORTISTA

    sub2.textLines("Dades de l'esportista")
    (x,y)=sub2.getCursor()
    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)

    sub2.textLines("")
    sub2.textLines("")
    sub2.textLines("Nom i cognoms                                                              NIF")

    (x,y)=sub2.getCursor()

    sub4.setTextOrigin(x,y)
    sub4.textLines(name)
    
    sub4.setTextOrigin(x+4*inch,y)
    sub4.textLines(nif)

    cme.drawText(sub4)
    sub2.setFont("Helvetica", 12)


    sub2.textLines("")
    sub2.textLines("")

    (x,y)=sub2.getCursor()
    cme.line(x,y,7.5*inch,y)

    cme.drawText(sub2)
    ## RESULTAT PROVES
    sub2.textLines("")
    sub2.setFont("Helvetica-Bold", 10)

    sub2.textLines("Dades de la valoració funcional medicoesportiva")
    (x,y)=sub2.getCursor()
    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)

    sub2.textLines("")

    sub2.textLines("Nom del centre mèdic")
    sub2.textLines("")

    sub2.setFont("Helvetica", 10)
    sub2.textLines("'El CIM'")

    (x,y)=sub2.getCursor()
    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)
    sub2.textLines("")
    sub2.setFont("Helvetica-Bold", 10)

    sub2.textLines("Proves mèdiques")
    sub2.textLines("(Cal marcar les realitzades i/o, si escau, afegir-ne d'altres)")

    cme.drawText(sub2)

    ## CASELLES ESQUERRA
    
    black = CMYKColor(0,0,0,1)
    cme.setFillColor(black)

    sub2.textLines("")
    sub2.textLines("")
    (x1,y1)=sub2.getCursor()
    cme.rect(x1 , y1 , width=10 , height=10 , fill=True)
    
    

    sub3.setTextOrigin(x1+15, y1)
    sub3.textLines("Antecedents personals i familiars")

    sub2.textLines("")
    sub2.textLines("")
    (x2,y2)=sub2.getCursor()
    cme.rect(x2,y2,width=10,height=10, fill = True)

    sub3.setTextOrigin(x2+15, y2)

    sub3.textLines("Exploració cardiorespiratoria bàsica")

    sub2.textLines("")
    sub2.textLines("")
    (x3,y3)=sub2.getCursor()
    cme.rect(x3,y3,width=10,height=10, fill=True)

    sub3.setTextOrigin(x3+15, y3)
    sub3.textLines("Exploració bàsica de l'aparell locomotor")

    ## CASELLES DRETA
    sub2.textLines("")
    sub2.textLines("")
    cme.rect(x1+3*inch,y1,width=10,height=10, fill=True)

    sub3.setTextOrigin(3*inch+x1+15, y1)
    sub3.textLines("Exploració per aparells")

    sub2.textLines("")
    sub2.textLines("")
    cme.rect(x2+3*inch,y2,width=10,height=10, fill=True)
    

    sub3.setTextOrigin(3*inch+x2+15, y2)
    sub3.textLines("Electrocardiograma")

    sub2.textLines("")
    sub2.textLines("")

    cme.rect(x3+3*inch,y3,width=10,height=10)

    sub3.setTextOrigin(3*inch+x3+15, y3)
    sub3.textLines("Ergometria (Prova esforç)")

    cme.drawText(sub3)

    ## CASELLES ABAIX
    sub3.textLines("")
    sub3.textLines("")

    (x,y)=sub3.getCursor()

    sub3.setTextOrigin(x3,y)
    sub3.textLines("Indicacions per a la pràctica d'exercici físic en funció dels resultats de les proves mèdiques")

    (x,y)=sub3.getCursor()
    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)

    sub3.textLines("")
    (x,y)=sub3.getCursor()
    cme.rect(x,y,width=10,height=10, fill=True)

    sub3.setTextOrigin(x+15, y)
    sub3.textLines("Sense contradiccions aparents per a la pràctica d'exercici físic i/o esport")

    sub3.textLines("")
    (x,y)=sub3.getCursor()
    cme.rect(x-15,y,width=10,height=10)

    sub3.setTextOrigin(x, y)
    sub3.textLines("Amb limitacions específiques per a l'exercici físic")
    cme.drawText(sub3)

    sub3.textLines("")
    (x,y)=sub3.getCursor()
    cme.rect(x-15,y,width=10,height=10)

    sub3.setTextOrigin(x, y)
    sub3.textLines("Contradicció absoluta per a la pràctica esportiva")
    cme.drawText(sub3)

    sub3.textLines("")
    sub3.textLines("")


    ## METGE
    (x,y)=sub3.getCursor()

    cme.line(x,y+0.1*inch,7.5*inch,y+0.1*inch)
    sub3.textLines("")

    (x,y)=sub3.getCursor()
    sub3.setTextOrigin(x,y)
    sub3.textLines("Dades del metge o metgessa declarant")



    sub3.setFont("Helvetica", 10)

    sub3.textLines("Nom i cognoms               Col·legi                    Núm. de col·legiat/ada")
    sub3.setFont("Helvetica", 12)
    sub3.textLines("")
    sub3.textLines("Pere Cambras Morales        Barcelona                    22843")

    (x,y)=sub3.getCursor()
    cme.line(x,y,7.5*inch,y)

    (x,y4)=sub3.getCursor()
    sub3.setTextOrigin(x,y4-10)
    sub3.textLines(date.today().strftime("%d"))
    (x,y)=sub3.getCursor()
    sub3.setTextOrigin(x+1/2+inch,y4-10)
    sub3.textLines("de")
    
    (x,y)=sub3.getCursor()
    sub3.setTextOrigin(x+1/2+inch,y4-10)
    sub3.textLines(date.today().strftime("%m"))

    (x,y)=sub3.getCursor()
    sub3.setTextOrigin(x+1/2+inch,y4-10)
    sub3.textLines("del")
    
    (x,y)=sub3.getCursor()
    sub3.setTextOrigin(x+1/2+inch,y4-10)
    sub3.textLines(date.today().strftime("%y"))


    cme.drawText(sub3)



    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")
    sub3.textLines("")

    (x,y)=sub3.getCursor()

    cme.drawImage("FIRMA.png", x,y ,width=2*inch,height=2*inch,preserveAspectRatio=True)

    #cme.save()
    return cme.getpdfdata()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)