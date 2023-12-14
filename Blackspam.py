import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyfiglet
from colorama import Fore, Style, init

# Initialiser colorama
init(autoreset=True)

# Liste des clés de licence générées
cles_de_licence = [
    "457bb2e5-2025-42e7-8a9d-e5c24bee71a2-2024-02-12",
    "4bf7c43a-2d48-4f8d-8074-604273ebffc4-2024-02-12",
    "53f50146-b172-4505-a166-bb4c508a6b8b-2024-02-12",
    "4dbb90d3-219c-424f-99eb-3cd05b5b5b73-2024-02-12",
    "c893038e-996e-430a-aa7f-5fb6e2b261f1-2024-02-12",
    "f33fac09-8e52-4220-9eb1-c8916846da49-2024-02-12",
    "e3a1202c-6cf5-4aed-8dbc-8ecf2282c6b7-2024-02-12",
    "421f2f4c-ce81-4bfd-83cc-f140196334e2-2024-02-12",
    "1751248a-f376-4fa3-b14d-79d534f90a3e-2024-02-12",
    "32a06bd0-7cc9-4267-80e1-68f3bd480737-2024-02-12",
    "21b54894-c9a0-4da0-8240-7fcb4971ea2a-2024-02-12",
    "5a33c7ca-b0b4-4541-ad8b-b4f0a4ef4339-2024-02-12",
    "2b0938b6-7d07-4d01-8e6a-01a9630c773c-2024-02-12",
    "5f85ea16-852b-4a90-a9a6-6358c114172b-2024-02-12",
    "3eac9aba-54dd-4a26-a85a-88d829adc943-2024-02-12",
    "ce1742e3-06ef-4a24-9544-050bcbe00365-2024-02-12",
    "bde2d6c0-e5c7-4555-8492-64eec59b24e6-2024-02-12",
    "41c82a54-4f82-4369-b193-373ab8e7e5e5-2024-02-12",
    "79cc9353-acb6-4085-866c-16e7c782cdf4-2024-02-12",
    "e4bc7eb4-f26e-4711-8f92-efd15338db2f-2024-02-12",
    "2e7c9369-43ca-4cc9-949a-3d6d52b8b4d1-2024-02-12",
    "a5045b61-101f-45e0-9476-82ace9df68be-2024-02-12",
    "b5c09b2d-f430-4750-89ef-6756ea2a246a-2024-02-12",
    "ff6f6ba5-5d0b-44a7-8f02-54ab3e3f2f31-2024-02-12",
    "f24238cf-cd90-4d8f-b8f6-df8b22e4fdcf-2024-02-12",
    "059fdb0e-692e-4e53-9c67-6b7e8554ff67-2024-02-12",
    "e1b1a056-0eb0-4b32-ab00-2a5a8b07391a-2024-02-12",
    "9952fdde-5800-4ddf-ba36-8cacd0ea5096-2024-02-12",
    "c186389d-2e0f-4cf9-8e8b-505719a5f1cc-2024-02-12",
]

# Fonction pour vérifier la clé de licence
def verifier_cle_licence(cle):
    return cle in cles_de_licence

# Creer un outil de scan
result = pyfiglet.Figlet(font='slant')
print(Fore.RED + result.renderText('Black_Spam'))
print(Fore.GREEN + "                  Created by Gioki45" + Style.RESET_ALL)
print(Fore.GREEN + "                  Version 1.0" + Style.RESET_ALL)
print(Fore.GREEN + "                  Telegram: @Gioki45" + Style.RESET_ALL)

def envoyer_email(adresse_expediteur, mot_de_passe, adresse_destinataire, nom_expediteur, sujet, message, serveur_smtp, port_smtp):
    # Crée un objet MIMEMultipart
    msg = MIMEMultipart()

    # Ajoute l'expéditeur et le destinataire à l'e-mail avec le nom personnalisé
    msg['From'] = f'{nom_expediteur} <{adresse_expediteur}>'
    msg['To'] = adresse_destinataire

    # Sujet de l'e-mail
    msg['Subject'] = sujet

    # Corps de l'e-mail
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Établit une connexion avec le serveur SMTP
        serveur = smtplib.SMTP(serveur_smtp, port_smtp)
        serveur.starttls()

        # Connecte au compte
        serveur.login(adresse_expediteur, mot_de_passe)

        # Envoie l'e-mail
        serveur.sendmail(adresse_expediteur, adresse_destinataire, msg.as_string())

        print(Fore.GREEN + 'E-mail envoyé avec succès' + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f'Erreur lors de l\'envoi de l\'e-mail: {e}' + Style.RESET_ALL)

    finally:
        # Ferme la connexion avec le serveur SMTP
        serveur.quit()

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Entrer la clé de licence")
        print("2. Quitter le script")

        choix = input("Choisissez une option (1 ou 2): ")

        if choix == '1':
            cle_licence = input("Entrez la clé de licence: ")

            # Vérifier la clé de licence
            if verifier_cle_licence(cle_licence):
                # Entrer les informations pour l'e-mail
                adresse_expediteur = input("Entrez votre adresse e-mail (expéditeur): ")
                mot_de_passe = input("Entrez votre mot de passe: ")
                adresse_destinataire = input("Entrez l'adresse e-mail du destinataire: ")
                nom_expediteur = input("Entrez votre nom (expéditeur): ")
                sujet = input("Entrez le sujet de l'e-mail: ")
                message = input("Entrez le corps de l'e-mail: ")

                # Ajouter les informations du serveur SMTP
                serveur_smtp = input("Entrez votre serveur SMTP: ")
                port_smtp = int(input("Entrez le port SMTP (par exemple, 587 pour TLS): "))

                envoyer_email(adresse_expediteur, mot_de_passe, adresse_destinataire, nom_expediteur, sujet, message, serveur_smtp, port_smtp)
            else:
                print(Fore.RED + "Clé de licence invalide. L'envoi d'e-mail est interdit." + Style.RESET_ALL)
        elif choix == '2':
            print("Le script a été quitté.")
            break
        else:
            print("Option invalide. Veuillez choisir 1 ou 2.")
