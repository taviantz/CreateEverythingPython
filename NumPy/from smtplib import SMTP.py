#experimenting with smtplib-SMTP protcol client 
#https://docs.python.org/3/library/smtplib.html#smtplib.SMTP

import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = "dante@dantetavaintz.com"
toaddrs  = ["taviantz@gmail.com"]
msg = "Hi here is a tested email newsletter. This is the start to our multitrillion dollar empire!!!"

# Collect the message
print("Enter additional lines for the message, end with ^D (Unix) or ^Z (Windows):")
lines = []
while True: 
    try:
        line = input()
    except EOFError: 
        break 
    if not line: 
        break
    lines.append(line)

# Add the additional lines to the message
msg += '\n' + '\n' .join(lines)

# Connect to the SMTP server 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login('dante@dantetaviantz.com', 'theiamtrillionairewith12zeros')

# Send the email 
server.sendmail(fromaddr, toaddrs, msg)

# Close the connection
server.quit()