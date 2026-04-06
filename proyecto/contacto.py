from flask import Blueprint, render_template,request
from flask_mail import Message
from . import mail

bpContacto =  Blueprint("contacto",__name__)

@bpContacto.route("/contacto/",methods=("GET","POST"))
def contacto():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        asunto = request.form.get("asunto")
        mensaje = request.form.get("mensaje")

        msg = Message(body=f"Nombre: {nombre}\nCorreo: {correo}\nAsunto: {asunto}\n\nEscribió:\n{mensaje}",subject=asunto,sender=correo,recipients=["sandbox.smtp.mailtrap.io","jonathanreyes_24@hotmail.com"])
        mail.send(msg)
        mensaje = "El correo fué enviado éxitosamente"
    return render_template("contacto.html",pagina="contacto",mensaje=mensaje)