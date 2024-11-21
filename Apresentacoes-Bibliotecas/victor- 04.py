from InquirerPy import inquirer

nome = inquirer.text("Qual seu nome?").execute()
cor = inquirer.select("Qual sua favorita?",
                      choices=["Preto", "Verde", "vermelho"]).execute()

#Atividade 02:

